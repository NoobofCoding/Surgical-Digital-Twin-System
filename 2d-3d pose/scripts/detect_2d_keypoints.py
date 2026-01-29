import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

def detect_2d_keypoints(frames):
    all_keypoints = []

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6
    ) as hands:

        for idx, frame in enumerate(frames):
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            frame_kps = []

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    for lm in hand.landmark:
                        frame_kps.append((lm.x, lm.y))
            else:
                frame_kps = [(0.0, 0.0)] * 21

            all_keypoints.append(frame_kps)

            if idx % 10 == 0:
                print(f"[Vision] Frame {idx}/{len(frames)} processed")

    print("[Vision] 2D keypoint extraction complete")
    return all_keypoints
