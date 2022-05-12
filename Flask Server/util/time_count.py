import os 

# *******************************get_audio_file(basepath)******************************* #
# 1. saved in array from a basepath of file                                              #           
# 2. list all the audio file and put String(file name) in audio_file list                #
# return a "List[]""                                                                     #
# *******************************get_audio_file(basepath)******************************* #
def get_audio_file(basepath):  
    audio_file = []
    for f_name in os.listdir(basepath):
        if f_name.endswith('.3gp'):
            audio_file.append(f_name)
        # This is for ios m4a audio file if problem delete    
        if f_name.endswith('.m4a'):  
            audio_file.append(f_name)
    return audio_file


# *******************************get_video_file(basepath)******************************* #
# 1. saved in array from a basepath of file                                              #
# 2. list all the audio file and put String(file name) in video_file String              #
# return a "String"                                                                      #
# *******************************get_video_file(basepath)******************************* #
def get_video_file(basepath):  
    video_file = ''
    for f_name in os.listdir(basepath):
        if f_name.endswith('.mp4'):
            video_file = f_name
            return video_file


# *******************************video_time_info_gap(video_file,basepath)********************************* #
# 1. two parameter                                                                                         #
#    - video_file: Video file name                                                                         #
#    - basepath: the file base path                                                                        #
# 2. Video file name e.g. 2022_05_12_09_37_14.mp4, reserve the 2022_05_12_09_37_14 in [video_name]         #
# 3. Search all the file in basepath directory if prefix video_time_info, find the video_time_info .txt    #
#    video_time_info2022_05_12_09_37_14.txt then prune the name to 2022_05_12_09_37_14 in [video_timeinfo] #
# 4. read the txt file using (day hour minute second milisecond) information generate                      #
#    [long_start] store the video start time                                                               #
#    [long_end] store the video end time                                                                   #
# return [the_time_gap]                                                                                    #
# *******************************video_time_info_gap(video_file,basepath)**********************************#
def video_time_info_gap(video_file,basepath):
    video_name = video_file[:-4]
    for f_name in os.listdir(basepath):
        if f_name[:15] == "video_time_info":
            video_timeinfo = f_name[:-4]
            video_timeinfo = video_timeinfo.strip('video_time_info')
            #found the info txt we want now open it to read info
            if video_timeinfo == video_name: 
                if os.path.isfile(os.path.join(basepath, f_name)):
                    line_number = 2
                    with open(basepath + '/' + f_name,"r",encoding="utf-8") as f:
                        while (line_number > 0):
                            tmp = f.readline()
                            the_string = tmp.split("_")                
                            if line_number == 2:
                                long_start = 0
                                
                                day_start = int(the_string[2])
                                hour_start = int(the_string[3])
                                minute_start = int(the_string[4])
                                second_start = int(the_string[5])
                                milisecond_start = int(the_string[6])

                                long_start = (((((long_start + day_start)*24 + hour_start)*60 + minute_start)*60 + second_start)*1000 + milisecond_start)
                                     
                            elif line_number == 1:
                                long_end = 0
                            
                                day_end = int(the_string[2])
                                hour_end = int(the_string[3])
                                minute_end = int(the_string[4])
                                second_end = int(the_string[5])
                                milisecond_end = int(the_string[6])
                                    
                                long_end = (((((long_end + day_end)*24 + hour_end)*60 + minute_end)*60 + second_end)*1000 + milisecond_end)
                                
                                the_time_gap = long_end - long_start
                                print("time video gap")
                                print(the_time_gap)
                                return the_time_gap

                            line_number = line_number - 1

# *****************************specific_audio_time_info_gap(audio_file,basepath)*************************** #
# audio_file is a audio file name e.g. 2022_05_12_09_37_14.3gp audio_name store 2022_05_12_09_37_14         #
# the process is tha same as video_time_info_gap(video_file,basepath)                                       #
# *****************************specific_audio_time_info_gap(audio_file,basepath)*************************** #
def specific_audio_time_info_gap(audio_file,basepath):
    audio_name = audio_file[:-4]
    for f_name in os.listdir(basepath):
        if f_name[:15] == 'audio_time_info':
            audio_timeinfo = f_name[:-4]
            audio_timeinfo = audio_timeinfo.strip('audio_time_info')
            if audio_timeinfo == audio_name:  
                if os.path.isfile(os.path.join(basepath, f_name)):
                    line_number = 2
                    with open(basepath + '/' + f_name,"r",encoding="utf-8") as f:
                        while (line_number > 0):
                            tmp = f.readline()
                            the_string = tmp.split("_")
                            #print(the_string)
                            if line_number == 2:
                                long_start = 0
                                
                                day_start = int(the_string[2])
                                hour_start = int(the_string[3])
                                minute_start = int(the_string[4])
                                second_start = int(the_string[5])
                                milisecond_start = int(the_string[6])

                                long_start = (((((long_start + day_start)*24 + hour_start)*60 + minute_start)*60 + second_start)*1000 + milisecond_start)
                                      
                            elif line_number == 1:
                                long_end = 0
                              
                                day_end = int(the_string[2])
                                hour_end = int(the_string[3])
                                minute_end = int(the_string[4])
                                second_end = int(the_string[5])
                                milisecond_end = int(the_string[6])
                                    
                                long_end = (((((long_end + day_end)*24 + hour_end)*60 + minute_end)*60 + second_end)*1000 + milisecond_end)
                                the_time_gap = long_end - long_start

                                return the_time_gap

                            line_number = line_number - 1



