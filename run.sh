echo "CREATING TIMELAPSE" >> ~/Documents/Personal/timelapse/CRON.log 2>&1 && 
say creating timelapse &&
date >> ~/Documents/Personal/timelapse/CRON.log 2>&1 &&
#CLEANUP OLD TIMELAPSE FILES
rm ~/Documents/Personal/timelapse/movie.mp4 >> ~/Documents/Personal/timelapse/CRON.log 2>&1 | bash &&
# python3 command to create movie
PYTHONPATH=/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 ~/Documents/Personal/timelapse/timelapse_improved.py >> ~/Documents/Personal/timelapse/CRON.log 2>&1 &&
rm -rf Camera1/**/* &&
say timelapse created &&
echo "TIMELAPSE CREATED" >> ~/Documents/Personal/timelapse/CRON.log 2>&1

