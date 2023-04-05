class NotEnoughUniqueLetters(Exception):
  pass


def most_common_letters(string):
  # remove the spaces
  string = string.replace(" ", "")

  #create a dictionary and store each character
  letters = {}

  #go through each letter and count amount of them
  for letter in string.lower():  #make all letters lower case
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1

  #list the letters in order of count reversed so highest first
  sorted_letters = sorted(letters, key=lambda x: letters[x], reverse=True)

  # If there are at least three letters in the sentence, return the first three
  unique_letters = len(letters.keys())
  if unique_letters < 3:
    raise NotEnoughUniqueLetters(
      "The sentence does not contain enough unique letters.")
  else:
    common_letters = sorted_letters[:3]
    return common_letters


print(most_common_letters("tapppasaaas"))