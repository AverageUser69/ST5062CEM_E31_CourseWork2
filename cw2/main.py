from enum import verify
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector
import re
import hashlib
import random
import smtplib
from email.mime.text import MIMEText
import string
from mysql.connector import Error
from tkinter import Tk, ttk, scrolledtext, messagebox
from tkinter import Canvas
from tkinter import Scrollbar
from tkinter import Toplevel


from tkinter import ttk
import mysql.connector

# global current_user_id
# --------------------------------------- Getting Input (sign_up_frame) --------------------------------------- #
"""
    This code accesses the values of several 'Entry' widgets in a GUI from (sign_up_frame).
"""
code = str(random.randint(100000, 999999))

def submit_sign_up():
    # # Access the values of the Entry widgets
    # first_name = first_name_entry.get()
    # last_name = last_name_entry.get()
    # phone_number = phone_number_entry.get()
    # email = email_entry.get()
    # password = password_entry.get()
    # confirm_password= confirm_password_entry.get()

# --------------------------------------- testing inputs (sign_up_frame) --------------------------------------- #
    first_name = "hello"
    last_name = "hello"
    phone_number = "1234556789"
    email = "subodh@gmail.com"
    password = "asdfghjkl!2"
    confirm_password= "asdfghjkl!2"
    
# --------------------------------------- Checking Email Pattern (sign_up_frame) --------------------------------------- #
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_pattern.match(email):
        messagebox.showerror("Error", "Invalid Email")
        return
    
# --------------------------------------- Checking First Name Length (sign_up_frame) --------------------------------------- #
    if len(first_name) > 12 or len(first_name) < 3:
        messagebox.showerror("Error", "First Name must be at least 3 characters and no longer than 12 characters")
        return

# --------------------------------------- Checking Last Name Length (sign_up_frame) --------------------------------------- #
    if len(last_name) > 12 or len(last_name) < 3:
        messagebox.showerror("Error", "Last Name must be at least 3 characters and no longer than 12 characters")
        return

# --------------------------------------- Checking Phone Number (sign_up_frame) --------------------------------------- #
    if not phone_number.isdigit() or len(phone_number) != 10:
        messagebox.showerror("Error", "Phone Number must only contain numbers and be 10 digits long")
        return
    if password != confirm_password:
        messagebox.showerror("Error", "Password and Confirm Password do not match")
        return
    
# --------------------------------------- Checking strength of Password (sign_up_frame) --------------------------------------- #
    password_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,24}$')
    if not password_pattern.match(password):
        messagebox.showerror("Error", "Password must be \n # at least 8 characters \n # no longer than 24 characters \n # at lest one number \n # one special character")
        return
    
# --------------------------------------- Hashing Password (sign_up_frame) --------------------------------------- #

    # password = hashlib.sha256(b'{password}').hexdigest()
    
    password =password.encode()
    password = hashlib.sha256(password).hexdigest()
    
    
      
# --------------------------------------- Connecting To Database (sign_up_frame) --------------------------------------- #
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="securefile"
    )

# --------------------------------------- Chicking Availability Of Email and Phone Number (sign_up_frame) --------------------------------------- #
    cursor = mydb.cursor()
    check_user_query = "SELECT * FROM userdata WHERE email_address =%s OR phone_number=%s"
    cursor.execute(check_user_query, (email, phone_number))
    result = cursor.fetchone()
    if result:
        messagebox.showerror("Error", "Email or Phone number already in use")
    else:
        verify_email()

    
    ##############################################################################################################
    ##############################################################################################################
        print("printed after verify email")
        print(code)
        
    ##
        # Email details
        to = email
        subject = "Complete Your Email Verification"
        body = f"""Dear Valued Customer,

        We hope this message finds you well. Please take a moment to complete your email verification process by entering the following code: {code}.

        Your email verification ensures that you can receive important updates and information from our services.

        Thank you for your time and cooperation. If you have any questions or concerns, please do not hesitate to reach out to us.

        Best Regards,
        The Secure File Transfer Protocol Team"""

        # Create message object
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        message['From'] = "securefiletransferprotocle@proton.me"

        # Send email
        server = smtplib.SMTP("smtp.sendgrid.net", 587)
        server.ehlo()
        server.starttls()
        server.login("apikey", "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")
        server.sendmail("securefiletransferprotocle@proton.me", [to], message.as_string())
        server.quit()
        print("##############################################################################################")
        print(code)
        print(first_name)
        print(last_name)
        print(phone_number)
        print(email)
        print(password)
        print(confirm_password)
    return first_name,last_name,phone_number,email,password,confirm_password
    
