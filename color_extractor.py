#!/usr/bin/env python3

import click
from numpy import unique
from numpy.ma import floor_divide
from scipy.misc import imread, imsave
from scipy.spatial.ckdtree import cKDTree


@click.command()
@click.argument('color_table')
@click.argument('image_file')
@click.argument('x', type=int)
@click.argument('y', type=int)
@click.argument('width', type=int)
@click.argument('height', type=int)
@click.option('-save-box', default=None, help='store rectangle image for debugging')
def color_extractor(color_table, image_file, x, y, width, height, save_box):
    """
    Extract a color histogram from a rectangle (x, y, width, height: pixels) within image_file.

    Color_table: TSV (r,g,b,color_name)
    """
    image = imread(image_file,mode='RGB')
    # print(image.shape)
    rectangle = image[y:y + height, x:x + width, :]
    if save_box:
        imsave(save_box, rectangle)

    histogram = ColorHistogram(rgb_names(read_tsv(color_table)))
    print_tsv(histogram.sample_from_rectangle(rectangle))


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


class ColorHistogram:
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
