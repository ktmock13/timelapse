#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import smtplib
import ffmpeg
import string
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from email.message import EmailMessage
import time
from datetime import date

#sample set
every_three_mins_06thru20 = '{[0][6789],[1][0123456789],[2][0]}-{[0][0369],[1][258],[2][147],[3][0369],[4][258],[5][147]}-00'
every_one_min_06thru20 = '{[0][6789],[1][0123456789],[2][0]}-{[012345][0123456789]}-00'

photos_path = '/Users/keithmock/Documents/Personal/timelapse/Camera1/%s/%s.jpg' % (date.today().isoformat(), every_one_min_06thru20)

# test_photos_path = '/Users/keithmock/Documents/Personal/timelapse/TESTDATA/*.jpg'

print(photos_path)
# create timelapse
print('start')
(
  ffmpeg
  .input(photos_path, pattern_type='glob', framerate=60)
  .output('movie.mp4')
  .overwrite_output()
  .run()
)

me = 'parking.budddy@gmail.com'
to_emails = ['parking.budddy@gmail.com', 'alyssaneubauer@icloud.com', 'apascal07@gmail.com']



# Create the container email message.
msg = EmailMessage()
msg['Subject'] = 'SF DAILY TIMELAPSE'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = me
msg['To'] = ', '.join(to_emails)
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

filename = "daily_timelapse.mp4"
attachment = open("movie.mp4", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.add_attachment(p) 


s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(me, 'placeholder') 
s.send_message(msg) 
s.quit() 
print('done')
