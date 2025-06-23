from tkinter import Tk,Label,Frame,Entry,Button,messagebox,filedialog # Importing necessary classes from tkinter: Tk for page creation|Label for title|
# frame for creating frames,Entry for input fields,Button for buttons|Entry for input fields|Button for buttons
from tkinter.ttk import Combobox  # Importing Combobox for dropdown menus(admin,users)
import time # Importing time module for time-related functions(for date)
from  PIL import Image,ImageTk # Importing Image and ImageTk from PIL for image handling
import random # Importing random module for generating random values(captcha)
import project_tables
import sqlite3
import project_mails
import os,shutil
import time



# Here create captcha
def random_captcha(length=4):
    letters = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # letters = 'abcdefghijklmnopqrstuvwxyz'   
    return ''.join(random.choice(letters) for i in range(length))

random_captcha()

# Function to refresh button the captcha label with a new captcha value
def refresh():
    captcha=random_captcha()
    captcha_lbl.configure(text=captcha)  # update the captcha label with a new captcha value





root = Tk()   # make a object of root window
root.state("zoomed")  # make the window full screen
root.configure(bg='sky blue')  # set the background color of the window 
root.title("ABC Bank")  # set the title of the window
root.resizable(width=False, height=False)  # make the window not resizable


# Outer Frame{


# create a title label with a specific font, background color, and underline style
title_lbl=Label(root,text="Banking Automation",font=('Arial',50,"bold","underline"),bg="sky blue")  # create a label for the title
title_lbl.pack() 

# create a label for the current date and time
today_lbl=Label(root,text=time.strftime('%A,%d %B %Y'),font=('Arial',10,"bold","underline"),bg="powder blue",fg=('blue'))  # create a label for the title
today_lbl.pack(pady=10)  # pack the title label to the window

# fix the logo image on the top left corner of the window
img = Image.open("C:/Users/Aditya Sharma/Desktop/DUCAT/SQL/SQL 26 SQlite Project_class_1/image/logo.jpg").resize((300, 150))     # open the image and resize it to 300x150 pixels
img_bitmap=ImageTk.PhotoImage(img,master=root)    # convert the image to a format that can be used in tkinter, it return bit_image
logo_lbl=Label(root,image=img_bitmap,bg="powder blue")  # create a label for the image
logo_lbl.place(relx=0,rely=0)  # place the image label at the top left corner of the window

# create a footer label with a specific font, background color, and text
footer_lbl=Label(root,text='Developed By:Aditya Sharma',bg='powder blue',fg='blue',font=('Arial',10,"bold"))  # create a label for the footer
footer_lbl.pack(side='bottom',pady=10)  # pack the footer label to the bottom of the window

# Outer Frame}



# inner frame{

# relx=left to right, rely=top to bottom, relwidth=width of the frame, relheight=height of the frame
# fg=foreground color, bg=background color, font=font style
# state=readonly means the user cannot edit the value of the combobox, it can only select from the given options
# width=width of the entry field, bd=border width
# command=the function to be called when the button is clicked
# place() method is used to place the widget at a specific position in the window
# show'*'=You can use the show option to hide the password characters in the entry field, it will show '*' instead of the actual password characters



