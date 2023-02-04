import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox



def show_sign_up():
    main_frame.grid_forget()
    sign_up_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

def show_log_in():
    main_frame.grid_forget()
    log_in_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

def back_to_main():
    sign_up_frame.grid_forget()
    log_in_frame.grid_forget()
    main_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
        

root = tk.Tk()
root.geometry("600x600")
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 3
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 4.5
root.geometry("+%d+%d" % (x, y))


main_frame = tk.Frame(root, bg="#006466")
main_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
for i in range(12):
    root.rowconfigure(i, minsize=50)
for i in range(12):
    root.columnconfigure(i, minsize=50)

project_text = ttk.Label(main_frame, text="Secure File Transfer Protocol", font=("Travelast", 30), foreground="white", background="#006466")
project_text.grid(row=0, column=2, columnspan=1, pady=20, padx=50)

by_text = ttk.Label(main_frame, text="by", font=("Hanging Letters", 25), foreground="white", background="#006466")
by_text.grid(row=1, column=2, columnspan=1, pady=10, padx=10)

name_text = ttk.Label(main_frame, text="Subodh Ghimire", font=("3x5", 35), foreground="white", background="#006466")
name_text.grid(row=2, column=2, columnspan=1, pady=(10,80), padx=10 ,sticky='n')

back_button = tk.Button(main_frame, text="Sign Up", command=show_sign_up, font=("Helvetica", 13), background="#065a60", 
                        foreground="white", relief="raised", bd=3, activebackground="#144552",activeforeground="#1985a1")
back_button.grid(row=4, column=2,sticky="s", padx=250, pady=10)
back_button.config(width=8)

back_button = tk.Button(main_frame, text="Log In", command=show_log_in, font=("Helvetica", 13), background="#065a60", 
                        foreground="white", relief="raised", bd=3, activebackground="#144552",activeforeground="#c5c3c6")
back_button.grid(row=5, column=2,sticky="s", padx=250, pady=10)
back_button.config(width=8)

back_button = tk.Button(main_frame, text="Exit", command=root.quit, font=("Helvetica", 13), background="#065a60", 
                        foreground="white", relief="raised", bd=3, activebackground="#144552",activeforeground="red")
back_button.grid(row=6, column=2, sticky="s", padx=250, pady=10)
back_button.config(width=8)

work_text = ttk.Label(main_frame, text="Send file online using the Secure File Transfer Protocol.", font=("Helvetica",10), foreground="white", background="#006466")
work_text.grid(row=8, column=2, columnspan=1, pady=(80,5), padx=50)

style = ttk.Style()
style.configure("Round.TEntry", fieldbackground="#ffffff", background="transparent", 
                 bd=5, relief="flat", padding=2, borderwidth=2,
                 highlightcolor="#597678", highlightbackground="#597678", 
                 borderradius=10)


sign_up_frame = tk.Frame(root, bg="#006466")

sign_up_text = ttk.Label(sign_up_frame, text="Sign Up", font=("Travelast", 25), foreground="white", background="#006466")
sign_up_text.grid(row=0, column=2, columnspan=1, pady=30, padx=50, sticky="nw")

'''sign up frame ---- first name lable and entry '''
first_name_label = tk.Label(sign_up_frame, text="First Name:", font=("Helvetica", 14), foreground="white", background="#006466")
first_name_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry", background='gray')
first_name_entry.configure(background='gray')

# first_name_entry.config(bd=2, relief="sunken")

first_name_label.grid(row=1, column=1, padx=20, pady=10, sticky="W")
first_name_entry.grid(row=1, column=2, padx=10, pady=10, sticky="W")

'''sign up frame ---- last name lable and entry '''
last_name_label = tk.Label(sign_up_frame, text="Last Name:", font=("Helvetica", 14), foreground="white", background="#006466")
last_name_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry")
# last_name_entry.config(bd=3, relief="sunken")

last_name_label.grid(row=2, column=1, padx=20, pady=10, sticky="W")
last_name_entry.grid(row=2, column=2, padx=10, pady=10, sticky="W")

'''sign up frame ---- phone number lable and entry '''
phone_number_label = tk.Label(sign_up_frame, text="Phone Number:", font=("Helvetica", 14), foreground="white", background="#006466")
phone_number_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), foreground="#006466",style="Round.TEntry")
# phone_number_entry.config(bd=3, relief="sunken")

