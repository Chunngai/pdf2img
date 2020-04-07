#!/usr/bin/env python

import os
import argparse

from pdf2image import convert_from_path


def pdf2img(pdf_path, output_folder, format_):
    print(f"converting {pdf_path} to {format_} images")

    output_file_name = f"{os.path.basename(pdf_path)}"
    convert_from_path(pdf_path, output_folder=output_folder,
                      output_file=output_file_name, fmt=format_,
                      thread_count=6)

    print(f"done. stored images in {output_folder} with {output_file_name} "
          "as basename")


def validate_dir(dir_input):
    if os.path.isdir(dir_input):
        return dir_input
    else:
        print(f"dir not exists. making dir {dir_input}")
        try:
            os.makedirs(dir_input)
        except Exception:
            print(f"{err_msg}failed to make dir {dir_input}")
            print(f"{os.getcwd()} will be used instead")

            return os.getcwd()
        else:
            return dir_input


if __name__ == '__main__':
    err_msg = "pdf2img.py: error: "

    parser = argparse.ArgumentParser(
        description="pdf2img.py - a tool for converting pdf files into images")
    parser.add_argument("--pdf_path", "-p", action="store", required=True,
                        help="path of the pdf to be converted")
    parser.add_argument("--output-folder", "-d", action="store",
                        default=os.getcwd(), type=validate_dir,
                        help="folder for saving converted images")
    parser.add_argument("--output-file-name", "-n", action="store",
                        default="img",
                        help="base file name of the images")
    parser.add_argument("--format", "-f", action="store", default="png",
                        choices=["jpeg", "jpg", "png", "tif", "tiff", "ppm"],
                        help="format of the images")

    args = parser.parse_args()

    pdf2img(args.pdf_path, args.output_folder, args.format)
