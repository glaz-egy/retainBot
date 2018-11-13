# -*- coding: utf-8 -*-

import datetime
import sys
import os

UserhadoList = ['滲み出す混濁の紋章', '湧き上がり・否定し・痺れ・瞬き・眠りを妨げる', '絶えず自壊する泥の人形', '反発せよ', '破道の九十']
HadoList = ['不遜なる狂気の器', '爬行する鉄の王女', '結合せよ', '地に満ち己の無力を知れ', '『黒棺』']

UserUBWList = ['体は剣で出来ている', '幾たびの戦場を越えて不敗', 'ただ一度の勝利もなし', '剣の丘で鉄を鍛つ', 'この体は']
UBWList = ['血潮は鉄で心は硝子', 'ただ一度の敗走もなく、', '担い手はここに独り', 'ならば我が生涯に意味は不要ず', '無限の剣で出来ていた']
GreetingDict = {'mooning': [4, 5, 6, 7, 8, 9],
                'noon': [10, 11, 12, 13, 14, 15, 16, 17, 18],
                'night': [19, 20, 21, 22, 23, 24, 0, 1, 2, 3]}
TimeZone = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

class Bot:
    def __init__(self):
        self.__version__ = 'interabot version: 0.0.3\nCopyright (c) 2018 Glaz egy.'
        self.HadoFlag = False
        self.HadoIndex = 0
        self.UBWFlag = False
        self.UBWIndex = 0

    def Response(self, text):
        comment = None
        if text == UserhadoList[self.HadoIndex] and not self.UBWFlag:
            self.HadoFlag = True
            comment = HadoList[self.HadoIndex]
            self.HadoIndex += 1
            if self.HadoIndex > 4:
                self.HadoFlag = False
                self.HadoIndex = 0
        elif text == UserUBWList[self.UBWIndex] and not self.HadoFlag:
            self.UBWFlag = True
            comment = UBWList[self.UBWIndex]
            self.UBWIndex += 1
            if self.UBWIndex >= len(UBWList):
                self.UBWFlag = False
                self.UBWIndex = 0
        elif self.UBWFlag:
            comment = '固有結界が途中で止っちゃうよ'
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