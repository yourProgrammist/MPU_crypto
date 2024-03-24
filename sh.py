from random import choice

output = ""
for i in range(1024):
    output += choice(list("0123456789abcdef"))
print(output)
