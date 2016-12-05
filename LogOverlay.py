import numpy as np
import pandas as pd
import argparse
from moviepy.editor import *

parser = argparse.ArgumentParser()
parser.add_argument('log_file', help='log to overlay on video')
parser.add_argument('video_in', help='input video')
#parser.add_argument('video_out', help='output video')
parser.add_argument('-s', '--start', help='time in sec at arming')
parser.add_argument('-e', '--end', help='time in sec at video end')
args = parser.parse_args()

flightModes = {0:'Stabilize', 1:'Acro', 2:'AltHold', 3:'Auto', 4:'Guided', 5:'Loiter', 6:'RTL', 7:'Circle', 8:'Position', 9:'Land', 10:'OF_Loiter', 11:'Drift', 13:'Sport', 14:'Flip', 15:'AutoTune', 16:'PosHold', 17:'Brake' }


log_df = pd.read_csv(args.log_file)

FirstGoodRow = 0
while True:
    if np.isnan(log_df['GPS_TimeUS'].loc[FirstGoodRow]):
        FirstGoodRow += 1
    else:
        start_time = log_df['GPS_TimeUS'].loc[FirstGoodRow]
        break
for i in range(FirstGoodRow, len(log_df['GPS_TimeUS'])):
    val = int(log_df['GPS_TimeUS'].iloc[i] - start_time) / 1000000
    log_df.set_value(i, 'GPS_TimeUS', val)


def lookup(_second, col):
    for i in range(0, len(log_df)):
        if log_df['GPS_TimeUS'].iloc[i] >= _second:
            if col == 'MODE_ModeNum':
                #return int(log_df[col].iloc[i])
                return flightModes.get(int(log_df[col].iloc[i]))
            break
    return log_df[col].iloc[i]


timeStart = int(args.start)
timeEnd = int(args.end)
clipDur = timeEnd - timeStart

clipList = []

#txt_title = ( TextClip('Testing', fontsize=80, font='FreeMono', color='white').set_position('center').set_duration(1).set_start(1))
txt_result = ( TextClip('                                                            ', fontsize=32, font='FreeMono', color='black').set_duration(1).set_start(1) )

for i in range(2, clipDur):
    relAlt = lookup(i, 'POS_RelAlt')
    gpsLat = lookup(i, 'GPS_Lat')
    gpsLong = lookup(i, 'GPS_Lng')
    flightMode = str(lookup(i, 'MODE_ModeNum'))
    _string = 'Alt:{:.2f}m Lat:{:.6f} Long:{:.6f} Mode:{}'.format(relAlt, gpsLat, gpsLong, flightMode)

    clipList.append(( TextClip(_string, fontsize=32, font='FreeMono', color='black').set_duration(1).set_start(i) ))
    

txt_result = CompositeVideoClip(clipList)
video = VideoFileClip(args.video_in).subclip(timeStart, timeEnd)

video = CompositeVideoClip([video, txt_result])
video.write_videofile('output.mp4', fps=25)















