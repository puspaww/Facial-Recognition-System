from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        ########VARIABLES###########
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_course=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()
        self.var_gender=StringVar()


        img = Image.open(r"C:\Users\User\Documents\Facial Recognition System\images\background.jpg")
        img = img.resize((1366,768), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img) 

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1366, height=768)

        title_lbl = Label(bg_img, text="Student Management System", font=("Comic Sans MS", 20, "bold"),bg="black",fg="white")
        title_lbl.place(x=0, y=0, width=1366, height=40)

        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=33,y=40, width=1300, height=625)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE, text="Student Details", font=("Comic Sans MS", 11, "bold"))
        Left_frame.place(x=50, y =20, width=600, height=200)

        #Department
        dep_label = Label(Left_frame, text="Department", font=("Comic Sans MS", 11, "bold"),bg="white",fg="black")
        dep_label.grid(row=0, column=0, padx=2, pady=10,sticky=W)

        
        dep_combo = ttk.Combobox(Left_frame,textvariable=self.var_dep,font=("Comic Sans MS", 11, "bold"), state="read only")
        dep_combo["values"] = ("Select Department", "Computer","Civil","Mechanical","Electrical")

        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

        #year
        Year_label = Label(Left_frame,text="Year", font=("Comic Sans MS", 11, "bold"),bg="white")
        Year_label.grid(row=1, column=0, padx=2, pady=10)

        Year_combo = ttk.Combobox(Left_frame,textvariable=self.var_year,font=("Comic Sans MS", 11, "bold"), state="read only")
        Year_combo["values"] = ("Select Year", "2018","2019","2020","2021","2022")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        #Semester
        Sem_label = Label(Left_frame,text="Semester", font=("Comic Sans MS", 11, "bold"),bg="white")
        Sem_label.grid(row=2, column=0, padx=2, pady=10)

        Sem_combo = ttk.Combobox(Left_frame,textvariable=self.var_sem,font=("Comic Sans MS", 11, "bold"), state="read only")
        Sem_combo["values"] = ("Select Semester", "I","II")
        Sem_combo.current(0)
        Sem_combo.grid(row=2, column=1, padx=2, pady=10,sticky=W)

        #Course
        Course_label = Label(Left_frame,text="  Course", font=("Comic Sans MS", 11, "bold"),bg="white")
        Course_label.grid(row=2, column=2, padx=2, pady=10, sticky=W)

        Course_entry = ttk.Entry(Left_frame,textvariable=self.var_course, width=20,font=("Comic Sans MS", 11, "bold"))
        Course_entry.grid(row = 2, column=3,padx=2,pady=10, sticky=W)


        #left bottom frame
        Leftbottom_frame = LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE, text="Student Information", font=("Comic Sans MS", 11, "bold"))
        Leftbottom_frame.place(x=50, y =250, width=600, height=345)

        #Student ID
        StudentID_label = Label(Leftbottom_frame,text="Student ID:", font=("Comic Sans MS", 11, "bold"),bg="white")
        StudentID_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        StudentID_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_id, width=20,font=("Comic Sans MS", 11, "bold"))
        StudentID_entry.grid(row = 0, column=1,padx=2,pady=10, sticky=W)

        #Student Name
        StudentName_label = Label(Leftbottom_frame,text="Student Name:", font=("Comic Sans MS", 11, "bold"),bg="white")
        StudentName_label.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        StudentName_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_name, width=20,font=("Comic Sans MS", 11, "bold"))
        StudentName_entry.grid(row = 1, column=1,padx=2,pady=10, sticky=W)

        #DOB
        DOB_label = Label(Leftbottom_frame,text="DOB:", font=("Comic Sans MS", 11, "bold"),bg="white")
        DOB_label.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        DOB_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_dob, width=20,font=("Comic Sans MS", 11, "bold"))
        DOB_entry.grid(row = 0, column=3,padx=2,pady=10, sticky=W)

        #email
        Email_label = Label(Leftbottom_frame,text="Email:", font=("Comic Sans MS", 11, "bold"),bg="white")
        Email_label.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        Email_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_email, width=20,font=("Comic Sans MS", 11, "bold"))
        Email_entry.grid(row = 1, column=3,padx=2,pady=10, sticky=W)

        #Phone 
        Phone_label = Label(Leftbottom_frame,text="Phone:", font=("Comic Sans MS", 11, "bold"),bg="white")
        Phone_label.grid(row=2, column=2, padx=2, pady=10, sticky=W)

        Phone_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_phone, width=20,font=("Comic Sans MS", 11, "bold"))
        Phone_entry.grid(row = 2, column=3,padx=2,pady=10, sticky=W)

        #Address
        Address_label = Label(Leftbottom_frame,text="Address:", font=("Comic Sans MS", 11, "bold"),bg="white")
        Address_label.grid(row=2, column=0, padx=2, pady=10, sticky=W)

        Address_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_address, width=20,font=("Comic Sans MS", 11, "bold"))
        Address_entry.grid(row = 2, column=1,padx=2,pady=10, sticky=W)

        #Gender
        Gender_label = Label(Leftbottom_frame,text="Gender:", font=("Comic Sans MS", 11, "bold"),bg="white")
        Gender_label.grid(row=3, column=0, padx=2, pady=10, sticky=W)

        Gender_entry = ttk.Entry(Leftbottom_frame,textvariable=self.var_gender, width=20,font=("Comic Sans MS", 11, "bold"))
        Gender_entry.grid(row = 3, column=1,padx=2,pady=10, sticky=W)

        #radiobuttons
        self.var_radio1=StringVar()
        radio_button_1=ttk.Radiobutton(Leftbottom_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radio_button_1.grid(row=4,column=0)

        self.var_radio2=StringVar()        
        radio_button_2=ttk.Radiobutton(Leftbottom_frame,variable=self.var_radio2,text="Do not take Photo Sample", value="No")
        radio_button_2.grid(row=4,column=1)

        #buttonframe
        button_frame = Frame(Leftbottom_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=240, width=590, height=40)

        save_button=Button(button_frame,text="Save",command=self.add_data, width=15,font=("Comic Sans MS", 11, "bold"), bg= "grey")
        save_button.grid(row=0, column=0)

        update_button=Button(button_frame,text="Update",width=16,command=self.update_data, font=("Comic Sans MS", 11, "bold"), bg= "grey")
        update_button.grid(row=0, column=1)

        delete_button=Button(button_frame,text="Delete",command=self.delete_data, width=15,font=("Comic Sans MS", 11, "bold"), bg= "grey")
        delete_button.grid(row=0, column=2)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data, width = 15,font=("Comic Sans MS", 11, "bold"), bg= "grey")
        reset_button.grid(row=0, column=3)

        button_frame1 = Frame(Leftbottom_frame, bd=2, relief=RIDGE, bg="white")
        button_frame1.place(x=0, y=280, width=590, height=40)

        take_sample_button=Button(button_frame1,text="Take Photo Sample",width=31,font=("Comic Sans MS", 11, "bold"), bg= "grey")
        take_sample_button.grid(row=0, column=0)

        Update_sample_button=Button(button_frame1,text="Update Photo Sample",width=32,font=("Comic Sans MS", 11, "bold"), bg= "grey")
        Update_sample_button.grid(row=0, column=1)


        

        

        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE, text="Student Details", font=("Comic Sans MS", 11, "bold"))
        Right_frame.place(x=700, y =20, width=550, height=575)




        ######Search System######
        Search_frame = LabelFrame(Right_frame,bg="white",relief=RIDGE, text="Search System", font=("Comic Sans MS", 11, "bold"))
        Search_frame.place(x=0, y =150, width=540, height=80)

        Search_label = Label(Search_frame,text="Search By:", font=("Comic Sans MS", 11, "bold"),bg="white")
        Search_label.grid(row=0, column=0, padx=2, pady=5)

        search_combo = ttk.Combobox(Search_frame,width =15,font=("Comic Sans MS", 11, "bold"), state="read only")
        search_combo["values"] = ("Select", "Student ID","Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame,width=15,font=("Comic Sans MS", 11, "bold"))
        search_entry.grid(row = 0, column=2,padx=2,pady=10, sticky=W)

        search_button=Button(Search_frame,text="Search",font=("Comic Sans MS", 11, "bold"), bg= "grey")
        search_button.grid(row=0, column=3)

        ShowAll_button=Button(Search_frame,text="Show All",font=("Comic Sans MS", 11, "bold"), bg= "grey")
        ShowAll_button.grid(row=0, column=4)



        #########Table Frame################
        table_frame = LabelFrame(Right_frame,bg="white",relief=RIDGE, font=("Comic Sans MS", 11, "bold"))
        table_frame.place(x=0, y =230, width=540, height=318)

        scroll_x=ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Department","Year", "Semester","Course", "Student_ID","Name","DOB","Email","Address","Phone","Gender","Photo_Sample"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_Y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_Y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Student_ID", text="Student_ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Photo_Sample",text="Photo_Sample")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Student_ID",width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Photo_Sample",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #############################add data##############################
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username = "root", password = "HELLOPUSPA@123", database = "Face_Recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                    self.var_dep.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_radio1.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully!", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)




    ###################fetching data from database##########################
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username = "root", password = "HELLOPUSPA@123", database = "Face_Recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #######################get cursor#####################################
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_course.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_email.set(data[7]),
        self.var_address.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_radio1.set(data[11])



    #############################update###################################
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) 
        else:
            try:
                Upadate = messagebox.askyesno("Update","Do you want to update the student details?",parent=self.root)
                if Upadate>0:

                    conn=mysql.connector.connect(host="localhost", username = "root", password = "HELLOPUSPA@123", database = "Face_Recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s, Year=%s, Semester=%s, Course=%s, Name=%s, DOB=%s,Email=%s,Address=%s,Phone=%s,Gender=%s, Photo_Sample=%s where Student_ID=%s",(self.var_dep.get(),self.var_year.get(),self.var_sem.get(),self.var_course.get(),self.var_name.get(),self.var_dob.get(),self.var_email.get(),self.var_address.get(),self.var_phone.get(),self.var_gender.get(),self.var_radio1.get(),self.var_id.get()))
                                                                                                                                                                                                          
                                                                                                                                                                                 

                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


    
    ###############################delete#########################################
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID must be required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username = "root", password = "HELLOPUSPA@123", database = "Face_Recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
            
    
    ########################reset###########################
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_course.set("")
        self.var_id.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_radio1.set("")

        



if __name__=="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()