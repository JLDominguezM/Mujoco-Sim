import mujoco
import mujoco.viewer
import time

# Load the model from the XML file
model = mujoco.MjModel.from_xml_path('myrobot.mujoco.xml')
data = mujoco.MjData(model)

# Launch the viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    while True:
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(0)  # Adjust the sleep time for desired speed