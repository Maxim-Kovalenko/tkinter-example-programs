import time as tm
import notifypy as ntp
import playsound as ps

ntimes = ['8:30', '9:25', '10:20', '11:25', '12:30', '13:25', '14:20', '15:15']

img = 'img/video-call.png'
startSfx = 'sfx/ntfsound.wav'

ntfStart = ntp.Notify()
ntfStart.application_name = 'Time Manager'
ntfStart.title = 'Enabled'
ntfStart.message = 'Notifier is now enabled'
ntfStart.audio = startSfx
ntfStart.icon = img
ntfStart.send(block=True)

path = 'sfx/asound.wav'
ntf = ntp.Notify()
ntf.icon = img
ntf.audio = path
ntf.application_name = 'Time Manager'

while True:
    timeNow = tm.localtime()
    hour = str(timeNow[3])
    minute = str(timeNow[4])
    sec = str(timeNow[5])
    """months = {1: 'Jan', 2: ' Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    days = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}"""
    strTime = hour + ':' + minute
    if ntimes[0] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '1st lesson starts (time now: %s)' % strTime
        ntf.message = '1st lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[1] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '2nd lesson starts (time now: %s)' % strTime
        ntf.message = '2nd lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[2] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '3rd lesson starts (time now: %s)' % strTime
        ntf.message = '3rd lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[3] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '4th lesson starts (time now: %s)' % strTime
        ntf.message = '4th lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[4] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '5th lesson starts (time now: %s)' % strTime
        ntf.message = '5th lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[5] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '6th lesson starts (time now: %s)' % strTime
        ntf.message = '6th lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[6] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '7th lesson starts (time now: %s)' % strTime
        ntf.message = '7th lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
    elif ntimes[7] == strTime:
        ntf.title = 'Lesson notification'
        #ntf.message = '8th lesson starts (time now: %s)' % strTime
        ntf.message = '8th lesson starts'
        ntf.send(block=True)
        tm.sleep(60)
