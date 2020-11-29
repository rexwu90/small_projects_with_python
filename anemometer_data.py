import sys
import os
import time
import datetime
import random

hour_count = 0

local_path = str(os.getcwd())
if not os.path.exists(local_path + "/txtFolder"):
    os.mkdir(local_path + "/txtFolder")

try:
    print ("If you want to stop the programe, please press Ctrl-C.")
    while True:
        # record the first time
        time1 = datetime.datetime.now()
        time.sleep(60)
        # record the second time after 60 second
        time2 = datetime.datetime.now()
        direction_random = round(random.uniform(0, 360), 2)
        min_speed_random = round(random.uniform(0, 50), 2)
        f = open("txtFolder/Wind_Direction_" + time2.strftime("%Y_%m_%d_%H%M") + "00.txt", "w")
        f.write("Time,SONT 2\n" + time1.strftime("%H:%M") + "," + str(direction_random))
        f.close()
        f = open("txtFolder/Wind_Speed_" + time2.strftime("%Y_%m_%d_%H%M") + "00.txt", "w")
        f.write("Time,SONT 2\n" + time1.strftime("%H:%M") + "," + str(min_speed_random))
        f.close()
        if (hour_count == 60):
            hourly_speed_random = round(random.uniform(0, 50), 2)
            f = open("txtFolder/Wind_Hourly_Speed_" + time2.strftime("%Y_%m_%d_%H%M") + "00.txt", "w")
            f.write("Time,Hax Speed\n" + time1.strftime("%H:%M") + "," + str(hourly_speed_random))
            f.close()
        else:
            hour_count += 1
except KeyboardInterrupt:
    pass
