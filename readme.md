# Charles Cornell App
This is a console application to find cropped images within a frame of a MP4/video.

## 📖 Story Time!
I wrote this in response to a challenge issued on November 26, 2022 by pianist, educator, and YouTube creator, [Charles Cornell][cornell_yt].

Cornell basically asks in [a community post][community_post] to find this candid image from a video frame that he found hisself:

![image to find](input\image_to_find.jpg)

This frame will be in a video that he will post later on Youtube, *[How is the Spy Family Soundtrack THIS Good?][spy_family_video]*. Whoever emails him a screenshot first gets Cornell's entire selection of music courses for free ($99 value!). 

**This is begging to be automated by a python program.**

And this program will separate your video into frames and search any image (cropped or not cropped) inside of each frame:

![Screenshot (Frame 425 if you're curious)](assets\found.png)

Shout out to Flynn for getting the win!

## 🛠 Installation & Setup
```bash
git clone git@github.com:dariustb/CharlesCornellApp.git
```

Go to the project directory

```bash
cd CharlesCornellApp
```

Set up virtual enviroment
```bash
python -m venv venv
source venv/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Add unincluded folders
```bash
mkdir input output
```

Open src/main and edit ref image and video paths
```python
video_path = "input/vid.mp4"
ref_path   = "input/ref.jpg"
```

## 🚀 Build and Run Locally
Run on console

```bash
python src/main.py
```

<!-- Links -->
[repo]: git@github.com:dariustb/CharlesCornellApp.git

[cornell_yt]: https://www.youtube.com/@CharlesCornellStudios

[community_post]: https://www.youtube.com/channel/UC4PIiYewI1YGyiZvgNlJNrA/community?lb=Ugkxlx5jZVyfMHIXrW2T43Eut6tu1673pgBB

[spy_family_video]: https://www.youtube.com/watch?v=lFIixuIdYhY
