# Mining for Credibility
Project for CS5362 Data Mining, Spring 2019<br/>
Group Members:
* Mahdokht Afravi
* Jonathan Avila
* Cristian Ayub
* Gerardo Cervantes

## Abstract
We used the publicly available FakeNewsCorpus dataset that consists of articles labelled as one of 11 types. We used articles labelled as 'fake', 'reliable', and 'conspiracy' to extract features. We convert the data to numerical data by using a spare matrix representation and using term frequency.  With this feature set, we apply clustering algorithms to the dataset, and are able to find useful information about about the data.  We train a model using linear regression that would predict whether an article is 'fake' or 'reliable' and find modest results. Our project site is a GitHub web page that can be found <a href="https://mahdafr.github.io/19s_cs5362-dm/">on GitHub Pages</a> which contains the source code, a PDF copy of the presentation slides, and a PDF copy of this report.

<details>
    <summary>How to Run</summary>
<p>This section describes how to run each script in the python environment equipped with the 'Prerequisites' stated below.</p>

<br/>
<h4>datafilter.py</h4>
Reads `news_cleaned_2018_02_13.csv` and writes rows matching article types supplied with `-article_types`. For a complete list of article types (tags), see <a href="https://github.com/several27/FakeNewsCorpus#formatting">this page</a>.
    <p>For example, to write 'fake' articles and 'reliable' articles into `fake.csv` and `reliable.csv` respectively, </p>
    <q>data_filter.py -article_types fake reliable</q><br/>

<br/>
<h4>data_preprocessing.py</h4>
Creates a sparse matrix of documents and word frequency. Default vocabulary size is 40,000.
    <q>data_preprocessing.py -filename="fake.csv" -article_limit=1000 -vocabulary_size=20000</q><br/>

<br/>
<h4>dbscan.py</h4>
<p>Runs DBSCAN and calculates outliers' distances to nearest cluster as measure of cluster fit. Reports on clusters made and noise articles. The file names are hardcoded to a specific directory (D:\dm_dataset\) where all files must be located in order to run this script.</p>

<br/>
<h4>kmeans_algorithm.py</h4>
<p>Runs k-means and reports random articles for manual analysis of clusters. The file names are hardcoded to a specific directory (D:\dm_dataset\) where all files must be located in order to run this script. k is also hardcoded.</p>

<br/>
<h4>linear_regression.py</h4>
<p>Runs linear regression and reports whether an article is fake or reliable. The file names are hardcoded to a specific directory (D:\dm_dataset\) where all files must be located in order to run this script.</p>

<br/>
<h4>naive_bayes.py</h4>
<p>Runs naive bayes. This script is a draft that is incomplete for this project.</p>

<br/>
<h4>Prerequisites</h4>
    <p><q>scipy</q> installed</p>
    <p><q>nltk</q> installed</p>
    <p><q>nltk.download('stopwords')</q></p>
    <p><q>nltk.download('punkt')</q></p>
</details>

<details>
    <summary>Resources</summary>
    <p>Fake News Corpus is available <a href="https://github.com/several27/FakeNewsCorpus">on GitHub</a>.</p>
</details>

<details>
    <summary>Downloadables</summary>
    <p>Visit the <a href="https://github.com/mahdafr/19s_cs5362-dm/releases">Releases page</a> of the project on GitHub to download a ZIP of all source code, report (as a PDF), and presentation slides (as a PDF).</p>
</details>

<details>
    <summary>Links</summary>
    <p><a href="https://github.com/mahdafr/19s_cs5362-dm/">Code</a></p>
    <p><a href="https://github.com/mahdafr/19s_cs5362-dm/blob/master/docs/slides.pdf">Slides</a></p>
    <p><a href="https://github.com/mahdafr/19s_cs5362-dm/blob/master/docs/report.pdf">Report</a></p>
</details>
