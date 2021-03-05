"""
Executes when the called using `python -m bbtm`.
Contains ability to handle the command line arguments.
"""

import os
import sys
import json
import argparse
from bbtm import core as bbtm

parser = argparse.ArgumentParser(description="A small python utility to export \
        your python programs.")

# For the name of the format.
parser.add_argument(
    'format', 
    help="Format in which you need to export your bookmarks.",
    choices=['markdown', 'csv'],
)

# Optional Argument for the output directory.
parser.add_argument(
    '-o', '--output',
    help="Specify the output path for the exported bookmarks.",
    
)

args = parser.parse_args()

if not os.path.isfile(bbtm.BOOKMARKS_PATH):
    print("I can't find the bookmarks, sorry!")
    sys.exit(1)

with open(bbtm.BOOKMARKS_PATH, "r") as file:
    print(os.getcwd())
    # file represents the Bookmarks path.
    data = json.load(file)
    BOOKMARKS = bbtm.parse_json(data['roots']['bookmark_bar']['children'])
    output = None

    if args.output:
        if os.path.isdir(os.path.dirname(args.output)):
            output = args.output

    if args.format == 'markdown':
        if output:
            bbtm.export_markdown(BOOKMARKS, output=output)
        else:
            bbtm.export_markdown(BOOKMARKS)

    elif args.format == 'csv':
        if output:
            bbtm.export_csv(BOOKMARKS, output)
        else:
            bbtm.export_csv(BOOKMARKS)


