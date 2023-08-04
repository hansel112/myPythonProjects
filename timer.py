import time
class Reminder:
    def __init__(self):
        self.ltime = 1
        self.work = "please rest"
    def timer(self):
        self.ltime *=10
        time.sleep(self.ltime)
        print("%s because you have read for %d seconds."% (self.work, self.ltime))
d = Reminder()
d.timer()
