from truckscenes import TruckScenes

# Path for initializing TruckScenes
metadata_path = 'D:/Srini/Autonomous_Proj/Data_MAN/man-truckscenes_metadata_v1.0-mini/man-truckscenes'

# Initialize the TruckScenes object
trucksc = TruckScenes('v1.0-mini', metadata_path, True)

# Select the first scene
my_scene = trucksc.scene[0]

# Retrieve the first sample token
first_sample_token = my_scene['first_sample_token']

# Render the first sample
trucksc.render_sample(first_sample_token)

my_sample = trucksc.get('sample', first_sample_token)
my_sample