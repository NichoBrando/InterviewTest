#Código refeito, pesquisando sobre alguns problemas que estavam ocorrendo
import random
import string

def addWord(words):
  sorting = random.choice([3, 5])
  lettersToSort = string.ascii_lowercase
  randomText = ''.join(random.choice(lettersToSort) for i in range(sorting))
  words.append(randomText)
  return words

def countPalindromes(words):
  palindromes = 0
  i = 0
  while(i < 10000):
    if words[i][:] == words[i][::-1]:
      palindromes += 1
    i += 1
  return palindromes

words = []
i = 0
while(i < 10000):
  words = addWord(words)
  i += 1
print("Quantidade de palíndromos: {}".format(countPalindromes(words)))