# Function to create the main screen of the banking software
def main_screen():



    def login_btn():
        # global ucan
        uacn=acn_no_entry.get()
        upass=acn_pass_entry.get()
        ucap =enter_cap_inentry.get()
        utype=user_combo.get()
        actual_cap=captcha_lbl.cget('text')

        

            
        if utype=="Admin":
                if uacn=='0' and upass=='admin':
                    if ucap==actual_cap:
                        frm.destroy()  # destroy the frame to clear the screen
                        admin_screen()

                    else:
                        messagebox.showerror('Login','Invalid Captcha')

                else:
                    messagebox.showerror('login','Invalid ACN/Password/Type')
        elif utype=='Customer':
            
                if ucap==actual_cap:
                    conobj=sqlite3.connect(database='bank.sqlite')  # connect to the database
                    curobj=conobj.cursor()  # create a cursor object to execute SQL queries
                    query = "select * from accounts where accounts_acno=? and accounts_pass=?"
                    curobj.execute(query,(uacn,upass)) # execute the query to check if the account number and email match 


                    tup=curobj.fetchone()  # fetch the result of the query
                    conobj.close()
                    if tup==None:
                        messagebox.showerror('User Login','Invalid ACN/Password')  # show an error message if the account number or password is invalid
                    else:
                        frm.destroy()
                        user_screen(uacn)

                else:
                    messagebox.showerror('Login','Invalid Captcha')

        else:
                messagebox.showerror("Login","Kindly select valid user type")







                    
                



    def forgot_pass_btn():
        def forgot():
            frm.destroy()
            forgot_screen()





    frm=Frame(root)  # create a frame for the main screen -------------------------
    # frm.place(relx=0.25,rely=.18,)  # place the frame in the window
    frm.place(relx=0.22, rely=0.18, relwidth=0.6,relheight=.7) # set the size of the frame to occupy 50% of the width and almost 50% of the height of the window
    frm.configure(bg='white')  # set the background color of the frame

    # create User Type label and dropdown menu
    user_lbl=Label(frm,text='User Type',fg='black',font=('Arial',15,"bold"))  # create a label for the footer
    user_lbl.place(relx=.17,rely=.1)  # place the label in the center of the frame
    
    # create a dropdown menu for user selection -----------------------
    user_combo=Combobox(frm,values=['----select----','Admin','Customer'],font=('Arial',15,""),state='readonly')  # create a dropdown menu for user selection
    user_combo.current(1)  # set the default value of the dropdown menu to 'Select User'
    user_combo.place(relx=.45,rely=.1)  # place the dropdown menu in the center of the frame
    

    # create a label for the account number and password entry fields ----------------------
    acn_lbl=Label(frm,text='ACN',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
    acn_lbl.place(relx=.17,rely=.22)
    # create an entry field for the account number
    acn_no_entry=Entry(frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
    acn_no_entry.place(relx=.45,rely=.22)  # place the entry field in the center of the frame
    acn_no_entry.focus()  # set the focus on the account number entry field



    # create a label and entry field for the password -------------------
    acn_pass_lbl=Label(frm,text='🔒Password',fg='black',font=('Arial',15,"bold"))  # create a label for the password
    acn_pass_lbl.place(relx=.16,rely=.35)  # place the label in the center of the frame

    # create an entry field for the password
    acn_pass_entry=Entry(frm,font=('Arial',15,""),width=20,bd=5,show='*')  # create an entry field for the password
    acn_pass_entry.place(relx=.45,rely=.35)  # place the entry field in the center of the frame



    # create a label for the captcha ---------------------------
    global captcha_lbl  # declare the captcha_lbl variable as global to access it in the refresh function
    # create a label for the captcha
    captcha_lbl =Label(frm,text=random_captcha(),fg='white',bg='black',font=('Arial',15,"bold"))
    captcha_lbl.place(relx=.45,rely=.46)

    # create refresh button to refresh captcha
    refresh_button=Button(frm,text='refresh',bg='red',fg='white',command=refresh)
    refresh_button.place(relx=.53,rely=.46  )
    
    # create entry field for the captcha
    entercap_lbl=Label(frm,text='Captcha',fg='black',font=('Arial',15,"bold"))  
    entercap_lbl.place(relx=.16,rely=.52)  

    # create captcha entry field
    enter_cap_inentry=Entry(frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the password
    enter_cap_inentry.place(relx=.45,rely=.52)



    # create login button -----------------------
    login_btn=Button(frm,text='Login',bg='light green',fg='white',font=('arial',15),bd=5,command=login_btn)
    login_btn.place(relx=.45,rely=.63)  # create a button for login and place it in the center of the frame

    # create reset button to reset details ----------------------
    reset_btn=Button(frm,text='Reset',bg='light green',fg='white',font=('arial',15),bd=5)
    reset_btn.place(relx=.30,rely=.63)

    # create forgot password button ----------------------
    forgot_pass_btn=Button(frm,text='Forgot Password',bg='light green',fg='white',font=('arial',15),bd=5,width=20,command=forgot_screen)
    forgot_pass_btn.place(relx=.29,rely=.75)


# here we create the admin screen
def admin_screen():

    



    # function to create open account btn screens for account operations
    def open_acn():
        global inner_frm
        inner_frm = Frame(frm, bg='white',highlightbackground='black', highlightthickness=2)
        inner_frm.place(relx=0.14, rely=0.2, relwidth=0.7, relheight=0.7)

        title_lbl=Label(inner_frm,text='Fill the details to open account', bg='white', font=('Arial', 14, "bold"), fg='purple')
        title_lbl.pack(pady=10)

        fname_lbl=Label(inner_frm,text='First Name',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        fname_lbl.place(relx=.15,rely=.27)
        # create an entry field for the account number
        fname_lbl_entry=Entry(inner_frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
        fname_lbl_entry.place(relx=.27,rely=.27)  # place the entry field in the center of the frame
        fname_lbl_entry.focus()

        lname_lbl=Label(inner_frm,text='Last Name',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        lname_lbl.place(relx=.50,rely=.27)
        # create an entry field for the account number
        lname_lbl_entry=Entry(inner_frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
        lname_lbl_entry.place(relx=.62,rely=.27)



        Email_lbl=Label(inner_frm,text='Mail ID',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        Email_lbl.place(relx=.15,rely=.36)
        # create an entry field for the account number
        Email_lbl_entry=Entry(inner_frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
        Email_lbl_entry.place(relx=.27,rely=.36)


        mob_lbl=Label(inner_frm,text='Number',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        mob_lbl.place(relx=.50,rely=.36)
        # create an entry field for the account number
        mob_lbl_entry=Entry(inner_frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
        mob_lbl_entry.place(relx=.62,rely=.36)


        gender_lbl =Label(inner_frm,text='Gender',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        gender_lbl.place(relx=.15,rely=.45)

        # create a dropdown menu for
        gender_combo=Combobox(inner_frm,values=['--select gender--','Male','Female','Others'],font=('Arial',15,""),state='readonly')  # create a dropdown menu for user selection
        gender_combo.current(0)  # set the default value of the dropdown menu to 'Select User'
        gender_combo.place(relx=.27,rely=.45)


        acn_type_lbl =Label(inner_frm,text='Type',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        acn_type_lbl.place(relx=.50,rely=.45)

        acn_type_combo=Combobox(inner_frm,values=['--selectaccount--','Saving','Current'],font=('Arial',15,""),state='readonly')  # create a dropdown menu for user selection
        acn_type_combo.current(0)  # set the default value of the dropdown menu to 'Select User'
        acn_type_combo.place(relx=.62,rely=.45)


        def open_acn_btn():
            fname = fname_lbl_entry.get().strip()
            number = mob_lbl_entry.get().strip()
            gender = gender_combo.get()
            acn_type = acn_type_combo.get()

            # Only First Name, Number, Gender, and Type are mandatory
            if not fname or not number or gender == '--select gender--' or acn_type == '--selectaccount--':
                messagebox.showerror("Error", "First Name, Number, Gender, and Type are mandatory.")
                return  # Do not proceed if any field is empty

            resp = messagebox.askyesno("Submit", "Sure:to open account")
            if resp:
                open_acn_db()  # Call this BEFORE destroying the frame
                inner_frm.destroy()
                admin_screen()

        def reset_acn_details():
            fname_lbl_entry.delete(0, 'end')
            lname_lbl_entry.delete(0, 'end')
            Email_lbl_entry.delete(0, 'end')
            mob_lbl_entry.delete(0, 'end')
            gender_combo.current(0)
            acn_type_combo.current(0)

        def open_acn_db():
            ufname=fname_lbl_entry.get()
            ulname=lname_lbl_entry.get()
            uemail=Email_lbl_entry.get()
            unumber=mob_lbl_entry.get()
            ugender=gender_combo.get()
            uacn_type=acn_type_combo.get()
            ubal=0.0
            uopendate = time.strftime('%d/%m/%Y %H:%M:%S')  # get the current date in the format of dd/mm/yyyy
            upass=random_captcha().replace(' ','')  # generate a random captcha for the password, remove spaces if any

            conobj=sqlite3.connect(database='bank.sqlite')  # connect to the database
            curobj=conobj.cursor()
            query = "insert into accounts values(null,?,?,?,?,?,?,?,?,?)"
            curobj.execute(query, (ufname, ulname, upass, uemail, unumber, ugender, uopendate, uacn_type, ubal))
            conobj.commit()
            
            messagebox.showinfo('Account Opened', 'Account opened successfully')  # show a message box to confirm the account opening
            print('Account Opened')  # print a message to the console

            conobj=sqlite3.connect(database='bank.sqlite')  # connect to the database
            curobj=conobj.cursor()
            query = "select max(accounts_acno) from accounts"
            curobj.execute(query)  # execute the query to get the maximum account number
            uacno=curobj.fetchone()[0]  # fetch the maximum account number from the query result
            conobj.close()  # close the database connection

            try:
                project_mails.send_mail(uemail,ufname,ulname,upass,uopendate)  # send an email to the user with the account details
                messagebox.showinfo('Email Sent', f'Email sent successfully{uemail}')  # show a message box to confirm the email sending
            except Exception as e:
                messagebox.showerror('open account',e)  # show an error message box if there is an error in sending the email

# table1='''create table accounts(
# accounts_acno integer primary key autoincrement,
# accounts_fname text,
# accounts_lname text,
# accounts_pass text,
# accounts_email text,
# accounts_mob text,
# accounts_gender text,
# accounts_opendate text,
# accounts_type text,
# accounts_bal float)

        conf_acn_btn = Button(
            inner_frm, text='Open Account', bg='blue', fg='white', font=('Arial', 14), width=20, bd=5,
            command=open_acn_btn  # Only call open_acn_btn, which handles everything
        )
        conf_acn_btn.place(relx=0.25, rely=0.60)


        reset_acn_detls_btn = Button(inner_frm, text='Reset', bg='blue', fg='white', font=('Arial', 14), width=20, bd=5,
                        command=reset_acn_details)  # create a button for login and place it in the center of the frame
        reset_acn_detls_btn.place(relx=0.55, rely=0.60)








    # function to create view account btn screens for account operations
    def view_acn():
       global view_command
       def view_command():
            uacn = acn_lbl_entry.get().strip()
            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = "select * from accounts where accounts_acno=?"
            curobj.execute(query, (uacn,))
            tup = curobj.fetchone()
            conobj.close()
            if tup is None:
                messagebox.showerror('View Account', 'Record not found')
            else:
                details = f"""
                Account No. : {tup[0]}
                First Name : {tup[1]}
                Last Name : {tup[2]}
                Email : {tup[4]}
                Mobile : {tup[5]}
                Balance : {tup[9]}
                """
            messagebox.showinfo('Account Details', details)

            inner_frm = Frame(frm, bg='white', highlightbackground='black', highlightthickness=2)
            inner_frm.place(relx=0.14, rely=0.2, relwidth=0.7, relheight=0.7)

            title_lbl = Label(inner_frm, text='Fill the details to view account', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)

            acn_lbl = Label(inner_frm, text='Account No.', fg='black', font=('Arial', 15, "bold"))
            acn_lbl.place(relx=.3, rely=.27)

            acn_lbl_entry = Entry(inner_frm, font=('Arial', 15, ""), width=20, bd=5)
            acn_lbl_entry.place(relx=.45, rely=.27)
            acn_lbl_entry.focus()

            chk_btn = Button(inner_frm, text='Check Details', font=('Arial', 14), command=view_command)
            chk_btn.place(relx=0.45, rely=0.4)








    # function to create delete account btn screens for account operations
    def delete_acn():

        def send_otp():
            uacn=acn_lbl_entry.get().strip()
        
            

            # aunthentication acount number and email
            conobj=sqlite3.connect(database='bank.sqlite')  # connect to the database
            curobj=conobj.cursor()  # create a cursor object to execute SQL queries
            query = "select * from accounts where accounts_acno=?"
            curobj.execute(query,(uacn,))  # execute the query to check if the account number and email match
            tup=curobj.fetchone()  # fetch the result of the query

            conobj.close()

            
            if tup==None:
                messagebox.showerror('Delete Account','Record not found')  # show an error message if the account number or email is invalid
            else:
                # if the account number and email match, generate a random OTP
                otp = str(random.randint(1000,9999))
                project_mails.send_otp_mail(tup[4],tup[1],otp)
                messagebox.showinfo('Delete Account','otp sent to registered mail id')

                otp_entry=Entry(inner_frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the password
                otp_entry.place(relx=.35,rely=.60)

                def verify():
                    uotp=otp_entry.get()
                    if otp==uotp:  # check if the entered OTP matches the generated OTP
                        respon= messagebox.askyesno('Delete Account',f'Are you sure you want to delete account {uacn}?')  # ask for confirmation before deleting the account
                        if not respon:
                            inner_frm.destroy()  # destroy the frame to clear the screen and call the main screen function again
                            acn_lbl_entry.delete(0,'end')
                            admin_screen() # call the main screen function to show the main screen again
                            return
                        conobj=sqlite3.connect(database='bank.sqlite')  # connect to the database
                        curobj=conobj.cursor()  # create a cursor object to execute SQL queries
                        query = "delete from accounts where accounts_acno=?"
                        curobj.execute(query,(uacn,))
                        conobj.commit()  # commit the changes to the database
                        conobj.close()  # close the database connection
                        

                        messagebox.showinfo('Delete Account',f'Your password:{tup[3]}')  # show the password in a message box
                        otp_entry.destroy()  # destroy the OTP entry field after verification
                        acn_lbl_entry.delete(0,'end')
                        verify_btn.destroy()
                        inner_frm.destroy()  
                        admin_screen()  # destroy the verify button after verification
                    else:
                        messagebox.showerror('Forgot Password','Invalid OTP')

            

            verify_btn=Button(inner_frm,text='Verify OTP',bg='Red',fg='white',font=('arial',15),bd=5,width=20,command=verify)
            verify_btn.place(relx=.35,rely=.70)

        inner_frm = Frame(frm, bg='white',highlightbackground='black', highlightthickness=2)
        inner_frm.place(relx=0.14, rely=0.2, relwidth=0.7, relheight=0.7)

        title_lbl=Label(inner_frm,text='Fill the details to delete account', bg='white', font=('Arial', 14, "bold"), fg='purple')
        title_lbl.pack(pady=10)

        acn_lbl=Label(inner_frm,text='Account No.',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
        acn_lbl.place(relx=.3,rely=.27)

        acn_lbl_entry=Entry(inner_frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
        acn_lbl_entry.place(relx=.45,rely=.27)
        acn_lbl_entry.focus()

        otp_lbl=Button(inner_frm,text='Send OTP',fg='gray',font=('Arial',15,"bold"),command=send_otp)  # create a label for the account number
        otp_lbl.place(relx=.5,rely=.37)



        







    # function to create open account btn screens for account operations
    def logout():
        resp=messagebox.askyesno("logout","Do you want to logout?")  # askyesno is used to ask a yes/no question after click logout btn, it returns True if yes and False if no
        if resp:
            frm.destroy()  # destroy the frame to clear the screen and call the main screen function again, this fun pass in command of logout_btn
            main_screen()

    




    frm = Frame(root, bg='light gray')
    frm.place(relx=0, rely=0.18, relwidth=1, relheight=0.7)

    user_lbl = Label(frm, text='Welcome Admin', fg='black', font=('Arial', 15, "bold"), bg='light gray')
    user_lbl.place(relx=0.41, rely=0.02)



    open_btn = Button(frm, text='Account Open', bg='green', fg='white', font=('Arial', 14), width=20, bd=5,
                      command=open_acn)
    open_btn.place(relx=0.03, rely=0.08)


    view_btn = Button(frm, text='View Account', bg='orange', fg='white', font=('Arial', 14), width=20, bd=5,command=view_acn)
    view_btn.place(relx=0.39, rely=0.08)

    delete_btn = Button(frm, text='Delete Account', bg='black', fg='white', font=('Arial', 14), width=20, bd=5,command=delete_acn)
    delete_btn.place(relx=0.80, rely=0.08)



    logout_btn = Button(frm, text='Logout', bg='red', fg='white', font=('Arial', 14), width=20, bd=5,
                        command=logout)
    logout_btn.place(relx=0.39, rely=0.91)




def forgot_screen():

    def back():
        frm.destroy()  # destroy the frame to clear the screen and call the main screen function again, this fun pass in command of back_btn
        main_screen()

        
    frm=Frame(root)  # create a frame for the main screen -------------------------
    # frm.place(relx=0.25,rely=.18,)  # place the frame in the window
    frm.place(relx=0.22, rely=0.18, relwidth=0.6,relheight=.7) # set the size of the frame to occupy 50% of the width and almost 50% of the height of the window
    frm.configure(bg='white')

    global send_otp  # declare the send_otp function as global to access it in the send_otp button command
    def send_otp():
        print("Send OTP button clicked")  # Debug line
        uacn=acn_no_entry.get().strip()
        umail=mail_entry.get().strip()
        ucap=enter_cap_inentry.get()
        if ucap!= forgot_captcha:  # check if the entered captcha matches the generated captcha
            messagebox.showerror('Forgot Password','Invalid Captcha')  # show an error message if the captcha is invalid
            return


        # aunthentication acount number and email
        conobj=sqlite3.connect(database='bank.sqlite')  # connect to the database
        curobj=conobj.cursor()  # create a cursor object to execute SQL queries
        query = "select * from accounts where accounts_acno=? and accounts_email=?"
        curobj.execute(query,(uacn,umail))  # execute the query to check if the account number and email match
        
        tup=curobj.fetchone()  # fetch the result of the query
        curobj.close()
        if tup==None:
            messagebox.showerror('Forgot Password','Invalid Account Number or Email')  # show an error message if the account number or email is invalid
        else:
            # if the account number and email match, generate a random OTP
            otp = str(random.randint(1000,9999))
            project_mails.send_otp_mail(umail,tup[0],otp)
            messagebox.showinfo('OTP sent tp given/registered mail id')

            otp_entry=Entry(frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the password
            otp_entry.place(relx=.45,rely=.70)

            def verify():
                uotp=otp_entry.get()
                if otp==uotp:  # check if the entered OTP matches the generated OTP
                    messagebox.showinfo('Forgot Password',f'Your password:{tup[3]}')  # show the password in a message box
                    otp_entry.destroy()  # destroy the OTP entry field after verification
                    verify_btn.destroy()  # destroy the verify button after verification
                else:
                    messagebox.showerror('Forgot Password','Invalid OTP')

            

            verify_btn=Button(frm,text='Verify OTP',bg='gray',fg='white',font=('arial',15),bd=5,command=verify)
            verify_btn.place(relx=.45,rely=.75)

        
        






        # Here you can add the functionality for forgot password screen

    back_btn = Button(frm, text='back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=back)
    back_btn.place(relx=0, rely=0)


    acn_lbl=Label(frm,text='ACN',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
    acn_lbl.place(relx=.17,rely=.22)
    # create an entry field for the account number
    acn_no_entry=Entry(frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
    acn_no_entry.place(relx=.45,rely=.22)  # place the entry field in the center of the frame
    acn_no_entry.focus()



    mail_lbl=Label(frm,text='Mail',fg='black',font=('Arial',15,"bold"))  # create a label for the account number
    mail_lbl.place(relx=.17,rely=.35)
    # create an entry field for the account number
    mail_entry=Entry(frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the account number
    mail_entry.place(relx=.45,rely=.35)  # place the entry field in the center of the frame
    mail_entry.focus()


    global captcha_lbl  # declare the captcha_lbl variable as global to access it in the refresh function
    forgot_captcha=random_captcha()
    # create a label for the captcha
    captcha_lbl =Label(frm,text=random_captcha(),fg='white',bg='black',font=('Arial',15,"bold"))
    captcha_lbl.place(relx=.45,rely=.46)

    # create refresh button to refresh captcha
    refresh_button=Button(frm,text='refresh',bg='red',fg='white',command=refresh)
    refresh_button.place(relx=.53,rely=.46)


    entercap_lbl=Label(frm,text='Captcha',fg='black',font=('Arial',15,"bold"))  
    entercap_lbl.place(relx=.16,rely=.52)  

    # create captcha entry field
    enter_cap_inentry=Entry(frm,font=('Arial',15,""),width=20,bd=5)  # create an entry field for the password
    enter_cap_inentry.place(relx=.45,rely=.52)


    # create send OTP button -----------------------
    otp_btn=Button(frm,command=send_otp,text='Send OTP',bg='gray',fg='white',font=('arial',15),bd=5)
    otp_btn.place(relx=.45,rely=.63)  # create a button for login and place it in the center of the frame

    # create reset button to reset details ----------------------
    reset_btn=Button(frm,text='Reset',bg='gray',fg='white',font=('arial',15),bd=5)
    reset_btn.place(relx=.30,rely=.63)




def user_screen(uacn=None):
        user_frm = Frame(root, bg='gray',highlightbackground='black', highlightthickness=2)
        user_frm.place(relx=0.14, rely=0.18, relwidth=0.7, relheight=0.7)

        # Define user_frm2 as a global variable so it can be accessed in logout_for_user
        global user_frm2
        user_frm2 = Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
        user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

        def logout_for_user():
            resp = messagebox.askyesno("Logout", "Do you want to logout?")
            if resp:
                user_frm.destroy()
                user_frm2.destroy()
                main_screen()


        
        # here we create the user screen with all the buttons for user operations

    
        def chk_details_btn_screen():

            global user_frm2
            try:
                user_frm2.destroy()
            except:
                pass


            user_frm2 = Frame(root, bg='white', highlightbackground='black', highlightthickness=2)
            user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

            title_lbl = Label(user_frm2, text='Fill the details to view account', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)
            back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5, command=user_screen)
            back_btn.place(relx=0, rely=0)

            conobj = sqlite3.connect('bank.sqlite')
            curobj = conobj.cursor()
            curobj.execute('select * from accounts where accounts_acno=?', (uacn,))
            tup = curobj.fetchone()
            conobj.close()
            details=f'''Account No. = {tup[0]}

            Opening Date = {tup[7]}

            Availabale Bal = {tup[9]}

            Email Id = {tup[4]}

            Mob No. = {tup[5]}
'''
            details_lbl = Label(user_frm2, text=details, bg='white', font=('Arial', 14), fg='black')
            details_lbl.pack(pady=10)








         
#         def chk_details_btn_screen():
#             user_frm2 =Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
#             user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

#             title_lbl=Label(user_frm2,text='Fill the details to view account', bg='white', font=('Arial', 14, "bold"), fg='purple')
#             title_lbl.pack(pady=10)
#             back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=user_screen)
#             back_btn.place(relx=0, rely=0)

#             conobj=sqlite3.connect('bank.sqlite')
#             curobj=conobj.cursor()
#             curobj.execute('select * from accounts where accounts_acno=?',(int(uacn),))
#             tup=curobj.fetchone()
#             conobj.close()

#             chk_details_btn_details =f'''Account No : {tup[0]}

# Opening Date : {tup[7]}

# Available Bal : {tup[9]}

# Email ID : {tup[4]}

# Mob No : {tup[5]}
# '''
#             chk_details_btn_details_lbl=Label(user_frm2,text=chk_details_btn_details,bg='white',fg='black',font=('arial',20,'bold'))
#             chk_details_btn_details_lbl.place(relx=.2,rely=.2)
            


        
        def deposit_btn_screen():

            def deposit():
                uamt = float(amt_entry.get())
                conobj = sqlite3.connect(database='bank.sqlite')
                curobj = conobj.cursor()
                curobj.execute("SELECT accounts_bal FROM accounts WHERE accounts_acno=?", (uacn,))
                result = curobj.fetchone()
                if result:
                    ubal = result[0]
                    curobj.execute("UPDATE accounts SET accounts_bal=accounts_bal+? WHERE accounts_acno=?", (uamt, uacn))
                    t = str(time.time())
                    utxnid = 'DP' + t[:t.index('.')]
                    curobj.execute(
                        "INSERT INTO stmts VALUES (?,?,?,?,?,?)",
                        (utxnid, uacn, uamt, 'CR', time.strftime("%d-%m-%Y %r"), ubal + uamt)
                    )
                    conobj.commit()
                    messagebox.showinfo('Deposit', f'{uamt} Amount Deposited')
                    user_frm2.destroy()
                    user_screen(uacn)
                else:
                    messagebox.showerror('Deposit', 'Account not found')
                conobj.close()





            user_frm2 =Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
            user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

            title_lbl=Label(user_frm2,text='Fill the details to deposit money', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)
            back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=user_screen)
            back_btn.place(relx=0, rely=0)

            amt_lbl=Label(user_frm2,text='Amount', bg='white', font=('Arial', 14, "bold"), fg='purple')
            amt_lbl.place(relx=.3,rely=.2)
            amt_entry=Entry(user_frm2,font=('Arial',14),bd=5)
            amt_entry.place(relx=.45,rely=.2)
            amt_entry.focus()
            dep_btn = Button(user_frm2, text='deposit', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=deposit)
            dep_btn.place(relx=0.45, rely=.4)





        def withdraw_btn_screen():

            
            def withdraw():
                uamt = float(amt_entry.get())
                conobj = sqlite3.connect(database='bank.sqlite')
                curobj = conobj.cursor()
                curobj.execute("SELECT accounts_bal FROM accounts WHERE accounts_acno=?", (uacn,))
                result = curobj.fetchone()
                if result:
                    ubal = result[0]
                    if ubal >= uamt:
                        # Update balance
                        curobj.execute("UPDATE accounts SET accounts_bal=accounts_bal-? WHERE accounts_acno=?", (uamt, uacn))
                        # Insert statement
                        t = str(time.time())
                        utxnid = 'WD' + t[:t.index('.')]
                        curobj.execute(
                            "INSERT INTO stmts VALUES (?, ?, ?, ?, ?, ?)",
                            (utxnid, uacn, uamt, 'WD', time.strftime("%d-%m-%Y %r"), ubal - uamt)
                        )
                        conobj.commit()
                        messagebox.showinfo('Withdraw', f'{uamt} Amount Withdrawn')
                        user_frm2.destroy()
                        user_screen(uacn)
                    else:
                        messagebox.showerror('Withdraw', f'Insufficient Balance: {ubal}')
                else:
                    messagebox.showerror('Withdraw', 'Account not found')
                conobj.close()

            user_frm2 =Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
            user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

            title_lbl=Label(user_frm2,text='Fill the details to withdraw money', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)
            back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=user_screen)
            back_btn.place(relx=0, rely=0)



            amt_lbl=Label(user_frm2,text='Amount', bg='white', font=('Arial', 14, "bold"), fg='purple')
            amt_lbl.place(relx=.3,rely=.2)
            amt_entry=Entry(user_frm2,font=('Arial',14),bd=5)
            amt_entry.place(relx=.45,rely=.2)
            amt_entry.focus()
            widr_btn = Button(user_frm2, text='withdraw', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=withdraw)
            widr_btn.place(relx=0.45, rely=.4)

                




            

        def updateprofile_btn_screen():
            user_frm2 =Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
            user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

            title_lbl=Label(user_frm2,text='Fill the details to update your profile', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)
            back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=user_screen)
            back_btn.place(relx=0, rely=0)








        def transfer_btn_screen():
            user_frm2 =Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
            user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

            title_lbl=Label(user_frm2,text='Fill the details to transfer money', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)
            back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=user_screen)
            back_btn.place(relx=0, rely=0)

        def history_btn_screen():
            from tktable import Table
            user_frm2 =Frame(root, bg='white',highlightbackground='black', highlightthickness=2)
            user_frm2.place(relx=0.35, rely=0.18, relwidth=0.5, relheight=0.7)

            title_lbl=Label(user_frm2,text='Fill the details to view history', bg='white', font=('Arial', 14, "bold"), fg='purple')
            title_lbl.pack(pady=10)
            back_btn = Button(user_frm2, text='Back', bg='black', fg='white', font=('Arial', 14), width=7, bd=5,command=user_screen)
            back_btn.place(relx=0, rely=0)

            
            import tktable
            table_headers = ("Txn ID", "Amount","Txn Type","Updated Bal","Date")
            mytable = tktable.Table(user_frm2, table_headers, col_width=150, headings_bold=True)
            mytable.pack(pady=10)
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            query='select stmts_txnid,stmts_amt,stmts_type,stmts_update_bal,stmts_date from stmts where stmts_acn=?'
            curobj.execute(query,(uacn,))
            for tup in curobj:
                mytable.insert_row(tup)
            conobj.close()
            import sys
            del sys.modules['tktable']

            

        def getdetail():
            conobj = sqlite3.connect(database='bank.sqlite')
            curobj = conobj.cursor()
            query = 'select * from accounts where accounts_acno=?'
            curobj.execute(query, (uacn,))
            tup = curobj.fetchone()
            conobj.close()
            return tup



        def update_profile():
            path = filedialog.askopenfilename()
            if not path:
                return  # User cancelled, do nothing

            shutil.copy(path, f'image/{uacn}.png')

            profile_img = Image.open(f'image/{uacn}.png').resize((200, 170))     # open the image and resize it to 300x150 pixels
            profile_img_bitmap = ImageTk.PhotoImage(profile_img, master=user_frm)    # convert the image to a format that can be used in tkinter, it returns bit_image
            profile_logo_lbl.image = profile_img_bitmap
            profile_logo_lbl.configure(image=profile_img_bitmap)  # keep a reference to the image to prevent it from being garbage collected
        
        

        


        
        details = getdetail()
        if details:
            welcome_text = f"Welcome, {details[1]} {details[2]}"
        else:
            welcome_text = "Welcome, User"

        user_lbl = Label(user_frm, text=welcome_text, fg='Orange', font=('Arial', 15, "bold"), bg='gray')
        user_lbl.place(relx=0.03, rely=0.35)

        if os.path.exists(f'image/{uacn}.png'):
            path = f'image/{uacn}.png'
        else:
            path = r"C:/Users/Aditya Sharma/Desktop/DUCAT/SQL/SQL 26 SQlite Project_class_1/image/user.jpg"

        profile_img = Image.open(path).resize((200, 170))     # open the image and resize it to 300x150 pixels
        profile_img_bitmap = ImageTk.PhotoImage(profile_img, master=user_frm)    # convert the image to a format that can be used in tkinter, it returns bit_image
        profile_logo_lbl = Label(user_frm, image=profile_img_bitmap)  # create a label for the image
        profile_logo_lbl.image = profile_img_bitmap  # keep a reference to the image to prevent it from being garbage collected
        profile_logo_lbl.place(relx=0.05, rely=0.01)       

        chk_details_btn = Button(user_frm2, text='Check Details', bg='yellow', fg='black', font=('Arial', 14), width=20, bd=5,command=chk_details_btn_screen)
        chk_details_btn.place(relx=0.30, rely=0.09)
        

        deposit_btn = Button(user_frm2, text='Deposit', bg='green', fg='black', font=('Arial', 14), width=20, bd=5,command=deposit_btn_screen)
        deposit_btn.place(relx=0.30, rely=0.19)

        withdraw_btn = Button(user_frm2, text='Withdraw', bg='pink', fg='black', font=('Arial', 14), width=20, bd=5,command=withdraw_btn_screen)
        withdraw_btn.place(relx=0.30, rely=0.29)

        updprofile_btn = Button(user_frm2, text='Update Profile', bg='sky blue', fg='black', font=('Arial', 14), width=20, bd=5,command=update_profile)
        updprofile_btn.place(relx=0.30, rely=0.39)

        transfer_btn = Button(user_frm2, text='transfer', bg='sky blue', fg='black', font=('Arial', 14), width=20, bd=5,command=transfer_btn_screen)
        transfer_btn.place(relx=0.30, rely=0.49)

        history_btn = Button(user_frm2, text='History', bg='sky blue', fg='black', font=('Arial', 14), width=20, bd=5,command=history_btn_screen)
        history_btn.place(relx=0.30, rely=0.59)
        


        logout_btn = Button(user_frm2, text='Logout', bg='red', fg='white', font=('Arial', 14), width=20, bd=5,
                        command=logout_for_user)
        logout_btn.place(relx=0.30, rely=0.91)  

    


        



        # user_frm2}

        # user_frm{
      





main_screen()





root.mainloop()  # run the main loop of the window for visable

# inner frame}


# proj=8 45:05
# withdraw btn not working
