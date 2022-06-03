import random
import ezgmail
import os
import time
os.chdir(r'C:\Users\steve\Documents\GitHub\python-training\automate\Ch18-Sending_Email_Text')

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
emails = ['abcd@gmail.com',
          'efgh@gmail.com',
          'ijkl@gmail.com',
          'opqr@gmail.com']
# maybe can be the indicies for the next round of random chores.
email_dict = {}


def assignment():
    for i in range(len(chores)):
        randomChore = random.choice(chores)
        randomEmail = random.choice(emails)
        email_dict[randomEmail] = randomChore
        ezgmail.send(randomEmail, f"Today's chore: {randomChore}",
                     f'You need to finish {randomChore} before 18p.m.')
        chores.remove(randomChore)
        emails.remove(randomEmail)


ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')
# This program will sleep for 24 hours and execute through a loop for seven days.
for i in range(7):
    assignment()
    time.sleep(86400)
