# ardupilot-video-overlay
Quick and dirty python script I wrote to overlay ardupilot (pixhawk) log data over my GoPro video.

Requires pandas, numpy and moviepy libraries. Currently I just use this with the quadcopter I've been building but it should work with any ardupilot log once converted to a csv. 

Tool to convert Bin to CSV found here:
https://github.com/PX4/Firmware/tree/master/Tools/sdlog2

## Usage

* Make sure to start recording video before arming the vehicle.
* When running the script four arguments are needed. In this order:
  1. -s, log start point in seconds.
  2. -e, log end point in seconds. Or where you want to truncate the output video.
  3. log_file, ardupilot log converted to CSV.
  4. video_file, MP4 video file.
* Watch the video and listen for the arming beep. That's the time to use as the start point.

I'm currently just using GoPro videos but it should work with any MP4.
