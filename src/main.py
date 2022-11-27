# Python v. 3.10.4, 64-bit
from functions import run

if __name__ == "__main__":
    video_path = "input/vid.mp4"       # Video we are searching through
    ref_path   = "input/ref.jpg"        # Image we are looking for in vid

    run(video_path, ref_path)

    print("Ending program...")
