import cv2
import threading
import streamlit as st
import pygame

from twilio.rest import Client

st.markdown("<h1 style='text-align: center; color: black;'>Real Time Prediction</h1>", unsafe_allow_html=True)

# Twilio configuration
account_sid = "AC6b0991f1c9a1f86c80e7ce51beac88ad"
auth_token = "98e9ce06594bd6110f09bd9384703713"
client = Client(account_sid, auth_token)
# Threading Event for stopping
stop_event = threading.Event()


# Function to play the alarm sound
def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("E:\\Project\\MiniProject\\fire\\alarm.mp3")
    pygame.mixer.music.play(1)
    # Wait for stop_event to be set to stop the alarm
    while not stop_event.is_set():
        pygame.time.Clock().tick(1)  # Adjust the tick rate as needed

    pygame.mixer.music.stop()


# Function to send an SMS
def send_sms_function():
    try:
        message = client.messages.create(
            body='Warning: Fire accident has been reported!',
            from_='+19416239647',  # Your Twilio phone number
            to='+918089368162'  # The phone number you want to send the SMS to
        )
        print(f"Alert SMS sent successfully to {message.to}")
    except Exception as e:
        print(e)

def main():
    stop = False
    FRAME_WINDOW = st.empty()

    def show_webcam():
        nonlocal stop
        fire_cascade = cv2.CascadeClassifier("E:\\Project\\MiniProject\\fire\\fire_detection_cascade_model.xml")
        vid = cv2.VideoCapture(0)
        runOnce = False

        while not stop:
            ret, frame = vid.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

            for (x, y, w, h) in fire:
                cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)

                if not runOnce:
                    print("SMS send initiated from webcam detection")
                    threading.Thread(target=send_sms_function).start()
                    threading.Thread(target=play_alarm).start()
                    runOnce = True

            FRAME_WINDOW.image(frame, channels="BGR")

            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

        st.write('Stopped')
        vid.release()
        # cv2.destroyAllWindows()

    col1, col2 = st.columns(2)

    live = col1.button("Live Video")
    stop_button = col2.button("Stop")

    # live = st.button("Live Video")
    # stop_button = st.button("Stop")

    if live:
        show_webcam()

    if stop_button:
        stop = True

if __name__ == '__main__':
    main()