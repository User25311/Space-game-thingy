import threading
# def stuff():
#     print("I SMELL U")



standard_time_red = 10 
standard_time_green = 12

def red_light_duration(priority, pedestrian):
    print("RĘD")
    global standard_time_red
    pedestrian_time = 0 
    if pedestrian:
        pedestrian_time = 15
        
    if priority == 1:
        priority_time = 20 
    elif priority == 2:
        priority_time = 15 
    else: 
        priority_time = 10

    final_wait_time = standard_time_red + priority_time + pedestrian_time
    return final_wait_time


def yellow_light_duration():
    print("YELLŒW")
    return 3





def green_light_duration(priority, pedestrian): 
    global standard_time_green
    print("GREEÑ")
    no_go = 0

    if priority == 1:
        priority_time = 10
    elif priority == 2:
        priority_time=12
    else:
        priority_time = 15

    if pedestrian:
        no_go = 5
    

    final_go_time = standard_time_green + priority_time - no_go
    return final_go_time
    

# green_light_duration(1,False)
# yellow_light_duration()
# red_light_duration(1, False)
# green_light_duration(1, True)
# yellow_light_duration()
# red_light_duration(1, True)

#green_light_time = green_light_duration(1, False)
green_light_time = 5
yellow_light_time = 2
red_light_time = 7
# yellow_light_time = yellow_light_duration()
# red_light_time = red_light_duration(1,False)
timerGY = threading.Timer(green_light_time, yellow_light_duration)
timerGY.start()
timerYL = threading.Timer(yellow_light_time, red_light_duration(1, False))
timerYL.start()
timerRL = threading.Timer(red_light_time, print("BACK TO GREEN"))
timerRL.start()

