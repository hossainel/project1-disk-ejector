# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 23:42:47 2018

@author: M Safayet El Hossain
"""
#!/usr/bin/python3

from platform import system as platform_name
from os import system
import ctypes
import time

class CD(object):
    def __init__(self, t):
        self.x = None
        self.t = t
        self.platforms_dictionary = {
            "Windows": {
                        "open" : 'ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)',
                        "close": 'ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)'
                       },
            "Darwin":  {
                        "open" : 'system("drutil tray open")',
                        "close": 'system("drutil tray closed")'
                       },
            "Linux":   {
                        "open" : 'system("eject cdrom")',
                        "close": 'system("eject -t cdrom")'
                       },
            "NetBSD":  {
                        "open" : 'system("eject cd")',
                        "close": 'system("eject -t cd")'
                       },
            "FreeBSD": {
                        "open" : 'system("sudo cdcontrol eject")',
                        "close": 'system("sudo cdcontrol close")'
                       }
        }
        self.runner()

    def runner(self):
        if platform_name() in self.platforms_dictionary:
            exec(self.platforms_dictionary[platform_name()]["open"])
            self.x = "Tray is opened"
            time.sleep(self.t)
            exec(self.platforms_dictionary[platform_name()]["close"])
        else:
            self.x = "Sorry, no OS found"
