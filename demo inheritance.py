import time
import webbrowser
class Reminder:
    def __init__(self):
        self.ltime = 1
        self.work = "please rest"
    def timer(self):
        start = 'T'
        while start == 'T':
            time.sleep(self.ltime*4)
            print(self.work)
            webbrowser.open('http://www.youtube.com')
            time.sleep(4)
            start = input('would you like to continue:')
       
d = Reminder()
d.timer()
