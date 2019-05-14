# Mining for Credibility
Project for CS5362 Data Mining, Spring 2019<br/>
Group Members:
* Mahdokht Afravi
* Jonathan Avila
* Cristian Ayub
* Gerardo Cervantes

<details>
<p>This section describes how to run each script in the python environment equipped with the 'Prerequisites' stated below.</p>

<h3>datafilter.py</h3>
    <p>Reads `news_cleaned_2018_02_13.csv` and writes rows matching article types supplied with `-article_types`. For a 
    complete list of article types (tags): [link](https://github.com/several27/FakeNewsCorpus#formatting)</p>
    <p>For example, to write 'fake' articles and 'reliable' articles into `fake.csv` and `reliable.csv` respectively, </p>
    `data_filter.py -article_types fake reliable`
  
<h3>data_preprocessing.py</h3>
    <p>Creates a sparse matrix of documents and word frequency. Default vocabulary size is 40,000.</p>
    <p>data_preprocessing.py -filename="fake.csv" -article_limit=1000 -vocabulary_size=20000</p>

<h2>Prerequisites<h2>
    `nltk.download('stopwords')`
    `nltk.download('punkt')`
</details>

<details>
    <p>Fake News Corpus: [on GitHub](https://github.com/several27/FakeNewsCorpus)</p>
</details>

<details>
    <p>Click on the `Releases` tab of the project on GitHub (or clicking [this link](https://github.com/mahdafr/19s_cs5362-dm)) to download a ZIP of all source code, report (as a PDF), and presentation slides (as a PDF).</p>
</details>
