import re 

# Compile a regex pattern to match strings that consist only of uppercase letters
pattern=re.compile("^[A-Z]+$")


test_strings = ["HELLO", "World", "PYTHON", "code", "JAVA123"]
for string in test_strings:
    if pattern.match(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")


print("\n--- Complex Pattern Matching ---\n")

# Compile a more complex regex pattern
pattern=re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
test_strings = ["abc123!A", "xyz4567@BC", "ab12#D", "mnopq890$EFG", "abcde12345!"]
for string in test_strings:
    if pattern.match(string):
        print(f"'{string}' matches the complex pattern.")
    else:
        print(f"'{string}' does not match the complex pattern.")



print("\n--- Fixed Length String Matching ---\n")
# Compile a regex pattern to match strings that are exactly 10 characters long
pattern=re.compile("^.{10}$")
test_strings = ["abcdefghij", "123456 890", "abc13! #$", "short", "thisiswaytoolong"]      
for string in test_strings:
    if pattern.match(string):
        print(f"'{string}' is exactly 10 characters long.")
    else:
        print(f"'{string}' is not exactly 10 characters long.")


#next level regex
# + 0 or more
# * 1 or more
# ? 0 or 1
# ? optional
# . any character even space and special character but not newline ,\. is used to match dot
#\w alphanumeric character [a-zA-Z0-9_] \W non alphanumeric character
#\d digit [0-9] \D non digit    
#\s whitespace [ \t\n\r\f\v] \S non whitespace
# ^ start of string
# $ end of string
# {m} exactly m times
# {m,n} from m to n times   
# [] character set if [] contains - then its range [a-z] [0-9],[ax] means a or x
# | or operator
# () grouping ex: (abc){2} means abcabc, (t|T)he means t or T but t|T dosn't it says t or The
# lookbehaind 
#(?<=the). means get any char after word 'the' 
#(?<!the). means get any char dosn't have the word 'the' befor 
#lookahead it diffrent than lockbehaind by removing less than char
# .(?=the) get any char thats followed by 'the'
# .(?!the) get any char not followed by 'the'
#?<name> names a group

#Now code from Coursera


# There are several main processing functions in re that you might use. The first, match() checks for a match
# that is at the beginning of the string and returns a boolean. Similarly, search(), checks for a match
# anywhere in the string, and returns a boolean.

# Lets create some text for an example
text = "This is a good day."

# Now, lets see if it's a good day or not:
if re.search("good", text): # the first parameter here is the pattern
    print("Wonderful!")
else:
    print("Alas :(")

# In addition to checking for conditionals, we can segment a string. The work that regex does here is called
# tokenizing, where the string is separated into substrings based on patterns. Tokenizing is a core activity
# in natural language processing, which we won't talk much about here but that you will study in the future

# The findall() and split() functions will parse the string for us and return chunks. Lets try and example
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."

# This is a bit of a fabricated example, but lets split this on all instances of Amy
print(re.split("Amy",text))

# You'll notice that split has returned an empty string, followed by a number of statements about Amy, all as
# elements of a list. If we wanted to count how many times we have talked about Amy, we could use findall()
print(re.findall("Amy", text))

# Now that we know how the python regex API works, lets talk about more complex patterns. The regex
# specification standard defines a markup language to describe patterns in text. Lets start with anchors.
# Anchors specify the start and/or the end of the string that you are trying to match. The caret character ^
# means start and the dollar sign character $ means end. If you put ^ before a string, it means that the text
# the regex processor retrieves must start with the string you specify. For ending, you have to put the $
# character after the string, it means that the text Regex retrieves must end with the string you specify.

# Here's an example
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."

# Lets see if this begins with Amy
if re.search("^Amy",text):
    print("found at first")
else :
    print("not found at first")
# Notice that re.search() actually returned to us a new object, called re.Match object. An re.Match object
# always has a boolean value of True, as something was found, so you can always evaluate it in an if statement
# as we did earlier. The rendering of the match object also tells you what pattern was matched, in this case
# the word Amy, and the location the match was in, as the span.



# Patterns and Character Classes
# Let's talk more about patterns and start with character classes. Let's create a string of a single learners'
# grades over a semester in one course across all of their assignments
grades="ACAAAABCBCBAA"

# If we want to answer the question "How many B's were in the grade list?" we would just use B
print(re.findall("B",grades))

# If we wanted to count the number of A's or B's in the list, we can't use "AB" since this is used to match
# all A's followed immediately by a B. Instead, we put the characters A and B inside square brackets
print(re.findall("[AB]",grades))

# This is called the set operator. You can also include a range of characters, which are ordered
# alphanumerically. For instance, if we want to refer to all lower case letters we could use [a-z] Lets build
# a simple regex to parse out all instances where this student receive an A followed by a B or a C
print(re.findall("[A][B-C]",grades))

# Notice how the [AB] pattern describes a set of possible characters which could be either (A OR B), while the
# [A][B-C] pattern denoted two sets of characters which must have been matched back to back. You can write
# this pattern by using the pipe operator, which means OR
print(re.findall("AB|AC",grades))

# We can use the caret with the set operator to negate our results. For instance, if we want to parse out only
# the grades which were not A's
print(re.findall("[^A]",grades))


# Note this carefully - the caret was previously matched to the beginning of a string as an anchor point, but
# inside of the set operator the caret, and the other special characters we will be talking about, lose their
# meaning. This can be a bit confusing. What do you think the result would be of this?
print(re.findall("^[^A]",grades))

# It's an empty list, because the regex says that we want to match any value at the beginning of the string
# which is not an A. Our string though starts with an A, so there is no match found. And remember when you are
# using the set operator you are doing character-based matching. So you are matching individual characters in
# an OR method.

# Quantifiers

# Quantifiers are the number of times you want a pattern to be matched in order to match. The most basic
# quantifier is expressed as e{m,n}, where e is the expression or character we are matching, m is the minimum
# number of times you want it to matched, and n is the maximum number of times the item could be matched.

# Let's use these grades as an example. How many times has this student been on a back-to-back A's streak?
print(re.findall("AA{2,10}",grades)) # we'll use 2 as our min, but ten as our max

# So we see that there were two streaks, one where the student had four A's, and one where they had only two
# A's

# We might try and do this using single values and just repeating the pattern
print(re.findall("A{1,1}A{1,1}",grades))

# As you can see, this is different than the first example. The first pattern is looking for any combination
# of two A's up to ten A's in a row. So it sees four A's as a single streak. The second pattern is looking for
# two A's back to back, so it sees two A's followed immediately by two more A's. We say that the regex
# processor begins at the start of the string and consumes variables which match patterns as it does.

# It's important to note that the regex quantifier syntax does not allow you to deviate from the {m,n}
# pattern. In particular, if you have an extra space in between the braces you'll get an empty result
print(re.findall("A{2,2}",grades))
# And as we have already seen, if we don't include a quantifier then the default is {1,1}
print(re.findall("AA",grades))
# Oh, and if you just have one number in the braces, it's considered to be both m and n
print(re.findall("A{2}",grades))
# Using this, we could find a decreasing trend in a student's grades
print(re.findall("A{1,10}B{1,10}C{1,10}",grades))
# Now, that's a bit of a hack, because we included a maximum that was just arbitrarily large. There are three
# other quantifiers that are used as short hand, an asterix * to match 0 or more times, a question mark ? to
# match one or more times, or a + plus sign to match one or more times. Lets look at a more complex example,
# and load some data scraped from wikipedia
with open("regex/ferpa.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen
print(wiki)