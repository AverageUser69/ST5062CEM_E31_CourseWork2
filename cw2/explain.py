# --------------------------------------- Required Lib --------------------------------------- #
# ---------------------------------------              --------------------------------------- #
# import os library
import os 
# import the regular expression library
import re 
# import the random library
import random 
# import the base64 library for encoding/decoding
import base64 
# import the hashlib library for creating hashes
import hashlib 
# import the requests library for sending HTTP requests
import requests 
# import the datetime library
import datetime 
# import tkinter library as tk
import tkinter as tk 
# import mysql connector library
import mysql.connector 
# import ttk library from tkinter
from tkinter import ttk 
# import filedialog library from tkinter
from tkinter import filedialog 
# import Error class from mysql.connector
from mysql.connector import Error 
# import messagebox library from tkinter
import tkinter.messagebox as messagebox 
#...............................generating random runber for the verification of the email

code = str(random.randint(100000, 999999))
# print(code)

# --------------------------------------- Getting Input (sign_up_frame) --------------------------------------- #

"""
    This code accesses the values of several 'Entry' widgets in a GUI from (sign_up_frame).
"""

def submit_sign_up():
    # Get the values entered in the first name entry widget
    first_name = first_name_entry.get()
    # Get the values entered in the last name entry widget
    last_name = last_name_entry.get() 
    # Get the values entered in the phone number entry widget
    phone_number = phone_number_entry.get() 
    # Get the values entered in the email entry widget
    email = email_entry.get() 
    # Get the values entered in the password entry widget
    password = password_entry.get()  
    # Get the values entered in the confirm password entry widget
    confirm_password= confirm_password_entry.get()

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

    # Create a cursor object to execute SQL queries
    cursor = mydb.cursor()

    # Define the query to select user data based on email or phone number
    check_user_query = "SELECT * FROM userdata WHERE email_address =%s OR phone_number=%s"

    # Execute the query and pass the email and phone number as parameters
    cursor.execute(check_user_query, (email, phone_number))

    # Fetch the result of the query
    result = cursor.fetchone()

    # Check if the result is not None
    if result:
        # Show an error message if the email or phone number is already in use
        messagebox.showerror("Error", "Email or Phone number already in use")
    else:
        # Call the verify_email function if the email and phone number are not in use
        verify_email()

        # print(code)
# --------------------------------------- Sending Mail --------------------------------------- #
    """
        This code first decrypt the given API using a algo and then it send mail with the code to the user with that email.
    
    """    
    def ceaser_cipher(ciphertext, term, total_chars):
        # Initialize an empty string to store the decrypted text
        apikey = ""
        
        # Loop through each character in the ciphertext
        for i, char in enumerate(ciphertext):
            
            # Calculate the shift amount for this character
            shift = term[i % len(term)]
            
            # Check if the character is an alphabet
            if char.isalpha():
                
                # Check if the character is uppercase
                if char.isupper():
                    
                    # Shift the uppercase character
                    shift_char = chr((ord(char) - shift - 65 + 26) % 26 + 65)
                    
                    # Add the shifted character to the decrypted text
                    apikey += shift_char
                    
                # If the character is lowercase
                else:
                    
                    # Shift the lowercase character
                    shift_char = chr((ord(char) - shift - 97 + 26) % 26 + 97)
                    
                    # Add the shifted character to the decrypted text
                    apikey += shift_char
                    
            # Check if the character is a digit
            elif char.isdigit():
                
                # Shift the digit character
                shift_char = chr((ord(char) - shift - 48 + 10) % 10 + 48)
                
                # Add the shifted digit to the decrypted text
                apikey += shift_char
                
            # If the character is not an alphabet or digit
            else:
                
                # Add the character to the decrypted text without shifting
                apikey += char
                
        # Return the decrypted text
        return apikey

    
