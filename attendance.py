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
import csv  # comma separated value
from tkinter import filedialog

Data = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_sem = StringVar()
        self.var_att = StringVar()

        img = Image.open(r"images\background.jpg")
        img = img.resize((1366, 768), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1366, height=768)

        title_lbl = Label(bg_img, text="Student's Management System", font=(
            "Comic Sans MS", 20, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=33, y=40, width=1300, height=625)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE,
                                font=("Comic Sans MS", 11, "bold"))
        Left_frame.place(x=50, y=20, width=600, height=200)

        # Left bottom frame
        Leftbottom_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE,
                                      text="Student Information", font=("Comic Sans MS", 11, "bold"))
        Leftbottom_frame.place(x=50, y=250, width=600, height=345)

        # Student ID
        StudentID_label = Label(Leftbottom_frame, text="Student ID:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        StudentID_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        StudentID_entry = ttk.Entry(
            Leftbottom_frame, width=20, textvariable=self.var_id, font=("Comic Sans MS", 11, "bold"))
        StudentID_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Student Name
        StudentName_label = Label(Leftbottom_frame, text="Student Name:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        StudentName_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        StudentName_entry = ttk.Entry(
            Leftbottom_frame, width=20, textvariable=self.var_name, font=("Comic Sans MS", 11, "bold"))
        StudentName_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Dep
        Dep_label = Label(Leftbottom_frame, text="Dep:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        Dep_label.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        Dep_entry = ttk.Entry(Leftbottom_frame, textvariable=self.var_dep, width=20, font=(
            "Comic Sans MS", 11, "bold"))
        Dep_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Date
        Date_label = Label(Leftbottom_frame, text="Date:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        Date_label.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        Date_entry = ttk.Entry(Leftbottom_frame, textvariable=self.var_date, width=20, font=(
            "Comic Sans MS", 11, "bold"))
        Date_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Time
        Time_label = Label(Leftbottom_frame, text="Time:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        Time_label.grid(row=2, column=2, padx=2, pady=10, sticky=W)

        Time_entry = ttk.Entry(Leftbottom_frame, textvariable=self.var_time, width=20, font=(
            "Comic Sans MS", 11, "bold"))
        Time_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # Sem
        Sem_label = Label(Leftbottom_frame, text="Sem:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        Sem_label.grid(row=2, column=0, padx=2, pady=10, sticky=W)

        Sem_entry = ttk.Entry(Leftbottom_frame, textvariable=self.var_time, width=20, font=(
            "Comic Sans MS", 11, "bold"))
        Sem_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # AttendanceStatus
        AttendanceStatus_label = Label(Leftbottom_frame, text="Attendance:", font=(
            "Comic Sans MS", 11, "bold"), bg="white")
        AttendanceStatus_label.grid(row=3, column=0, padx=2, pady=10)

        AttendanceStatus_combo = ttk.Combobox(Leftbottom_frame, textvariable=self.var_att, font=(
            "Comic Sans MS", 11, "bold"), state="read only")
        AttendanceStatus_combo["values"] = ("Status", "Present",
                                            "Absent")
        AttendanceStatus_combo.current(0)
        AttendanceStatus_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # buttonframe
        button_frame = Frame(Leftbottom_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=280, width=590, height=40)

        Import_button = Button(button_frame, command=self.import_data, text="Import", width=15, font=(
            "Comic Sans MS", 11, "bold"), bg="grey")
        Import_button.grid(row=0, column=0)

        Export_button = Button(button_frame, command=self.export_data, text="Export", width=16, font=(
            "Comic Sans MS", 11, "bold"), bg="grey")
        Export_button.grid(row=0, column=1)

        Update_button = Button(button_frame, text="Update", width=15, font=(
            "Comic Sans MS", 11, "bold"), bg="grey")
        Update_button.grid(row=0, column=2)

        Reset_button = Button(button_frame, command=self.reset_data, text="Reset", width=15, font=(
            "Comic Sans MS", 11, "bold"), bg="grey")
        Reset_button.grid(row=0, column=3)

        # Right Label frame
        Right_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE,
                                 text="Attendance Status", font=("Comic Sans MS", 11, "bold"))
        Right_frame.place(x=700, y=20, width=550, height=575)

        table_frame = LabelFrame(
            Right_frame, bg="white", relief=RIDGE, font=("Comic Sans MS", 11, "bold"))
        table_frame.place(x=0, y=0, width=540, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_Y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.Attendance_table = ttk.Treeview(table_frame, columns=("Student_ID", "Name", "Department", "Semester", "Time", "Date",
                                                                   "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_Y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_Y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("Student_ID", text="Student_ID")
        self.Attendance_table.heading("Name", text="Name")
        self.Attendance_table.heading("Department", text="Department")
        self.Attendance_table.heading("Semester", text="Semester")
        self.Attendance_table.heading("Time", text="Time")
        self.Attendance_table.heading("Date", text="Date")
        self.Attendance_table.heading("Attendance", text="Attendance")

        self.Attendance_table["show"] = "headings"

        self.Attendance_table.column("Student_ID", width=100)
        self.Attendance_table.column("Name", width=100)
        self.Attendance_table.column("Department", width=100)
        self.Attendance_table.column("Semester", width=100)
        self.Attendance_table.column("Time", width=100)
        self.Attendance_table.column("Date", width=100)
        self.Attendance_table.column("Attendance", width=100)

        self.Attendance_table.pack(fill=BOTH, expand=1)
        self.Attendance_table.bind("<ButtonRelease>", self.get_cursor)

        ############# Fetch data###########

    def fetchData(self, rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("", END, values=i)

    # Import csv
    def import_data(self):
        global Data
        Data.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                Data.append(i)
            self.fetchData(Data)

    # Export csv
    def export_data(self):
        try:
            if len(Data) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found", parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(file_name, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in Data:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Exported!", "Your Data has been Exported to "+os.path.basename(file_name)+" successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.Attendance_table.focus()
        content = self.Attendance_table.item(cursor_row)
        rows = content["values"]

        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_sem.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_att.set(rows[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_sem.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_att.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
