import cv2
import mediapipe as mp
import numpy as np

keys = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]

# Function to draw the keyboard
def draw_keyboard(frame):
    for i, row in enumerate(keys):
        for j, key in enumerate(row):
            x = j * 60 + 20
            y = i * 60 + 100
            cv2.rectangle(frame, (x, y), (x+50, y+50), (255, 0, 0), 2)
            cv2.putText(frame, key, (x+15, y+35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

def detect_key(frame, x, y):
    for i, row in enumerate(keys):
        for j, key in enumerate(row):
            x1 = j * 60 + 20
            y1 = i * 60 + 100
            x2 = x1 + 50
            y2 = y1 + 50
            if x1 < x < x2 and y1 < y < y2:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, key, (x1+15, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                return key
    return None

source = cv2.VideoCapture(1)
drawing = mp.solutions.drawing_utils
drawing_styles = mp.solutions.drawing_styles
hand = mp.solutions.hands
hands = hand.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6
)

last_pressed_key = None

while True:
    data, frame = source.read()
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    draw_keyboard(frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing.draw_landmarks(frame, hand_landmarks, hand.HAND_CONNECTIONS,
                                   drawing_styles.get_default_hand_landmarks_style(),
                                   drawing_styles.get_default_hand_connections_style())
            
            x1 = int(hand_landmarks.landmark[8].x * frame.shape[1])
            y1 = int(hand_landmarks.landmark[8].y * frame.shape[0])
            x2 = int(hand_landmarks.landmark[12].x * frame.shape[1])
            y2 = int(hand_landmarks.landmark[12].y * frame.shape[0])
            
            if not (abs(x1 - x2) <= 0.12 * frame.shape[1] and abs(y1 - y2) <= 0.12 * frame.shape[0]):
                detected_key = detect_key(frame, x1, y1)
                if detected_key and detected_key != last_pressed_key:
                    print(f"Key Pressed: {detected_key}")
                    last_pressed_key = detected_key
            else:
                last_pressed_key = None

    cv2.imshow("Virtual Keyboard", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

source.release()
cv2.destroyAllWindows()
