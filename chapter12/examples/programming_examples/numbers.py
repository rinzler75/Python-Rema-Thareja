class TimeUp(Exception):
    pass
def message(c):
    start_timer=0
    stop_timer=1000000
    count=start_timer
    try:
        while True:
            count+=1
            if count==stop_timer:
                raise TimeUp
    except TimeUp as t:
        print(c,end=" ")
for i in range(31):
    message(i)