import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
        greetings = 'Hello,{}'.format(who_to_greet)
        return greetings

print(greet('World'))
print(greet('Corey'))