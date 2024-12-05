#################################################################################
# Example of using a custom config directory
#################################################################################

import os
import cv2
from test_interface import create_or_replace_folder, record_video, main_interface
from  example_11_reid_classifier import create_model_pkl

from pyppbox.standalone import setConfigDir, detectPeople, trackPeople, reidPeople
from pyppbox.utils.visualizetools import visualizePeople
import subprocess
import sys


    
user_name = main_interface()









# Use a custom config directory "cfg"
setConfigDir(config_dir="cfg", load_all=True)

# input_video = "gta.mp4"
# input_video = "boris.mp4"
# input_video = "users/luca/video_test.mp4"
base_path = "video_test.mp4"
user_path = "users"
input_video = os.path.join(user_path, user_name, base_path)
print(input_video)
# output_dir = "cropped_body"
output_base = "cropped_body"
output_dir = os.path.join(output_base, user_name)


# Créer le dossier s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

print(output_dir)

cap = cv2.VideoCapture(input_video)
# cap = cv2.VideoCapture(0)

frame_count = 0
saved_count = 0



while cap.isOpened():
    hasFrame, frame = cap.read()

    if hasFrame:

        # Detect people without visualizing
        detected_people, _ = detectPeople(frame, img_is_mat=True, visual=False)

        for p in detected_people:
            '''
            (x, y) = p.repspoint
            miniframe = frame.copy()

            miniframe = miniframe[
                y + int(-125):
                y + int(75), 
                x + int(-55):
                x + int(55)
            ]
            # cv2.imwrite(filename, image)
            # cv2.imshow("face", miniframe)
            '''
            box_xyxy = p.box_xyxy
            cropped_frame = frame[box_xyxy[1]:box_xyxy[3], box_xyxy[0]:box_xyxy[2]]

            output_path = os.path.join(output_dir, f"frame_{frame_count:06d}.jpg")
            cv2.imwrite(output_path, cropped_frame)
            saved_count += 1

        frame_count += 1

        visualized_mat = visualizePeople(
            frame, 
            detected_people
        )

        # cv2.imshow("pyppbox: example_03_custom_cfg_directory.py", visualized_mat)

        '''
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
        
        cv2.imshow("pyppbox: example_03_custom_cfg_directory.py", visualized_mat)
        
        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()



# # Chemin du dossier à créer
# folder_path = "cropped_face"

# # Créer le dossier s'il n'existe pas
# os.makedirs(folder_path, exist_ok=True)
    
# # script_name = "align_dataset_mtcnn.py"

# # arguments = ["'cropped_body'", "'cropped_face'", "--gpu_memory_fraction 0.5"]
# # # Use sys.executable to ensure the same Python interpreter is used
# # subprocess.run([sys.executable, script_name, *arguments], check=True)   

# Path to your .cmd file
cmd_file = "align_interface.cmd"

# Execute the .cmd file
subprocess.run([cmd_file], check=True, shell=True)

create_model_pkl()
