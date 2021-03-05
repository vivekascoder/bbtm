import sys
import json
import os
import csv
import datetime


HOME = os.getenv("HOME")
BRAVE_BOOKMARK = ".config/BraveSoftware/Brave-Browser/Default/Bookmarks"
BOOKMARKS_PATH = os.path.join(HOME, BRAVE_BOOKMARK)


def parse_timestamp(timestamp: str):
    """
    Convert the Chrome epoch timestamp into datetime object.
    """
    epoch_start = datetime.datetime(1601, 1, 1)
    delta = datetime.timedelta(microseconds=int(timestamp))
    return epoch_start + delta


def parse_json(json_list):
    """
    This function scraps the bookmark's url and name.
    and append it to a variable called BOOKMARKS.
    """
    BOOKMARKS = []
    for json_data in json_list:
        if 'children' in json_data:
            parse_json(json_data['children'])
        else:
            BOOKMARKS.append({
                'name': json_data['name'],
                'url': json_data['url'],
                'date': parse_timestamp(json_data['date_added'])
            })

    return BOOKMARKS


def export_markdown(items, output=None):
    """
    Returns the Markdown string.
    """
    if not output:
        output = os.path.join(os.getcwd(), 'bookmarks.md')
    base_template = "# My Bookmarks.\n"
    base_template += "- Exported by bbtm.py\n"

    for mark in items:
        base_template += f"- {mark['name']}\n"
        base_template += f"\t- {mark['date']}\n"
        base_template += f"\t- {mark['url']}\n"

    base_template += "\n----\n> Exported using bbtm.py"

    # print(base_template)
    # sys.stdout.write(base_template)
    with open(output, "w") as file:
        file.write(base_template)


def export_csv(items, file_name=None):
    """
    Exports the bookmarks into a csv file.
    """
    if not file_name:
        file_name = os.path.join(os.getcwd(), 'bookmarks.csv')
    print(file_name)
    with open(file_name, mode="w") as bookmark_file:
        fieldnames = ['date', 'name', 'url']
        writer = csv.DictWriter(bookmark_file, fieldnames=fieldnames)

        for row in items:
            writer.writerow(row)




