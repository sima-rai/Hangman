import random

guess_words=['apple', 'banana']
word=random.choice(guess_words)
length=len(word)
display=  "_" * length


print(word)

guess=input("enter your guess")
guess=guess.strip()


if guess in word:
  index=word.find(guess) #so yo function le index return garcha
  print(index)
  word=word[:index]+ "_" + word[index+1:]
  print(word)
  display= display[:index] + guess + display[index+1:]
  print(display)