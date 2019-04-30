import csv

NEWLINE = ""
TAG_INDEX = 3  # column containing tag
DELIMITER = ","
ENCODING = "utf-8"
DATA_CSV = r"D:\dataset\original.csv"

fake_csv = open("fake.csv", "w+", encoding=ENCODING, newline=NEWLINE)
fake_writer = csv.writer(fake_csv, delimiter=DELIMITER)

credible_csv = open("credible.csv", "w+", encoding=ENCODING, newline=NEWLINE)
credible_writer = csv.writer(credible_csv, delimiter=DELIMITER)

conspiracy_csv = open("conspiracy.csv", "w+", encoding=ENCODING, newline=NEWLINE)
conspiracy_writer = csv.writer(conspiracy_csv, delimiter=DELIMITER)

unreliable_csv = open("unreliable.csv", "w+", encoding=ENCODING, newline=NEWLINE)
unreliable_writer = csv.writer(unreliable_csv, delimiter=DELIMITER)

csv.field_size_limit(2147483647)  # avoid errors on huge fields
with open(DATA_CSV, encoding=ENCODING, newline=NEWLINE) as csv_file:
    reader = csv.reader(csv_file, delimiter=DELIMITER)
    for row in reader:
        if len(row) > TAG_INDEX:
            if row[TAG_INDEX] == "fake":
                fake_writer.writerow(row)
            elif row[TAG_INDEX] == "credible":
                credible_writer.writerow(row)
            elif row[TAG_INDEX] == "conspiracy":
                conspiracy_writer.writerow(row)
            elif row[TAG_INDEX] == "unreliable":
                unreliable_writer.writerow(row)

fake_csv.close()
conspiracy_csv.close()
unreliable_csv.close()
credible_csv.close()
