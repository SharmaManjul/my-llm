import tiktoken

print("tiktoken version:", tiktoken.__version__)
tokenizer = tiktoken.get_encoding("gpt2")

text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)

text2 = "akwirw ier"

text3 = "How are you? " 

integers = tokenizer.encode(text3, allowed_special={"<|endoftext|>"})
print("Encoded integers:", integers)

strings = tokenizer.decode(integers)
print("Decoded text:", strings)