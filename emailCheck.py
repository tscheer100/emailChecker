import imapclient
import json
import smtplib
import time

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

with open("vars.json", 'r') as j:
    var = json.load(j)

user = var["username"]
pwd = var["password"]
target = var["target"]
num = str(var["phone"])
carrier = var["carrier"]
text = var["msg"]

conn.login(user, pwd)
conn.select_folder("INBOX")
UIDs = conn.search(['UNSEEN', ['FROM', target]])



# sets carrier list with corresponding email
carriers = {
    'att': '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com',
    'boost mobile': '@myboostmobile.com',
    'cricket': '@sms.mycricket.com',
    'metroPCS': '@mymetropcs.com',
    'tracfone': '@mmst5.tracfone.com',
    'US cellular': '@email.uscc.net',
    'virgin': '@vmobl.com'
}

while True:
    print(len(UIDs))

    if len(UIDs) >= 1:
        to_number = num + '{}'.format(carriers[carrier])
        auth = (user, pwd)

        # Establish a secure session with gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])

        # Send text message through SMS gateway of destination number
        server.sendmail(auth[0], to_number, text)
    else:
        pass

    time.sleep(600)