# --------------------------------------- Sending Mail --------------------------------------- #
    
    # Decrypt the key
    def decrypt_file():
        # Ciphertext to be decrypted, encoded in base64
        ciphertext = "MHl4MTgxOTZkMTYzODc2NGY4NHduZzN2MjIzazFyaXUtNDdxdzk2NGotdno1OGI4YTg="
        # Decode the ciphertext from base64
        ciphertext = base64.b64decode(ciphertext.encode()).decode()
        # Calculate the total number of characters in the ciphertext
        total_chars = len(ciphertext)
        # Constant value for the decryption algorithm
        a = 12345678
        # List to store the decryption terms for each character
        term = []
        # Loop through each character in the ciphertext
        for n in range(1, total_chars):
            # If the character is an uppercase letter or a lowercase letter
            if (ord(ciphertext[n]) >= 65 and ord(ciphertext[n]) <= 90) or (ord(ciphertext[n]) >= 97 and ord(ciphertext[n]) <= 122):
                # Calculate the decryption term using a different formula for letters
                t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + a*n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 25) % 50 - 25
            else:
                # Calculate the decryption term using a different formula for non-letters
                t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 10) % 18 - 9
            # Add the decryption term to the list of terms
            term.append(t)


        apikey = ceaser_cipher(ciphertext, term, total_chars)    
        # Mailgun API endpoint
        endpoint = "https://api.mailgun.net/v3/sandbox63bc9e703d3842f4932630753e1030d6.mailgun.org/messages"
        # Email details
        api_key=apikey
        to =email
        subject = "Complete Your Email Verification"
        body = f"""Dear Valued Customer,

        We hope this message finds you well. Please take a moment to complete your email verification process by entering the following code: {code}.

        Your email verification ensures that you can receive important updates and information from our services.

        Thank you for your time and cooperation. If you have any questions or concerns, please do not hesitate to reach out to us.

        Best Regards,
        The Secure File Transfer Protocol Team"""

        # Make a POST request to the Mailgun API
        return requests.post(
            endpoint,
            auth=("api", api_key),
            data={
                "from":"Mailgun Sandbox <postmaster@sandbox63bc9e703d3842f4932630753e1030d6.mailgun.org>",
                "to": to,
                "subject": subject,
                "text": body
            }
        )
      
        # Check if the email was sent successfully
    decrypt_file()
    return first_name,last_name,phone_number,email,password,confirm_password
    
# --------------------------------------- Inserting Data inside Database (sign_up_frame) --------------------------------------- #

def verify_code_function(sign_up_values):
    # Unpack the values from sign_up_values
    first_name, last_name, phone_number, email, password, confirm_password = sign_up_values    
    
    # Get the entered verification code from the user
    verify_code = verify_code_entry.get()
    
    # Check if the verification code is empty
    if verify_code == "":
        # Display an error message if the code is empty
        messagebox.showerror("Error","Verification code cannot be empty.")
        return
    
    # Check if the entered verification code is incorrect
    if verify_code != code:
        # Display an error message if the code is incorrect
        messagebox.showerror("Error","Invalid Verification code.")
        return
    
    try:
        # Connect to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="securefile"
        )
        
        # Create a cursor to execute the SQL commands
        mycursor = mydb.cursor()
        
        # Prepare the SQL command to insert the user data into the database
        sql = "INSERT INTO userdata (first_name, last_name, email_address, phone_number, password) VALUES (%s, %s, %s, %s, %s)"
        val = (first_name, last_name, email, phone_number, password)
        
        # Execute the SQL command
        mycursor.execute(sql, val)
        
        # Commit the changes to the database
        mydb.commit()
        
        # Close the database connection
        mydb.close()
        
        # Show a success message if the account creation is successful
        if messagebox.showinfo("Success", "Email Verified!\n Account Created Successfully.") == "ok":
            # Call the log_in_after_verification function
            log_in_after_verification()
            
            # Clear the input fields
            first_name_entry.delete(0, "end")
            last_name_entry.delete(0, "end")
            phone_number_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")
            confirm_password_entry.delete(0, "end")
    except Error:
        # Display an error message if the account creation fails
        messagebox.showerror("Error", "Failed to create account. Please try again later.")
        
        # Clear the input fields
        first_name_entry.delete(0, "end")
        last_name_entry.delete(0, "end")
        phone_number_entry.delete(0, "end")
        email_entry.delete(0, "end")
        password_entry.delete(0, "end")
        confirm_password_entry.delete(0, "end")
        
        # Call the verify_email function
        verify_email()

    
# --------------------------------------- Getting Input (log_in_frame) --------------------------------------- #

