import smtplib
import ssl
from time import sleep

import playsound
from gtts import gTTS

from rt import mail

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "internationalphotographer12@gmail.com"
password = input("enter your password")
recived = mail

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email

def send():
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()# Can be omitted
    server.starttls(context=context)# Secure the connection
    server.ehlo()# Can be omitted
    server.login(sender_email, password)
    subject = "this is bot message service"
    body = """
         your mail got hacked 
    
                    """

    msg = f"subject:{subject} \n\n {body}"
    server.sendmail(sender_email, recived, msg)
    speak("hey email sent")
    server.quit()


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)



x=0
for x in range(100):
    send()
    x = x + 1
    sleep(10)



# server.quit()