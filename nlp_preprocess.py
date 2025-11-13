# nlp_preprocess.py

import spacy

# Load spaCy English model (install if missing: python3 -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Text to process
text = "John enjoys playing football while Mary loves reading books in the library."

# Apply spaCy NLP pipeline
doc = nlp(text)

# Get spaCy's stopword list
stop_words = nlp.Defaults.stop_words

# List to store processed tokens
clean_tokens = []

# Loop through each token and filter based on conditions
for tok in doc:
    is_valid_word = tok.text.lower() not in stop_words
    is_alpha_only = tok.is_alpha
    is_target_pos = tok.pos_ in ["NOUN", "VERB"]

    if is_valid_word and is_alpha_only and is_target_pos:
        clean_tokens.append(tok.lemma_.lower())  # Add lemmatized form

# Display results
print("Original Text:")
print(text)

print("\nProcessed Tokens (lemmatized nouns/verbs, stopwords removed):")
print(clean_tokens)
