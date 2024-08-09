import cv2

config_file = r"C:\Users\sahua\OneDrive\Desktop\ML Projects\object detection\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = r"C:\Users\sahua\OneDrive\Desktop\ML Projects\object detection\frozen_inference_graph.pb"

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
file_name = r"C:\Users\sahua\OneDrive\Desktop\ML Projects\object detection\coco.names"
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
print(len(classLabels))

model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open the video")

font_scale = 1
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Detect objects
    ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)

    # Draw bounding boxes and labels on the frame
    if len(ClassIndex) != 0:
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            cv2.rectangle(frame, boxes, (255, 0, 0), 2)
            cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=font_scale, color=(0, 255, 0), thickness=2)

    # Display the frame
    cv2.imshow('Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
