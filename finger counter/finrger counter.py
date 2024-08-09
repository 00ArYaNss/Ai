import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=2, detectionCon=0.8)

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# Initialize the previous finger configuration and the current displayed image
previous_fingerup = None
current_fing = cv2.imread(r'C:\Users\sahua\OneDrive\Desktop\ML Projects\finger counter\finger images\zero.png')

while True:
    success, img = video.read()
    if not success:
        print("Failed to capture image")
        break
    
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0]
        lmlist = hand['lmList']  # Ensure we're accessing the correct key
        if lmlist:
            fingerup = detector.fingersUp(hand)
            
            # Check if the finger configuration has changed
            if fingerup != previous_fingerup:
                print(f"Finger Up: {fingerup}")  # Debug print
                previous_fingerup = fingerup  # Update the previous configuration

                if fingerup == [0, 0, 0, 0, 0]:
                    current_fing = cv2.imread(r"finger images/zero.png")
                elif fingerup == [0, 0, 0, 0, 1]:
                    current_fing = cv2.imread(r"finger images/one.png")
                elif fingerup == [0, 0, 0, 1, 0]:
                    current_fing = cv2.imread(r"finger images/one.png")
                elif fingerup == [0, 0, 0, 1, 1]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [0, 0, 1, 0, 0]:
                    current_fing = cv2.imread(r"finger images/one.png")
                elif fingerup == [0, 0, 1, 0, 1]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [0, 0, 1, 1, 0]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [0, 0, 1, 1, 1]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [0, 1, 0, 0, 0]:
                    current_fing = cv2.imread(r"finger images/one.png")
                elif fingerup == [0, 1, 0, 0, 1]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [0, 1, 0, 1, 0]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [0, 1, 0, 1, 1]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [0, 1, 1, 0, 0]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [0, 1, 1, 0, 1]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [0, 1, 1, 1, 0]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [0, 1, 1, 1, 1]:
                    current_fing = cv2.imread(r"finger images/four.png")
                elif fingerup == [1, 0, 0, 0, 0]:
                    current_fing = cv2.imread(r"finger images/one.png")
                elif fingerup == [1, 0, 0, 0, 1]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [1, 0, 0, 1, 0]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [1, 0, 0, 1, 1]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [1, 0, 1, 0, 0]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [1, 0, 1, 0, 1]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [1, 0, 1, 1, 0]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [1, 0, 1, 1, 1]:
                    current_fing = cv2.imread(r"finger images/four.png")
                elif fingerup == [1, 1, 0, 0, 0]:
                    current_fing = cv2.imread(r"finger images/two.png")
                elif fingerup == [1, 1, 0, 0, 1]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [1, 1, 0, 1, 0]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [1, 1, 0, 1, 1]:
                    current_fing = cv2.imread(r"finger images/four.png")
                elif fingerup == [1, 1, 1, 0, 0]:
                    current_fing = cv2.imread(r"finger images/three.png")
                elif fingerup == [1, 1, 1, 0, 1]:
                    current_fing = cv2.imread(r"finger images/four.png")
                elif fingerup == [1, 1, 1, 1, 0]:
                    current_fing = cv2.imread(r"finger images/four.png")
                elif fingerup == [1, 1, 1, 1, 1]:
                    current_fing = cv2.imread(r"finger images/five.png")

                if current_fing is None:
                    print(f"Error: Could not read finger image for gesture {fingerup}.")
                    break
    else:
        # If no hands are detected, reset to zero.png
        previous_fingerup = None
        current_fing = cv2.imread(r"finger images/zero.png")
        if current_fing is None:
            print("Error: Could not read default finger image.")
            break

    current_fing = cv2.resize(current_fing, (220, 280))
    img[50:330, 20:240] = current_fing

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
