pip install transformers
pip install spacy
from transformers import pipeline
import spacy

llama_model = pipeline("text-generation", model="Llama/llama-base-0001", tokenizer="Llama/llama-base-0001")

nlp = spacy.load("en_core_web_sm")

def get_llama_output(question):
    llama_output = llama_model(question, max_length=200, num_return_sequences=1)
    raw_text = llama_output[0]['generated_text']
    
    return raw_text

def extract_entities(text):
    doc = nlp(text)
    entities = []
    
    for ent in doc.ents:
        entities.append((ent.text, ent.start_char, ent.end_char, ent.label_))
    
    return entities

# Example usage
question = "The capital of France is..."
raw_text = get_llama_output(question)
entities = extract_entities(raw_text)

print("Raw Text:")
print(raw_text)
print("\nEntities:")
for entity in entities:
    print(entity)
