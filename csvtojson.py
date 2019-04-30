import csv
import json

NEWLINE = ""
TAG_INDEX = 3  # column containing tag
CONTENTS_INDEX = 5  # column containing contents
DELIMITER = ","
ENCODING = "utf-8"
DATA_CSV = r"D:\dm_dataset\reliable.csv"
DESIRED_TAG = "reliable"

contents = []

csv.field_size_limit(2147483647)  # avoid errors on huge fields
with open(DATA_CSV, encoding=ENCODING, newline=NEWLINE) as csv_file:
    reader = csv.reader(csv_file, delimiter=DELIMITER)
    for row in reader:
        if len(row) > TAG_INDEX and row[TAG_INDEX] == DESIRED_TAG:
            contents.append(row[CONTENTS_INDEX])

with open(r"D:\dm_dataset\reliable.json", "w") as file:
    json.dump(contents, file)