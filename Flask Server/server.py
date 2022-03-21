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




@app.route("/Audio_store",methods=['GET', 'POST'])
def audio():
    if request.files:
        room_number = request.form["room_number"]
        audio_txt = request.files["audio_info"]
        audio = request.files["audio"]

        #create a room dir for store files
        roomdir = file_save_path + "/" + room_number
        CHECK_FOLDER = os.path.isdir(roomdir)
        if not CHECK_FOLDER:
            os.makedirs(roomdir)
            print("created folder : ", roomdir)
        else:
            print( roomdir, "folder already exists.")

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

