'''
Greets the world 
'''
import datetime
current_time = datetime.datetime.now()

print("This is 2020")

if current_time.hour < 12:
    print("Good morning")
elif current_time.hour < 18:
    print("Good afternoon")
else:
    print("Good evening")