# --------------------------------------- Inserting Data inside Database (sign_up_frame) --------------------------------------- #
def verify_code_function(sign_up_values):
    first_name, last_name, phone_number, email, password, confirm_password = sign_up_values
    
    print("======================================================================================")
    print(code)
    print(first_name)
    print(last_name)
    print(phone_number)
    print(email)
    print(password)
    print(confirm_password)
    
    verify_code = verify_code_entry.get()
    if verify_code == "":
        print(code)
        messagebox.showerror("Error","Verification code cannot be empty.")
        return
    if verify_code != code:
        print(code)
        messagebox.showerror("Error","Invalid Verification code.")
        return
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="securefile"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO userdata (first_name, last_name, email_address, phone_number, password) VALUES (%s, %s, %s, %s, %s)"
        val = (first_name, last_name, email, phone_number, password)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        if messagebox.showinfo("Success", "Email Verified!\n Account Created Successfully.") == "ok":
            log_in_after_verification()
            print("==========changed==========")
            first_name_entry.delete(0, "end")
            last_name_entry.delete(0, "end")
            phone_number_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")
            confirm_password_entry.delete(0, "end")
    except Error as e:
        print("Error while connecting to MySQL", e)
        messagebox.showerror("Error", "Failed to create account. Please try again later.")



            # first_name_entry.delete(0, "end")
            # last_name_entry.delete(0, "end")
            # phone_number_entry.delete(0, "end")
            # email_entry.delete(0, "end")
            # password_entry.delete(0, "end")
            # confirm_password_entry.delete(0, "end")
            # verify_email()

# --------------------------------------- Testing Input In (sign_up_frame) --------------------------------------- #
    print("First Name:",first_name)
    print("Last Name:", last_name)
    print("Phone Number:",phone_number)
    print("Email:", email)
    print("Password:", password)
    print("Confirm Password:",confirm_password)
    


# --------------------------------------- Switching to (sign_up_frame) --------------------------------------- #
""" 
        This code defines a function show_sign_up that switches the displayed frame 
    from main_frame to sign_up_frame.
    """

def show_sign_up():
    main_frame.grid_forget()
    sign_up_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

# --------------------------------------- Switching to (log_in_frame) --------------------------------------- #
"""
        This code defines a function show_log_in that switches the displayed frame 
    from main_frame to log_in_frame.
    """
    
def show_log_in():
    main_frame.grid_forget()
    log_in_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
        
        
        
def verify_email():
    sign_up_frame.grid_forget()
    verify_email_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
        
# --------------------------------------- Switching Back to (main_frame) --------------------------------------- #
"""
        This code defines a function back_to_main that switches the displayed frame 
    from either the sign_up_frame or the log_in_frame back to the main_frame.
    """
    
def back_to_main():
    sign_up_frame.grid_forget()
    log_in_frame.grid_forget()
    main_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
              

