import email, imaplib
import time
import datetime


# disregard this - scratch file for fun

# def get_latest_email_subject():
#     m = imaplib.IMAP4_SSL("imap.gmail.com")
#     m.login('amishmenon', 'mghpgyvwtadwqeif')
#     date = (datetime.date.today() - datetime.timedelta(minutes=1)).strftime("%d-%b-%Y")
#     m.select('"TradingView"')
#     resp, items = m.search(None, '(FROM TradingView SENTSINCE {date})'.format(date=date))
#     items = items[0].split()
#     for emailid in items:
#         resp, data = m.fetch(emailid,"(RFC822)")
#         email_body = data[0][1]
#         mail = email.message_from_bytes(email_body)
#         try:
#             subject = mail['Subject']
#             if 'TradingView Alert' in subject:
#                 return subject
#         except Exception as e:
#             print(e)



