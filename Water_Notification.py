from email import message
import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title = "Water Notification",
            message = "Hydrate yourself, have a glass of water.",
            app_icon = "D:\Coding\Python_Practice\Harry_Practice_Problems_Playlist\water_icon.ico",
            ticker = "Water Notification",
            timeout = 5
        )
        time.sleep(15*60)