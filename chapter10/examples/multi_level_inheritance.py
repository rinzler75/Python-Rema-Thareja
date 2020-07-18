class Person:
    def name(self):
        print("Name...")
class Teacher(Person):
    def Qualification(self):
        print("Qualifiction ..... Ph.D must")
class HOD(Teacher):
    def experience(self):
        print("Experience......at least 15 years")
hod = HOD()
hod.name()
hod.Qualification()
hod.experience()
