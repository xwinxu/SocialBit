# install mysql library with conda first...
# import MySQLdb
import face_recognition
import pymysql
from datetime import datetime, timedelta

import cv2

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# host="localhost"
# user="root"
# passwd="root"
db = pymysql.connect(host="104.198.61.190",
                  user="bowen",
                  passwd="bowen",
                  db="friends")
# take this out because this cursor is part of another cursor wrapper
# replace with db.cursor() as cursor below
# the below syntax is for another pymysql thing
# cursor = db.cursor()

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
winnie_image = face_recognition.load_image_file("winnie.png")
winnie_face_encoding = face_recognition.face_encodings(winnie_image)[0]

# Load a second sample picture and learn how to recognize it.
david_image = face_recognition.load_image_file("david.png")
david_face_encoding = face_recognition.face_encodings(david_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    winnie_face_encoding,
    david_face_encoding
]
known_face_names = [
    "Barack Winnie",
    "David Biden"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
start = 0
current_face = ''
# temp = ''
is_start = True
is_delay = False

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # append onto a face_names list after recognizing and storing the name of the face
            face_names.append(name)

    process_this_frame = not process_this_frame

    # record duration of face meeting
    # if face_names:
    #     if current_face == face_names[0]:
    #         pass
    #     elif current_face == "":
    #         start = datetime.now()
    #         current_face = face_names[0]
    # else:
    #     if current_face:
    #         timeout = datetime.now()
    #         # duration = str(datetime.now() - start)
    #         duration = datetime.now() - start
    #         try:
    #             #print(duration)
    #             with db.cursor() as cursor:
    #                 sql = "INSERT INTO node VALUES (%s,%s,%s)"
    #                 cursor.execute(sql, (current_face, 'MIT', duration))
    #             db.commit()
    #         except:     
    #             db.rollback()
    #         current_face = ""

    # if someone appears and there wasn't a face previously (new session)
    if face_names and is_start:
        # start the timer
        start = datetime.now()
        # set the current face
        current_face = face_names[0]
        is_start = False
        # set a temporary variable, when you leave the frame the current is set to none, but we want temp reset too
        #temp = ""
    # if someone leaves the frame
    elif not face_names and current_face and not is_delay:
        delay = datetime.now()
        is_delay = True
    # person comes back before 3 seconds, accounts for unknowns too
    elif face_names and is_delay:
        is_delay = False
    # person away for 3 seconds or more
    elif is_delay:
    # elif not face_names and current_face and not on_hold:
    #     # face goes out of the frame, start calculating delay time
    #     delay = datetime.now()
    #     # keep track of the face that just left the frame so that it can be added to database
    #     on_hold = True
    #     # temp = current_face
    #     # current_face = ""
    # elif temp:
        # difference between current time and when delay started (exited the frame)
        difference = (datetime.now() - delay).total_seconds()
        # print(difference)
        # if it's been three seconds, submit it to the database. Else go to next data frame and turn off the is_delay flag
        # to indicate that 3 seconds hasn't passed for this one person
        if difference > 3:
            # subtract the 3 second delay from the time frame as well
            duration = datetime.now() - timedelta(seconds=3) - start
            print(duration)
            try:
                with db.cursor() as cursor:
                    sql = "INSERT INTO node VALUES (%s,%s,%s)"
                    cursor.execute(sql, (current_face, 'MIT', str(duration)))
                db.commit()
            except:     
                db.rollback()
            # reset once a person has left the frame for more than three seconds
            is_delay = False
            is_start = True

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
