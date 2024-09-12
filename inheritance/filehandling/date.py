import time
from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time is:", current_time, end="")
    
 