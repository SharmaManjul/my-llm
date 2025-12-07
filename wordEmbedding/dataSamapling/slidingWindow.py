import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

encoded_text = tokenizer.encode(raw_text)
print(len(encoded_text))

encoded_sample = encoded_text[50:]

context_size = 4
x = encoded_sample[:context_size]
y = encoded_sample[1:context_size+1]
print(f"x: {x}")
print(f"y:      {y}")

for i in range(1, context_size+1):
    context = encoded_sample[:i]
    desired = encoded_sample[i]

    print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))