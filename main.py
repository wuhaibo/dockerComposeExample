import time

filename = "log.txt"
file = open(filename, 'w+') 

while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    file.write(f"{current_time}: write action")
    time.sleep(1)