def display_user_data(user_id):
    # Connect to the database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="securefile"
    )
    cursor = mydb.cursor()

    # Retrieve the user data
    query = "SELECT first_name, last_name, email_address, phone_number FROM userdata WHERE id=%s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    if result:
        first_name, last_name, email, phone_number = result

        # Create a new window to display the user data
        display_window = Toplevel(root)
        display_window.title("User Data")

        first_name_label = ttk.Label(display_window, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=10, pady=10)
        first_name_value = ttk.Label(display_window, text=str(first_name))
        first_name_value.grid(row=0, column=1, padx=10, pady=10)

        last_name_label = ttk.Label(display_window, text="Last Name:")
        last_name_label.grid(row=1, column=0, padx=10, pady=10)
        last_name_value = ttk.Label(display_window, text=str(last_name))
        last_name_value.grid(row=1, column=1, padx=10, pady=10)

        email_label = ttk.Label(display_window, text="Email:")
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_value = ttk.Label(display_window, text=str(email))
        email_value.grid(row=2, column=1, padx=10, pady=10)

        phone_number_label = ttk.Label(display_window, text="Phone Number:")
        phone_number_label.grid(row=3, column=0, padx=10, pady=10)
        phone_number_value = ttk.Label(display_window, text=str(phone_number))
        phone_number_value.grid(row=3, column=1, padx=10, pady=10)
    else:
        messagebox.showerror("Error", "User not found")



        
        
        
        
        
 
        
        
def log_in_after_verification():
    verify_email_frame.grid_forget()
    log_in_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
        
# --------------------------------------- Creating The Main Window --------------------------------------- #
"""
        This code creates the main window of a Tkinter GUI application and sets its 
    dimensions and location on the screen.
    """
    
root = tk.Tk()
root.geometry("600x600")
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 4.5
root.geometry("+%d+%d" % (x, y))

# --------------------------------------- Creating (main_frame) --------------------------------------- #
"""
        This code creates a Tkinter Frame widget and assigns it to the variable main_frame. 
    """
    
main_frame = tk.Frame(root, bg="#006466")

# --------------------------------------- Setting Layoput in (main_frame) --------------------------------------- #
"""
        This code sets the layout of the main_frame using the grid geometry manager.
    """
    
main_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
for i in range(12):
    root.rowconfigure(i, minsize=50)
for i in range(12):
    root.columnconfigure(i, minsize=50)
    
# --------------------------------------- Topic Text (main_frame) --------------------------------------- #
"""
       This code creates a Label widget with the text "Secure File Transfer Protocol" 
    in the main_frame. 
    """
    
project_text = ttk.Label(main_frame, text="Secure File Transfer Protocol", 
                         font=("Travelast", 30), foreground="white", background="#006466")
project_text.grid(row=0, column=2, columnspan=1, pady=20, padx=50)

# --------------------------------------- By Text (main_frame) --------------------------------------- #
"""
       This code creates a Label widget with the text "By" 
    in the main_frame. 
    """
    
by_text = ttk.Label(main_frame, text="by", font=("Hanging Letters", 25), foreground="white", 
                    background="#006466")
by_text.grid(row=1, column=2, columnspan=1, pady=10, padx=10)

# --------------------------------------- Name Text (main_frame) --------------------------------------- #
"""
       This code creates a Label widget with the text "Subodh Ghimire" 
    in the main_frame. 
    """
    
name_text = ttk.Label(main_frame, text="Subodh Ghimire", font=("3x5", 35), foreground="white", 
                      background="#006466")
name_text.grid(row=2, column=2, columnspan=1, pady=(10,80), padx=10 ,sticky='n')

# --------------------------------------- Sign Up Button (main_frame) --------------------------------------- #
"""
        This code creates a button widget with the text "Sign Up" and adds it to the main_frame.
    """
    
back_button = tk.Button(main_frame, text="Sign Up", command=show_sign_up, font=("Helvetica", 13), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="#1985a1")
back_button.grid(row=4, column=2,sticky="s", padx=250, pady=10)
back_button.config(width=8)

# --------------------------------------- Log In Button (main_frame) --------------------------------------- #
"""
        This code creates a button widget with the text "Log In" and adds it to the main_frame.
    """
    
back_button = tk.Button(main_frame, text="Log In", command=show_log_in, font=("Helvetica", 13), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="#c5c3c6")
back_button.grid(row=5, column=2,sticky="s", padx=250, pady=10)
back_button.config(width=8)

