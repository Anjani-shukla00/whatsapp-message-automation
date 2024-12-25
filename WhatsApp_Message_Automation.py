'''Twilio is a library that provides the facility to 
connect with the WhatsApp API, and its Client class is directly used for sending messages.'''

'''The `datetime` module is used to work with both the current and future times in Python.'''

# Step-1 Install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os

# Step-2 Twilio credentials
# Replace these with environment variables or secure storage
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'xxxx')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'xxxx')
client = Client(account_sid, auth_token)

# Step-3 Define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+xxx',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Step-4 User input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +123): ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step-5 Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

try:
    # Combine date and time
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()
    print(f"Current system time: {current_datetime}")

    # Calculate delay
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print('The specified time is in the past. Please enter a future date and time.')
    else:
        print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
        # Wait until the scheduled time
        time.sleep(delay_seconds)
        # Send the message
        send_whatsapp_message(recipient_number, message_body)

except ValueError as e:
    print(f'Invalid date or time format: {e}')
