
import time
import sys

time_start = time.time()
seconds = 0
alien = 0

while True:
    try:
        sys.stdout.write("\r{alien} ALien {seconds} Seconds".format(alien= alien, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start)
        if seconds %5 == 0:
            print(" one alien added")
            alien += 1
            seconds = 0
            
    except KeyboardInterrupt:
        break