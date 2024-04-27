# Named Entity Recognition (NER) Application

This is a simple Python application that performs Named Entity Recognition (NER) on input text using the Natural Language Toolkit (NLTK) library.

## Overview

Named Entity Recognition (NER) is a natural language processing task that aims to identify and classify named entities mentioned in unstructured text into pre-defined categories such as names of persons, organizations, locations, etc.

This application utilizes NLTK, a popular Python library for natural language processing, to tokenize input text, tag words with their parts of speech (POS), and then identify named entities using a process called chunking.

## Prerequisites

- Python 3
- NLTK library

## Installation

1. Clone this repository:
git clone https://github.com/your-username/ner-application.git


2. Navigate to the project directory:
cd ner-application



3. Install the required dependencies using pip:
pip install -r requirements.txt



4. Run the application:
python ner_application.py



## Usage

1. When prompted, enter a sentence or text containing named entities.

2. Press Enter, and the application will identify and print the named entities found in the input text along with their corresponding categories.

## Example

Input:
Steve Jobs founded Apple Inc. in California.


Output:
(S
(PERSON Steve/NNP)
Jobs/NNP
founded/VBD
(ORGANIZATION Apple/NNP Inc./NNP)
in/IN
(GPE California/NNP)
./.)