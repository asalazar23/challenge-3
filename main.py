# Adrian Salazar , Sam Zajczenko, and Andrzej Blachuta

# fork this challenge to your own repl
#share this challenge with another person in the room.

#Day 3 Python Challenge

# The task is as follows: You are going to create a program that first asks the user to enter text. It can be any text, an entire article, a paragraph, a sentence, a poem, whatever you want. Then the program will ask the user to enter three random letters. From that moment on, our code is going to process that information and result in five different types of analysis:

# 1. How many times each of those letters they have chosen appears. To achieve this, I advise you to store those letters in a list, and then use a method of strings that allows you to count how many times a substring appears within the string. One thing to keep in mind is that when searching for letters, there can be upper and lower case and this will affect the result. So, to make sure that absolutely all letters are counted, you should pass both the original text and the letters to be searched to lowercase.

# 2. How many words are in the whole text? To achieve this part, remember that there is a string method that allows us to transform it into a list. And then there is a function that allows us to find out the length of a list.

# 3. What are the first and last letters of the text? Here, we will clearly use indexing.

# 4. The system will show us how the text would look like if we inverted the order of the words. Is there any method that allows us to invert the order of a list? And another one that allows us to join these elements with spaces in between?

# 5. The system will tell us if the word “python” is inside the text. This part can be a bit complicated to imagine, but I'll give you a hint: you can use Booleans to make your enquiry and a dictionary to find ways to express your answer.


# SOURCES
text = input("Enter a work of literature: ")
let1 = input("Enter a random letter: ")
let2 = input("Enter a random letter: ")
let3 = input("Enter a random letter: ")
print("-------")
# SECTION ONE ---------------- DONE
upperlet1 = let1.upper()
upperlet2 = let2.upper()
upperlet3 = let3.upper()
lowerlet1 = let1.lower()
lowerlet2 = let2.lower()
lowerlet3 = let3.lower()
lowerTotal = text.count(upperlet1) + text.count(upperlet2) + text.count(upperlet3)
upperTotal = text.count(lowerlet1) + text.count(lowerlet2) + text.count(lowerlet3)
joined = lowerTotal + upperTotal

print("Total times letters appear: " + str(joined))
print("-------")
# SEClowerlet1TWO ---------------- DONE
two_list = text.split(" ")
print("Amount of words in the literature: " + str(len(two_list)))
print("-------")

# SECTION THREE ---------------- DONE
print("First letter: " + str(text[0]))
print("Last letter: " + str(text[-1]))
print("-------")
# SECTION FOUR ---------------- DONE
print("Reversed text: " + str(text[::-1]))
print("-------")
# SECTION FIVE ---------------- DONE
p = "python" in text
print("Is 'python' in the literature? " + str(p))


