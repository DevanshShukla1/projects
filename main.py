# -*- coding: utf-8 -*-
import cv2
from imutils.video import FPS
import imutils
from detect_lane import *
from preprocessing_image import *
from lane_marking import *

# Use webcam as video source, 0 represents the default webcam
cap = cv2.VideoCapture(0)
fps = FPS().start()

if __name__ == '__main__':
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=450)
        preprocessed_image = preprocess_image(frame)
        lane_marking_image = lane_marking_detection(preprocessed_image, True)

        detector = LaneDetector()
        processed_img = detector.process(frame, lane_marking_image)

        cv2.imshow("Screen", processed_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        fps.update()

    # Stop the timer and display FPS information
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()
