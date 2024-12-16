#################################################################################
# Example of using a custom config directory
#################################################################################

import os
import cv2

from pyppbox.standalone import setConfigDir, detectPeople, trackPeople, reidPeople
from pyppbox.utils.visualizetools import visualizePeople


# Use a custom config directory "cfg"
setConfigDir(config_dir="cfg", load_all=True)

# input_video = "gta.mp4"
input_video = "boris.mp4"
output_dir = "cropped_body"

cap = cv2.VideoCapture(0)

frame_count = 0
saved_count = 0

while cap.isOpened():
    hasFrame, frame = cap.read()

    if hasFrame:

        # Detect people without visualizing
        detected_people, _ = detectPeople(frame, img_is_mat=True, visual=False)


        # Track the detected people
        tracked_people = trackPeople(frame, detected_people, img_is_mat=True)

        # Re-identify the tracked people
        
        reidentified_people, reid_count = reidPeople(
            frame, 
            tracked_people, 
            img_is_mat=True
        )
        

        # Visualize people in video frame with reid status `show_reid=reid_count`
        visualized_mat = visualizePeople(
            frame, 
            reidentified_people, 
            show_reid=reid_count
        )
        
        # cv2.imshow("abl", visualized_mat)s
        cv2.imshow("abl_interface", visualized_mat)
        
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

