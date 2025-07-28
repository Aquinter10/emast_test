def reverse_string(sentence):
    return sentence[::-1]
def palindromo(sentence):
    return sentence == reverse_string(sentence)

print(palindromo("radar"))