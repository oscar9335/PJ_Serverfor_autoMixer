from asyncio.windows_events import NULL
import flask
# import werkzeug
from flask import request, send_file, redirect, url_for
import os
from os import walk

import util.mixer_ver1 as mixer

app = flask.Flask(__name__)

file_save_path = "store_files"
# step1: this list is to contain the room in service, 
# step2: once all the participation download the file , remove the # from list  

list_room = []   #String
room_info_dic = {}
aroomnum = str(99999)


@app.route('/', methods=['GET', 'POST'])
def home():

    return "Hello"

@app.route('/sendsettingtoclient', methods=['GET', 'POST'])
def sendsettingtoclient():
    roomtosend = request.form["roomcode"]
    if roomtosend:
        print("request success in [homepage]")
        roomFramerateinfo_key = "room" + roomtosend + "framerate"
        roomFramerateinfo_value = room_info_dic[roomFramerateinfo_key]
        print(roomFramerateinfo_value)
        
        return roomFramerateinfo_value

    else:
        return "Error no room number"




@app.route('/Room', methods=['GET', 'POST'])
def room():
    # the return OK & No & Yes is important message for client to know if the Room is existed or not
    action = request.form["action"]
    room_number = request.form["room_number"]

    if(action == "CREATE"):
        print(room_number)
        for existed_room in list_room:
            if existed_room == room_number:
                return "No, Existed Room"

        # not yet append to room list until setting confirm
        print("create debug")
        print(list_room)
        return "Ok, Room Create Successful"

    elif(action == "JOIN"):
        for existed_room in list_room:
            if existed_room == room_number:
                print("JOIN LOL")
                return "Yes, room join success"
    
        return "No, room doesn't exist, please press CREATE "
        
    return "Check internet connection!"

@app.route('/Setting', methods = ['POST'])
def config_setting():
    
    room_number_forsaveuse = request.form["roomnumbersetting"]
    audioframerate = request.form["audioSetting"]

    if room_number_forsaveuse:
        # room1234framerate 
        framerate_key = "room" + room_number_forsaveuse + "framerate"
        room_info_dic[framerate_key] = audioframerate

        # the room is created until confirm bt click
        list_room.append(room_number_forsaveuse)

        print(list_room)

        print(room_info_dic) # debug usage



        #correct return "SUCCESS"
        return 'SUCCESS'
    else:   
        return "Nothing receive"


@app.route('/Compose' ,methods = ['GET', 'POST'])
def compose():
    room_number = request.form["room_number"]
    do = request.form["compose_file"]

    room_info_dic_this_key = "room" + room_number + "framerate"
    for_room_audio_fps = int(room_info_dic[room_info_dic_this_key])

    print(type(for_room_audio_fps))
    print(for_room_audio_fps)


    # return "testtest"
    if do == "compose":
        roomdir = file_save_path + "/" + room_number
        composed_video = mixer.compose_the_mastepice(roomdir,for_room_audio_fps)
        print(composed_video)
        
        if composed_video == "OK":
            print("Compose successful")
            return "Compose successful!!!"
        else:
            return "failed : NO compose !!!" + composed_video
    
    else:
        return "Something wrong with request!"
  



# the roomnumber will be post to server when client use the postRoom to create or join the room 
# aroomnum = str(1)
@app.route('/Download_get_roomnumber',methods=['GET', 'POST'])
def dwgetroom():
    room_number = request.form["roomcode"]
    # print(type(room_number))
    print("in dwgetroom:" + room_number )
    if room_number:
        print("downloading")
        return redirect(url_for('download',aroomnum = str(room_number)))
    else:
        print("NOOB")
        return "NOOB"

   
# if the route is not existed then Not Found
# aroomnum parameter will attach the room number to it
@app.route('/Download/<aroomnum>', methods=['GET', 'POST'])
def download(aroomnum):
    # if exist the route do the following
    # room_number = request.form["room_number"]
    roomdir = file_save_path + "/" + aroomnum
    print(roomdir)
    
    for dirPath, dirNames, all_files in walk(roomdir):
        for afile in all_files:
            print(afile)
            # print(type(afile))
            if afile == "composed.mp4":
                filepath = roomdir + "/" + "composed.mp4"
                print("Check reacton")
                return send_file(filepath, download_name = "composed.mp4")

    return "Haven't composed yet!!!"

    


@app.route("/Audio_store",methods=['GET', 'POST'])
def audio():
    if request.files:
        room_number = request.form["room_number"]
        audio_txt = request.files["audio_info"]
        audio = request.files["audio"]

        # test if the above three request acquired 
        ### this is for degug ###
        if(room_number == NULL):
            print("Error no room number acquired!!!")
            return "room_number not post successfully!!"
        else:
            print("Room number is:{name}".format(name = room_number))
        if(audio_txt == NULL):
            print("Error no audio_txt(info) acquired!!!")
            return "audio_txt not post successfully!!"
        else:
            print("Yes you acquired a audio txt information!") 
            print("This is a :{name}".format(name = type(audio_txt)))   
        if(audio == NULL):
            print("Error no audio acquired!!!")
            return "audio not post successfully!!"
        else:
            print("Yes you acquired a audio ") 
            print(audio.filename)
            print("This is a :{name}".format(name = type(audio)))
        ### this is for debug ###


        audioname = audio.filename

        #create a room dir for store files
        roomdir = file_save_path + "/" + room_number
        CHECK_FOLDER = os.path.isdir(roomdir)
        if not CHECK_FOLDER:
            os.makedirs(roomdir)
            print("created folder : ", roomdir)
        else:
            print( roomdir, "folder already exists.")

        print()

        for dirPath, dirNames, all_files in walk(roomdir):
            for afile in all_files:
                print(afile)
                #print(type(afile))
                if afile == audioname:
                    return "You have already uploaded the Audio"

        #store the file in the specific dir
        audio.save(os.path.join(roomdir,audio.filename))
        audio_txt.save(os.path.join(roomdir,audio_txt.filename))

        print("audio saved")
        return "OK, Audio upload finished"

    else:
        return "Something went wrong while upload audio!!!"




@app.route("/Video_store",methods=['GET', 'POST'])
def video():
    if request.files:
        room_number = request.form["room_number"]
        video_txt = request.files["video_info"]
        video = request.files["video"]

        videoname = video.filename

        #create a room dir for store files
        roomdir = file_save_path + "/" + room_number
        CHECK_FOLDER = os.path.isdir(roomdir)
        if not CHECK_FOLDER:
            os.makedirs(roomdir)
            print("created folder : ", roomdir)
        else:
            print( roomdir, "folder already exists.")

        for dirPath, dirNames, all_files in walk(roomdir):
            for afile in all_files:
                print(afile)
                print(type(afile))
                if afile == videoname:
                    return "You have already uploaded the Video"

        #store the file in the specific dir
        video.save(os.path.join(roomdir,video.filename))
        video_txt.save(os.path.join(roomdir,video_txt.filename))
        
        print("video saved")
        return "OK, Video upload finished"
    else:
        return "Something went wrong while upload video!!!"





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)





