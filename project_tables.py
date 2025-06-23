import sqlite3
conobj=sqlite3.connect(database='bank.sqlite')
curobj=conobj.cursor()

table1='''create table if not exists accounts(
accounts_acno integer primary key autoincrement,
accounts_fname text,
accounts_lname text,
accounts_pass text,
accounts_email text,
accounts_mob text,
accounts_gender text,
accounts_opendate text,
accounts_type text,
accounts_bal float)
'''



# ufname=fname_lbl_entry.get()
#             ulname=lname_lbl_entry.get()
#             uemail=Email_lbl_entry.get()
#             unumber=mob_lbl_entry.get()
#             ugender=gender_combo.get()
#             uacn_type=acn_type_combo.get()
#             ubal=0.0
#             uopendate=time.strftime('%d/%m/%Y')  # get the current date in the format of dd/mm/yyyy
#             upass=random_captcha()
    


table2 = '''create table if not exists stmts(
stmts_txnid text primary key,
stmts_acn integer,
stmts_amt float,
stmts_type text,
stmts_date text,
stmts_update_bal float,
foreign key(stmts_acn) references accounts(accounts_acno))
'''

try:
    curobj.execute(table1)
    curobj.execute(table2)
    print('table crrated')
except Exception as e:
    print(e)
conobj.close()


