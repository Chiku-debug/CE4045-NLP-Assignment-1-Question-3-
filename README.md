# CE4045-NLP-Assignment-1

## Running Directory
The source_code directory has all python scripts for the assignment. Change to the directory to run the code.
```
$ cd source_code
```

## Python Version
* Python 3.7

## Dataset directory
All the datasets are located in the `source_code/dataset`.

Contents:

* Task 1:
  * domain_1_patent/
  * domain_2_financial_management/
  * domain_3_computer_science/
  * domain_1_sentences.txt
  * domain_2_sentences.txt
  * domain_3_sentences.txt
  
* Task 2:
  * reviews4_goemon.txt
  * reviews4_goemon_noun_adj_pairs_manual.csv
  
* Task 3:
  * review.txt

## Results directory
All the results of all tasks are located in `source_code/results`.

## Installation Guide
Make sure you have the libraries below installed in your machine.
* matplotlib==3.0.3
* nltk==3.4
* beautifulsoup4==4.7.1
* requests==2.21.0
* xlwt==1.3.0
* spacy==2.3.2

Use below command to install the required library.
```
$ pip install [library name]
```

Download the required spacy model. Run below commands in terminal.
```
$ python -m spacy download en_core_web_sm
```

Download the required nltk models. Run below commands in python shell.
```python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('vader_lexicon')
```

## Usage Guide
**1. Domain Specific Dataset Analysis**

Execute the following command in command prompt to run this task.

Replace the `dataset name` with one of the listed datasets:
* patent
* csai
* financial
* all

Note on datasets for each task: 

* Tokenization and Stemming: patent, csai, financial. 
* Sentence Segmentation: all. 
* POS Tagging: all
```
$ python main.py --analysis [dataset name]
```

**2. Development of <Noun - Adjective> Pair Ranker**
  
Execute the following command in command prompt to run this task.
```
$ python main.py --pair True
```

**3. Sentiment Analysis Application**

Execute the following command in command prompt to run this task.
```
$ python main.py --sentiment True
```

## Tasks Output Log
All the outputs are located in `source_code/results`. The format of output files is [task name]_output.txt.
