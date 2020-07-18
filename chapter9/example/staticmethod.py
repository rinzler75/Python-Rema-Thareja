class Choice:
    def __init__(self,subjects):
        self.subjects=subjects
    @staticmethod
    def validate_subject(subjects):
        if "CSA" == subjects:
            print("This option is no longer available.")
        else:
            return True
subjects=["DS","CSA","FoC","OS","ToC"]
#all checks if all the elements in the iterable are true or not
if all(Choice.validate_subject(i) for i in subjects):
    ch=Choice(subjects)
    print("You have been alloted the subjects: ",subjects)