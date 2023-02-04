import tkinter as tk

def show_sign_up():
    main_frame.grid_forget()
    sign_up_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

def show_sign_in():
    main_frame.grid_forget()
    sign_in_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

def back_to_main():
    sign_up_frame.grid_forget()
    sign_in_frame.grid_forget()
    main_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

root = tk.Tk()
root.geometry("600x600")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
for i in range(12):
    root.rowconfigure(i, minsize=50)
for i in range(12):
    root.columnconfigure(i, minsize=50)

sign_up_button = tk.Button(main_frame, text="Sign Up", command=show_sign_up)
sign_up_button.grid(row=10, column=0)
sign_in_button = tk.Button(main_frame, text="Sign In", command=show_sign_in)
sign_in_button.grid(row=0, column=1)
exit_button = tk.Button(main_frame, text="Exit", command=root.quit)
exit_button.grid(row=0, column=2)


sign_up_frame = tk.Frame(root)

sign_up_text = tk.Label(sign_up_frame, text="Sign Up", font=("Helvetica", 20), fg="blue")
sign_up_text.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")



first_name_label = tk.Label(sign_up_frame, text="First Name:", font=("Helvetica", 16))
first_name_label.grid(row=1, column=1)
first_name_entry = tk.Entry(sign_up_frame, width=30)
first_name_entry.grid(row=1, column=2)

last_name_label = tk.Label(sign_up_frame, text="Last Name:", font=("Helvetica", 16))
last_name_label.grid(row=2, column=1)
last_name_entry = tk.Entry(sign_up_frame, width=30)
last_name_entry.grid(row=2, column=2)

phone_number_label = tk.Label(sign_up_frame, text="Phone Number:", font=("Helvetica", 16))
phone_number_label.grid(row=3, column=1)
phone_number_entry = tk.Entry(sign_up_frame, width=30)
phone_number_entry.grid(row=3, column=2)

email_label = tk.Label(sign_up_frame, text="Email:", font=("Helvetica", 16))
email_label.grid(row=4, column=1)
email_entry = tk.Entry(sign_up_frame, width=30)
email_entry.grid(row=4, column=2)

password_label = tk.Label(sign_up_frame, text="Password:", font=("Helvetica", 16))
password_label.grid(row=5, column=1)
password_entry = tk.Entry(sign_up_frame, show="*", width=30)
password_entry.grid(row=5, column=2)

confirm_password_label = tk.Label(sign_up_frame, text="Confirm Password:", font=("Helvetica", 16))
confirm_password_label.grid(row=6, column=1)
confirm_password_entry = tk.Entry(sign_up_frame, show="*", width=30)
confirm_password_entry.grid(row=6, column=2)



submit_button = tk.Button(sign_up_frame, text="Submit", command=back_to_main)
submit_button.grid(row=7, column=0)
back_button = tk.Button(sign_up_frame, text="Back", command=back_to_main)
back_button.grid(row=8, column=0, sticky="nw")






sign_in_frame = tk.Frame(root)
email_label = tk.Label(sign_in_frame, text="Email:", font=("Helvetica", 16))
email_label.grid(row=0, column=0)
email_entry = tk.Entry(sign_in_frame, width=30)
email_entry.grid(row=0, column=1)

password_label = tk.Label(sign_in_frame, text="Password:", font=("Helvetica", 16))
password_label.grid(row=1, column=0)
password_entry = tk.Entry(sign_in_frame, show="*", width=30)
password_entry.grid(row=1, column=1)

submit_button = tk.Button(sign_in_frame, text="Submit", command=back_to_main)
submit_button.grid(row=2, column=0)

back_button = tk.Button(sign_in_frame, text="Back", command=back_to_main)
back_button.grid(row=9, column=0)

root.mainloop()