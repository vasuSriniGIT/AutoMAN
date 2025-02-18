from truckscenes import TruckScenes

# Provide the path to the root directory of the dataset
dataset_root = r'D:\Srini\Autonomous_Proj\Data_MAN\man-truckscenes_metadata_v1.0-mini\man-truckscenes'

# Initialize the TruckScenes object
trucksc = TruckScenes('v1.0-mini', dataset_root, True)

# List available scenes
trucksc.list_scenes()

# Select the first scene
my_scene = trucksc.scene[0]

# Retrieve the first sample token
first_sample_token = my_scene['first_sample_token']

# Render the first sample
trucksc.render_sample(first_sample_token)
