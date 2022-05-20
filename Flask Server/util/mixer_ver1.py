import util.time_count as count
from moviepy.editor import *


# video_file_name = video file name(String)
# video_time_gap: find the correponding video info .txt using video_file_name 
# video_time_gap_float making the time into float 

# audio fps need to be place into the mixer as a parameter
def compose_the_mastepice(basepath,fps_audio):

    # to get the video file name
    # to get the video time Duration with floating number in [video_time_gap_float]
    video_file_name = count.get_video_file(basepath)
    video_time_gap = count.video_time_info_gap(video_file_name,basepath)
    video_time_gap_float = video_time_gap/1000

    # receive a list in audio_file[]
    audio_file = count.get_audio_file(basepath)
    all_audio = [] 
    

    # (0,afloat could be ignore since the video has to be the raw one)
    # main_video = VideoFileClip(basepath + "/" + video_file_name).subclip(0,video_time_gap_float)
    main_video = VideoFileClip(basepath + "/" + video_file_name) 

    # prune audios time info one by one
    for the_audio in audio_file:

        # receive one audio duration at a time
        the_audio_time_gap = count.specific_audio_time_info_gap(the_audio,basepath)
        the_audio_duration = the_audio_time_gap/1000

        start_place = 0
        start_place_float = 0.0
        
        end_place = 0
        end_place_float = 0.0

        starting_time = 0
        starting_time_float = 0.0

        #obtain [start_diff,end_diff]
        startdiff_enddiff = count.video_minus_audio(video_file_name,the_audio,basepath)

    # Note #
    # start_diff = long_video_start - long_audio_start
    #   @ using video start time - audio start time
    #   @@ if video start eleaier then audio -> the start_diff is negative
    #   @@ if video start later then audio -> the start_diff is positive

    # end_diff = long_video_end - long_audio_end
    #   @ using video end time - audio end time
    #   @@ if video end eleaier then audio -> the end_diff is negative
    #   @@ if video end later then audio -> the end_diff is positive     
        
    # setting time to use
    # video start earlier than audio
    # Use CompositeAudioClip with clip.set_start().
        if (startdiff_enddiff[0] < 0): 
            starting_time = (-1) * startdiff_enddiff[0]
            starting_time_float = starting_time/1000

    # setting time to use
    # video start later than audio
    # Use CompositeAudioClip with clip.set_start().
        elif (startdiff_enddiff[0] > 0):# video start later than audio
            start_place = startdiff_enddiff[0]
            start_place_float = start_place/1000

    # Use case 1 2
    # video end earlier than audio

    # video start earlier than audio
    # 1            start                                   end   
    # audio time                 ****************************
    # video time            ***************************

    # video start later than audio 
    # 2
    # audio time             ********************************
    # video time                 *******************
        if (startdiff_enddiff[1] < 0):
            # video start earlier than audio so audio append from time {start of audio to end of video}
            if (starting_time_float > 0):
                audio_set = AudioFileClip(basepath + "/" + the_audio, fps=fps_audio).subclip(0.0,video_time_gap_float - starting_time_float)
                audio_set = audio_set.set_start(starting_time_float)
                all_audio.append(audio_set)

            # video start later than audio    
            else: # starting_time_float == 0
                print("PPPPP")
                print(start_place_float)
                print(video_time_gap_float)
                print(start_place_float + video_time_gap_float)
                print("PPPPP")
                audio_set = AudioFileClip(basepath + "/" + the_audio, fps=fps_audio).subclip(start_place_float,start_place_float + video_time_gap_float)
                all_audio.append(audio_set)

    # Use case 3 4
    # video end later than audio

    # video start earlier than audio
    # 3          start                                        end
    # audio time            ****************************
    # video time       ***************************************

    # video start later than audio
    # 4
    # audio time        ****************************       
    # video time              ********************************

        elif (startdiff_enddiff[1] > 0):# video end later than audio
            if (starting_time_float > 0):
                audio_set = AudioFileClip(basepath + "/" + the_audio, fps=fps_audio).subclip(0.0)
                audio_set = audio_set.set_start(starting_time_float)
                all_audio.append(audio_set)
            else: # starting_time_float == 0
                # audio_set = AudioFileClip(basepath + "/" + the_audio).subclip(start_place_float) 
                audio_set = AudioFileClip(basepath + "/" + the_audio, fps=fps_audio).subclip(0,start_place_float - the_audio_duration) 
                all_audio.append(audio_set)
        


    audio_compose = CompositeAudioClip(all_audio)

    # audio_compose.write_audiofile(filename= basepath + "\composedaudio.mp3", fps = fps_audio,codec = "libmp3lame")

    #  new_video = main_video.set_audio(audio_compose)

    audio_compose.write_audiofile(filename= basepath + "\composedaudio.mp3", fps = fps_audio,codec = "libmp3lame")

    # if new_video.write_videofile(filename= basepath + "\composed.mp4",codec='libx264',preset = "ultrafast"):
    #     return "something went wrong"
    # else:
    #     return "OK"

    import ffmpeg

    # mute the audio there 
    video = ffmpeg.input(basepath + '/' + video_file_name,**{'an':None})

    audio = ffmpeg.input(basepath + '/' + 'composedaudio.mp3')

    stream = ffmpeg.output(video, audio, basepath + "/" + "composed.mp4")

    if ffmpeg.run(stream):
        return "OK"
    else:
        return "something went wrong"
   
    

# note #
# subclip If t_end is not provided, it is assumed to be the duration of the clip
#         If t_end is a negative value, it is reset to ``clip.duration + t_end. ``
#         If normally set t_end (t_start,t_end) is the start timestamp and end timestamp