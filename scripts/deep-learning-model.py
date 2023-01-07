from transformers import AutoTokenizer, AutoModel

# Load the tokenizer and model from the "GroNLP/bert-base-dutch-cased" checkpoint
tokenizer = AutoTokenizer.from_pretrained("GroNLP/bert-base-dutch-cased")
model = AutoModel.from_pretrained("GroNLP/bert-base-dutch-cased")

# Define a function to predict the complexity score for a word
def predict_complexity(word: str) -> float:
  # Encode the word using the tokenizer and model
  input_ids = tokenizer.encode(word, return_tensors='pt')
  encoded_word = model(input_ids)[0]

  # Use the encoded representation to predict the complexity score
  complexity_score = model.predict(encoded_word)

  return complexity_score

# Test the function on a sample word
word = "complex"
score = predict_complexity(word)
print(f'Complexity score for "{word}": {score}')
