# -*- coding: utf-8 -*-

import pickle

class Spell:
    def __init__(self, spellfile):
        self.SpellFile = spellfile
        try:
            self.SpellDic = self.LoadSpell(FileName=self.SpellFile)
        except FileNotFoundError:
            self.SpellDic = {}
            self.SaveSpell(self.SpellDic, FileName=self.SpellFile)

    def AddSpell(self, SpellData, SpellName):
        if SpellName in self.SpellDic.keys() and SpellData[0] in self.SpellDic['SpellList'].keys():
            return -1
        else:
            self.SpellDic[SpellName] = SpellData
            self.SpellDic['SpellList'] = {SpellData[0]: SpellName}
            self.SaveSpell(self.SpellDic, FileName=self.SpellFile)
    
    def CallSpell(self, SpellName, Index):
        return self.SpellDic[SpellName][Index]

    def SaveSpell(self, Data, FileName='spellmain.sp'):
        with open(FileName, 'wb') as f:
            pickle.dump(Data, f)

    def LoadSpell(self, FileName='spellmain.sp'):
        with open(FileName, 'rb') as f:
            SpellData = pickle.load(f)
        return SpellData
    
if __name__=='__main__':
    spells = Spell('test.sp')
    SpellName = '黒棺'
    print(spells.SpellDic)