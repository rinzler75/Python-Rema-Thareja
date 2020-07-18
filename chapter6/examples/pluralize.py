import re
def pluralize(noun):
    if re.search(r'[sxz]$',noun):
        return re.sub('$','es',noun)
    elif re.search(r'[^aeioudgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search(r'[^aeiou]y$',noun):
        return re.sub('y$','ies',noun)
    else:
        return noun+'s'
List=["bush","fox","toy","cap"]
for i in List:
    print(i," - ",pluralize(i))