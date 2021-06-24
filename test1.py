import cv2
import label_image
import time
import os,random

face_cascade = cv2.CascadeClassifier(cv2.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
size = 4
text = 0
now = time.time()### For calculate seconds of video
future = now + 10  #### here is second of time which taken by emotion recognition system ,you can change it


while True:
    ret, img = cap.read()
#    mini = cv2.resize(img, (int(img.shape[1] / size), int(img.shape[0] / size)))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    for (x, y, w, h) in faces:
#        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
        sub_face = img[y:y + h, x:x + w]
        FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()
        print(text)
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == 'Angry':
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(img, text, (x + h, y), font, 1, (0, 25,255), 2)

        if text == 'Smile':
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,260,0), 7)
            cv2.putText(img, text, (x + h, y), font, 1, (0,260,0), 2)

        if text == 'Neutral':
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 7)
            cv2.putText(img, text, (x + h, y), font, 1, (0, 255, 255), 2)

        if text == 'Sad':
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,191,255), 7)
            cv2.putText(img, text, (x + h, y), font, 1, (0,191,255), 2)

    cv2.imshow('img', img)
    if time.time() > future: ##after 20second music will play
        try:
            cv2.destroyAllWindows()
            if text == 'Angry':
                randomfile = random.choice(os.listdir("./songs/Angry/"))
                print('You are angry !!!! please calm down:) ,I will play song for you :' + randomfile)
                file = ('C:/Users/sumuk/Desktop/Capstone Project/final1/Music_player_with_Emotions_recognition-master/songs/Angry/' + randomfile)
                os.startfile(file)

            if text == 'Smile':
                randomfile = random.choice(os.listdir("./songs/Smile/"))
                print('You are smiling :) ,I playing special song for you: ' + randomfile)
                file = ('C:/Users/sumuk/Desktop/Capstone Project/final1/Music_player_with_Emotions_recognition-master/songs/Smile/' + randomfile)
                os.startfile(file)

            if text == 'Neutral':
                randomfile = random.choice(os.listdir("./songs/Fear/"))
                print('You are Neutral of something ,I playing song for you: ' + randomfile)
                file = ('C:/Users/sumuk/Desktop/Capstone Project/final1/Music_player_with_Emotions_recognition-master/songs/Fear/' + randomfile)
                os.startfile(file)

            if text == 'Sad':
                randomfile = random.choice(os.listdir("./songs/Sad/"))
                print('You are sad,dont worry:) ,I playing song for you: ' + randomfile)
                file = ('C:/Users/sumuk/Desktop/Capstone Project/final1/Music_player_with_Emotions_recognition-master/songs/Sad/' + randomfile)
                os.startfile(file)
            break
        except Exception as e:
            print(e)
            print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
            break

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()