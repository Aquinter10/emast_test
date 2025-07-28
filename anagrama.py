def anagrama(word1, word2):
    return sorted(word1) == sorted(word2)

print(anagrama("miel","lime"))