import sqlite3
import datetime
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import DateEntry

# Initialize the database connection
connector = sqlite3.connect("school_management.db")
cursor = connector.cursor()

# Create tables if they do not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (
                    STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT NOT NULL,
                    EMAIL TEXT NOT NULL,
                    PHONE_NO TEXT NOT NULL,
                    GENDER TEXT NOT NULL,
                    DOB TEXT NOT NULL,
                    STREAM TEXT NOT NULL
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS TEACHER_MANAGEMENT (
                    TEACHER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT NOT NULL,
                    EMAIL TEXT NOT NULL,
                    PHONE_NO TEXT NOT NULL,
                    GENDER TEXT NOT NULL,
                    DOB TEXT NOT NULL,
                    SUBJECT TEXT NOT NULL
                  )''')


class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the window
        window_width = 800
        window_height = 600
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Set the geometry of the window
        self.root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

        self.create_login_ui()

    def create_login_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.login_frame = Frame(self.root, bg='lightgreen')
        self.login_frame.place(relwidth=1, relheight=1)

        Label(self.login_frame, text="School Management System", font=("Arial", 25), bg='lightgreen').pack(pady=20)

        Label(self.login_frame, text="Username:", font=("Arial", 14), bg='lightgreen').pack(pady=5)
        self.username_entry = Entry(self.login_frame, font=("Arial", 14))
        self.username_entry.pack(pady=5)

        Label(self.login_frame, text="Password:", font=("Arial", 14), bg='lightgreen').pack(pady=5)
        self.password_entry = Entry(self.login_frame, show='*', font=("Arial", 14))
        self.password_entry.pack(pady=5)

        Button(self.login_frame, text="Login", font=("Arial", 14), command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Add your login validation logic here
        if username == "admin" and password == "tech":  # Example validation
            self.create_main_ui()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def create_main_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        menu_frame = Frame(self.root, bg='lightgreen')
        menu_frame.pack(fill=BOTH, expand=True)

        Button(menu_frame, text="Student Management", font=("Arial", 15),
               command=self.create_student_management_ui).pack(pady=10)
        Button(menu_frame, text="Teacher Management", font=("Arial", 15),
               command=self.create_teacher_management_ui).pack(pady=10)
        Button(menu_frame, text="Take Attendance", font=("Arial", 15),
               command=self.create_Take_attendance_ui).pack(pady=10)
        Button(menu_frame, text="Logout", font=("Arial", 14), command=self.create_login_ui).pack(pady=10)


    def create_student_management_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        student_frame = Frame(self.root, bg='LightBlue')
        student_frame.pack(fill=BOTH, expand=True)

        Label(student_frame, text="STUDENT MANAGEMENT SYSTEM", font=("Arial", 25), bg='lightgreen').pack(side=TOP,
                                                                                                        fill=X)

        student_left_frame = Frame(student_frame, bg='lightgreen')
        student_left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

        student_right_frame = Frame(student_frame, bg='White')
        student_right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(student_left_frame, text="Name", font=("Arial", 13)).grid(row=0, column=0, padx=10, pady=5, sticky=E)
        Label(student_left_frame, text="Email", font=("Arial", 13)).grid(row=1, column=0, padx=10, pady=5, sticky=E)
        Label(student_left_frame, text="Contact", font=("Arial", 13)).grid(row=2, column=0, padx=10, pady=5, sticky=E)
        Label(student_left_frame, text="Gender", font=("Arial", 13)).grid(row=3, column=0, padx=10, pady=5, sticky=E)
        Label(student_left_frame, text="DOB", font=("Arial", 13)).grid(row=4, column=0, padx=10, pady=5, sticky=E)
        Label(student_left_frame, text="Stream", font=("Arial", 13)).grid(row=5, column=0, padx=10, pady=5, sticky=E)

        self.name_strvar = StringVar()
        self.email_strvar = StringVar()
        self.contact_strvar = StringVar()
        self.gender_strvar = StringVar()
        self.stream_strvar = StringVar()

        Entry(student_left_frame, textvariable=self.name_strvar).grid(row=0, column=1, padx=14, pady=5)
        Entry(student_left_frame, textvariable=self.email_strvar).grid(row=1, column=1, padx=14, pady=5)
        Entry(student_left_frame, textvariable=self.contact_strvar).grid(row=2, column=1, padx=14, pady=5)
        Entry(student_left_frame, textvariable=self.gender_strvar).grid(row=3, column=1, padx=14, pady=5)
        self.dob = DateEntry(student_left_frame)
        self.dob.grid(row=4, column=1, padx=12, pady=5)
        Entry(student_left_frame, textvariable=self.stream_strvar).grid(row=5, column=1, padx=14, pady=5)

        Button(student_left_frame, text="Submit and Add Record", bg='SpringGreen', command=self.add_student_record).grid(row=6, column=0,
                                                                                                       columnspan=2,
                                                                                                       pady=15)
        Button(student_left_frame, text="View Record", command=self.view_student_record).grid(row=7, column=0,
                                                                                              columnspan=2, pady=15)
        Button(student_left_frame, text="Delete Record", command=self.remove_student_record).grid(row=8, column=0,
                                                                                                  columnspan=2, pady=15)
        Button(student_left_frame, text="Reset Form", command=self.reset_student_form).grid(row=9, column=0,
                                                                                            columnspan=2, pady=15)
        Button(student_left_frame, text="Display Records", command=self.display_student_records).grid(row=10, column=0,
                                                                                                      columnspan=2,
                                                                                                      pady=15)
        Button(student_left_frame, text="Logout", command=self.create_login_ui).grid(row=11, column=0, columnspan=2,
                                                                                     pady=17)

        self.student_tree = ttk.Treeview(student_right_frame, columns=(
            'Student ID', "Name", "Email", "Phone No", "Gender", "DOB", "Stream"),
                                         show='headings')
        self.student_tree.pack(fill=BOTH, expand=True)
        self.student_tree.heading('Student ID', text='Student ID')
        self.student_tree.heading('Name', text='Name')
        self.student_tree.heading('Email', text='Email')
        self.student_tree.heading('Phone No', text='Phone No')
        self.student_tree.heading('Gender', text='Gender')
        self.student_tree.heading('DOB', text='DOB')
        self.student_tree.heading('Stream', text='Stream')

    def create_teacher_management_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        teacher_frame = Frame(self.root, bg='LightBlue')
        teacher_frame.pack(fill=BOTH, expand=True)

        Label(teacher_frame, text="TEACHER MANAGEMENT SYSTEM", font=("Arial", 24), bg='LightBlue').pack(side=TOP,
                                                                                                        fill=X)

        teacher_left_frame = Frame(teacher_frame, bg='LightBlue')
        teacher_left_frame.pack(side=LEFT, fill=Y, padx=20, pady=10)

        teacher_right_frame = Frame(teacher_frame, bg='White')
        teacher_right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=200, pady=10)

        Label(teacher_left_frame, text="Name", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=E)
        Label(teacher_left_frame, text="Email", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=E)
        Label(teacher_left_frame, text="Contact", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=E)
        Label(teacher_left_frame, text="Gender", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=E)
        Label(teacher_left_frame, text="DOB", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky=E)
        Label(teacher_left_frame, text="Subject", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky=E)

        self.teacher_name_strvar = StringVar()
        self.teacher_email_strvar = StringVar()
        self.teacher_contact_strvar = StringVar()
        self.teacher_gender_strvar = StringVar()
        self.teacher_subject_strvar = StringVar()

        Entry(teacher_left_frame, textvariable=self.teacher_name_strvar).grid(row=0, column=1, padx=10, pady=5)
        Entry(teacher_left_frame, textvariable=self.teacher_email_strvar).grid(row=1, column=1, padx=10, pady=5)
        Entry(teacher_left_frame, textvariable=self.teacher_contact_strvar).grid(row=2, column=1, padx=10, pady=5)
        Entry(teacher_left_frame, textvariable=self.teacher_gender_strvar).grid(row=3, column=1, padx=10, pady=5)
        self.teacher_dob = DateEntry(teacher_left_frame)
        self.teacher_dob.grid(row=4, column=1, padx=10, pady=5)
        Entry(teacher_left_frame, textvariable=self.teacher_subject_strvar).grid(row=5, column=1, padx=10, pady=5)

        Button(teacher_left_frame, text="Submit and Add Record", command=self.add_teacher_record).grid(row=6, column=0,
                                                                                                       columnspan=2,
                                                                                                       pady=10)
        Button(teacher_left_frame, text="View Record", command=self.view_teacher_record).grid(row=7, column=0,
                                                                                              columnspan=2, pady=10)
        Button(teacher_left_frame, text="Delete Record", command=self.remove_teacher_record).grid(row=8, column=0,
                                                                                                  columnspan=2, pady=10)
        Button(teacher_left_frame, text="Reset Form", command=self.reset_teacher_form).grid(row=9, column=0,
                                                                                            columnspan=2, pady=10)
        Button(teacher_left_frame, text="Display Records", command=self.display_teacher_records).grid(row=10, column=0,
                                                                                                      columnspan=2,
                                                                                                      pady=10)
        Button(teacher_left_frame, text="Logout", command=self.create_login_ui).grid(row=11, column=0, columnspan=2,
                                                                                     pady=10)

        self.teacher_tree = ttk.Treeview(teacher_right_frame, columns=(
            'Teacher ID', "Name", "Email", "Phone No", "Gender", "DOB", "Subject"),
                                         show='headings')
        self.teacher_tree.pack(fill=BOTH, expand=True)
        self.teacher_tree.heading('Teacher ID', text='Teacher ID')
        self.teacher_tree.heading('Name', text='Name')
        self.teacher_tree.heading('Email', text='Email')
        self.teacher_tree.heading('Phone No', text='Phone No')
        self.teacher_tree.heading('Gender', text='Gender')
        self.teacher_tree.heading('DOB', text='DOB')
        self.teacher_tree.heading('Subject', text='Subject')

    def create_Take_attendance_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        attendance_frame = Frame(self.root, bg='lightblue')
        attendance_frame.pack(fill=BOTH, expand=True)

        Label(attendance_frame, text="ATTENDANCE MANAGEMENT", font=("Arial", 25), bg='springgreen').pack(side=TOP, fill=X)

        attendance_left_frame = Frame(attendance_frame, bg='springgreen')
        attendance_left_frame.pack(side=LEFT, fill=Y, padx=11, pady=11)

        attendance_right_frame = Frame(attendance_frame, bg='lightblue')
        attendance_right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(attendance_left_frame, text="Student ID", font=("Arial", 13)).pack(pady=5)
        Label(attendance_left_frame, text="Date", font=("Arial", 13)).pack(pady=5)
        Label(attendance_left_frame, text="Status", font=("Arial", 13)).pack(pady=5)

        self.attendance_id_strvar = StringVar()
        self.attendance_date_strvar = StringVar()
        self.attendance_status_strvar = StringVar()

        Entry(attendance_left_frame, textvariable=self.attendance_id_strvar).pack(pady=5)
        self.attendance_date_entry = DateEntry(attendance_left_frame)
        self.attendance_date_entry.pack(pady=5)
        Entry(attendance_left_frame, textvariable=self.attendance_status_strvar).pack(pady=5)

        Button(attendance_left_frame, text="Submit and Add Record", bg='SpringGreen', command=self.add_attendance_record).pack(pady=5)
        Button(attendance_left_frame, text="View Record", command=self.view_attendance_record).pack(pady=10)
        Button(attendance_left_frame, text="Remove Record", command=self.remove_attendance_record).pack(pady=10)
        Button(attendance_left_frame, text="Reset Form", command=self.reset_attendance_form).pack(pady=10)
        Button(attendance_left_frame, text="Display Records", command=self.display_attendance_records).pack(pady=10)
        Button(attendance_left_frame, text="Logout", command=self.create_login_ui).pack(pady=5)

        self.attendance_tree = ttk.Treeview(attendance_right_frame,
                                            columns=('Attendance ID', 'Student ID', 'Date', 'Status'),
                                            show='headings')
        self.attendance_tree.pack(fill=BOTH, expand=True)
        self.attendance_tree.heading('Attendance ID', text='Attendance ID')
        self.attendance_tree.heading('Student ID', text='Student ID')
        self.attendance_tree.heading('Date', text='Date')
        self.attendance_tree.heading('Status', text='Status')
    def reset_student_form(self):
        self.name_strvar.set('')
        self.email_strvar.set('')
        self.contact_strvar.set('')
        self.gender_strvar.set('')
        self.dob.set_date(datetime.datetime.now().date())
        self.stream_strvar.set('')

    def reset_teacher_form(self):
        self.teacher_name_strvar.set('')
        self.teacher_email_strvar.set('')
        self.teacher_contact_strvar.set('')
        self.teacher_gender_strvar.set('')
        self.teacher_dob.set_date(datetime.datetime.now().date())
        self.teacher_subject_strvar.set('')

    def add_student_record(self):
        name = self.name_strvar.get()
        email = self.email_strvar.get()
        contact = self.contact_strvar.get()
        gender = self.gender_strvar.get()
        dob = self.dob.get_date()
        stream = self.stream_strvar.get()

        if not name or not email or not contact or not gender or not dob or not stream:
            messagebox.showerror("Error", "All fields are required.")
            return

        cursor.execute(
            "INSERT INTO SCHOOL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?, ?, ?, ?, ?, ?)",
            (name, email, contact, gender, dob, stream))
        connector.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        self.reset_student_form()

    def add_teacher_record(self):
        name = self.teacher_name_strvar.get()
        email = self.teacher_email_strvar.get()
        contact = self.teacher_contact_strvar.get()
        gender = self.teacher_gender_strvar.get()
        dob = self.teacher_dob.get_date()
        subject = self.teacher_subject_strvar.get()

        if not name or not email or not contact or not gender or not dob or not subject:
            messagebox.showerror("Error", "All fields are required.")
            return

        cursor.execute(
            "INSERT INTO TEACHER_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, SUBJECT) VALUES (?, ?, ?, ?, ?, ?)",
            (name, email, contact, gender, dob, subject))
        connector.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        self.reset_teacher_form()

    def view_student_record(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to view.")
            return

        student_id = self.student_tree.item(selected_item)['values'][0]
        cursor.execute("SELECT * FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=?", (student_id,))
        student_record = cursor.fetchone()

        if student_record:
            messagebox.showinfo("Student Record",
                                f"ID: {student_record[0]}\nName: {student_record[1]}\nEmail: {student_record[2]}\nPhone: {student_record[3]}\nGender: {student_record[4]}\nDOB: {student_record[5]}\nStream: {student_record[6]}")
        else:
            messagebox.showerror("Error", "No record found.")

    def view_teacher_record(self):
        selected_item = self.teacher_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to view.")
            return

        teacher_id = self.teacher_tree.item(selected_item)['values'][0]
        cursor.execute("SELECT * FROM TEACHER_MANAGEMENT WHERE TEACHER_ID=?", (teacher_id,))
        teacher_record = cursor.fetchone()

        if teacher_record:
            messagebox.showinfo("Teacher Record",
                                f"ID: {teacher_record[0]}\nName: {teacher_record[1]}\nEmail: {teacher_record[2]}\nPhone: {teacher_record[3]}\nGender: {teacher_record[4]}\nDOB: {teacher_record[5]}\nSubject: {teacher_record[6]}")
        else:
            messagebox.showerror("Error", "No record found.")

    def remove_student_record(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        student_id = self.student_tree.item(selected_item)['values'][0]
        cursor.execute("DELETE FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=?", (student_id,))
        connector.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        self.display_student_records()

    def remove_teacher_record(self):
        selected_item = self.teacher_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        teacher_id = self.teacher_tree.item(selected_item)['values'][0]
        cursor.execute("DELETE FROM TEACHER_MANAGEMENT WHERE TEACHER_ID=?", (teacher_id,))
        connector.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        self.display_teacher_records()

    def display_student_records(self):
        self.student_tree.delete(*self.student_tree.get_children())
        cursor.execute("SELECT * FROM SCHOOL_MANAGEMENT")
        records = cursor.fetchall()
        for record in records:
            self.student_tree.insert('', END, values=record)

    def display_teacher_records(self):
        self.teacher_tree.delete(*self.teacher_tree.get_children())
        cursor.execute("SELECT * FROM TEACHER_MANAGEMENT")
        records = cursor.fetchall()
        for record in records:
            self.teacher_tree.insert('', END, values=record)

    def add_attendance_record(self):
        student_id = self.attendance_id_strvar.get()
        date = self.attendance_date_entry.get_date()
        status = self.attendance_status_strvar.get()

        cursor.execute('''INSERT INTO ATTENDANCE (STUDENT_ID, DATE, STATUS) 
                          VALUES (?, ?, ?)''',
                       (student_id, date, status))
        connector.commit()
        messagebox.showinfo("Success", "Attendance record added successfully!")
        self.reset_attendance_form()

    def view_attendance_record(self):
        attendance_id = simpledialog.askinteger("Input", "Enter Attendance ID:")
        if attendance_id:
            cursor.execute('''SELECT * FROM ATTENDANCE WHERE ATTENDANCE_ID = ?''', (attendance_id,))
            record = cursor.fetchone()
            if record:
                self.attendance_id_strvar.set(record[1])
                self.attendance_date_entry.set_date(record[2])
                self.attendance_status_strvar.set(record[3])
            else:
                messagebox.showerror("Error", "Record not found.")

    def remove_attendance_record(self):
        attendance_id = simpledialog.askinteger("Input", "Enter Attendance ID to remove:")
        if attendance_id:
            cursor.execute('''DELETE FROM ATTENDANCE WHERE ATTENDANCE_ID = ?''', (attendance_id,))
            connector.commit()
            messagebox.showinfo("Success", "Attendance record removed successfully!")
            self.display_attendance_records()

    def reset_attendance_form(self):
        self.attendance_id_strvar.set('')
        self.attendance_date_entry.set_date(datetime.date.today())
        self.attendance_status_strvar.set('')

    def display_attendance_records(self):
        for row in self.attendance_tree.get_children():
            self.attendance_tree.delete(row)
        cursor.execute('''SELECT * FROM ATTENDANCE''')
        rows = cursor.fetchall()
        for row in rows:
            self.attendance_tree.insert('', 'end', values=row)


root = Tk()
app = SchoolManagementSystem(root)
root.mainloop()