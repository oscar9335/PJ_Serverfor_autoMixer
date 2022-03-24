import os 


def get_audio_file(basepath):  # saved in array cina a basepath of file
    # the basepath could be changed if needed 
    #basepath = 'files'
    audio_file = []
    #find the correspond information.txt for the specific .3gp audio file
    for f_name in os.listdir(basepath):
        if f_name.endswith('.3gp'):
            audio_file.append(f_name)
    return audio_file

def get_video_file(basepath):  # saved in array cina a basepath of file
    # the basepath could be changed if needed 
    #basepath = 'files'
    video_file = ''
    #find the correspond information.txt for the specific .3gp audio file
    for f_name in os.listdir(basepath):
        if f_name.endswith('.mp4'):
            video_file = f_name
            return video_file

def specific_audio_time_info_gap(audio_file,basepath):
    audio_name = audio_file.strip(".3gp")
    for f_name in os.listdir(basepath):
        audio_timeinfo = f_name.strip('audio_time_info')
        audio_timeinfo = audio_timeinfo.strip('.txt')
        if audio_timeinfo == audio_name:  #found the info txt we wnat now open it to read info
            if os.path.isfile(os.path.join(basepath, f_name)):
                line_number = 2
                with open(basepath + '/' + f_name,"r") as f:
                    while (line_number > 0):
                        tmp = f.readline()
                        the_string = tmp.split("_")
                        #print(the_string)
                        if line_number == 2:
                            long_start = 0
                            year_start = int(the_string[0])
                            month_start = int(the_string[1])
                            day_start = int(the_string[2])
                            hour_start = int(the_string[3])
                            minute_start = int(the_string[4])
                            second_start = int(the_string[5])
                            milisecond_start = int(the_string[6])

                            if(month_start == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_start = month_start*31
                            elif(month_start == 4 or 6 or 9 or 11):
                                long_start = month_start*30
                            elif(month_start == 2):
                                long_start = month_start*28

                            long_start = (((((long_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
                            #print(long_start)      
                        elif line_number == 1:
                            long_end = 0
                            year_end = int(the_string[0])
                            month_end = int(the_string[1])
                            day_end = int(the_string[2])
                            hour_end = int(the_string[3])
                            minute_end = int(the_string[4])
                            second_end = int(the_string[5])
                            milisecond_end = int(the_string[6])
                                
                            if(month_end == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_end = month_end*31
                            elif(month_end == 4 or 6 or 9 or 11):
                                long_end = month_end*30
                            elif(month_end == 2):
                                long_end = month_end*28

                            long_end = (((((long_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
                            #print(long_end)
                            return (long_end - long_start)

                        line_number = line_number - 1



def videostart_minus_audiostart(video_file,audio_file,basepath):
    long_audio_start = 0
    long_video_start = 0

    video_name = video_file.strip(".mp4")
    audio_name = audio_file.strip(".3gp")

    for f_name in os.listdir(basepath):
        audio_start_timeinfo = f_name.strip('audio_time_info')
        audio_start_timeinfo = audio_start_timeinfo.strip('.txt')

        video_start_timeinfo = f_name.strip('video_time_info')
        video_start_timeinfo = video_start_timeinfo.strip('.txt')

        if audio_start_timeinfo == audio_name:
            if os.path.isfile(os.path.join(basepath, f_name)):
                with open(basepath + '/' + f_name,"r") as f:
                    tmp = f.readline()
                    the_string = tmp.split("_")
                    year_start = int(the_string[0])
                    month_start = int(the_string[1])
                    day_start = int(the_string[2])
                    hour_start = int(the_string[3])
                    minute_start = int(the_string[4])
                    second_start = int(the_string[5])
                    milisecond_start = int(the_string[6])

                    if(month_start == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                        long_audio_start = month_start*31
                    elif(month_start == 4 or 6 or 9 or 11):
                        long_audio_start = month_start*30
                    elif(month_start == 2):
                        long_audio_start = month_start*28

                    long_audio_start = (((((long_audio_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
        elif video_start_timeinfo == video_name:
            if os.path.isfile(os.path.join(basepath, f_name)):
                with open(basepath + '/' + f_name,"r") as f:
                    tmp = f.readline()
                    the_string = tmp.split("_")
                    year_start = int(the_string[0])
                    month_start = int(the_string[1])
                    day_start = int(the_string[2])
                    hour_start = int(the_string[3])
                    minute_start = int(the_string[4])
                    second_start = int(the_string[5])
                    milisecond_start = int(the_string[6])

                    if(month_start == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                        long_video_start = month_start*31
                    elif(month_start == 4 or 6 or 9 or 11):
                        long_video_start = month_start*30
                    elif(month_start == 2):
                        long_video_start = month_start*28

                    long_video_start = (((((long_video_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
    return (long_audio_start - long_audio_start)

def videoend_minus_audioend(video_file,audio_file,basepath):
    long_audio_end = 0
    long_video_end = 0

    video_name = video_file.strip(".mp4")
    audio_name = audio_file.strip(".3gp")

    for f_name in os.listdir(basepath):
        audio_end_timeinfo = f_name.strip('audio_time_info')
        audio_end_timeinfo = audio_end_timeinfo.strip('.txt')

        video_end_timeinfo = f_name.strip('video_time_info')
        video_end_timeinfo = video_end_timeinfo.strip('.txt')

        if audio_end_timeinfo == audio_name:
            if os.path.isfile(os.path.join(basepath, f_name)):
                with open(basepath + '/' + f_name,"r") as f:
                    tmp = f.readline()
                    the_string = tmp.split("_")
                    year_end = int(the_string[0])
                    month_end = int(the_string[1])
                    day_end = int(the_string[2])
                    hour_end = int(the_string[3])
                    minute_end = int(the_string[4])
                    second_end = int(the_string[5])
                    milisecond_end = int(the_string[6])

                    if(month_end == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                        long_audio_end = month_end*31
                    elif(month_end == 4 or 6 or 9 or 11):
                        long_audio_end = month_end*30
                    elif(month_end == 2):
                        long_audio_end = month_end*28

                    long_audio_end = (((((long_audio_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
        elif video_end_timeinfo == video_name:
            if os.path.isfile(os.path.join(basepath, f_name)):
                with open(basepath + '/' + f_name,"r") as f:
                    tmp = f.readline()
                    the_string = tmp.split("_")
                    year_end = int(the_string[0])
                    month_end = int(the_string[1])
                    day_end = int(the_string[2])
                    hour_end = int(the_string[3])
                    minute_end = int(the_string[4])
                    second_end = int(the_string[5])
                    milisecond_end = int(the_string[6])

                    if(month_end == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                        long_video_end = month_end*31
                    elif(month_end == 4 or 6 or 9 or 11):
                        long_video_end = month_end*30
                    elif(month_end == 2):
                        long_video_end = month_end*28

                    long_video_end = (((((long_video_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
    return (long_audio_end - long_audio_end)


def video_minus_audio(videofile,audiofile,basepath):
    audio_name = audiofile.strip(".3gp")
    video_name = videofile.strip(".mp4")

    long_audio_start = 0
    long_audio_end = 0
    long_video_start = 0
    long_video_end = 0
    start_diff = 0
    end_diff = 0


    for f_name in os.listdir(basepath):
        #audio
        audio_timeinfo = f_name.strip('audio_time_info')
        audio_timeinfo = audio_timeinfo.strip('.txt')
        #video
        video_timeinfo = f_name.strip('video_time_info')
        video_timeinfo = video_timeinfo.strip('.txt')

        if audio_timeinfo == audio_name:  #found the info txt we wnat now open it to read info
            if os.path.isfile(os.path.join(basepath, f_name)):
                line_number = 2
                with open(basepath + '/' + f_name,"r") as f:
                    while (line_number > 0):
                        tmp = f.readline()
                        the_string = tmp.split("_")
                        #print(the_string)
                        if line_number == 2:
                            year_start = int(the_string[0])
                            month_start = int(the_string[1])
                            day_start = int(the_string[2])
                            hour_start = int(the_string[3])
                            minute_start = int(the_string[4])
                            second_start = int(the_string[5])
                            milisecond_start = int(the_string[6])

                            if(month_start == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_audio_start = month_start*31
                            elif(month_start == 4 or 6 or 9 or 11):
                                long_audio_start = month_start*30
                            elif(month_start == 2):
                                long_audio_start = month_start*28

                            long_audio_start = (((((long_audio_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
                            #print(long_start)      
                        elif line_number == 1:
                            year_end = int(the_string[0])
                            month_end = int(the_string[1])
                            day_end = int(the_string[2])
                            hour_end = int(the_string[3])
                            minute_end = int(the_string[4])
                            second_end = int(the_string[5])
                            milisecond_end = int(the_string[6])
                                
                            if(month_end == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_audio_end = month_end*31
                            elif(month_end == 4 or 6 or 9 or 11):
                                long_audio_end = month_end*30
                            elif(month_end == 2):
                                long_audio_end = month_end*28

                            long_audio_end = (((((long_audio_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
                            #print(long_end)
                        line_number = line_number - 1
        if video_timeinfo == video_name:  #found the info txt we wnat now open it to read info
            if os.path.isfile(os.path.join(basepath, f_name)):
                line_number = 2
                with open(basepath + '/' + f_name,"r") as f:
                    while (line_number > 0):
                        tmp = f.readline()
                        the_string = tmp.split("_")
                        #print(the_string)
                        if line_number == 2:
                            year_start = int(the_string[0])
                            month_start = int(the_string[1])
                            day_start = int(the_string[2])
                            hour_start = int(the_string[3])
                            minute_start = int(the_string[4])
                            second_start = int(the_string[5])
                            milisecond_start = int(the_string[6])

                            if(month_start == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_video_start = month_start*31
                            elif(month_start == 4 or 6 or 9 or 11):
                                long_video_start = month_start*30
                            elif(month_start == 2):
                                long_video_start = month_start*28

                            long_video_start = (((((long_video_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
                            #print(long_start)      
                        elif line_number == 1:
                            year_end = int(the_string[0])
                            month_end = int(the_string[1])
                            day_end = int(the_string[2])
                            hour_end = int(the_string[3])
                            minute_end = int(the_string[4])
                            second_end = int(the_string[5])
                            milisecond_end = int(the_string[6])
                                
                            if(month_end == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_video_end = month_end*31
                            elif(month_end == 4 or 6 or 9 or 11):
                                long_video_end = month_end*30
                            elif(month_end == 2):
                                long_video_end = month_end*28

                            long_video_end = (((((long_video_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
                            #print(long_end)
                        line_number = line_number - 1

    start_diff = long_video_start - long_audio_start
    end_diff = long_video_end - long_audio_end
    return [start_diff,end_diff]
        


def video_time_info_gap(video_file,basepath):
    video_name = video_file.strip(".mp4")
    for f_name in os.listdir(basepath):
        video_timeinfo = f_name.strip('video_time_info')
        video_timeinfo = video_timeinfo.strip('.txt')
        if video_timeinfo == video_name:  #found the info txt we wnat now open it to read info
            if os.path.isfile(os.path.join(basepath, f_name)):
                line_number = 2
                with open(basepath + '/' + f_name,"r") as f:
                    while (line_number > 0):
                        tmp = f.readline()
                        the_string = tmp.split("_")
                        #print(the_string)
                        if line_number == 2:
                            long_start = 0
                            year_start = int(the_string[0])
                            month_start = int(the_string[1])
                            day_start = int(the_string[2])
                            hour_start = int(the_string[3])
                            minute_start = int(the_string[4])
                            second_start = int(the_string[5])
                            milisecond_start = int(the_string[6])

                            if(month_start == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_start = month_start*31
                            elif(month_start == 4 or 6 or 9 or 11):
                                long_start = month_start*30
                            elif(month_start == 2):
                                long_start = month_start*28

                            long_start = (((((long_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
                            #print(long_start)      
                        elif line_number == 1:
                            long_end = 0
                            year_end = int(the_string[0])
                            month_end = int(the_string[1])
                            day_end = int(the_string[2])
                            hour_end = int(the_string[3])
                            minute_end = int(the_string[4])
                            second_end = int(the_string[5])
                            milisecond_end = int(the_string[6])
                                
                            if(month_end == 1 or 3 or 5 or 7 or 8 or 10 or 12):
                                long_end = month_end*31
                            elif(month_end == 4 or 6 or 9 or 11):
                                long_end = month_end*30
                            elif(month_end == 2):
                                long_end = month_end*28

                            long_end = (((((long_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
                            #print(long_end)
                            return (long_end - long_start)

                        line_number = line_number - 1