#!/usr/bin/env python3
import json

import click
from numpy import unique
from numpy.ma import floor_divide
from scipy.misc import imread, imsave
from scipy.spatial.ckdtree import cKDTree


@click.command()
@click.option('-colors', help='color table file: tsv (r, g, b, color_name)')
@click.option('-image', help='input image file (.jpg, .gif, .png...)')
@click.option('-x', type=int, help='left bounding box corner (pixels)')
@click.option('-y', type=int, help='top bounding box corner (pixels)')
@click.option('-width', type=int, help='bounding box width (pixels)')
@click.option('-height', type=int, help='bounding box height (pixels)')
@click.option('-save-box', default=None, help='store sample region to file for debugging')
@click.option('-output-format', type=click.Choice(['tsv', 'json']), default='tsv')
def color_extractor(colors, image, x, y, width, height, save_box, output_format):
    """
    Extract a color histogram from a sampling rectangle within an image.
    """
    image_data = imread(image, mode='RGB')
    # print(image.shape)
    rectangle = image_data[y:y + height, x:x + width, :]
    if save_box:
        imsave(save_box, rectangle)

    extractor = ColorExtractor(rgb_names(read_tsv(colors)))
    histogram = extractor.sample_from_rectangle(rectangle)
    if output_format == 'tsv':
        print_tsv(histogram)
    else:
        print(json.dumps({k: int(v) for v, k in histogram}))


def read_tsv(file_name):
    with open(file_name) as fh:
        for line in fh:
            yield line.strip().split('\t')


def print_tsv(data):
    for d in data:
        print('\t'.join(str(v) for v in d))


def rgb_names(data):
    for r, g, b, name in data:
        yield int(r), int(g), int(b), name


class ColorExtractor:
    def __init__(self, color_data):
        color_data = list(color_data)
        self.color_names = [name for r, g, b, name in color_data]
        self.kdtree = cKDTree([(r, g, b) for r, g, b, name in color_data])

    def sample_from_rectangle(self, rectangle):
        distances, indices = self.kdtree.query(rectangle)
        keys, counts = unique(indices, return_counts=True)
        percents = floor_divide(counts * 100, (1 + sum(counts)))
        histogram = [(pct, self.color_names[key]) for pct, key in zip(percents, keys) if pct > 0]
        histogram = sorted(histogram, reverse=True)
        return histogram


if __name__ == '__main__':
    color_extractor()
