import re

print('Enter a potential password:')
password = input()

# pw must contain a letter.
pass8regex = re.compile(r'[A-Za-z]')
pass1 = pass8regex.search(password)

# pw must have upper case letter.
passupregex = re.compile(r'[a-z]*[A-Z]+[a-z]*') 
pass2 = passupregex.search(password)

# pw must have a digit.
passdigitregex = re.compile(r'[A-Za-z]*[0-9]+[A-Za-z]*')
pass3 = passdigitregex.search(password)

  
if len(password) < 8:
    print('[WEAK PASSWORD: LESS THAT 8 CHARACTERS]')
elif pass1 == None:
    print('[WEAK PASSWORD: NO LETTER CHARACTER]')
elif pass2 == None:
    print('[WEAK PASSWORD: NO UPPERCASE LETTER]')
elif pass3 == None:
    print('[Weak password: No digit character]')
else:
    print('[STRONG PASSWORD]')