def validate_log_in_credentials():
    # Get the entered email and password from the GUI entry widgets
    log_email = log_email_entry.get()
    log_password = log_password_entry.get()
    
    # Check if the email is in the correct format
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not email_pattern.match(log_email):
        # If the email is not in the correct format, show an error message
        messagebox.showerror("Error", "Invalid Email")
        return
    # Hash the password using SHA-256
    log_password =log_password.encode()
    log_password = hashlib.sha256(log_password).hexdigest()
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="securefile"
    )
    # Create a cursor object to execute the database query
    cursor = mydb.cursor()
    # Check if the email and password match an existing user in the database
    query = "SELECT email_address, password, id FROM userdata WHERE email_address=%s and password=%s"
    cursor.execute(query, (log_email, log_password))
    result = cursor.fetchone() 
    # If the email and password match an existing user, show the home page
    if result:
        current_user_id = result[2]
        show_home_page(current_user_id)
        return 
    else:
        # If the email and password do not match, show an error message
        messagebox.showerror("Error", "Invalid Credentials")
        return False



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
        
# --------------------------------------- Switching to (verify_email_frame) --------------------------------------- #  
        
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
        
# --------------------------------------- Switching to (home_page_frame) --------------------------------------- #

"""
        This code defines a function show_log_in that switches the displayed frame 
    from main_frame to log_in_frame.
    """        

def show_home_page(current_user_id):
    main_frame.grid_forget()
    home_page_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)
    
# --------------------------------------- Connect to the database and retrieve the user data --------------------------------------- #

    # Connect to the database to retrieve the first name and last name of the current user
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="securefile"
    )
    cursor = mydb.cursor()
    query = "SELECT first_name, last_name FROM userdata WHERE id = %s"
    cursor.execute(query, (current_user_id,))
    result = cursor.fetchone()

    # Display a welcome message on the home page using the full name
    if result:
        full_name = str(result[0]) + " " + str(result[1])
        home_text = ttk.Label(home_page_frame, text=f"Welcome, {full_name}", font=("Helvetica", 15), foreground="white", background="#006466")
        home_text.grid(row=0, column=1, pady=20, padx=10)

    # Connect to the database to retrieve the file names of the current user
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="securefile"
        )
        cursor = mydb.cursor()
        query = "SELECT file_name FROM filestorage WHERE user_id = %s"
        cursor.execute(query, (current_user_id,))
        file_names = cursor.fetchall()

        # Display the file names on the home page
        if file_names:
            row = 3
            column = 0
            files_text = ttk.Label(home_page_frame, text="Files:", font=("Helvetica", 15), foreground="white", background="#006466")
            files_text.grid(row=2, column=0, pady=10, padx=20,sticky="w")

            
# --------------------------------------- Arranging the Files in Alphabaticl Order --------------------------------------- #

            # Loop through each file name in the list of file names
            for i in range(len(file_names)):
                # Use bubble sort to sort the list of file names in ascending order
                for j in range(len(file_names) - i - 1):
                    if file_names[j] > file_names[j + 1]:
                        file_names[j], file_names[j + 1] = file_names[j + 1], file_names[j]
                # Loop through each file name in the sorted list of file names
            for i, file_name in enumerate(file_names):
                # Construct the file path using the file name
                file_path = "C:/Users/98218/OneDrive/Desktop/online_file/" + str(file_name[0])

# --------------------------------------- Decrypt the Users File --------------------------------------- #

                # Define a function that decrypts the cipher text using a Ceaser cipher algorithm
                def ceaser_cipher(ciphertext, term, total_chars):
                    plaintext = ""
                    # Loop through each character in the cipher text
                    for i, char in enumerate(ciphertext):
                        shift = term[i % len(term)]
                        # If the character is a letter (upper or lower case)
                        if char.isalpha():
                            if char.isupper():
                                shift_char = chr((ord(char) - shift - 65 + 26) % 26 + 65)
                                plaintext += shift_char
                            else:
                                shift_char = chr((ord(char) - shift - 97 + 26) % 26 + 97)
                                plaintext += shift_char
                        # If the character is a digit
                        elif char.isdigit():
                            shift_char = chr((ord(char) - shift - 48 + 10) % 10 + 48)
                            plaintext += shift_char
                        # If the character is not a letter or a digit
                        else:
                            plaintext += char
                    return plaintext
                
