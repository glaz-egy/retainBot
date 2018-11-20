# -*- coding: utf-8 -*-

import pickle

class Study:
    def __init__(self, studyfile):
        self.StudyFile = studyfile
        try:
            self.StudyDic = self.LoadStudy(filename=self.StudyFile)
        except:
            self.StudyDic = {}
            self.SaveStudy(self.StudyDic, filename=self.StudyFile)
    
    def AddStudy(self, Subject, Unit, Ques, Ans):
        if not Subject in self.StudyDic.keys():
            self.StudyDic[Subject] = {Unit: {}}
        if not Unit in self.StudyDic[Subject].keys():
            self.StudyDic[Subject][Unit] = {}
        for i in range(len(Ques)):
            self.StudyDic[Subject][Unit][Ques[i]] = Ans[i]

        self.SaveStudy(self.StudyDic, filename=self.StudyFile)

    def DelStudy(self, DelObj, delkey):
        if delkey == 'Ques':
            try:
                for Subject in self.StudyDic.keys():
                    for Unit in Subject.keys():
                        del self.StudyDic[Subject][Unit][DelObj]
            except:
                return -1
        elif delkey == 'Unit':
            try:
                for Subject in self.StudyDic.keys():
                    del self.StudyDic[Subject][DelObj]
            except:
                return -2
        elif delkey == 'Subject':
            try:
                del self.StudyDic[DelObj]
            except:
                return -3
        else: return -4
        self.SaveStudy(self.StudyDic, filename=self.StudyFile)
    
    def LoadStudy(self, filename='StudyMain.sf'):
        with open(filename, 'rb') as f:
            StudyDic = pickle.load(f)
        return StudyDic
    
    def SaveStudy(self, Data, filename='StudyMain.sf'):
        with open(filename, 'wb') as f:
            pickle.dump(Data, f)
        
if __name__=='__main__':
    study = Study('test.sf')
    Subject = 'tset'
    Unit = 'test1'
    """
    while True:
        ques, ans = input('::').split(',')
        if ques == ans:
            break
        study.AddStudy(Subject, Unit, [ques,], [ans,])
    """
    for ques, ans in study.StudyDic[Subject][Unit].items():
        print(ques)
        a = input('Ans>')
        if ans == a: print('correct answer')
        else: print('fail')