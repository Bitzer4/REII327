from subprocess import call
f = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/measurements.txt measurements.txt"
call ([f], shell=True)

