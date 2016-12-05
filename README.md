# ardupilot-video-overlay
Quick and dirty python script I wrote to overlay ardupilot (pixhawk) log data over my GoPro video. Overlays Alt, Lat/Long and Flight Mode.

Requires pandas, numpy and moviepy libraries. Currently I just use this with the quadcopter I've been building but it should work with any ardupilot log once converted to a csv. 

Tool to convert Bin to CSV found here:
https://github.com/PX4/Firmware/tree/master/Tools/sdlog2

## Usage

* Make sure to start recording video before arming the vehicle.
* When running the script four arguments are needed. In this order:
  * -s, log start point in seconds.
  * -e, log end point in seconds. Or where you want to truncate the output video.
  * log_file, ardupilot log converted to CSV.
  * video_file, MP4 video file.
* Watch the video and listen for the arming beep. That's the time to use as the start point.

I'm currently just using GoPro videos but it should work with any MP4.

### To-Do
  * Right now it just iterates through the CSV in one second intervals. If for some reason the data at that time doesn't exsit it just grabs the next good value. The "To-Do" is to increase the resolution of the time intervals and iterate through the CSV row by row instead of time.
  * Add an arg/args to control other data points to overlay on the video.
