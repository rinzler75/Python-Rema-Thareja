import re
pattern = r"hi(de)?" #check 0 or 1 repetations 
if re.search(pattern,"hidedededede"): #here one repetation is there
    print("Match hidededede")
if re.search(pattern,"hi"):
    print("Match hi")