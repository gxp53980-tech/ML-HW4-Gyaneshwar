# ner_pronoun_check.py

import spacy

# Load spaCy English model (install if needed: python3 -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Text to analyze
text = "Chris met Alex at Apple headquarters in California. He told him about the new iPhone launch."

# Process the text
doc = nlp(text)

# --- Named Entity Recognition ---
print("Named Entities, their labels, and explanations:\n")
for entity in doc.ents:
    label = entity.label_
    description = spacy.explain(label)
    print(f"{entity.text} --> {label} ({description})")

# --- Pronoun Ambiguity Check ---
pronouns_to_check = {"he", "she", "they", "him", "her", "them"}

# Identify pronouns present in the text
found_pronouns = [token.text.lower() for token in doc if token.text.lower() in pronouns_to_check]

if found_pronouns:
    print("\n⚠️ Warning: Possible pronoun ambiguity detected!")
    print(f"Pronouns found: {set(found_pronouns)}")
else:
    print("\nNo pronoun ambiguity detected.")