# --------------------------------------- Genrate Algorythm To decrypt the text --------------------------------------- #

                def open_file(file_path):
                    # Open the file with read access
                    with open(file_path, "r") as f:
                        # Read the contents of the file
                        cipher_text = f.read()

                    # Decode the base64 encoded ciphertext
                    ciphertext = base64.b64decode(cipher_text.encode()).decode()

                    # Get the total number of characters in the ciphertext
                    total_chars = len(ciphertext)

                    # Get the current user id
                    a = current_user_id

                    # Initialize a list to store the terms
                    term = []

                    # Loop through each character in the ciphertext
                    for n in range(1, total_chars):
                        # Check if the character is a letter (uppercase or lowercase)
                        if (ord(ciphertext[n]) >= 65 and ord(ciphertext[n]) <= 90) or (ord(ciphertext[n]) >= 97 and ord(ciphertext[n]) <= 122):
                            # Calculate the term for the letter
                            
                            
                            t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + a*n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 25) % 50 - 25
                        
                        
                        else:
                            # Calculate the term for a non-letter character
                            t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 10) % 18 - 9
                        # Add the term to the list
                        term.append(t)

                    # Decrypt the ciphertext using the terms
                    plaintext = ceaser_cipher(ciphertext, term, total_chars)

                    # Create a new window to display the decrypted plaintext
                    read_file_window = tk.Toplevel(home_page_frame)
                    read_file_window.title(str(file_name))

                    # Get the screen width and height
                    screen_width = read_file_window.winfo_screenwidth()
                    screen_height = read_file_window.winfo_screenheight()

                    # Set the size of the window
                    window_width = 400
                    window_height = 400

                    # Calculate the coordinates to center the window on the screen
                    x_coordinate = (screen_width/2) - (window_width/2)
                    y_coordinate = (screen_height/2) - (window_height/2)

                    # Set the geometry of the window
                    read_file_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

                    # Create a text widget to display the plaintext
                    text = tk.Text(read_file_window, font=("Helvetica", 12))
                    text.pack(fill="both", expand=True)
                    text.insert("1.0", plaintext)
                    text.config(state="disabled")

                # Convert file_name to a string
                file_name = str(file_name[0])

                # Create a new file name with '.txt' extension
                new_file_name = ".".join(file_name.rsplit(".", 2)[:1]) + ".txt"

                # Create a button for each file
                browse_button = tk.Button(home_page_frame, text=str(new_file_name), command=lambda file_path=file_path: open_file(file_path), font=("Helvetica", 10), 
                                background="#006466", foreground="white", relief="raised", 
                                activebackground="#006466", activeforeground="#c5c3c6")

                # Place the button on the grid in the home_page_frame
                browse_button.grid(row=row, column=column, padx=(10),pady=(10))

                # Set the width of the button
                browse_button.config(width=18)

                # Increment the column and row values for the next button
                column += 1
                if column == 3:
                    row += 1
                    column = 0

                # If no files are found, display a message
        else:
            files_text = ttk.Label(home_page_frame, text="No files found", font=("Helvetica", 12), foreground="white", background="#006466")
            files_text.grid(row=2, column=0, columnspan=3, pady=10, padx=(50,70)) 
                
# --------------------------------------- Search Entry code --------------------------------------- #

        search_entry = ttk.Entry(home_page_frame, width=20, font=("Helvetica", 12), 
                                    foreground="#006466", style="Round.TEntry",justify='center')
        search_entry.grid(row=1, column=1, padx=10, pady=10)

        
        search_button = tk.Button(home_page_frame, text="Search", command=lambda:search_files(), font=("Helvetica", 10), 
                          background="#065a60", foreground="white", relief="raised", bd=1, 
                          activebackground="#144552", activeforeground="#c5c3c6")
        search_button.grid(row=1, column=2, padx=(65,0),pady=5,sticky="w")
        search_button.config(width=7)
        
