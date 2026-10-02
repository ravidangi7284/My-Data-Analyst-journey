from plyer import notification
import time

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='My App',
        timeout=10  # Notification will stay for 10 seconds
    )

if __name__ == "__main__":
    send_notification("Water Reminder", "Don't forget to drink water!")
    time.sleep(10)  # Wait for 10 seconds before sending the next notification
    send_notification("Water Reminder", "It's time to drink more water!")

