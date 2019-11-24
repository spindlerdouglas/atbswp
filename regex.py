import re

#myRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #groups
myRegex = re.compile(r'\(\d\d\d\)-(\d\d\d)-(\d\d\d\d)') #groups
mo = myRegex.search('My number is (415)-555-4242') #string to be searched
#print(mo.group(1), mo.group(2), mo.group(3))
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())


batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())


batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())


batRegex = re.compile(r'Bat(wo)+man')
#mo = batRegex.search('The Adventures of Batman)
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())


regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())


digitRegex = re.compile(r'(\d){3,5}')  # python uses greedy matching
mo = digitRegex.search('1234567890')
print(mo.group())

digitRegex = re.compile(r'(\d){3,}')  # 3 or more digits
mo = digitRegex.search('1234567890')
print(mo.group())


digitRegex = re.compile(r'(\d){3,5}?')  # character '?' to use non-greedy matching
mo = digitRegex.search('1234567890')
print(mo.group())


vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'
lettersRegex = re.compile(r'[a-z]')

vowelRegex = re.compile(r'[^aeiouAEIOU]') # exclusion list

beginsWithHelloRegex = re.compile(r'^Hello')   # ^ = must exist at start
beginsWithHelloRegex.search('Hello there!')
beginsWithHelloRegex.search('He said "Hello"')  # does not match

endsWithWorldRegex = re.compile(r'world!$')   # $ = must exist at end


atRegex = re.compile(r'.at')    # . means any character except new line
atRegex.findall('The cat in the hat sat on the flat mat.')   # flat is not retrieved -> only 'lat'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: Douglas Last Name: Spindler')

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
nongreedy.findall(serve)

greedy = re.compile(r'<(.*)>')
greedy.findall(serve)


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')   # DOT stops at new line character
mo = dotStar.search(prime)
print(mo.group())

dotStar = re.compile(r'.*', re.DOTALL)  #DOTALL to match all characters including \n
mo = dotStar.search(prime)
print(mo.group())

vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE) # or re.I


namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))


# re.VERBOSE allows for whitespace and comments into the regex string
re.compile(r'''
(\d\d\d-)|      # area code (without parens, with dash)
(\(\d\d\d\) )   # -or- area code with parens and no dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last 4 digits
\sx\d{2,4}  # extension, like x1234
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)     # bitwise OR operator to pass multiple arguments into one single parameter


