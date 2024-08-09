import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=2, detectionCon=0.8)

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    success, img = video.read()
    if not success:
        print("Failed to capture image")
        break
    
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)

    # Default image
    fing = cv2.imread(r"finger images/zero.png")
    if fing is None:
        print("Error: Could not read default finger image.")
        break

    if hands:
        hand = hands[0]
        lmlist = hand['lmList']  # Ensure we're accessing the correct key
        if lmlist:
            fingerup = detector.fingersUp(hand)
            print(f"Finger Up: {fingerup}")  # Debug print
            if fingerup == [0, 0, 0, 0, 0]:
                fing = cv2.imread(r"finger images/zero.png")
            elif fingerup == [0, 0, 0, 0, 1]:
                fing = cv2.imread(r"finger images/one.png")
            elif fingerup == [0, 0, 0, 1, 0]:
                fing = cv2.imread(r"finger images/one.png")
            elif fingerup == [0, 0, 0, 1, 1]:
                fing = cv2.imread(r"finger images/two.png")
                
                
            elif fingerup == [0, 0, 1, 0, 0]:
                fing = cv2.imread(r"finger images/one.png")
            elif fingerup == [0, 0, 1, 0, 1]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [0, 0, 1, 1, 0]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [0, 0, 1, 1, 1]:
                fing = cv2.imread(r"finger images/three.png")
            
            
            elif fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread(r"finger images/one.png")
            elif fingerup == [0, 1, 0, 0, 1]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [0, 1, 0, 1, 0]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [0, 1, 0, 1, 1]:
                fing = cv2.imread(r"finger images/three.png")
                
                
            elif fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [0, 1, 1, 0, 1]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread(r"finger images/four.png")     
                
            if fingerup == [1, 0, 0, 0, 0]:
                fing = cv2.imread(r"finger images/one.png")
            elif fingerup == [1, 0, 0, 0, 1]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [1, 0, 0, 1, 0]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [1, 0, 0, 1, 1]:
                fing = cv2.imread(r"finger images/three.png")
                
                
            elif fingerup == [1, 0, 1, 0, 0]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [1, 0, 1, 0, 1]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [1, 0, 1, 1, 0]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [1, 0, 1, 1, 1]:
                fing = cv2.imread(r"finger images/four.png") 
                
                
            elif fingerup == [1, 1, 0, 0, 0]:
                fing = cv2.imread(r"finger images/two.png")
            elif fingerup == [1, 1, 0, 0, 1]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [1, 1, 0, 1, 0]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [1, 1, 0, 1, 1]:
                fing = cv2.imread(r"finger images/four.png")  
                
            elif fingerup == [1, 1, 1, 0, 0]:
                fing = cv2.imread(r"finger images/three.png")
            elif fingerup == [1, 1, 1, 0, 1]:
                fing = cv2.imread(r"finger images/four.png")
            elif fingerup == [1, 1, 1, 1, 0]:
                fing = cv2.imread(r"finger images/four.png")
            elif fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread(r"finger images/five.png")            
                                         

            if fing is None:
                print(f"Error: Could not read finger image for gesture {fingerup}.")
                break

    fing = cv2.resize(fing, (220, 280))
    img[50:330, 20:240] = fing

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
