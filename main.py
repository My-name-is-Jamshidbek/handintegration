import cv2
import mediapipe as mp
import numpy as np
import requests

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.6)

cap = cv2.VideoCapture(0)


def is_thumb_closed(landmarks):
    thumb_tip = landmarks[4]
    thumb_mcp = landmarks[2]
    return thumb_tip.x < thumb_mcp.x


def is_finger_closed(landmarks, tip_id, dip_id):
    return landmarks[tip_id].y > landmarks[dip_id].y


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            finger_tips = [4, 8, 12, 16, 20]
            finger_dips = [3, 7, 11, 15, 19]

            finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
            finger_states = []

            for i in range(5):
                if i == 0:
                    if is_thumb_closed(hand_landmarks.landmark):
                        finger_states.append('0')
                    else:
                        finger_states.append('1')
                else:
                    if is_finger_closed(hand_landmarks.landmark, finger_tips[i], finger_dips[i]):
                        finger_states.append('0')
                    else:
                        finger_states.append('1')

            status_message = ''.join(finger_states)
            cv2.putText(frame, status_message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            try:
                response = requests.get(f'http://192.168.4.1/sendSignal?data={status_message}')
                if response.status_code == 200:
                    print(f"Signal sent successfully: {status_message}")
                else:
                    print(f"Failed to send signal: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error sending request: {e}")

    cv2.imshow('Hand Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
