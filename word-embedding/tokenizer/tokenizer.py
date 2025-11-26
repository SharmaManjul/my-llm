import re
from simple_tokenizer_v1 import SimpleTokenizerV1
from simple_tokenizer_v2 import SimpleTokenizerV2

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
all_words = sorted(list(set(stringTokens)))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocab_size = len(all_words)
print("Vocabulary size:", vocab_size)
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)
print('\n')

# Using the tokenizer_v1 class to encode and decode
print("Using SimpleTokenizerV1 to encode and decode:")
tokenizer = SimpleTokenizerV1(vocab)
sample_text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(sample_text)
print("Ids of encoded sample text:", ids)
decode_text = tokenizer.decode(ids)
print("Decoded text from ids:", decode_text)
print('\n')

# Using the tokenizer_v2 class to encode and decode
print("Using SimpleTokenizerV2 to encode and decode with unknown text:")
tokenizer_v2 = SimpleTokenizerV2(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
ids_v2 = tokenizer_v2.encode(text)
print("Ids of encoded sample text:", ids_v2)
decode_text_v2 = tokenizer_v2.decode(ids_v2)
print("Decoded text from ids:", decode_text_v2)
