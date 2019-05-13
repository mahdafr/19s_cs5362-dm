# Mining for Credibility
Project for CS5362 Data Mining, Spring 2019<br/>
Group Members:
* Mahdokht Afravi
* Jonathan Avila
* Cristian Ayub
* Gerardo Cervantes

## How to Run
This section describes how to run each script in the python environment equipped with the 'Prerequisites' stated below.

### datafilter.py

Reads `news_cleaned_2018_02_13.csv` and writes rows matching article types supplied with `-article_types`. For a 
complete list of article types (tags): https://github.com/several27/FakeNewsCorpus#formatting

For example, to write 'fake' articles and 'reliable' articles into `fake.csv` and `reliable.csv` respectively,

    data_filter.py -article_types fake reliable
    
### data_preprocessing.py

Creates a sparse matrix of documents and word frequency. Default vocabulary size is 40,000.

    data_preprocessing.py -filename="fake.csv" -article_limit=1000 -vocabulary_size=20000

### Prerequisites 

    nltk.download('stopwords')
    nltk.download('punkt')
    
### Resources
Fake News Corpus: https://github.com/several27/FakeNewsCorpus


## Downloadables
Click on the `Releases` tab of the project on GitHub (or clicking [this link](https://github.com/mahdafr/19s_cs5362-dm)) to download a ZIP of all source code, report (as a PDF), and presentation slides (as a PDF).
