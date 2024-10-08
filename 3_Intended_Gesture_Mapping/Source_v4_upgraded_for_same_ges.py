#consecutive_frames = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
def intended_gesture_map(predicted_class, consecutive_frames):
    if predicted_class == 0:
        consecutive_frames[0] += 1
    else:
        consecutive_frames[0] = 0

    if predicted_class == 1:
        consecutive_frames[1] += 1
    else:
        consecutive_frames[1] = 0

    if predicted_class == 2:
        consecutive_frames[2] += 1
    else:
        consecutive_frames[2] = 0

    if predicted_class == 3:
        consecutive_frames[3] += 1
    else:
        consecutive_frames[3] = 0

    if predicted_class == 4:
        consecutive_frames[4] += 1
    else:
        consecutive_frames[4] = 0

    if predicted_class == 5:
        consecutive_frames[5] += 1
    else:
        consecutive_frames[5] = 0

    for gesture, count in consecutive_frames.items():
        intended_gesture = None
        for gesture, count in consecutive_frames.items():
            if count == 3:
                intended_gesture = gesture
                break

        if intended_gesture is not None:
            # Reset counts to 0 for all gestures
            for gesture in consecutive_frames:
                consecutive_frames[gesture] = 0

        return intended_gesture