class Student:
    def name(self):
        print('Name...')
class Academic_Performance(Student):
    def Acad_score(self):
        print("Academic score.....90% and above")
class ECA(Student):
    def ECA_score(self):
        print("ECA Score......60% and above")
class Result(Academic_Performance,ECA):
    def eligibility(self):
        print("*************Minimum Eligibility to Apply***************")
        self.name()
        self.Acad_score()
        self.ECA_score()
R=Result()
R.eligibility()