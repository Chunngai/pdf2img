#!/usr/bin/python3

import argparse
import time

import PyPDF2


def imgs2pdf(orig_pdf, new_pdf_name, from_, to):
    reader = PyPDF2.PdfFileReader(orig_pdf)
    pages = []
    for page_num in range(from_, to + 1):
        pages.append(reader.getPage(page_num - 1))

    writer = PyPDF2.PdfFileWriter()
    for page in pages:
        writer.addPage(page)
    with open(new_pdf_name, "ab+") as f:
        writer.write(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--orig-pdf", required=True)
    parser.add_argument("--new-pdf-name", default=str(time.time()))
    parser.add_argument("--from_", required=True, type=int)
    parser.add_argument("--to", required=True, type=int)

    args = parser.parse_args()
    if ".pdf" not in args.new_pdf_name:
        args.new_pdf_name = args.new_pdf_name + ".pdf"

    imgs2pdf(args.orig_pdf, args.new_pdf_name, args.from_, args.to)