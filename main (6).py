# This function returns the entirety of "Dracula" as a string
from sre_constants import CATEGORY_UNI_NOT_DIGIT
from typing import Counter

# Function to display Dracula text
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

# Lowers the letters and splits the text 
dracula = readBook()
text = dracula.lower().split()

# Prints 'Result' title
print("=== Results ===")
# Empty Print statement
print()

# 1. How many four letter words are there
# List for fourletterwords
fourletterwords = []
# Go through each word in the book
for word in text:
# If the length of the word is four letters add to the list(NO Repeats)
  if(len(word)== 4 and word not in fourletterwords):
# Add the word to the list 
    fourletterwords.append(word)

# Print the number of four letter words
print(f"There are {len(fourletterwords)} words that are four letters long.")
print()

# 2. Every word that shows up 500 times or more
# Create an empty collection that holds words and the number of times they show up
print("These words show up 5,000 times or more: ")
count = {}
# Go through each word in the text
for word in text:
# If it's already in our collection, add one to the count
 if word in count:
   count[word] += 1
# Otherwise just count the word
 else:
   count[word] = 1
# Go through each key, value in the collection created
for key,value in count.items():
# Find the keys that have a value of 500 or more
  if(value >= 500):
# Print the word and the number of times it shows up
    print(f"{key} - {value}")

# 3. Word that shows up the most
# Create an empty collection that holds words and the number of times they show up
count = {}
# Go through each word in the text
for word in text:
# If it's already in our collection, add one to the count
 if word in count:
   count[word] += 1
# Otherwise just count the word
 else:
   count[word] = 1
# Go through each key, value in the collection created
for key,value in count.items():
# Find the key with the highest value:
  if(value > 7000):
# Empty print statement
    print()
# Print statment for the word that shows up the most
    print(f"'the' is the words that appears the most, a total of {value} times")
