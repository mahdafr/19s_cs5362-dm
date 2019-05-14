# Mining for Credibility
Project for CS5362 Data Mining, Spring 2019<br/>
Group Members:
* Mahdokht Afravi
* Jonathan Avila
* Cristian Ayub
* Gerardo Cervantes

<details>
    <summary>How to Run</summary>
<p>This section describes how to run each script in the python environment equipped with the 'Prerequisites' stated below.</p>

<h4>datafilter.py</h4>
Reads `news_cleaned_2018_02_13.csv` and writes rows matching article types supplied with `-article_types`. For a complete list of article types (tags), see https://github.com/several27/FakeNewsCorpus#formatting.
    <p>For example, to write 'fake' articles and 'reliable' articles into `fake.csv` and `reliable.csv` respectively, </p>
    <q>data_filter.py -article_types fake reliable</q><br/>
  
<h4>data_preprocessing.py</h4>
Creates a sparse matrix of documents and word frequency. Default vocabulary size is 40,000.
    <q>data_preprocessing.py -filename="fake.csv" -article_limit=1000 -vocabulary_size=20000</q><br/>

<h4>Prerequisites<h4>
    <p><q>nltk.download('stopwords')</q><br/>
        <q>nltk.download('punkt')</q></p>
</details>

<details>
    <summary>Resources</summary>
    <p>Fake News Corpus is available on GitHub at https://github.com/several27/FakeNewsCorpus.</p>
</details>

<details>
    <summary>Downloadables</summary>
    <p>Click on the <em>Releases</em> tab of the project on GitHub (or visiting https://github.com/mahdafr/19s_cs5362-dm/releases) to download a ZIP of all source code, report (as a PDF), and presentation slides (as a PDF).</p>
</details>
