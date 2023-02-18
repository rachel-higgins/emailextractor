'''This python script uses the modules re and pyperclip. It takes a new block 
of text and parses through to find and extract every email. It uses pyperclip 
to wait for new text to appear on the clipboard and then processes the text,  
opens emails.txt and writes each email on a new single line. The script 
emailgenerator.py found in this directory can be ran at the point that app.py 
is requesting new text. The email generateor script is for testing the email 
extractor only.
'''

import re
import pyperclip

# Ask the user for new text
print('Please copy some new text to extract email addresses:')
pyperclip.waitForNewPaste()
text = pyperclip.paste()

# Use find all to retrieve emails in the text
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Writes each email to the file on a new line
with open('emails.txt', 'w') as email_file:
    for email in emails:
        email_file.write(email + '\n')
    # Lets the user know the extraction is complete
    print(f'{len(emails)} emails found and saved to emails.txt')
    email_file.close()
