import time

filename = "/var/docker-share/log.txt"


while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)    
    with open(filename,'a') as file:
        file.write(f"{current_time}: write action")
    time.sleep(1)