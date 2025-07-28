import string

def clean_string(sentence):
    return ''.join(
        c.lower() for c in sentence if c.isalnum()
    )

def reverse_string(sentence):
    return sentence[::-1]

def palindromo(sentence):
    cleaned = clean_string(sentence)
    return cleaned == reverse_string(cleaned)

print(palindromo("todo,,.odot"))
print(palindromo("miel leim"))
print(palindromo("Muy buenos dias!"))