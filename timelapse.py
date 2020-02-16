#!/home/myuser/bin/python
# libraries to be imported 
import smtplib
import ffmpeg
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# create timelapse
print('start')
(
  ffmpeg
  .input('/Users/keithmock/Documents/Personal/timelapse/Camera1/**/{[0][56789],[1]*,[2][01]}-{[0][0369],[1][258],[2][147],[3][0369],[4][258],[5][147]}-00.jpg', pattern_type='glob', framerate=12)
  .output('movie.mp4')
  .overwrite_output()
  .run()
)

fromaddr = "parking.budddy@gmail.com"
toaddr = "parking.budddy@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Daily Timelapse"
  
# string to store the body of the mail 
body = "Here is today's timelapse from Window Cam"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "daily_timelapse.mp4"
attachment = open("movie.mp4", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "placeholder") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 
print('start')
#  .input('/Users/keithmock/Documents/Personal/timelapse/Camera1/**/{[0][56789],[1]*,[2][01]}-{[0][0369],[1][258],[2][147],[3][0369],[4][258],[5][147]}-00.jpg', pattern_type='glob', framerate=12)
