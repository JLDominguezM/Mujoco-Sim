import mujoco
import mujoco.viewer
import time

# Load the model from the XML file
model = mujoco.MjModel.from_xml_path('myrobot.mujoco.xml')
data = mujoco.MjData(model)

# Launch the viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
  # Get the start time
  start = time.time()
  while viewer.is_running() and time.time() - start < 30:
    # Step the simulation
    mujoco.mj_step(model, data)

    # Synchronize the viewer
    viewer.sync()