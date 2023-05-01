from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from main import Face_Recognition_System

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
        self.root.wm_iconbitmap("images\login.ico")

        self.bg = ImageTk.PhotoImage(file=r"images\photos\images.png")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=510, y=170, width=340, height=450)

        img1 = Image.open(
            r"images\photos\972105c5a775f38cf33d3924aea053f1.jpg")
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
        img2 = Image.open(
            r"images\photos\972105c5a775f38cf33d3924aea053f1.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photo_image2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photo_image2, bg="black", borderwidth=0)
        lblimg2.place(x=550, y=330, width=25, height=25)

        img3 = Image.open(r"images\photos\download.png")
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
            messagebox.showerror("Error!", "All fields are required")
        else:
            conn = mysql.connector.connect(
                # host="localhost", user="root", password="Legion@123", database="codewithme")
                host="localhost", user="root", password="HELLOPUSPA@123", database="login_&_register")
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
                # host="localhost", user="root", password="Legion@123", database="codewithme")
                host="localhost", user="root", password="HELLOPUSPA@123", database="login_&_register")
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
                # host="localhost", user="root", password="Legion@123", database="codewithme")
                host="localhost", user="root", password="HELLOPUSPA@123", database="login_&_register")
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
        self.bg = ImageTk.PhotoImage(file=r"images\photos\images.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =============left image============
        self.bg1 = ImageTk.PhotoImage(file=r"images\photos\download (1).png")
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

        img1 = Image.open(r"images\photos\llo.jfif")
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
                # host="localhost", user="root", password="Legion@123", database="codewithme")
                host="localhost", user="root", password="HELLOPUSPA@123", database="login_&_register")
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


if __name__ == "__main__":
    main()
