# -*- coding: utf-8 -*-
import cv2
from imutils.video import FPS
import time
from detect_lane import *
from file_video_stream_fast import FileVideoStream
from preprocessing_image import *

print("[INFO] starting video file thread...")

# Use the default camera (index 0) as the video source
cap = cv2.VideoCapture(0)

fps = FPS().start()

def process_video(video_input, video_output):
    detector = LaneDetector()

    clip = VideoFileClip(os.path.join('test_videos', video_input))
    processed = clip.fl_image(detector.process)
    processed.write_videofile(os.path.join(
        'output_videos', video_output), audio=False)

if __name__ == '__main__':
    # setup()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # You can resize the frame if needed
        # frame = imutils.resize(frame, width=450)

        preprocessed_image = preprocess_image(frame, True)

        detector = LaneDetector()
        processed_img = detector.process(frame, preprocessed_image)

        cv2.imshow("Video", processed_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        fps.update()

    # Stop the timer and display FPS information
    fps.stop()
    plt.show()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

