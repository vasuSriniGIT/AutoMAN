import cv2
import numpy as np
from truckscenes import TruckScenes

# Path for initializing TruckScenes
metadata_path = 'D:/Srini/Autonomous_Proj/Data_MAN/man-truckscenes_metadata_v1.0-mini/man-truckscenes'

# Initialize the TruckScenes object
trucksc = TruckScenes('v1.0-mini', metadata_path, verbose=True)

# Select the first scene
my_scene = trucksc.scene[0]

# Retrieve the first sample token
current_sample_token = my_scene['first_sample_token']

# Initialize the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For .mp4 format
out = None  # Initialize as None

# Iterate through all samples in the scene
while current_sample_token:
    # Render the current sample
    img = trucksc.render_sample(current_sample_token)
    
    # Check if the image is valid
    if img is not None:
        # Convert the image to a NumPy array
        img_cv = np.array(img)
        
        # Check if the image has more than 2 dimensions (height, width, channels)
        if img_cv.ndim == 3 and img_cv.shape[2] == 4:  # If the image has an alpha channel
            img_cv = img_cv[:, :, :3]  # Remove the alpha channel
        elif img_cv.ndim == 2:  # If the image is grayscale
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_GRAY2BGR)  # Convert to BGR format

        # Initialize the VideoWriter object with the first frame's size
        if out is None:
            height, width, layers = img_cv.shape
            size = (width, height)
            out = cv2.VideoWriter('truck_scenes_video.mp4', fourcc, 1, size)  # 1 frame per second

        # Write the current frame to the video
        out.write(img_cv)
    else:
        print(f"Warning: Rendered image for sample token {current_sample_token} is None.")
    
    # Retrieve the current sample
    current_sample = trucksc.get('sample', current_sample_token)
    
    # Move to the next sample
    current_sample_token = current_sample['next']

# Release the VideoWriter object
if out:
    out.release()
else:
    print("No frames were written to the video.")
