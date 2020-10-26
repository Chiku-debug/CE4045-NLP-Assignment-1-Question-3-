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
* domain_1_patent/
* domain_2_financial_management/
* domain_3_computer_science/
* domain_1_sentences.txt
* domain_2_sentences.txt
* domain_3_sentences.txt

## Installation Guide
Make sure you have the libraries below installed in your machine.
* matplotlib==3.0.3
* nltk==3.4
* beautifulsoup4==4.7.1
* requests==2.21.0

Use below command to install the required library.
```
$ pip install [library name]
```

Download the required nltk models. Run below commands in python shell.
```python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> nltk.download('averaged_perceptron_tagger')
```

## Usage Guide
**1. Domain Specific Dataset Analysis**

Execute the following command in command prompt to run this task.

Replace the `dataset name` with one of the listed tasks:
* patent
* csai
* financial
* all
```
$ python main.py --analysis [dataset name]
```

