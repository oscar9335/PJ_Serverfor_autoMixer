import os
import time_count as count
from moviepy.editor import *

basepath = 'files'

video_file = count.get_video_file(basepath)
video_time_gap = count.video_time_info_gap(video_file,basepath)
video_time_gap_float = video_time_gap/1000

audio_file = count.get_audio_file(basepath)
# print(afloat)

#(0,afloat could be ignore since the video has to be the raw one)
main_video = VideoFileClip(basepath + "/" + video_file).subclip(0,video_time_gap_float)
all_audio = []  

for the_audio in audio_file:
    start_place = 0
    start_place_float = 0.0
    end_place = 0
    end_place_float = 0.0
    starting_time = 0
    starting_time_float = 0.0

    the_audio_time_gap = count.specific_audio_time_info_gap(the_audio,basepath)
    the_duration = the_audio_time_gap/1000

    #obtain [#######1,######2]

    start_end = count.video_minus_audio(video_file,the_audio,basepath)
    if (start_end[0] < 0): 
        # video start earlier than audio
        # Use CompositeAudioClip with clip.set_start().
        starting_time = (-1) * start_end[0]
        starting_time_float = starting_time/1000

        
        
    elif (start_end[0] > 0):# video start later than audio
        start_place = start_end[0]
        start_place_float = start_place/1000

    if (start_end[1] < 0):# video end earlier than audio
        if (starting_time_float > 0):
            audio_set = AudioFileClip(basepath + "/" + the_audio).subclip(0.0,video_time_gap_float - starting_time_float)
            audio_set = audio_set.set_start(starting_time_float)
            all_audio.append(audio_set)
            
        else:
            audio_set = AudioFileClip(basepath + "/" + the_audio).subclip(start_place_float,start_place_float + video_time_gap_float)
            all_audio.append(audio_set)


    elif (start_end[1] > 0):# video end later than audio
        if (starting_time_float > 0):
            audio_set = AudioFileClip(basepath + "/" + the_audio).subclip(0.0,the_duration)
            audio_set = audio_set.set_start(starting_time_float)
            all_audio.append(audio_set)
        else:
            audio_set = AudioFileClip(basepath + "/" + the_audio).subclip(start_place_float)
            all_audio.append(audio_set)
    


audio_compose = CompositeAudioClip(all_audio)
new_video = main_video.set_audio(audio_compose)

new_video.write_videofile(filename="my_test2.mp4",codec='libx264')
