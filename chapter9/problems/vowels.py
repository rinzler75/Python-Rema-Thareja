class vowels:
    def __init__(self,first_word):
        pass
    @staticmethod
    def check(first_word):
        if first_word in "aeiouAEIOU":
            return True
        else:
            return False
words=["kumar",'cat',"bat",'rat',"aeiit"]
if all(vowels.check(i[0]) for i in words):
    print("All the words are starting with Vowels")
else:
    print("All the words doesn't start from vowels")