# --------------------------------------- Exit Button (main_frame) --------------------------------------- #
"""
        This code creates a button widget with the text "Exit" and adds it to the main_frame.
    """
    
back_button = tk.Button(main_frame, text="Exit", command=root.quit, font=("Helvetica", 13), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="red")
back_button.grid(row=6, column=2, sticky="s", padx=250, pady=10)
back_button.config(width=8)

# --------------------------------------- Footer Lable (main_frame) --------------------------------------- #
"""
       This code creates a Label widget with the text "Subodh Ghimire" 
    in the main_frame but at buttom. 
    """

work_text = ttk.Label(main_frame, text="Send file online using the Secure File Transfer Protocol.", 
                      font=("Helvetica",10), foreground="white", background="#006466")
work_text.grid(row=8, column=2, columnspan=1, pady=(80,5), padx=50)

# --------------------------------------- Styling Entry Widget --------------------------------------- #
"""
        This code defines a style named "Round" for a Tkinter ttk entry widget.
    """
    
style = ttk.Style()
style.configure("Round.TEntry", fieldbackground="#ffffff", background="transparent", 
                 bd=5, relief="flat", padding=2, borderwidth=2,
                 highlightcolor="#597678", highlightbackground="#597678", 
                 borderradius=10)

# --------------------------------------- Creating (sign_up_frame) --------------------------------------- #
"""
        This code creates a Tkinter frame widget, with a background color of "#006466".
    """
    
sign_up_frame = tk.Frame(root, bg="#006466")

# --------------------------------------- sign_up Text (sign_up_frame) --------------------------------------- #
"""
               This code creates a Label widget with the text "Sign Up" 
    in the sign_up_frame. 
    """

sign_up_text = ttk.Label(sign_up_frame, text="Sign Up", font=("Travelast", 25), foreground="white", 
                         background="#006466")
sign_up_text.grid(row=0, column=2, columnspan=1, pady=30, padx=50, sticky="nw")

# --------------------------------------- First Name (sign_up_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "First Name:" and an Entry widget, 
    both inside the 'sign_up_frame'. 
    """
    
first_name_label = tk.Label(sign_up_frame, text="First Name:", font=("Helvetica", 14), 
                            foreground="white", background="#006466")
first_name_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), 
                             foreground="#006466", style="Round.TEntry", background='gray')
first_name_entry.configure(background='gray')

first_name_label.grid(row=1, column=1, padx=20, pady=10, sticky="W")
first_name_entry.grid(row=1, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Last Name (sign_up_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Last Name:" and an Entry widget, 
    both inside the 'sign_up_frame'. 
    """
    
last_name_label = tk.Label(sign_up_frame, text="Last Name:", font=("Helvetica", 14), 
                           foreground="white", background="#006466")
last_name_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), 
                            foreground="#006466", style="Round.TEntry")

last_name_label.grid(row=2, column=1, padx=20, pady=10, sticky="W")
last_name_entry.grid(row=2, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Phone Number (sign_up_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Phone Number:" and an Entry widget, 
    both inside the 'sign_up_frame'. 
    """
    
phone_number_label = tk.Label(sign_up_frame, text="Phone Number:", font=("Helvetica", 14), 
                              foreground="white", background="#006466")
phone_number_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), 
                               foreground="#006466",style="Round.TEntry")

phone_number_label.grid(row=3, column=1, padx=20, pady=10, sticky="W")
phone_number_entry.grid(row=3, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Email (sign_up_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Email:" and an Entry widget, 
    both inside the 'sign_up_frame'. 
    """
    
email_label = tk.Label(sign_up_frame, text="Email:", font=("Helvetica", 14), 
                       foreground="white", background="#006466")
email_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), 
                        foreground="#006466", style="Round.TEntry")

