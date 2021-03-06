
import random
import words

file = open("words.py", "r")
file = file.readline().strip("['[\"")

fileList = file.split("\",\"")

def valid_word(fileList):
  word = random.choice(fileList)
  while "-" in word or " " in word or len(word) < 5:
    word = random.choice(fileList)
  return word

letterGuess = ""

while True:
  underscList = []
  wrGuessList = []
  guessedList = []
  guessesLeft = 10

  print("\nLet's play hangman!")

  word = valid_word(fileList)

  print("\nYour word has", len(word), "letters.")

  # creates underscore list size of word for display
  for char in word:
    underscList.append("_")

  print()

  for item in underscList:
    print(item, end = " ")

  print()

  while guessesLeft > 0 and underscList.count("_") > 0:
    print("\nYou have", guessesLeft, "wrong guesses remaining.")

    letterGuess = input("\nGuess a letter, or 'quit' to exit: ")
    if letterGuess.lower() == 'quit':
      break

    # Counts number of letterGuess in word
    letterCount = word.count(letterGuess.lower())
    if letterCount > 0:
      print("\nNice! Your letter is in the word")


    # for len(word) num of times, check if each index in word matches letter guessed
      for x in range(len(word)):
        # then change each instance in underscore display list
        if word[x] == letterGuess.lower():
          underscList[x] = letterGuess.upper()

    else:
      print("\nSorry, that letter is not in the word.")
      wrGuessList.append(letterGuess)
      guessesLeft-=1

    # display part of word visible
    for item in underscList:
      print(item, end = " ")

    print("\n")

    # display wrong letters already guessed
    print("Previous guesses: ")
    for item in wrGuessList:
      print(item.upper(), end = " ")

  print("\n\nYour word was:\n" + word.upper())
  if underscList.count("_") > 0:
    print("\n\nBetter luck next time!")
  else:
    print("\nGood job!")

  play = input("\nPlay again? Y/N: ")
  if play.lower().startswith("y") == False:
    break
  elif letterGuess == "quit":
    break