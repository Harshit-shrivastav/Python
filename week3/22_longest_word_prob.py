while(words != -1):
  words = input()
  for word in words:
    if len(word) > len(word_store):
      word_store = word
print(f'Greatest word = {word_store}')
     