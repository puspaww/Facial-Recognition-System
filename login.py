from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

# 2:19:00 line 100


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        self.bg = ImageTk.PhotoImage(file=r"photos\images.png")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=170, width=340, height=450)

        img1 = Image.open(r"photos\972105c5a775f38cf33d3924aea053f1.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photo_image1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photo_image1, bg="black", borderwidth=0)
        lblimg1.place(x=630, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "Times New Roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=(
            "Times New Roman", 20, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("Times New Roman", 15, "bold"))
        self.txtuser.place(x=40, y=200, width=270)

        password = lbl = Label(frame, text="Password", font=(
            "Times New Roman", 20, "bold"), fg="white", bg="black")
        password.place(x=70, y=230)

        self.txtpass = ttk.Entry(frame, font=("Times New Roman", 15, "bold"))
        self.txtpass.place(x=40, y=270, width=270)

        # =======Icon images=================================
        img2 = Image.open(r"photos\972105c5a775f38cf33d3924aea053f1.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photo_image2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photo_image2, bg="black", borderwidth=0)
        lblimg2.place(x=550, y=330, width=25, height=25)

        img3 = Image.open(r"photos\download.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photo_image3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photo_image3, bg="black", borderwidth=0)
        lblimg3.place(x=550, y=405, width=25, height=25)

        # LoginButton
        loginbtn = Button(frame, command=self.login, text="Login", font=("Times New Roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=310, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "Times New Roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=360, width=160)

        # Forgot password button
        forgotbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=(
            "Times New Roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=15, y=390, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error!", "all Fields are required")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Legion@123", database="codewithme")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s", (
                self.txtuser.get(),
                self.txtpass.get(),
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username")
            else:
                open_main = messagebox.askyesno("YES/NO", "Accept only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
        # open the interface
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    # ===============================reset password==================================

    def reset_pass(self):
        if self.combo_security.get() == "Select":
            messagebox.showerror(
                "Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror(
                "Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror(
                "Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Legion@123", database="codewithme")
            my_cursor = conn.cursor()
            query = (
                "select * from register where email = %s and securityQ = %s and securityA = %s")
            value = (self.txtuser.get(), self.combo_security.get(),
                     self.txt_security.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "New Password is set", parent=self.root2)
                self.root2.destroy()

    # =======================================forgot_password_window==========================

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Legion@123", database="codewithme")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror(
                    "Error", "please enter the valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forgot password", font=(
                    "Times New Roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=-200, relwidth=1, relheight=1)

                Security = Label(self.root2, text="Select Security Question", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                Security.place(x=50, y=80)

                self.combo_security = ttk.Combobox(self.root2, font=(
                    "times new roman", 15, "bold"), state="readonly")
                self.combo_security["values"] = (
                    "Select", "Your Birth Place", "Your Pet name")
                self.combo_security.place(x=50, y=110, width=250)
                self.combo_security.current(0)

                security_A = Label(self.root2, text="Security Answer", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=(
                    "times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=130, y=300)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

    # ========================variables=======================

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # =============bg image============
        self.bg = ImageTk.PhotoImage(file=r"photos\images.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =============left image============
        self.bg1 = ImageTk.PhotoImage(file=r"photos\download (1).png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ==============main frame====================
        frame = Frame(self.root, bg='white')
        frame.place(x=520, y=100, width=800, height=550)
        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ======================label and entry===================

        # ============row1============

        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=(
            "times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last name", font=(
            "times new roman", 15, "bold"), fg="black", bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ============row2============

        contact = Label(frame, text="Contact No.", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ============row3============

        Security = Label(frame, text="Select Security Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        Security.place(x=50, y=240)

        self.combo_security = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", 15, "bold"), state="readonly")
        self.combo_security["values"] = (
            "Select", "Your Birth Place", "Your Pet name")
        self.combo_security.place(x=50, y=270, width=250)
        self.combo_security.current(0)

        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ============row4============

        pswd = Label(frame, text="Password.", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_email.place(x=370, y=340, width=250)

        # ===============check buton==============
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree the terms and conditions", font=(
            "times new roman", 12, "bold"), bg="white", offvalue=0, onvalue=1)
        checkbtn.place(x=50, y=380)

        # ================buttons=================

        img1 = Image.open(r"photos\llo.jfif")
        img1 = img1.resize((200, 45), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, command=self.register_data,
                    borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=10, y=420, width=200)

        # img2 = Image.open(r"photos\lol.jfif")
        # img2 = img2.resize((200,45),Image.LANCZOS)
        # self.photoimage2 = ImageTk.PhotoImage(img2)
        # b2 = Button(frame,image = self.photoimage2,borderwidth=0,cursor = "hand2",font = ("times new roman",15,"bold"),fg = "white")
        # b2.place(x = 330, y = 420, width=200)

        # =====================function declaration================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passowrds do not match")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please Agree Our Terms and Conditions")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Legion@123", database="codewithme")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess", "Registered Successfully")


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # bg image
        img = Image.open(r"images\background.jpg")
        img = img.resize((1366, 768), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1366, height=768)

        title_lbl = Label(bg_img, text="FACIAL RECOGNITION SYSTEM", font=(
            "Comic Sans MS", 20, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        # Student button
        img1 = Image.open(r"images\student_details.png")
        img1 = img1.resize((200, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img, image=self.photoimg1,
                    command=self.student_details, cursor="hand2")
        b1.place(x=100, y=250, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details,
                      cursor="hand2", font=("Comic Sans MS", 16, "bold"), bg="black", fg="white")
        b1_1.place(x=100, y=450, width=200, height=40)

        # face detect
        img2 = Image.open(r"images\faceid.png")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img, image=self.photoimg2,
                    cursor="hand2", command=self.face_data)
        b2.place(x=400, y=250, width=200, height=200)

        b2_1 = Button(bg_img, text="Face Detect", cursor="hand2", command=self.face_data, font=(
            "Comic Sans MS", 16, "bold"), bg="black", fg="white")
        b2_1.place(x=400, y=450, width=200, height=40)

        # attendance
        img3 = Image.open(r"images\attendance.png")
        img3 = img3.resize((200, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img, image=self.photoimg3,
                    command=self.attendance_data, cursor="hand2")
        b3.place(x=700, y=250, width=200, height=200)

        b3_1 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=(
            "Comic Sans MS", 16, "bold"), bg="black", fg="white")
        b3_1.place(x=700, y=450, width=200, height=40)

        # exit
        img4 = Image.open(r"images\exit.png")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b4.place(x=1000, y=250, width=200, height=200)

        b4_1 = Button(bg_img, text="Exit", cursor="hand2", font=(
            "Comic Sans MS", 16, "bold"), bg="black", fg="white")
        b4_1.place(x=1000, y=450, width=200, height=40)

        # train data
        b1_1 = Button(self.root, text="Train Data", command=self.train_data, cursor="hand2", font=(
            "Comic Sans MS", 16, "bold"), bg="black", fg="white")
        b1_1.place(x=550, y=550, width=200, height=40)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    main()
