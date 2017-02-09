import smtplib 


from_addr = 'info3180.ainsley@gmail.com' 
to_addr = 'ainsley.denton47@gmail.com' 
message = """From: {} <{}> 
To: {} <{}> 
Subject: {}


 
{} 
"""

from_name = "Info3180 Ainsley"
to_name = "Ainsley Denton"
subject = "Hey there!"
msg = "Hello world! This is a message to you!"


message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 


# Credentials (if needed) 
username = 'info3180.ainsley@gmail.com' 
password = 'p@$$w0rd!!!' 


# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 
