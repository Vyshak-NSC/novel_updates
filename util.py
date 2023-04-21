import re
from bs4 import BeautifulSoup as bs
from requests import get as get_url
from plyer import notification as notif

class LNChecker:
    def __init__(self,name):
        self.name = name
        self.response = self.generate_url()

    def generate_url(self):
        self.name = self.name.replace(" ","-").lower()
        url = "https://readnovelfull.me/" + self.name + "/"
        return get_url(url)

    def get_curr_chap(self):
        match = re.search("Latest chapter*(.*)", self.response.text)
        if match:
            res = bs(match.group(), "html.parser")
            title = res.find('a').get('title')
        else:
            title = "Novel not FOund"
        return title

    def get_prev_chap(self):
        with open("DDLatestChap.txt", "r") as fr:
            prev_chap = fr.read()
        return prev_chap

    def set_prev_chap(self,titlename):
        with open("DDLatestChap.txt", "w") as fw:
            fw.write(titlename)

    def notify_msg(self):
        msg_title = "Chapter updated for " + self.name.title()
        msg = "Latest chapter is " + self.get_curr_chap()
        notif.notify(title=msg_title,message=msg)

    def run(self):
        curr_chap = self.get_curr_chap()
        prev_chap = self.get_prev_chap()

        if not prev_chap:
            self.set_prev_chap(curr_chap)

        if curr_chap == prev_chap:
            return 0
        else:
            self.set_prev_chap(curr_chap)
            self.notify_msg()
