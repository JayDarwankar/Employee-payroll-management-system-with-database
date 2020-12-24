from tkinter import *
import pymysql
from tkinter import messagebox,ttk
import time
import os
import tempfile

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management system by Jay Darwankar".center(390))
        self.root.geometry("1350x750+0+0")
        bg_color = "LightGray"
        title = Label(self.root, text="Employee Payroll Management System", bg=bg_color, fg="black",
                      font="arial 30 bold", anchor="w", padx=10)
        title.place(x=0, y=0, relwidth=1)
        btn_emp = Button(self.root, text="All Employee's",command=self.emp_structure, font="Times 13 bold", bd=4, relief=GROOVE,
                            bg="dark slate gray",
                            fg="white").place(x=1030, y=12, width=150, height=30)

        # ============Frame1==============================
        # =====variables========

        self.var_Empcode = StringVar()
        self.var_designation = StringVar()
        self.var_doj = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_age = StringVar()
        self.var_experience = StringVar()
        self.var_gender = StringVar()
        self.var_id = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.bg_color="thistle3"
        F1 = Frame(self.root, bd=3, relief=GROOVE, bg=self.bg_color)
        F1.place(x=10, y=60, width=750, height=620)
        title = Label(F1, text="Employee Details", bg="yellow", fg="black", font="arial 20 bold", anchor="w",
                      padx=10).place(x=0, y=0, relwidth=1)

        emp_lbl = Label(F1, text="Employee Code:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                        padx=10).place(x=10, y=70)
        emp_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 15 bold",
                        textvariable=self.var_Empcode).place(x=200, y=70)

        search_btn = Button(F1, text="Search",command=self.search, font="arial 15 bold", bd=4, relief=SUNKEN, bg="dark slate gray",
                            fg="white").place(x=500, y=70, width=100, height=30)

        des_lbl = Label(F1, text="Designation:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                        padx=10).place(x=10, y=150)
        des_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=20,
                        textvariable=self.var_designation).place(x=200, y=150)

        date_job_lbl = Label(F1, text="D.O.J:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                             padx=10).place(x=400, y=150)
        date_job_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                             textvariable=self.var_doj).place(x=500, y=150)

        name_lbl = Label(F1, text="Name:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                         padx=10).place(x=10, y=220)
        name_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=18,
                         textvariable=self.var_name).place(x=200, y=220)

        date_of_birth_lbl = Label(F1, text="D.O.B:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                                  padx=10).place(x=400, y=220)
        date_of_birth_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                                  textvariable=self.var_dob).place(x=500, y=220)

        age_lbl = Label(F1, text="Age:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                        padx=10).place(x=10, y=290)
        age_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                        textvariable=self.var_age).place(x=200, y=290)

        experience_lbl = Label(F1, text="Experience:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                               padx=10).place(x=400, y=290)
        experience_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                               textvariable=self.var_experience).place(x=540,
                                                                       y=290)

        gender_lbl = Label(F1, text="Gender:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                           padx=10).place(x=10, y=370)
        gender_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                           textvariable=self.var_gender).place(x=200, y=370)

        id_lbl = Label(F1, text="ID Proof:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                       padx=10).place(x=400, y=370)
        id_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                       textvariable=self.var_id).place(x=540, y=370)

        email_lbl = Label(F1, text="Email:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                          padx=10).place(x=10, y=450)
        email_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=20,
                          textvariable=self.var_email).place(x=200, y=450)

        contact_lbl = Label(F1, text="Contact:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                            padx=10).place(x=400, y=450)
        contact_txt = Entry(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=15,
                            textvariable=self.var_contact).place(x=540, y=450)

        address_lbl = Label(F1, text="Address:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                            padx=10).place(x=10, y=510)
        address_t = Text(F1, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold")
        address_t.place(x=200, y=510, width=440, height=100)

        # =============Frame2=============================

        # =====variables========

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net = StringVar()

        F2 = Frame(self.root, bd=3, relief=GROOVE, bg=self.bg_color)
        F2.place(x=770, y=60, width=575, height=300)
        emp_salary_lbl = Label(F2, text="Employee Salary Details", fg="black", bg="yellow", font='arial 20 bold',
                               anchor="w").place(x=0, y=0, relwidth=1)

        month_lbl = Label(F2, text="Month:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                          padx=10).place(x=8, y=50)
        month_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                          textvariable=self.var_month).place(x=90, y=50)

        year_lbl = Label(F2, text="Year:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                         padx=10).place(x=190, y=50)
        year_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                         textvariable=self.var_year).place(x=260, y=50)

        salary_lbl = Label(F2, text="Salary:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                           padx=10).place(x=370, y=50)
        salary_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=12,
                           textvariable=self.var_salary).place(x=450, y=50)

        # ===Total_absent row=====
        total_days_lbl = Label(F2, text="Total Days:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                               padx=10).place(x=8, y=100)
        total_days_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                               textvariable=self.var_days).place(x=170, y=100)

        absent_lbl = Label(F2, text="Absents Days:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                           padx=10).place(x=280, y=100)
        absent_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                           textvariable=self.var_absent).place(x=460, y=100)

        # ======medical_Pf row===============

        medical_lbl = Label(F2, text="Medical:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                            padx=10).place(x=8, y=150)
        medical_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                            textvariable=self.var_medical).place(x=170, y=150)

        pf_lbl = Label(F2, text="PF:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                       padx=10).place(x=280, y=150)
        pf_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                       textvariable=self.var_pf).place(x=460, y=150)

        # ==============convence net salary row================

        convence_lbl = Label(F2, text="Convence:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                             padx=10).place(x=8, y=200)
        convence_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                             textvariable=self.var_convence).place(x=170,
                                                                   y=200)

        net_salary_lbl = Label(F2, text="Net Salary:", bg=self.bg_color, fg="black", font="arial 15 bold", anchor="w",
                               padx=10).place(x=280, y=200)
        net_salary_txt = Entry(F2, bg="lightyellow", bd=3, relief=SUNKEN, font="arial 13 bold", width=10,
                               textvariable=self.var_net).place(x=460, y=200)

        calculate_btn = Button(F2, text="Calculate", command=self.calculate, font="arial 15 bold", fg="White",
                               bg="saddle brown", bd=4, relief=SUNKEN).place(x=40, y=250, height=30)
        save_btn = Button(F2, text="Save", font="arial 15 bold", command=self.add, fg="black", bg="yellow", bd=4,
                          relief=SUNKEN).place(x=170, y=250, height=30)
        clear_btn = Button(F2, text="Clear",command=self.clear, font="arial 15 bold", fg="White", bg="green", bd=4, relief=SUNKEN).place(
            x=260, y=250, height=30)

        update_btn = Button(F2, text="Update",command=self.update, font="arial 15 bold", fg="White", bg="green", bd=4, relief=SUNKEN).place(
            x=350, y=250, height=30)
        delete_btn = Button(F2, text="Delete",command=self.delete, font="arial 15 bold", fg="White", bg="green", bd=4, relief=SUNKEN).place(
            x=460, y=250, height=30)

        # ==============Frame3=============================

        F3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        F3.place(x=770, y=380, width=575, height=300)
        # ====Calculator frame=======

        self.var_text = StringVar()
        self.var = " "

        def btn_click(num):
            self.var = self.var + str(num)
            self.var_text.set(self.var)

        cal_frame = Frame(F3, bd=2, relief=GROOVE, bg="white")
        cal_frame.place(x=2, y=2, width=248, height=290)

        def result():
            res = str(eval(self.var))
            self.var_text.set(res)
            self.var = " "

        def clear():
            self.var_text.set("")
            self.var = " "

        cal_lbl = Label(cal_frame, text="CALCULATOR", font="arial 15 bold", bg=bg_color).place(x=0, y=0, relwidth=1,
                                                                                               h=50)

        txt_result = Entry(cal_frame, font="arial 18 bold", bd=2, relief=RIDGE, bg="lightyellow", justify=RIGHT,
                           textvariable=self.var_text).place(x=0, y=45, relwidth=1, height=40)
        # =====ButtonRow1=======
        btn_7 = Button(cal_frame, text="7", font="arial 10 bold", command=lambda: btn_click(7)).place(x=0, y=85, w=60,
                                                                                                      h=50)
        btn_8 = Button(cal_frame, text="8", font="arial 10 bold", command=lambda: btn_click(8)).place(x=62, y=85, w=60,
                                                                                                      h=50)
        btn_9 = Button(cal_frame, text="9", font="arial 10 bold", command=lambda: btn_click(9)).place(x=123, y=85, w=60,
                                                                                                      h=50)
        btn_divide = Button(cal_frame, text="/", font="arial 10 bold", command=lambda: btn_click("/")).place(x=184,
                                                                                                             y=85, w=60,
                                                                                                             h=50)

        # =====ButtonRow2=======
        btn_4 = Button(cal_frame, text="4", font="arial 10 bold", command=lambda: btn_click(4)).place(x=0, y=135, w=60,
                                                                                                      h=50)
        btn_5 = Button(cal_frame, text="5", font="arial 10 bold", command=lambda: btn_click(5)).place(x=62, y=135, w=60,
                                                                                                      h=50)
        btn_6 = Button(cal_frame, text="6", font="arial 10 bold", command=lambda: btn_click(6)).place(x=123, y=135,
                                                                                                      w=60, h=50)
        btn_multiply = Button(cal_frame, text="*", font="arial 10 bold", command=lambda: btn_click("*")).place(x=184,
                                                                                                               y=135,
                                                                                                               w=60,
                                                                                                               h=50)

        # =====ButtonRow3=======
        btn_1 = Button(cal_frame, text="1", font="arial 10 bold", command=lambda: btn_click(1)).place(x=0, y=185, w=60,
                                                                                                      h=50)
        btn_2 = Button(cal_frame, text="2", font="arial 10 bold", command=lambda: btn_click(2)).place(x=62, y=185, w=60,
                                                                                                      h=50)
        btn_3 = Button(cal_frame, text="3", font="arial 10 bold", command=lambda: btn_click(3)).place(x=123, y=185,
                                                                                                      w=60, h=50)
        btn_minus = Button(cal_frame, text="-", font="arial 10 bold", command=lambda: btn_click("-")).place(x=184,
                                                                                                            y=185, w=60,
                                                                                                            h=50)

        # =====ButtonRow4=======
        btn_0 = Button(cal_frame, text="0", font="arial 10 bold", command=lambda: btn_click(0)).place(x=0, y=235, w=60,
                                                                                                      h=50)
        btn_point = Button(cal_frame, text="C", font="arial 10 bold", command=clear).place(x=62, y=235, w=60, h=50)
        btn_plus = Button(cal_frame, text="+", font="arial 10 bold", command=lambda: btn_click("+")).place(x=123, y=235,
                                                                                                           w=60, h=50)
        btn_equal = Button(cal_frame, text="=", font="arial 10 bold", command=result).place(x=184, y=235, w=60, h=50)

        # =====Salary text area=======
        sal_frame = Frame(F3, bd=2, relief=GROOVE, bg="white")
        sal_frame.place(x=250, y=2, width=320, height=290)

        title_sal = Label(sal_frame, text="Salary Receipt", bg=bg_color, fg="black", font="arial 20 bold", anchor="w",
                          padx=10).place(x=0, y=0, relwidth=1)

        inside_sal_frame = Frame(sal_frame, bd=2, relief=GROOVE, bg="white")
        inside_sal_frame.place(x=0, y=38, width=314, height=213)
        sample = f'''\t Tata consultant service\nAddress:Shivaji Square tilak ward warora
---------------------------------------------------------
Employee ID\t\t: -----
Salary\t\t: Dec-2020
Generated On\t\t: 20-12-2020
---------------------------------------------------------
Total Days\t\t: DD
Total Present\t\t: DD
Total Absent\t\t: DD
Convence\t\t: Rs-----
Medical\t\t: Rs.-----
Gross Payment\t\t: Rs------
Net Salary\t\t: Rs--------
---------------------------------------------------------
This is computer generated slip, not
required any signature   
'''

        y_scroll = Scrollbar(inside_sal_frame, orient=VERTICAL)
        y_scroll.pack(fill=Y, side=RIGHT)

        self.text_area = Text(inside_sal_frame, font='Times 11 bold', bg="lightyellow", yscrollcommand=y_scroll.set)
        self.text_area.pack(fill=BOTH, expand=1)
        y_scroll.config(command=self.text_area.yview)
        self.text_area.insert(END, sample)
        print_btn = Button(sal_frame, text="Print",command=self.print, font="arial 15 bold", bg="green").place(x=180, y=255, h=30, w=120)
        self.check_connection()

        ###=====all function start==============


    def search(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary where emp_code=%s", (self.var_Empcode.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid employee Id, please try with another employee ID")
            else:

                self.var_Empcode.set(row[0])
                self.var_designation.set(row[1])
                self.var_doj.set(row[2])
                self.var_name.set(row[3])
                self.var_dob.set(row[4])
                self.var_age.set(row[5])
                self.var_experience.set(row[6])
                self.var_gender.set(row[7])
                self.var_id.set(row[8])
                self.var_email.set(row[9])
                self.var_contact.set(row[10])
                self.var_month.set(row[11])
                self.var_year.set(row[12])
                self.var_salary.set(row[13])
                self.var_days.set(row[14])
                self.var_absent.set(row[15])
                self.var_medical.set(row[16])
                self.var_pf.set(row[17])
                self.var_convence.set(row[18])
                self.var_net.set(row[19])
                file_ = open('receipt_data/' + str(row[20]), 'r')
                self.text_area.delete('1.0', END)
                for i in file_:
                    self.text_area.insert(END, i)
                file_.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def clear(self):

        self.var_Empcode.set(' ')
        self.var_designation.set(' ')
        self.var_doj.set(' ')
        self.var_name.set(' ')
        self.var_dob.set(' ')
        self.var_age.set(' ')
        self.var_experience.set(' ')
        self.var_gender.set(' ')
        self.var_id.set(' ')
        self.var_email.set(' ')
        self.var_contact.set(' ')
        self.var_month.set(' ')
        self.var_year.set(' ')
        self.var_salary.set(' ')
        self.var_days.set(' ')
        self.var_absent.set(' ')
        self.var_medical.set(' ')
        self.var_pf.set(' ')
        self.var_convence.set(' ')
        self.var_net.set(' ')
        self.text_area.delete('1.0',END)









    def delete(self):
        if self.var_Empcode.get()== "":
            messagebox.showerror("Error","Employee Code is compulsory")
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where emp_code=%s", (self.var_Empcode.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid employee Id, please try with another employee ID")
                else:
                    op = messagebox.askyesno("Confirm", "Do u really want to delete the data?")
                    if op == True:
                        cur.execute("delete from emp_salary where emp_code=%s", (self.var_Empcode.get()))
                        con.commit()
                        con.close()

                        messagebox.showinfo("Delete", f"{self.var_Empcode.get()} code data deleted successfully")


            except Exception as ex:
                    messagebox.showerror("Error", f"Error due to: {str(ex)}")




    def update(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary where emp_code=%s", (self.var_Empcode.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Id, please go with the another employee ID")
            else:
                cur.execute(
                    "'emp_salary' SET 'designation'=%s,'doj'=%s,'name'=%s,'dob'=%s,'age'=%s,'experience'=%s,'gender'=%s,'Id_proof'=%s,'email'=%s,'contact'=%s,'months'=%s,'year'=%s,'salary'=%s,'total_days'=%s,'absent_days'=%s,'medical'=%s,'pf'=%s,'convence'=%s,'net_salary'=%s,'salary_receipt'=%s WHERE 'emp_code'=%s",
                    (

                        self.var_designation.get(),
                        self.var_doj.get(),
                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_age.get(),
                        self.var_experience.get(),
                        self.var_gender.get(),
                        self.var_id.get(),
                        self.var_email.get(),
                        self.var_contact.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net.get(),
                        self.var_Empcode.get()+".txt",
                        self.var_Empcode.get()



                    )
                    )
                con.commit()
                con.close()
                file_=open("receipt_data/"+str(self.var_Empcode.get())+".txt",'w')
                file_.write(self.text_area.get('1.0',END))
                file_.close()
                messagebox.showinfo("Record updated successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")



    def add(self):

        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary where emp_code=%s", (self.var_Empcode.get()))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "Employee Id already present please go with the another employee ID")
            else:
                cur.execute(
                    "insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_Empcode.get(),
                        self.var_designation.get(),
                        self.var_doj.get(),
                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_age.get(),
                        self.var_experience.get(),
                        self.var_gender.get(),
                        self.var_id.get(),
                        self.var_email.get(),
                        self.var_contact.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net.get(),
                        self.var_Empcode.get()+".txt",



                    )
                    )
                con.commit()
                con.close()
                file_=open("receipt_data/"+str(self.var_Empcode.get())+".txt",'w')
                file_.write(self.text_area.get('1.0',END))
                file_.close()
                messagebox.showinfo("Record saved successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    def calculate(self):
        if self.var_month.get() == "" or self.var_salary.get() == "" or self.var_year.get() == "" or self.var_days.get() == "" or self.var_absent.get() == "" or self.var_medical.get() == "" or self.var_pf.get() == "" or self.var_convence.get() == "" or self.var_salary.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            per_day = int(self.var_salary.get()) / int(self.var_days.get())
            work_day = int(self.var_days.get()) - int(self.var_absent.get())
            sal = per_day * work_day
            deduct = int(self.var_medical.get()) + int(self.var_pf.get())
            addition = int(self.var_convence.get())
            net_sal = sal - deduct + addition
            self.var_net.set(str(round(net_sal, 2)))
            self.text_area.delete('1.0', END)
            self.text_area.insert(END,"\tTata Consulant Services")
            self.text_area.insert(END, "\nAddress:Shivaji square tilak ward warora")
            self.text_area.insert(END, "\n--------------------------------------------------------")
            self.text_area.insert(END, f"\nEmployee ID\t\t:\t{self.var_Empcode.get()}")
            self.text_area.insert(END, f"\nEmp Name\t\t:\t{self.var_name.get()}")
            self.text_area.insert(END, f"\nSalary Of\t\t:\t{self.var_month.get()}-{self.var_year.get()}")
            self.text_area.insert(END, f"\nGenerated On\t\t:\t{str(time.strftime('%d-%m-%y'))}")
            self.text_area.insert(END, "\n--------------------------------------------------------")
            self.text_area.insert(END, f"\nTotal Days\t\t:\t{self.var_days.get()}")
            self.text_area.insert(END, f"\nTotal Present\t\t:\t{self.var_days.get()}-{self.var_absent.get()}")
            self.text_area.insert(END, f"\nTotal Absent\t\t:\t{self.var_absent.get()}")
            self.text_area.insert(END, f"\nConvence\t\t:\t{self.var_convence.get()}")
            self.text_area.insert(END, f"\nMedical\t\t:\t{self.var_medical.get()}")
            self.text_area.insert(END, f"\nPF\t\t:\t{self.var_pf.get()}")
            self.text_area.insert(END, f"\nGross Salary\t\t:\t{self.var_salary.get()}")
            self.text_area.insert(END, f"\nNet Salary\t\t:\t{self.var_net.get()}")
            self.text_area.insert(END, "\n--------------------------------------------------------")
            self.text_area.insert(END, "\nThis is computer generated slip, not required any signature")



    def check_connection(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def show(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            rows = cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")


    def emp_structure(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Details")
        self.root2.geometry("1000x500+120+100")
        bg_color = "LightGray"

        title = Label(self.root2, text="Employee Details", bg=bg_color, fg="black",
                      font="arial 30 bold", anchor="w", padx=10)
        title.place(x=0, y=0, relwidth=1)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2, orient=VERTICAL)
        scrollx=Scrollbar(self.root2, orient=HORIZONTAL)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)




        #=====tree view=====
        self.employee_tree = ttk.Treeview(self.root2,columns=('emp_code', 'designation', 'doj', 'name', 'dob', 'age', 'experience', 'gender', 'Id_proof', 'email', 'contact', 'months', 'year', 'salary', 'total_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.employee_tree.heading('emp_code',text='EID')
        self.employee_tree.heading('designation', text='Designation')
        self.employee_tree.heading('doj', text='DOJ')
        self.employee_tree.heading('name', text='Name')
        self.employee_tree.heading('dob', text='DOB')
        self.employee_tree.heading('age', text='Age')
        self.employee_tree.heading('experience', text='Experience')
        self.employee_tree.heading('gender', text='Gender')
        self.employee_tree.heading('Id_proof', text='Id-Proof')
        self.employee_tree.heading('email', text='Email')
        self.employee_tree.heading('contact', text='Contact')
        self.employee_tree.heading('months', text='Months')
        self.employee_tree.heading('year', text='Year')
        self.employee_tree.heading('salary', text='Salary')
        self.employee_tree.heading('total_days', text='Total-days')
        self.employee_tree.heading('absent_days', text='Absent-days')
        self.employee_tree.heading('medical', text='Medical')
        self.employee_tree.heading('pf', text='PF')
        self.employee_tree.heading('convence', text='Convence')
        self.employee_tree.heading('net_salary', text='Net-Salary')
        self.employee_tree.heading('salary_receipt', text='Salary-receipt')
        self.employee_tree['show'] = 'headings'

        self.employee_tree.column('emp_code', width=100)
        self.employee_tree.column('designation', width=200)
        self.employee_tree.column('doj', width=100)
        self.employee_tree.column('name', width=200)
        self.employee_tree.column('dob', width=100)
        self.employee_tree.column('age', width=100)
        self.employee_tree.column('experience', width=100)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('Id_proof', width=100)
        self.employee_tree.column('email', width=250)
        self.employee_tree.column('contact', width=100)
        self.employee_tree.column('months', width=100)
        self.employee_tree.column('year', width=100)
        self.employee_tree.column('salary', width=100)
        self.employee_tree.column('total_days', width=100)
        self.employee_tree.column('absent_days', width=100)
        self.employee_tree.column('medical', width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence', width=100)
        self.employee_tree.column('net_salary', width=100)
        self.employee_tree.column('salary_receipt', width=100)
        self.employee_tree.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.employee_tree.yview)

        scrollx.config(command=self.employee_tree.xview)
        self.show()

        self.root2.mainloop()

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.text_area.get('1.0',END))
        os.startfile(file_,'print')



root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
