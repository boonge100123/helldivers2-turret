import cv2
import torch

# Load YOLOv5s model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Open camera
cap = cv2.VideoCapture(0)

target_class = 0  # 'person' class in COCO dataset

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Run YOLOv5 inference
    results = model(frame)

    # Process detections
    for *xyxy, conf, cls in results.xyxy[0]:
        if int(cls) == target_class:
            x1, y1, x2, y2 = map(int, xyxy)
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            print(f"Detected person with confidence {conf:.2f} at center: ({cx}, {cy})")

    # Show the frame with detections
    results.render()
    cv2.imshow('YOLOv5 Detection Test - Person Only', results.ims[0])

    # Exit on 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
