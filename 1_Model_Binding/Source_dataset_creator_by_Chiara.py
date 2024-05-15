import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import mediapipe as mp
import os

SAVE_PATH =r'C:\Users\M\Desktop\Images\6\L'

def predict_gesture(cap, model_path):    # Load the trained model
    model = load_model(model_path)

    _, first_frame = cap.read()
    first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    gesture = None

    frame_count = 0

    while True:
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        difference = cv2.absdiff(first_gray, gray_frame)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

        # Find hand landmarks using MediaPipe
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract hand region coordinates
                x_min, y_min = frame.shape[1], frame.shape[0]
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Crop hand region from the difference frame with some padding
                padding = 30  # Adjust the padding as needed
                hand_crop = difference[max(0, y_min - padding):min(y_max + 10, difference.shape[0]),
                            max(0, x_min - padding):min(x_max + padding, difference.shape[1])]
                cv2.imshow("Hand Crop", hand_crop)

                # Save the hand region image with the detected gesture label
                if SAVE_PATH:
                    if not os.path.exists(SAVE_PATH):
                        os.makedirs(SAVE_PATH)
                    gesture_label = "No_Gesture" if gesture is None else f"Gesture_{gesture}"
                    cv2.imwrite(os.path.join(SAVE_PATH, f"{gesture_label}_frame_{frame_count}.png"), hand_crop)
                    frame_count += 1

                resized_img = cv2.resize(hand_crop, (75, 75))

                # Convert grayscale to RGB by repeating the single channel
                img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)

                # Expand dimensions to create a batch of 1 image
                img_array = np.expand_dims(img_rgb, axis=0)
                img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

                # Make predictions
                predictions = model.predict(img_array)
                #print(predictions)
                # Get the predicted class label
                predicted_class = np.argmax(predictions)

                # Get the probability of the predicted class
                predicted_probability = predictions[0][predicted_class]

                if predicted_class == 0:
                    if predicted_probability > 0.9:
                        gesture = 0
                    else:
                        gesture = None

                elif predicted_class == 1:
                    if predicted_probability > 0.9:
                        gesture = 1
                    else:
                        gesture = None

                elif predicted_class == 2:
                    if predicted_probability > 0.8:
                        gesture = 2
                    else:
                        gesture = None

                elif predicted_class == 3:
                    if predicted_probability > 0.9:
                        gesture = 3
                    else:
                        gesture = None

                elif predicted_class == 4:
                    if predicted_probability > 0.6:
                        gesture = 4
                    else:
                        gesture = None
                elif predicted_class == 5:
                    if predicted_probability > 0.6:
                        gesture = 5
                    else:
                        gesture = None

                elif predicted_class == 6:
                    if predicted_probability > 0.6:
                        gesture = 6
                    else:
                        gesture = None

                yield gesture

        cv2.imshow("First frame", first_frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("Difference", difference)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
model_path = "Media/7_gesture_model_13th_attempt.h5"
for gesture in predict_gesture(cap, model_path):
    if gesture is None:
        print("No gesture detected.")
    else:
        print("Predicted Gesture:", gesture)