NLP Preprocessing with spaCy

This project demonstrates a simple Natural Language Processing (NLP) pipeline using spaCy to preprocess text.
The script removes stopwords, filters nouns and verbs, and applies lemmatization to generate clean, meaningful tokens.

Features

Uses spaCy's English model (en_core_web_sm)

Removes:

Stopwords

Non-alphabetic tokens

Keeps only:

Nouns

Verbs

Converts all tokens to lemmatized lowercase forms

Outputs the original text and the final list of processed tokens

Technologies Used

Python 3

spaCy

Installation

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Install required dependencies:

pip install spacy


Download the spaCy English model:

python3 -m spacy download en_core_web_sm

Usage

Run the script using:

python3 nlp_preprocess.py

Example Output
Original Text:
John enjoys playing football while Mary loves reading books in the library.

Processed Tokens (lemmatized nouns/verbs, stopwords removed):
['enjoy', 'play', 'football', 'love', 'read', 'book', 'library']

File Structure
├── nlp_preprocess.py
├── README.md

Contributions

You may submit issues or pull requests to improve preprocessing, add new features, or enhance documentation.

License

This project is open-source and available under the MIT License.
