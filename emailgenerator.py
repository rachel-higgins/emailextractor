'''This python script uses the modules random, string, and pyperclip to 
generate a block of text that contains 10 emails inserted within the block of 
text. This was created to test the email extractor app in this directory.
Pyperclip is used to automatically copy the block of text to the clipboard.
The best way to use these two scripts is to run app.py and while it waits for 
a new paste, run email emailgenerator.py. app.py will then take care of the 
rest.
'''

import random
import string
import pyperclip

# Generate 10 random emails
emails = []
for i in range(10):
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
    domain = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 5)))
    tld = ''.join(random.choices(['com', 'net', 'org'], weights=[0.6, 0.3, 0.1]))
    email = f'{username}@{domain}.{tld}'
    emails.append(email)

# Join the emails into a block of text with random words
words = []
for i in range(100): 
    word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))
    words.append(word)
    if i in [4, 10, 17, 19, 38, 39, 44, 59, 79, 99]:
        words.append(random.choice(emails))
text = ' '.join(words)

# Copy the block of text to the clipboard
pyperclip.copy(text)

# Let the user know the text has been copied to the clipboard
print('The block of text has been copied to the clipboard.')
