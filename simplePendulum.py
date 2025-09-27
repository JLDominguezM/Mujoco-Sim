import mujoco
import mujoco.viewer
import time

# Load the model from the XML file
model = mujoco.MjModel.from_xml_path('myrobot.mujoco.xml')
data = mujoco.MjData(model)

# Launch the viewer
with mujoco.viewer.launch(model, data) as viewer:
    while True:
        mujoco.mj_step(model, data)
        viewer.sync()