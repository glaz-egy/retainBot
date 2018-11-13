# -*- coding: utf-8 -*-

import datetime
import sys
import os

UserhadoList = ['滲み出す混濁の紋章', '湧き上がり・否定し・痺れ・瞬き・眠りを妨げる', '絶えず自壊する泥の人形', '反発せよ', '破道の九十']
HadoList = ['不遜なる狂気の器', '爬行する鉄の王女', '結合せよ', '地に満ち己の無力を知れ', '『黒棺』']

UserUBWList = []
UBWList = []
GreetingDict = {'mooning': [4, 5, 6, 7, 8, 9],
                'noon': [10, 11, 12, 13, 14, 15, 16, 17, 18],
                'night': [19, 20, 21, 22, 23, 24, 0, 1, 2, 3]}
TimeZone = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

class Bot:
    def __init__(self):
        self.__version__ = 'interabot version: 0.0.3\nCopyright (c) 2018 Glaz egy.'
        self.HadoFlag = False
        self.HadoIndex = 0

    def Response(self, text):
        if text == UserhadoList[self.HadoIndex]:
            self.HadoFlag = True
            comment = HadoList[self.HadoIndex]
            self.HadoIndex += 1
            if self.HadoIndex > 4:
                self.HadoFlag = False
                self.HadoIndex = 0
        elif self.HadoFlag:
            comment = '今詠唱中だよ？　どうしたの'
        elif '今何時' in text:
            now = datetime.datetime.now(TimeZone)
            comment = '{}:{:02}だよ！'.format(now.hour, now.minute)
        elif 'おはよう' in text:
            now = datetime.datetime.now(TimeZone)
            if not now.hour in GreetingDict['mooning']:
                comment = 'おはようじゃないよ！　今、{}時だよ'.format(now.hour)
            else:
                comment = 'おはよう！'
        elif 'こんばん' in text:
            now = datetime.datetime.now(TimeZone)
            if not now.hour in GreetingDict['night']:
                comment = 'こんばんわじゃないよ！　今、{}時だよ'.format(now.hour)
            else:
                comment = 'こんばんわ！'
        elif 'こんにち' in text:
            comment = 'こんにちは！'
        elif text in UserhadoList:
            self.HadoFlag = True
            comment = HadoList[self.HadoIndex]
        return comment