# return [start_diff,end_diff] for every audio    
# start_diff = long_video_start - long_audio_start
#   @ using video start time - audio start time
#   @@ if video start eleaier then audio -> the start_diff is negative
#   @@ if video start later then audio -> the start_diff is positive

# end_diff = long_video_end - long_audio_end
#   @ using video end time - audio end time
#   @@ if video end eleaier then audio -> the end_diff is negative
#   @@ if video end later then audio -> the end_diff is positive 



def video_minus_audio(videofile,audiofile,basepath):
    # prune off .3gp .mp4
    audio_name = audiofile[:-4]
    video_name = videofile[:-4]

    long_audio_start = 0
    long_audio_end = 0

    long_video_start = 0
    long_video_end = 0

    start_diff = 0
    end_diff = 0
    
    # find the video information obtain two variable [long_video_start] & [long_video_end]
    for f_name in os.listdir(basepath):
        #video
        if f_name[:15] == 'video_time_info':
            video_timeinfo = f_name[:-4]
            video_timeinfo = video_timeinfo.strip('video_time_info')
            if video_timeinfo == video_name:  #found the info txt we wnat now open it to read info
                if os.path.isfile(os.path.join(basepath, f_name)):
                    line_number = 2
                    with open(basepath + '/' + f_name,"r") as f:
                        while (line_number > 0):
                            tmp = f.readline()
                            the_string = tmp.split("_")
                            #print(the_string)
                            if line_number == 2:
                              
                                day_start = int(the_string[2])
                                hour_start = int(the_string[3])
                                minute_start = int(the_string[4])
                                second_start = int(the_string[5])
                                milisecond_start = int(the_string[6])

                                long_video_start = (((((long_video_start + day_start)*24 + hour_start)*60 + minute_start)*60 + second_start)*1000 + milisecond_start)
                                # print(long_video_start)      
                            elif line_number == 1:
                               
                                day_end = int(the_string[2])
                                hour_end = int(the_string[3])
                                minute_end = int(the_string[4])
                                second_end = int(the_string[5])
                                milisecond_end = int(the_string[6])
                                    
                                long_video_end = (((((long_video_end + day_end)*24 + hour_end)*60 + minute_end)*60 + second_end)*1000 + milisecond_end)
                                # print(long_video_end)

                            line_number = line_number - 1

    # one audio "information" file at a time until all file being processed 
    # obtain two information variable [long_audio_start] & [long_audio_end]
    for f_name in os.listdir(basepath):
        #audio
        if f_name[:15] == 'audio_time_info':
            audio_timeinfo = f_name[:-4]
            audio_timeinfo = audio_timeinfo.strip('audio_time_info')
            # match "audio.txt" and "audio.3gp"
            if audio_timeinfo == audio_name:  #found the info txt we wnat now open it to read info
                if os.path.isfile(os.path.join(basepath, f_name)):
                    line_number = 2
                    with open(basepath + '/' + f_name,"r") as f:
                        while (line_number > 0):
                            tmp = f.readline()
                            the_string = tmp.split("_")
                            # print(the_string)
                            if line_number == 2:
                                
                                day_start = int(the_string[2])
                                hour_start = int(the_string[3])
                                minute_start = int(the_string[4])
                                second_start = int(the_string[5])
                                milisecond_start = int(the_string[6])

                                long_audio_start = (((((long_audio_start + day_start)*24 + hour_start)*60 + minute_start)*60 + second_start)*1000 + milisecond_start)
                                print(long_audio_start)      
                            elif line_number == 1:
                                
                                day_end = int(the_string[2])
                                hour_end = int(the_string[3])
                                minute_end = int(the_string[4])
                                second_end = int(the_string[5])
                                milisecond_end = int(the_string[6])
                                    
                                long_audio_end = (((((long_audio_end + day_end)*24 + hour_end)*60 + minute_end)*60 + second_end)*1000 + milisecond_end)
                                print(long_audio_end)

                            line_number = line_number - 1
        

    # obtain the video time info - audio time info in [start_diff] & [end_diff]
    # the meaning of these two variable can be directly received from the following 
    start_diff = long_video_start - long_audio_start
    end_diff = long_video_end - long_audio_end
    print(start_diff)
    print(end_diff)


    return [start_diff,end_diff]
        
