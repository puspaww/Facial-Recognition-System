from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from student import Student

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        
        title_lbl = Label(self.root, text="Train Data Sets", cursor="hand2", font=("Comic Sans MS", 20, "bold"),bg="black",fg="white")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        #button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2",font=("Comic Sans MS",16, "bold"),bg="black",fg="white")
        b1_1.place(x=600, y=300, width=200, height=40)

    def train_classifier(data_dir):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')      #converts to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #Train the cassifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data Sets Completed!")








if __name__=="__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()