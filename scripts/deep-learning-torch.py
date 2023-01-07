import torch
import torch.nn as nn
import torch.optim as optim

# Function to preprocess the text data
def preprocess_text(text):
    # Tokenize the text
    tokenizer = torch.preprocessing.text.Tokenizer(num_words=100)
    tokenizer.fit_on_texts([text])
    sequences = tokenizer.texts_to_sequences([text])
    data = torch.preprocessing.sequence.pad_sequences(sequences, padding='post', maxlen=100)
    return data

# Function to create a simple LSTM model
def create_model():
    model = torch.nn.Sequential(
        torch.nn.Embedding(input_dim=100, output_dim=50, input_length=100),
        torch.nn.LSTM(input_size=50, hidden_size=50, num_layers=1, batch_first=True, bidirectional=False),
        torch.nn.Linear(in_features=50, out_features=1),
        torch.nn.Sigmoid()
    )
    return model

# Function to simplify the text
def simplify_text(text):
    # Preprocess the text data
    data = preprocess_text(text)
    
    # Convert the data to a PyTorch tensor
    data = torch.tensor(data, dtype=torch.long)


print(simplify_text("de archaïsche globglob trespasseert van a naar b"))
    
   
