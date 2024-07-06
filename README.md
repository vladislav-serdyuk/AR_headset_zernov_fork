# AR_headset
## Managed by [Zernov](https://www.youtube.com/@zernovtech)
[README.md на русском](./READMERUS.md)

## About
Hey! This is my own code for creating an AR/MR helmet based on Linux and Python. This thing uses MediaPipe and Cv2 for video streams.
I started it only something like 2 months ago, so ain't so good
Biggest framerate you can get with this code is around 30, so you should use NASA supercomputer.

# Let's begin!

(Be sure you are using Python 3.11)
Before running this code you should install all dependency, so you can use [requirements](requirements.txt) for that:

```console
pip install -r requirements.txt
```

## Configuration

After installing all dependency, you can set config of application.

In the file [config.ini](./config.ini) you can find some configuration lines:
```ini
[Camera]
mode=ps5camera
# 1camera, 2camera, ps4camera (2560x800), ps5camera (3840x1080), camera_off
resolution_w=1280
resolution_h=720
first_camera_id=0
second_camera_id=1
ps5camera_id=0
ps4camera_id=0
rotate_image=False
...
```

Here you can set your camera type.
1camera - 1 USB UVC WEBCam.\
2camera - 2 different USB UVC WEBCam's. Just cameras, nothing interesting.\
ps4camera - HD (720p) stereo camera, made for Playstation 4. Works with cable and [driver](https://github.com/Hackinside/PS4-CAMERA-DRIVERS)\
ps5camera - Full HD (1080p) stereo camera for PS5. Doesn't need a cable, but needs [driver](https://github.com/Hackinside/PS5_camera_files)
camera_off - work without camera (black screen).

In the end of configuration you can turn on/off video recording, GUI, barrel_distortion and web interface:
```python
[Options]
active_interface=True
video_recording=False
tracking_active=True
webserver_active=True
barrel_distortion=False
```
That's it. 

## RUN

After setting up all configuration variables you can check your webcam(s) and directly run this code:
```console
python3.11 AR_HeadSet.py
```
or
```console
python3 AR_HeadSet.py
```

## Check the video

After starting code up you can check videostream by opening 
```http
yourip:5000
```
for example:
```http
localhost:5000
```
Then you should see stream from camera and GUI
## The end 
