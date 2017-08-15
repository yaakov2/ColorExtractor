# Color extractor script

Extract a color histogram from a sampling rectangle within an image.

### Installation of dependencies

    sudo -H pip3 install -r requirements.txt

### Sample usage with output

    ./color_extractor.py -colors Data/colors2.tsv -image Data/image.jpg -x 297 -y 263 -width 43 -height 18

    33	dark_jungle_green
    14	mint_cream
    10	white
    7	black
    6	medium_jungle_green
    4	smoky_black
    4	licorice
    4	ghost_white
    1	white_smoke
    1	oxford_blue
    1	anti_flash_white

    ./color_extractor.py -colors Data/colors2.tsv -image Data/image.jpg -x 297 -y 263 -width 43 -height 18 -output-format json

    {"white": 10, "mint_cream": 14, "ghost_white": 4, "dark_jungle_green": 33, "smoky_black": 4, "black": 7, "medium_jungle_green": 6, "licorice": 4, "anti_flash_white": 1, "oxford_blue": 1, "white_smoke": 1}

### Command line options:

    ./color_extractor.py --help
    Usage: color_extractor.py [OPTIONS]

      Extract a color histogram from a sampling rectangle within an image.

    Options:
      -colors TEXT               color table file: tsv (r, g, b, color_name)
      -image TEXT                input image file (.jpg, .gif, .png...)
      -x INTEGER                 left bounding box corner (pixels)
      -y INTEGER                 top bounding box corner (pixels)
      -width INTEGER             bounding box width (pixels)
      -height INTEGER            bounding box height (pixels)
      -save-box TEXT             store sample region to file for debugging
      -output-format [tsv|json]
      --help                     Show this message and exit.


