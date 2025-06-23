import gmail
mail='xxxxxxxxxxxxxxxxxxx'            #enter mail id
passw='xxxxxxxxxxxxxxxxxx'            #enter password after 2 step varification


def send_mail(to_mail,uacno,ufname,upass,udate):#(body)

        
        con=gmail.GMail(mail,passw)
        sub= 'Account Opened with ABC Bank'
        body=f"""Dear {ufname},
        Your account has been successfully opened with ABC Bank.
        Your account number is {uacno}
        Your password is {upass}
        Open date is {udate}
        Kindly change your password after logging in for the first time.
        Thank you for choosing ABC Bank.
        """
        msg=gmail.Message(to=to_mail,subject=sub,text=body)
        con.send(msg)



def send_otp_mail(to_mail,ufname,uotp):
    con=gmail.GMail('adityasharma51123@gmail.com','gaee wknt mgpx yjtd')
    sub='OTP for password recovery'
    body=f"""Dear {ufname},
        Your OTP to get password = {uotp}
   
    Kindly verify this otp to application 
    Thanks
    ABC Bank
    Noida
    """
    msg=gmail.Message(to=to_mail,subject=sub,text=body)
    con.send(msg)

# import yagmail

# def send_mail_for_openacn(email, fname, lname, password, opendate):
#     yag = yagmail.SMTP('your_email@gmail.com', 'your_password')
#     subject = "Your New Bank Account Details"
#     body = f"Dear {fname} {lname},\nYour account has been created.\nPassword: {password}\nOpen Date: {opendate}\n\nThank you!"
#     yag.send(email, subject, body)