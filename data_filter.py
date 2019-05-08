import csv
import argparse


def filter_articles(article_types):

    csv.field_size_limit(2147483647)  # avoid errors on huge fields

    # following: https://github.com/several27/FakeNewsCorpus#formatting
    keys = ['', 'id', 'domain', 'type', 'url', 'content', 'scraped_at', 'inserted_at', 'updated_at', 'title', 'authors',
            'keywords', 'meta_keywords', 'meta_description', 'tags', 'summary']

    full_csv_file = open('news_cleaned_2018_02_13.csv', encoding='utf-8', newline='')  # csv for reading

    for article_type in article_types:

        type_csv_file = open(article_type + '.csv', 'w+', encoding='utf-8', newline='')  # csv for writing

        # zip keys and row values into a dictionary; write to csv if 'type' is a match
        csv_writer = csv.writer(type_csv_file, delimiter=',')
        for row in csv.reader(full_csv_file, delimiter=','):
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
