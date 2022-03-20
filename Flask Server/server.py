import flask
import werkzeug
from flask import request, send_file
import os
from os import walk

app = flask.Flask(__name__)

file_save_path = "store_files"
# step1: this list is to contain the room in service, 
# step2: once all the participation download the file , remove the # from list  
list_room = []   #String

@app.route('/', methods=['GET', 'POST'])
def home():

    return "Hello /"

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
        list_room.append(room_number)
        print(list_room)
        return "Ok, Room Create Successful"
    elif(action == "JOIN"):
        for existed_room in list_room:
            if existed_room == room_number:
                print("JOIN LOL")
                return "Yes, room join success"
        
        return "No, room doesn't exist, please press CREATE "
        
    return "Check internet connection!"


# the roomnumber will be post to server when client use the postRoom to create or join the room 
aroomnum = str(1)   
# if the route is not existed then Not Found
@app.route('/Download' + aroomnum , methods=['GET', 'POST'])
def download():
    # if exist the route do the following
    print("Check reacton")
    return send_file("store_files\Atest.mp4", download_name = "Atest.mp4")



# for further develop
# I should add a String that save the file to the specific file 
# such as I type 2341 on android app and this number will be get to flask server 
# and then mkdir a dir [2341] after that all the files type this num will be saved in that
@app.route("/Audio_store",methods=['GET', 'POST'])
def audio():
    if request.files:
        audio_txt = request.files["audio_info"]
        audio = request.files["audio"]

        audio.save(os.path.join(file_save_path,audio.filename))
        audio_txt.save(os.path.join(file_save_path,audio_txt.filename))

        print("audio saved")

        return "OK, Audio upload finished"
        
    else:
        return "Something went wrong while upload audio!!!"

@app.route("/Video_store",methods=['GET', 'POST'])
def video():
    if request.files:
        video_txt = request.files["video_info"]
        video = request.files["video"]

        videoname = video.filename

        for dirPath, dirNames, all_files in walk(file_save_path):
            for afile in all_files:
                print(afile)
                print(type(afile))
                if afile == videoname:
                    return "You have already uploaded the Video"

        video.save(os.path.join(file_save_path,video.filename))
        video_txt.save(os.path.join(file_save_path,video_txt.filename))

        print("video saved")
        return "OK, Video upload finished"
    else:
        return "Something went wrong while upload video!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