email_label.grid(row=4, column=1, padx=20, pady=10, sticky="W")
email_entry.grid(row=4, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Password (sign_up_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Password:" and an Entry widget, 
    both inside the 'sign_up_frame'. 
    """
    
password_label = tk.Label(sign_up_frame, text="Password:", font=("Helvetica", 14), 
                          foreground="white", background="#006466")
password_entry = ttk.Entry(sign_up_frame, show="*", width=25, font=("Helvetica", 16), 
                           foreground="#006466", style="Round.TEntry")

password_label.grid(row=5, column=1, padx=20, pady=10, sticky="W")
password_entry.grid(row=5, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Confirm Password (sign_up_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Confirm Password:" and an Entry widget, 
    both inside the 'sign_up_frame'. 
    """
    
confirm_password_label = tk.Label(sign_up_frame, text="Confirm Password:", font=("Helvetica", 14), 
                                  foreground="white", background="#006466")
confirm_password_entry = ttk.Entry(sign_up_frame, show="*", width=25, font=("Helvetica", 16), 
                                   foreground="#006466", style="Round.TEntry")

confirm_password_label.grid(row=6, column=1, padx=20, pady=10, sticky="W")
confirm_password_entry.grid(row=6, column=2, padx=10, pady=10, sticky="W")

def toggle_password_visibility(show_password_var):
    if show_password_var.get() == 1:
        confirm_password_entry.config(show="")
        password_entry.config(show="")
        show_password_checkbox.config(foreground="black")
    else:
        confirm_password_entry.config(show="*")
        password_entry.config(show="*")
        show_password_checkbox.config(foreground="white")

show_password_var = tk.IntVar(value=0)
show_password_checkbox = tk.Checkbutton(sign_up_frame, text="Show Password", variable=show_password_var,
                                        command=lambda: toggle_password_visibility(show_password_var),
                                        foreground="black", background="#006466")
show_password_checkbox.grid(row=7, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Submit Button (sign_up_frame) --------------------------------------- #
"""
        This code creates a "Submit" button in the sign_up_frame.
    """
    
submit_button = tk.Button(sign_up_frame, text="Submit", command=submit_sign_up, font=("Helvetica", 12), 
                          background="#065a60", foreground="white", relief="raised", bd=3,
                          activebackground="#144552",activeforeground="#1985a1")
submit_button.grid(row=9, column=2,sticky="e",pady=10)
submit_button.config(width=8)

# --------------------------------------- Back Button (sign_up_frame) --------------------------------------- #
"""
        This code creates a "Back" button in the sign_up_frame.
    """
    
back_button = tk.Button(sign_up_frame, text="Back", command=back_to_main, font=("Helvetica", 12), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="red")
back_button.grid(row=11, column=1, sticky="sw",padx=10,pady=20)
back_button.config(width=8)

# ---------------------------------------  Creating (log_in_frame) --------------------------------------- #
"""
        This code creates a Tkinter frame widget, with a background color of "#006466".
    """
    
log_in_frame = tk.Frame(root, bg="#006466")

# --------------------------------------- log_in text (log_in_frame) --------------------------------------- #
"""
               This code creates a Label widget with the text "Log In" 
    in the log_in_frame. 
    """
    
log_in_text = ttk.Label(log_in_frame, text="Log In", font=("Travelast", 25), 
                        foreground="white", background="#006466")
log_in_text.grid(row=0, column=2, columnspan=1, pady=30, padx=50)

# --------------------------------------- Email (log_in_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Email:" and an Entry widget, 
    both inside the 'log_in_frame'. 
    """

log_email_label = tk.Label(log_in_frame, text="Email:", font=("Helvetica", 14), 
                           foreground="white", background="#006466")
log_email_entry = ttk.Entry(log_in_frame, width=25, font=("Helvetica", 16), 
                            foreground="#006466", style="Round.TEntry")

log_email_label.grid(row=2, column=1, padx=20, pady=10, sticky="W")
log_email_entry.grid(row=2, column=2, padx=10, pady=10, sticky="W")

# --------------------------------------- Password (log_in_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Password:" and an Entry widget, 
    both inside the 'log_in_frame'. 
    """
    
log_password_label = tk.Label(log_in_frame, text="Password:", font=("Helvetica", 14), 
                              foreground="white", background="#006466")
log_password_entry = ttk.Entry(log_in_frame, show="*", width=25, font=("Helvetica", 16), 
                               foreground="#006466", style="Round.TEntry")

log_password_label.grid(row=3, column=1, padx=20, pady=10, sticky="W")
log_password_entry.grid(row=3, column=2, padx=10, pady=10, sticky="W")

def toggle_password_visibility_log_in(show_password_var_log_in):
    if show_password_var_log_in.get() == 1:
        log_password_entry.config(show="")
        show_password_checkbox.config(foreground="black")
    else:
        log_password_entry.config(show="*")
        show_password_checkbox.config(foreground="black")

show_password_var_log_in = tk.IntVar(value=0)
show_password_checkbox_log_in = tk.Checkbutton(log_in_frame, text="Show Password", variable=show_password_var_log_in,
                                        command=lambda: toggle_password_visibility_log_in(show_password_var_log_in),
                                        foreground="black", background="#006466")
show_password_checkbox_log_in.grid(row=4, column=2, padx=10, pady=10, sticky="W")


# --------------------------------------- Back Button (log_in_frame) --------------------------------------- #
'''sign up frame ---- back button '''
back_button = tk.Button(log_in_frame, text="Back", command=back_to_main, font=("Helvetica", 12), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="red")
back_button.grid(row=6, column=1, sticky="w",padx=10,pady=150)
back_button.config(width=8)

def show_sign_up_back():
    verify_email_frame.grid_forget()
    sign_up_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
# ---------------------------------------  Creating (log_in_frame) --------------------------------------- #
"""
        This code creates a Tkinter frame widget, with a background color of "#006466".
    """
    
verify_email_frame = tk.Frame(root, bg="#006466")

# --------------------------------------- log_in text (log_in_frame) --------------------------------------- #
"""
               This code creates a Label widget with the text "Log In" 
    in the log_in_frame. 
    """
    
log_in_text = ttk.Label(verify_email_frame, text="Verify Email", font=("Travelast", 25), 
                        foreground="white", background="#006466")
log_in_text.grid(row=0, column=2, columnspan=1, pady=30, padx=50)


# --------------------------------------- Footer Lable (main_frame) --------------------------------------- #
"""
       This code creates a Label widget with the text "Subodh Ghimire" 
    in the main_frame but at buttom. 
    """

work_text = ttk.Label(verify_email_frame, text="We have sent 6 digit code in your email.Please kindly verify your Email.", 
                      font=("Helvetica",10), foreground="white", background="#006466")
work_text.grid(row=1, column=2, columnspan=1, pady=(10,20), sticky=("e"))


# --------------------------------------- Email (log_in_frame) --------------------------------------- #
"""
        This code creates two Tkinter widgets, a label with text "Email:" and an Entry widget, 
    both inside the 'log_in_frame'. 
    """
verify_code_entry = ttk.Entry(verify_email_frame, width=10, font=("Helvetica", 25), 
                            foreground="#006466", style="Round.TEntry",justify='center')
verify_code_entry.grid(row=3, column=2, padx=10, pady=10)

# --------------------------------------- Verify Button (verify_email_frame) --------------------------------------- #
'''log in frame ----  loin button '''
verify_email_button = tk.Button(verify_email_frame, text="Verify", command=lambda: verify_code_function(submit_sign_up()), font=("Helvetica", 12), 
                          background="#065a60", foreground="white", relief="raised", bd=3, 
                          activebackground="#144552", activeforeground="#c5c3c6")
verify_email_button.grid(row=5, column=2, padx=10,pady=50)
verify_email_button.config(width=8)


# --------------------------------------- Back Button (log_in_frame) --------------------------------------- #
'''sign up frame ---- back button '''
back_button = tk.Button(verify_email_frame, text="Back", command=show_sign_up_back, font=("Helvetica", 12), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="red")
back_button.grid(row=6, column=1, sticky="w",padx=10,pady=150)
back_button.config(width=6)

root.mainloop()
