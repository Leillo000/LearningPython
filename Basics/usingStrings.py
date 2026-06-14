"""

I skipped some steps, but this is a way to define a variable or constant in python, 
we can specify the type, but it's optional, i like to specify to have a better readable code.
All this file and their comments aren't mine, they are from the official Python documentation.

"""

# Str means string
myFirstString : str = "This is an example of how to declarate a string in Python"

# This is another way to define a variable
mySecondString = "\"This is a way to quote a quote inside strings\""

# Jump between lines
jumpLine : str = "First Line \nSecond Line"

# If we don't want to create tab or newline, we adjust by adding r before our string to obtain a "raw string"
# r means raw string

# Example without r
withoutR : str = 'C:\this\name'

# Example with r
withR : str = r'C:\this\name'

# Multiline String - We can use it by adding """ and ending with """
multiLine : str = """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

# Concatenate string
finalExpresion : str = "?"
concatenate : str = "Hello everyone, " + "how old are you" * 3 + finalExpresion * 2

word = "Hello Alexa!"

# We can index the string
indexString : str = word

# We can exlude strings, by slicing them
# We start from position 0 (included) to position 5 (excluded)
slicedWord : str = word[0 : 5]

"""

Another examples for sliced words:

word[:2]   # character from the beginning to position 2 (excluded)
Output: He

word[4:]   # characters from position 4 (included) to the end
Output: o Alexa!

word[-2:]  # characters from the second-last (included) to the end
Output: a!


============== Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s: ==============

********************

word[:2] + word[2:]

(word[:2])  (word[2:])
'He         llo Alexa!

********************
  
word[:4] + word[4:]

(word[:2])  (word[2:])
'Hell'      'o Alexa!'

********************

"""

print(myFirstString)
print(mySecondString)
print(jumpLine)
print(withoutR)
print(withR)
print(multiLine)
print(concatenate)

# This is an example for indexing strings

# Position 0 of the string is 'H'
print(indexString[0])
# Position 11 of the string is '!'
print(indexString[11])
# Is the same, but counting from the right (the string), position -1 is '!', too
# In negative, 1 is really position 1, and not 0.
print(indexString[-1])
print(slicedWord)