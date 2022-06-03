import ezgmail, os
os.chdir(r'C:\Users\steve\Documents\GitHub\python-training\automate\Ch18-Sending_Email_Text')
ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')
ezgmail.send('史帝芬主帳號@gmail.com', 'Hi, Steven', 'This is thibe from python ezgmail.')
text = open('example.txt', 'w')
text.write('this is an example')
text.close()
ezgmail.send('史帝芬主帳號@gmail.com', 'Hi, Steven', 'This is thibe from python ezgmail.', ['example.txt'])
ezgmail.send('史帝芬主帳號@gmail.com', 'Hi, Steven', 'This is cc for you and thibe and also bcc to someone you do not know',
cc='史蒂芬副帳號@gmail.com', bcc='帳號@gmail.com')
for i in range(5):
    ezgmail.send('史蒂芬副帳號@gmail.com', f'Hi, steven{i}', f'This is testing{i} email from funky!')
ezgmail.EMAIL_ADDRESS
ezgmail.init(tokenFile='token01.json', credentialsFile='credentials.json')
unreadThreads = ezgmail.unread()
ezgmail.summary(unreadThreads)
len(unreadThreads)
str(unreadThreads[0])
len(unreadThreads[0].messages)
str(unreadThreads[0].messages[0])
unreadThreads[0].messages[0].subject
unreadThreads[0].messages[0].body
unreadThreads[0].messages[0].timestamp
unreadThreads[0].messages[0].sender
unreadThreads[0].messages[0].recipient
recentThreads = ezgmail.recent()
recentThreads
# searching
resultThreads = ezgmail.search('史帝芬主帳號')
len(resultThreads)
ezgmail.summary(resultThreads)
resultThreads_2 = ezgmail.search('subject:Hi')
len(resultThreads_2)
ezgmail.summary(resultThreads_2)
# download attachments
threads = ezgmail.search('some nice pics')
len(threads)
threads[0].messages[0].attachments
threads[0].messages[0].downloadAttachment('graduate.jpg')
threads[0].messages[0].downloadAllAttachments(downloadFolder='graduation2021')
# SMTP
# 彭彭版本
import email.message
msg = email.message.EmailMessage()
msg["From"]="帳號@gmail.com"
msg["To"]="帳號@gmail.com"
msg["Subject"]="This is a testing email"
msg.add_alternative("<div><h1>大驚喜</h1><div><a href='https://unsplash.com/'>在unsplash裡面發掘更多風景圖吧<a>", subtype="html")
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('帳號@gmail.com', '密碼')
server.send_message(msg)
server.close()
# 到網路上搜尋 gmail smtp server 或是 yahoo smtp server等等
# 課本版本
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo() # 250 means success
smtpObj.login('帳號@gmail.com', '密碼') # 235 means success
smtpObj.sendmail('帳號@gmail.com',
    '史帝芬主帳號@gmail.com',
    'Subject: So long. \nDear Steven, so long and thanks for all your help.\n'
    'Sincerely, Funky.')
smtpObj.quit()
# IMAP
from imapclient import IMAPClient
import email
server = IMAPClient('imap.gmail.com', use_uid=True)
server.login('帳號@gmail.com', '密碼')
select_info = server.select_folder('INBOX', readonly=True) # 防止意外刪掉Email，在用fetch()方法取得Email時，不會標示為已讀。
print('%d messages in INBOX' % select_info[b'EXISTS'])
select_info
server.search(['ALL'])
server.search(['DELETED'])
server.search(['Seen'])
server.search(['FLAGGED'])
server.search(['DRAFT'])
server.search(['RECENT'])
messages = server.search("UNSEEN")
for uid, message_data in server.fetch(messages, "RFC822").items():
    email_message = email.message_from_bytes(message_data[b"RFC822"])
    print(uid, email_message.get("From"), email_message.get("Subject"))
messages = server.search(['FROM', '帳號@gmail.com'])
messages = server.search(['ON', '18-Sep-2021'])
for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    print(f'ID #{msgid}: "{envelope.subject.decode()}" received {envelope.date}')
UIDs = server.search(['seen'])
rawMessages = server.fetch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[6][b'BODY[]'])
message.get_subject()
message.get_address('from')
message.get_address('to')
message.get_address('cc')
message.get_address('bcc')
message.text_part != None
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
server.select_folder('INBOX', readonly=False)
UIDs = server.search(['seen'])[0]
UIDs
server.delete_messages(UIDs) # Gmail 會自動清除用delete_messages()刪除的Email，不等IMAP客戶端呼叫expunge()
server.expunge()
server.logout()
# twilio
from twilio.rest import Client
accountSID = 'A你的SID'
authToken = '你的Token'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '我的號碼'
myCellPhone = '你的號碼'
message = twilioCli.messages.create(body='Mr. Wang - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)