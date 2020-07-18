class Marks:
    def __init__(self):
        self.max_marks={"Maths":100,"Computers":50,"SST":100,"Science":75}
    def __contains__(self,sub):
        if sub in self.max_marks:
            return True
        else: 
            return False
    def __getitem__(self,sub):
        return self.max_marks
    def __str__(self):
        return "The dictionary has name of subjects and maximum marks alloted to them"
M=Marks()
print(str(M))
sub=input("Enter the subject for which you want to know extra marks: ")
if sub in M: #control goes to the contain part
    print("Social Studies paper has maximum marks alloted = ",M[sub])