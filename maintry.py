from tkinter import*
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import tkinter.font as font

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Face Recognition")
        self.geometry("1366x768+0+0")

        frame_1 = customtkinter.CTkFrame(self)
        frame_1.pack(pady=20, padx=40, fill="both", expand=True)

        title_label = customtkinter.CTkLabel(master=frame_1, text="Facial Recognition App", font=customtkinter.CTkFont(size=40, weight="bold"))
        title_label.pack(padx=0, pady=20)

        
        a = customtkinter.CTkOptionMenu(master=frame_1, values=["Dark", "Light"], command=self.change_appearance_mode_event)
        a.pack(padx=0, pady=30)


        #student details pic
        student_details_pic = Image.open(r"C:\Users\User\Documents\Facial Recognition System\images\student_details.png")
        student_details_pic = student_details_pic.resize((200,200), Image.LANCZOS)
        self.studentDetailsPic = ImageTk.PhotoImage(student_details_pic)
        studentDetailsPic = Label(image=self.studentDetailsPic, bg="#2b2b2b")
        studentDetailsPic.place(x=150, y=200, width=200, height=200)

        #student details button
        b2=Button(master=frame_1, text="Student Details", border=0,cursor="hand2")
        b2['font']=font.Font(size=16)
        b2.place(x=100, y=400, width=200, height=50)


        #faceid pic
        face_id_pic = Image.open(r"C:\Users\User\Documents\Facial Recognition System\images\faceid.png")
        face_id_pic = face_id_pic.resize((200,200), Image.LANCZOS)
        self.faceidpic = ImageTk.PhotoImage(face_id_pic)
        faceidpic = Label(image=self.faceidpic, bg="#2b2b2b")
        faceidpic.place(x=400, y=200, width=200, height=200)

        #faceid button
        b1=Button(master=frame_1, text="Face Scan", border=0,cursor="hand2")
        b1['font']=font.Font(size=16)
        b1.place(x=365, y=400, width=200, height=50)


        #attendance pic
        attendance_pic = Image.open(r"C:\Users\User\Documents\Facial Recognition System\images\attendance.png")
        attendance_pic = attendance_pic.resize((200,200), Image.LANCZOS)
        self.attendancepic = ImageTk.PhotoImage(attendance_pic)
        attendancepic = Label(image=self.attendancepic, bg="#2b2b2b")
        attendancepic.place(x=700, y=200, width=200, height=200)

        #attendance button
        b1=Button(master=frame_1, text="Attendance", border=0,cursor="hand2")
        b1['font']=font.Font(size=16)
        b1.place(x=665, y=400, width=200, height=50)



        #exit pic
        exit_pic = Image.open(r"C:\Users\User\Documents\Facial Recognition System\images\exit.png")
        exit_pic = exit_pic.resize((200,200), Image.LANCZOS)
        self.exitpic = ImageTk.PhotoImage(exit_pic)
        exitpic = Label(image=self.exitpic, bg="#2b2b2b")
        exitpic.place(x=1000, y=200, width=200, height=200)

        #exit button
        b1=Button(master=frame_1, text="Exit", border=0,cursor="hand2")
        b1['font']=font.Font(size=16)
        b1.place(x=965, y=400, width=200, height=50)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
  






if __name__ == "__main__":
    app = App()
    app.mainloop()