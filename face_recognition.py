from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from student import Student


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        img_FD = Image.open(r"images\background.jpg")
        img_FD = img_FD.resize((1366, 768), Image.LANCZOS)
        self.photoimg_FD = ImageTk.PhotoImage(img_FD)

        bg_img_FD = Label(self.root, image=self.photoimg_FD)
        bg_img_FD.place(x=0, y=0, width=1366, height=768)

        title_lbl_fd = Label(self.root, text="Face Recognition", cursor="hand2", font=(
            "Comic Sans MS", 20, "bold"), bg="black", fg="white")
        title_lbl_fd.place(x=0, y=0, width=1366, height=40)

        button_fd = Button(bg_img_FD, text="Face Recognition", command=self.face_detect,
                           cursor="hand2", font=("Comic Sans MS", 16, "bold"), bg="grey", fg="black")
        button_fd.place(x=600, y=300, width=200, height=40)

    #################### Attendance#####################
    def mark_attendance(self, fd3, fd, fd1, fd2):
        with open("Attendance.csv", "r+", newline="\n") as f:
            dataList = f.readlines()
            name_list = []
            for line in dataList:
                entry = line.split((","))
                name_list.append(entry[0])

            #### for no repition of attendance####
            if ((fd3 not in name_list) and (fd not in name_list) and (fd1 not in name_list) and (fd2 not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(
                    f"\n{fd3},{fd},{fd1},{fd2},{dtString},{d1},Present")

    #################### face recognition##############

    def face_detect(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbour)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+h])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="HELLOPUSPA@123", database="Face_Recognition")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "Select Name from student where Student_ID=" + str(id))
                fd = my_cursor.fetchone()
                fd = "+".join(fd)

                my_cursor.execute(
                    "Select Department from student where Student_ID=" + str(id))
                fd1 = my_cursor.fetchone()
                fd1 = "+".join(fd1)

                my_cursor.execute(
                    "Select Semester from student where Student_ID="+str(id))
                fd2 = my_cursor.fetchone()
                fd2 = "+".join(fd2)

                my_cursor.execute(
                    "Select Student_ID from student where Student_ID="+str(id))
                fd3 = my_cursor.fetchone()
                fd3 = "+".join(fd3)

                if confidence > 80:
                    cv2.putText(
                        img, f"Student_ID:{fd3}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(
                        img, f"Name:{fd}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(
                        img, f"Department:{fd1}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(
                        img, f"Semester:{fd2}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(fd3, fd, fd1, fd2)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Student", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
