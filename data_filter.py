import csv
import argparse
import csv_const


def filter_articles(article_types):

    csv.field_size_limit(2147483647)  # avoid errors on huge fields

    keys = csv_const.FIELDS

    full_csv_file = open('news_cleaned_2018_02_13.csv', encoding=csv_const.ENCODING,
                         newline=csv_const.NEWLINE)  # csv for reading

    for article_type in article_types:

        type_csv_file = open(article_type + '.csv', 'w+', encoding=csv_const.ENCODING,
                             newline=csv_const.NEWLINE)  # csv for writing

        # zip keys and row values into a dictionary; write to csv if 'type' is a match
        csv_writer = csv.writer(type_csv_file, delimiter=csv_const.DELIMITER)
        for row in csv.reader(full_csv_file, delimiter=csv_const.DELIMITER):
            fields = dict(zip(keys, row))
            if 'type' in fields and fields['type'] == article_type:  # some articles don't have a type (?)
                csv_writer.writerow(row)

        type_csv_file.close()

    full_csv_file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Extract articles by type')
    parser.add_argument('-article_types', nargs='+', type=str, required=True, help='a list of article types')
    args = parser.parse_args()
    filter_articles(args.article_types)
