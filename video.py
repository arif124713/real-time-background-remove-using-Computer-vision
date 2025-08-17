import numpy as np
import cv2
from ultralytics import YOLO

model = YOLO('yolo11n-seg.pt')

def image_background_remove(frame):
    # Run YOLO segmentation on the frame
    results = model.predict(frame, verbose=False)  # process single frame
    r = results[0]

    if r.masks is None:  # if nothing detected, just return original frame
        return frame

    masks = r.masks.data.cpu().numpy()
    mask = np.sum(masks, axis=0)  # combine all masks
    mask = (mask * 255).astype(np.uint8)

    # Resize mask to match frame
    mask_resized = cv2.resize(mask, (frame.shape[1], frame.shape[0]))

    # Create 3-channel mask for RGB image
    mask_rgb = cv2.merge([mask_resized, mask_resized, mask_resized])

    # Apply mask
    result = cv2.bitwise_and(frame, mask_rgb)

    # Add alpha channel (transparency)
    b, g, r = cv2.split(result)
    rgba = cv2.merge([b, g, r, mask_resized])

    return rgba


# ---- Main Loop ----
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = image_background_remove(frame)
    cv2.imshow('frame', output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
