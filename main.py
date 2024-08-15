import ctypes
import subprocess

scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)


if scaleFactor==100:
    subprocess.run(["python", "base_100.py"])
elif scaleFactor==125:
    subprocess.run(["python", "base_125.py"])
else:
    subprocess.run(["python", "message.py"])