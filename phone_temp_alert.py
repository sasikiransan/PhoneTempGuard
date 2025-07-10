import os
import time
from plyer import notification

def get_battery_temp():
    result = os.popen("adb shell dumpsys battery").read()
    for line in result.splitlines():
        if "temperature" in line:
            temp_milli = int(line.strip().split(":")[1])
            return temp_milli / 10
    return None

while True:
    temp = get_battery_temp()
    if temp:
        print(f"[INFO] Battery Temp: {temp}°C")
        if temp >= 38:
            notification.notify(
                title="🔥 Phone Overheating!",
                message=f"Battery is {temp}°C — Please unplug or cool it ❄️❤️",
                timeout=10
            )
    else:
        notification.notify(
            title="⚠️ Phone Not Detected!",
            message="Check USB and make sure ADB debugging is ON.",
            timeout=10
        )
    time.sleep(600)
