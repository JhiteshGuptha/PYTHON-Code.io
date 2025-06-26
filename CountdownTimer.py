# Countdown Timer in python

import time

# This function Delays the output time by the value entered inside the ()

countTime = int(input("Enter the time in Seconds: "))

while countTime < 0:
    print("Time cannot be -ve")
    countTime = int(input("Enter the time in Seconds: "))

for i in reversed(range(0, countTime + 1)):
    if i == 0:
        continue
    else:
        print(i)
        time.sleep(1)
print("Alarm! Alarm!")