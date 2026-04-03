# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "miniaudio>=1.61",
# ]
# ///

# imports
import atexit
import os
import sys
import time
from pathlib import Path

import miniaudio


def restart_script():
    print("DONT QUIT")
    os.execv(sys.executable, [sys.executable] + sys.argv)


atexit.register(restart_script)

songpy_parent_path = Path(__file__).parent
audiofile_path = songpy_parent_path / "bullofheaven-lovelypear.mp3"

path_str = str(audiofile_path)
info = miniaudio.get_file_info(path_str)

print("listen to bull of heaven - lovely pear. DONT QUIT OR I WILL HACK YOU")

with miniaudio.PlaybackDevice(
    output_format=info.sample_format,
    sample_rate=info.sample_rate,
    nchannels=info.nchannels,
) as device:
    stream = miniaudio.stream_file(path_str)
    device.start(stream)

    time.sleep(info.duration)

atexit.unregister(restart_script)

# created by unsandpiper8 2/4/2026 for the python-9246 repo.