phone_number_label.grid(row=3, column=1, padx=20, pady=10, sticky="W")
phone_number_entry.grid(row=3, column=2, padx=10, pady=10, sticky="W")

'''sign up frame ---- email lable and entry '''
email_label = tk.Label(sign_up_frame, text="Email:", font=("Helvetica", 14), foreground="white", background="#006466")
email_entry = ttk.Entry(sign_up_frame, width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry")
# email_entry.config(bd=3, relief="sunken")

email_label.grid(row=4, column=1, padx=20, pady=10, sticky="W")
email_entry.grid(row=4, column=2, padx=10, pady=10, sticky="W")

'''sign up frame ---- password lable and entry '''
password_label = tk.Label(sign_up_frame, text="Password:", font=("Helvetica", 14), foreground="white", background="#006466")
password_entry = ttk.Entry(sign_up_frame, show="*", width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry")
# password_entry.config(bd=3, relief="sunken")

password_label.grid(row=5, column=1, padx=20, pady=10, sticky="W")
password_entry.grid(row=5, column=2, padx=10, pady=10, sticky="W")


'''sign up frame ---- confirm password lable and entry '''
confirm_password_label = tk.Label(sign_up_frame, text="Confirm Password:", font=("Helvetica", 14), foreground="white", background="#006466")
confirm_password_entry = ttk.Entry(sign_up_frame, show="*", width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry")
# confirm_password_entry.config(bd=3, relief="sunken")

confirm_password_label.grid(row=6, column=1, padx=20, pady=10, sticky="W")
confirm_password_entry.grid(row=6, column=2, padx=10, pady=10, sticky="W")

'''sign up frame ---- submit button '''
submit_button = tk.Button(sign_up_frame, text="Submit", command=back_to_main, font=("Helvetica", 12), background="#065a60", 
                          foreground="white", relief="raised", bd=3,activebackground="#144552",activeforeground="#1985a1")
submit_button.grid(row=9, column=2,sticky="e",pady=40)
submit_button.config(width=8)

'''sign up frame ---- back button '''
back_button = tk.Button(sign_up_frame, text="Back", command=back_to_main, font=("Helvetica", 12), background="#065a60", 
                        foreground="white", relief="raised", bd=3, activebackground="#144552",activeforeground="red")
back_button.grid(row=11, column=1, sticky="w",padx=10,pady=20)
back_button.config(width=8)




log_in_frame = tk.Frame(root, bg="#006466")

log_in_text = ttk.Label(log_in_frame, text="Log In", font=("Travelast", 25), foreground="white", background="#006466")
log_in_text.grid(row=0, column=2, columnspan=1, pady=30, padx=50)

'''sign up frame ---- email lable and entry '''
log_email_label = tk.Label(log_in_frame, text="Email:", font=("Helvetica", 14), foreground="white", background="#006466")
log_email_entry = ttk.Entry(log_in_frame, width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry")
# email_entry.config(bd=3, relief="sunken")

log_email_label.grid(row=2, column=1, padx=20, pady=10, sticky="W")
log_email_entry.grid(row=2, column=2, padx=10, pady=10, sticky="W")

'''sign up frame ---- password lable and entry '''
log_password_label = tk.Label(log_in_frame, text="Password:", font=("Helvetica", 14), foreground="white", background="#006466")
log_password_entry = ttk.Entry(log_in_frame, show="*", width=25, font=("Helvetica", 16), foreground="#006466", style="Round.TEntry")
# password_entry.config(bd=3, relief="sunken")

log_password_label.grid(row=3, column=1, padx=20, pady=10, sticky="W")
log_password_entry.grid(row=3, column=2, padx=10, pady=10, sticky="W")

'''log in frame ----  loin button '''
log_in_button = tk.Button(log_in_frame, text="Log In", command=back_to_main, font=("Helvetica", 12), background="#065a60", 
                          foreground="white", relief="raised", bd=3, activebackground="#144552",activeforeground="#c5c3c6")
log_in_button.grid(row=5, column=2, padx=10,pady=50)
log_in_button.config(width=8)

'''sign up frame ---- back button '''
back_button = tk.Button(log_in_frame, text="Back", command=back_to_main, font=("Helvetica", 12), background="#065a60", 
                        foreground="white", relief="raised", bd=3, activebackground="#144552",activeforeground="red")
back_button.grid(row=6, column=1, sticky="w",padx=10,pady=210)
back_button.config(width=8)

root.mainloop()