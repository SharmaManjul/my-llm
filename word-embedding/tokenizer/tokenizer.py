import re
from simple_tokenizer_v1 import SimpleTokenizerV1

# Reading the raw text file
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total no. of characters:", len(raw_text))
print(raw_text[:99])
print('\n')

# Creating string tokens by splitting on punctuation and whitespace
stringTokens = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
stringTokens = [item.strip() for item in stringTokens if item.strip()]
print("Total no. of string tokens:", len(stringTokens))
print("First 20 string tokens:", stringTokens[:30])
print('\n')

# Creating sorted vocabulary of unique tokens
all_words = sorted(set(stringTokens))
vocab_size = len(all_words)
print("Vocabulary size:", vocab_size)
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(list(vocab.items())[:6]):
    print(item)
print('\n')

# Using the tokenizer class to encode and decode
tokenizer = SimpleTokenizerV1(vocab)
sample_text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(sample_text)
print("Ids of encoded sample text:", ids)
decode_text = tokenizer.decode(ids)
print("Decoded text from ids:", decode_text)