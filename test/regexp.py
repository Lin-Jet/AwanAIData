import re

# https://www.youtube.com/watch?v=AEE9ecgLgdQ
# https://www.python-engineer.com/posts/regular-expressions/

test_string = '123abc456789abc123ABC'

pattern = re.compile("abc")
matches = pattern.finditer(test_string)

matches = re.finditer(r"abc", test_string)
print("finditer: \n")
for match in matches:
        print(match)

print('\n')
pattern = re.compile("abc")
matches = pattern.findall(test_string)

matches = re.findall(r"abc", test_string)

# match(), search(), findall(s)
print("findall: \n")
for match in matches:
        print(match)
print('\n')
# a = r"\tHello" #this is a raw string

# print(a)


#match() starts matching at beginning
pattern = re.compile("123")
match = pattern.match(test_string)

match = re.match(r"123", test_string)
print("match: \n")
print(match)

print('\n')


#will find first instance only
match = re.search(r"abc", test_string)

print("search: \n")
print(match)

#split and sub
print('\n')
print('\n')

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

# group, start, end, span]
for match in matches:
        print(match.span(), match.start(), match.end())
        print(match.group(0))

"""
Metacharacters are characters with a special meaning:
All meta characters: . ^ $ * + ? { } [ ] \ | ( )
Meta characters need need to be escaped (with ) if we actually want to search for the char.

. Any character (except newline character) "he..o"
^ Starts with "^hello"
\$ Ends with "world\$"
* Zero or more occurrences "aix*"
+ One or more occurrences "aix+"
{ } Exactly the specified number of occurrences "al{2}"
[] A set of characters "[a-m]"
\ Signals a special sequence (can also be used to escape special characters) "\d"
| Either or "falls|stays"
( ) Capture and group
"""

pattern = re.compile(r".")
matches = pattern.finditer(test_string)
print("meta char . : ")
for match in matches:
    print(match.span())


pattern = re.compile(r"^123a")
matches = pattern.finditer(test_string)
print("meta char ^ : ")
for match in matches:
    print(match)

"""
\d mathces any decimal digit
\D matches non digit
\s any whitespace char space " " tab "\t" newlline "\n"
\S any non whitespace character;
\w anyaphanumeric word char a-zA-Z0-9_
\W any non alphanumeric character
\b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
\A Returns a match if the specified characters are at the beginning of the string "\AThe"
\Z Returns a match if the specified characters are at the end of the string "Spain\Z"



"""


string_test = "hello 123_ heyhoh hohey"

pattern = re.compile(r"\Bhey")
matches = pattern.finditer(string_test)
print("\nthis is for blocks B: \n")
for match in matches:
    print(match.span())


string = "hello 123456789_AAZ--"

# pattern = re.compile(r"[lo]")
pattern = re.compile(r"[a-zA-Z5-8-]")
matches = pattern.finditer(string)
print("\nthis is for set: \n")
for match in matches:
    print(match)

#quanitifiers
"""
* : 0 or more
+ : 1 or more
? : 0 or 1, used when a character can be optional
{4} : exact number
{4,6} : range numbers (min, max)
"""


string1 = "hello_123456789 12345"

matches = re.finditer( r"_?\d+",  string1)
print("\n this is for quanitifiers: \n")
for match in matches:
    print(match)


dates = '''
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

matches = re.finditer(r"\d{4}[-/]\d[57][-/]\d{2}", dates)
print("\nthis is an exampel with dates: \n")
for match in matches:
    print(match)

print('\n')

my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""

pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s\w+")
matches = pattern.finditer(my_string)
print("This is for conditionals: \n")
for match in matches:
    print(match)
print('\n')


emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
pattern = re.compile(r"([a-zA-Z0-9-]+)@([a-z-]+)\.((com|de|org))")
matches = pattern.finditer(emails)
print("This is for Grouping: \n")
for match in matches:
    print(match.group(1))
print('\n')




#Modificatoins

#split(into a list), sub(all substrings find and then replace with diff string)

test_string = "123abc456789abc123ABC"
test2 = """[qa] hello this issome text123  
[asdf] helhihihihih3
[alksjdf] asdfasdflasdlfkjasdlfj
"""
pattern = re.compile(r"\[(\w+)\]\s(\w+)")
matches = pattern.finditer(test2)
q=[]
a=[]
for match in matches:
    q.append(match.group(1))
    a.append(match.group(2))

for i in q:
    print("[q] :", i)
for j in a:
    print("[a] :", j)




test_string = "123abc456789abc123ABC"
pattern = re.compile(r"45")
splitted = pattern.split(test_string)
print("Splits: \n")
print(splitted)
print('\n')

test_string = "hello world, you are the best world"
pattern = re.compile(r"world")
subbed_string = pattern.sub("planet", test_string)
print("Sub: \n")
print(subbed_string + '\n')




urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""

pattern = re.compile(r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
print("\nUrls: \n")
matches = pattern.finditer(urls)
for match in matches:
        print(match.group(0))

subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)
print("\n")

my_string = "Hello World"
pattern = re.compile(r"world", re.IGNORECASE)
matches = pattern.finditer(my_string)

for match in matches:
    print(match) 



