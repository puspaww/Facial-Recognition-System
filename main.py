from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #bg image
        img = Image.open(r"images\background.jpg")
        img = img.resize((1366,768), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img) 

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1366, height=768)

        title_lbl = Label(bg_img, text="FACIAL RECOGNITION SYSTEM", font=("Comic Sans MS", 20, "bold"),bg="black",fg="white")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        #Student button
        img1 = Image.open(r"images\student_details.png")
        img1 = img1.resize((200,200), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1) 

        b1 = Button(bg_img, image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=100, y=250, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("Comic Sans MS",16, "bold"),bg="black",fg="white")
        b1_1.place(x=100, y=450, width=200, height=40)

        #face detect
        img2 = Image.open(r"images\faceid.png")
        img2 = img2.resize((200,200), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2) 

        b2 = Button(bg_img, image=self.photoimg2,cursor="hand2")
        b2.place(x=400, y=250, width=200, height=200)

        b2_1 = Button(bg_img, text="Face Detect",cursor="hand2",font=("Comic Sans MS",16, "bold"),bg="black",fg="white")
        b2_1.place(x=400, y=450, width=200, height=40)

        #attendance
        img3 = Image.open(r"images\attendance.png")
        img3 = img3.resize((200,200), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3) 

        b3 = Button(bg_img, image=self.photoimg3,cursor="hand2")
        b3.place(x=700, y=250, width=200, height=200)

        b3_1 = Button(bg_img, text="Attendance",cursor="hand2",font=("Comic Sans MS",16, "bold"),bg="black",fg="white")
        b3_1.place(x=700, y=450, width=200, height=40)

        #exit
        img4 = Image.open(r"images\exit.png")
        img4 = img4.resize((200,200), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4) 

        b4 = Button(bg_img, image=self.photoimg4,cursor="hand2")
        b4.place(x=1000, y=250, width=200, height=200)

        b4_1 = Button(bg_img, text="Exit",cursor="hand2",font=("Comic Sans MS",16, "bold"),bg="black",fg="white")
        b4_1.place(x=1000, y=450, width=200, height=40)

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

        
if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