# --------------------------------------- Search For Files --------------------------------------- # 
                                    
        # This function is used to search for files
        def search_files():
            # Get the search string entered by the user
            search_string = search_entry.get()
            
            # List to store search results
            search_results = []
            
            # Loop through the list of all file names
            for file_name in file_names:
                # Check if the search string is present in the current file name
                if search_string in str(file_name[0]):
                    # If present, add the file name to the list of search results
                    search_results.append(file_name[0])
            
            # If search results are found
            if search_results:
                # Create a new window to display the search results
                search_window = tk.Toplevel(home_page_frame)
                search_window.title("Search Results")
                
                # Get the screen width and height
                screen_width = search_window.winfo_screenwidth()
                screen_height = search_window.winfo_screenheight()
                
                # Set the dimensions of the search results window
                window_width = 400
                window_height = 400
                
                # Calculate the x and y coordinates to center the window
                x_coordinate = (screen_width/2) - (window_width/2)
                y_coordinate = (screen_height/2) - (window_height/2)
                
                # Set the geometry of the search window
                search_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
                
                # Set the background color of the search window
                search_window.config(bg="#006466")
                
                # Display a label to indicate the search results
                results_text = ttk.Label(search_window, text="Results", font=("Helvetica", 15), foreground="white", background="#006466")
                results_text.grid(row=0, column=0, pady=10, padx=50,sticky="n")
                
                # Initialize the row and column for displaying the search results
                result_row = 2
                result_column = 0
                
                # Loop through the list of search results
                for result in search_results:
                    # Create a button for each search result
                    result_button = tk.Button(search_window, text=result, command=lambda file_path=f"C:/Users/98218/OneDrive/Desktop/online_file/{result}": open_file(file_path), font=("Helvetica", 10), 
                    background="#006466", foreground="white", relief="raised", 
                    activebackground="#006466", activeforeground="#c5c3c6")
                    
                    # Display the button in the search results window
                    result_button.grid(row=result_row, column=result_column, padx=(30),pady=(10))
                    
                    # Set the width of the button
                    result_button.config(width=40)
                    
                    # Increment the row for the next search result
                    result_row += 1
            else:
                messagebox.showerror("Error", "No search results found")           
        def insert_into_database(file_path):
            # Connect to the database 'securefile' using the mysql connector library
            mydb = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="securefile"
                        )

            # Create a cursor object to execute queries
            cursor = mydb.cursor()

            # SQL query to insert data into the 'filestorage' table
            query = "INSERT INTO filestorage (user_id, time, file_name) VALUES (%s, %s, %s)"

            # Get the original file name and timestamp to create a new file name
            original_file_name = os.path.basename(file_path)
            time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            new_file_name = f"{os.path.splitext(original_file_name)[0]}.{time_stamp}{os.path.splitext(original_file_name)[1]}"

            # Values to be inserted into the database table
            values = (current_user_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), new_file_name)

            # Execute the query to insert data into the database
            cursor.execute(query, values)

            # Commit the changes to the database
            mydb.commit()

                    
            # Ceaser Cipher Function
            def ceaser_cipher(plaintext, term, total_chars):
                # Initialize the ciphertext to be returned
                ciphertext = ""
                # Loop through each character in the plaintext
                for i, char in enumerate(plaintext):
                    # Use the i-th term of the key to shift the i-th character
                    shift = term[i % len(term)]
                    # Check if the character is an alphabet
                    if char.isalpha():
                        # Check if the character is uppercase
                        if char.isupper():
                            # Shift the uppercase character using the shift value
                            shift_char = chr((ord(char) + shift - 65) % 26 + 65)
                            # Add the shifted character to the ciphertext
                            ciphertext += shift_char
                        else:
                            # Shift the lowercase character using the shift value
                            shift_char = chr((ord(char) + shift - 97) % 26 + 97)
                            # Add the shifted character to the ciphertext
                            ciphertext += shift_char
                    # Check if the character is a digit
                    elif char.isdigit():
                        # Shift the digit character using the shift value
                        shift_char = chr((ord(char) + shift - 48) % 10 + 48)
                        # Add the shifted character to the ciphertext
                        ciphertext += shift_char
                    # If the character is not an alphabet or a digit, add it as is to the ciphertext
                    else:
                        ciphertext += char
                # Encode the ciphertext using base64 encoding and return the result
                b64_ciphertext = base64.b64encode(ciphertext.encode()).decode()
                return b64_ciphertext


        # Open the file specified by file_path in read mode
            with open(file_path, "r") as f:
                # Read the content of the file
                file_content = f.read()
                term = []
            # Store the current user id in a variable
            a = current_user_id
            # Calculate the total number of characters in the file
            total_chars = len(file_content)
            plaintext = file_content
            # Loop through each character in the plaintext
            for n in range(1, total_chars):
                # If the character is a letter (upper or lower case)
                if (ord(plaintext[n]) >= 65 and ord(plaintext[n]) <= 90) or (ord(plaintext[n]) >= 97 and ord(plaintext[n]) <= 122):
                    # Calculate the shift term for the character
                    t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + a*n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 25) % 50 - 25
                else:
                    # Calculate the shift term for the character
                    t = ((((n**5 + n**3 + a*n**2 + a*n) * (n**7 + n**5 + a*n**3 + n**2 + 2*a*n + a)) % 100000 - 50000) // 1000 + 10) % 18 - 9
                # Append the shift term to the term list
                term.append(t)
            # Call the ceaser_cipher function to encrypt the plaintext using the calculated shift terms
            ciphertext = ceaser_cipher(plaintext, term, total_chars)
            
            # Construct the path to the newly encrypted file
            new_file_path = "C:/Users/98218/OneDrive/Desktop/online_file/" + new_file_name
            # Open the newly encrypted file in write mode
            with open(new_file_path, "w") as f:
                # Write the encrypted content to the file
                f.write(ciphertext)

            # Show a success message to the user
            messagebox.showinfo("Success", "File successfully uploaded")

                        
        # Function to open a file dialog and select a file
        def browse_file():
            # Show a file dialog to select a text file
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            # If a file is selected
            if file_path:
                # Call the insert_into_database function with the selected file's path
                insert_into_database(file_path)

        # "Browse" button to open the file dialog
        browse_button = tk.Button(home_page_frame, text="Browse", command=lambda: browse_file(), font=("Helvetica", 10), 
                        background="#065a60", foreground="white", relief="raised", bd=1, 
                        activebackground="#144552", activeforeground="#c5c3c6")
        # Place the button in the home_page_frame grid
        browse_button.grid(row=1, column=0, padx=(20,10),pady=5,sticky="nw")
        # Set the width of the button
        browse_button.config(width=7)

        # "Refresh" button to refresh the home page
        refresh_button = tk.Button(home_page_frame, text="refresh", command=lambda: show_home_page(current_user_id), font=("Helvetica", 10), 
                        background="#065a60", foreground="white", relief="raised", bd=1, 
                        activebackground="#144552", activeforeground="#c5c3c6")
        # Place the button in the home_page_frame grid
        refresh_button.grid(row=2, column=2, padx=(25,10),pady=5,sticky="n")
        # Set the width of the button
        refresh_button.config(width=7)  
                    
    # If there is no file selected
    else:
        # Return from the function
        return


# --------------------------------------- Switching to (open_file_frame) --------------------------------------- # 
  
def open_file_format():
    home_page_frame.grid_forget()
    open_file_frame.grid(row=0, column=0, rowspan=12, columnspan=12, sticky="nsew")
    for i in range(12):
        root.rowconfigure(i, minsize=50)
    for i in range(12):
        root.columnconfigure(i, minsize=50)

 # --------------------------------------- Switching to (log_in_frame) --------------------------------------- # 
       
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
       This code creates a Label widget with the text "Secure File Vault" 
    in the main_frame. 
    """
    
project_text = ttk.Label(main_frame, text="Secure File Vault", 
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

work_text = ttk.Label(main_frame, text="Protecting your precious memories, one file at a time.", 
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
# --------------------------------------- Toogle password visibility (log_in_frame) --------------------------------------- #
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


# --------------------------------------- Log In Button (log_in_frame) --------------------------------------- #
'''log in frame ----  loin button '''
log_in_button = tk.Button(log_in_frame, text="Log In", command=validate_log_in_credentials, font=("Helvetica", 12), 
                          background="#065a60", foreground="white", relief="raised", bd=3, 
                          activebackground="#144552", activeforeground="#c5c3c6")
log_in_button.grid(row=5, column=2, padx=10,pady=50)
log_in_button.config(width=8)

# --------------------------------------- Back Button (log_in_frame) --------------------------------------- #
'''sign up frame ---- back button '''
back_button = tk.Button(log_in_frame, text="Back", command=back_to_main, font=("Helvetica", 12), 
                        background="#065a60", foreground="white", relief="raised", bd=3, 
                        activebackground="#144552",activeforeground="red")
back_button.grid(row=6, column=1, sticky="w",padx=10,pady=150)
back_button.config(width=8)

# --------------------------------------- Switch to (sign_up_frame) --------------------------------------- #

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

# --------------------------------------- Refresh Frame --------------------------------------- #

def refresh_frame():
    home_page_frame.after(1000, refresh_frame)
    
home_page_frame = tk.Frame(root, bg="#006466")


open_file_frame = tk.Frame(root, bg="#006466")

# home_page_frame.after(1000,refresh_frame)

root.mainloop()
