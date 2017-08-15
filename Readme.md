# Color extractor script

    ./color_extractor.py --help
    Usage: color_extractor.py [OPTIONS] COLOR_TABLE IMAGE_FILE X Y WIDTH HEIGHT

      Extract a color histogram from a rectangle (x, y, width, height: pixels)
      within image_file.

      Color_table: TSV (r,g,b,color_name)

    Options:
      -save-box TEXT  store rectangle image for debugging
      --help          Show this message and exit.

# Installation and execution

    sudo -H pip3 install -r requirements.txt

    ./color_extractor.py Data/colors2.tsv Data/image.jpg 297 263 43 18
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


