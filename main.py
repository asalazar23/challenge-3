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

# SECTION ONE ---------------- DONE
lowerLet = let1.lower, let2.lower, let3.lower
upperLet = let1.upper, let2.upper, let3.upper
lowerTotal = text.count(let1) + text.count(let2) + text.count(let3)
upperTotal = text.count(let1) + text.count(let2) + text.count(let3)

print(lowerTotal)
print(upperTotal)
print("-------")
# SECTION TWO ---------------- DONE
two_list = text.split(" ")
print(len(two_list))

# SECTION THREE ---------------- DONE
print(text[0])
print(text[-1])

# SECTION FOUR
print(text[::-1])

# SECTION FIVE

p = "p" in text
y = "y" in text
t = "t" in text
h = "h" in text
o = "o" in text
n = "n" in text
python = 
print(python)

# im gonna push it hold up