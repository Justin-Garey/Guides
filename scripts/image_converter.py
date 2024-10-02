#!/bin/python3

import os
import argparse
from PIL import Image

FILETYPES = ('.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.png')

def convert_images(directory, filetype, save):
    for filename in os.listdir(directory):
        if filename.lower().endswith(FILETYPES) and not filename.lower().endswith(('.' + filetype)): 
            file_path = os.path.join(directory, filename)
            with Image.open(file_path) as img:
                png_filename = os.path.splitext(filename)[0] + '.' + filetype
                png_file_path = os.path.join(directory, png_filename)
                img.save(png_file_path)
            if not save:
                os.remove(file_path)  # Remove the original file
            print(f"Converted {filename} to {png_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to PNG format.")
    parser.add_argument('directory', type=str, help='The directory containing images to convert.')
    parser.add_argument('-f', '--filetype', type=str, help='The filetype to convert the images to.', default='png')
    parser.add_argument('-s', '--save', action='store_true', help='Save the original files')
    args = parser.parse_args()

    convert_images(args.directory, args.filetype, args.save)
