import pandas as pd
import re
df=pd.read_csv(r'C:\Users\GGMU\Desktop\Data Engineer\TEST\March12FinalTest\intelligentGuessing\intelligentGuessingDataSet',encoding='latin-1')
df=df.set_index('rownum')
firstname=df.columns.get_loc('firstname')
d_firstname=df.iloc[:,firstname:firstname+1]
d_firstname
lastname=df.columns.get_loc('lastname')
d_lastname=df.iloc[:,lastname:lastname+1]
d_lastname
email=df.columns.get_loc('email')
d_email=df.iloc[:,email:email+1]
d_email
pattern=df.columns.get_loc('Email Pattern')
d_Pattern=df.iloc[:,pattern:pattern+1]
d_Pattern
h = re.findall('[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*', str(df))
email_users = [ x.split('@')[0] for x in h ]
email_name=[x.split('.')[0] for x in email_users]
if d_firstname == email_name[0] and d_lastname == email_name[1] or d_firstname == '' and d_lastname == email_name[1]:
    pattern = ''.join([pattern, '<11>','<22>'])
elif d_firstname == email_name[0] and d_lastname.replace(" ","") == email_name[1] or d_firstname == '' and d_lastname.replace(" ","") == email_name[1]:
    pattern = ''.join([pattern, '<11>','<20><21>'])
elif d_lastname:
    if d_firstname == email_name[0] and d_lastname.split(' ')[0] == email_name[1]:
        pattern = ''.join([pattern, '<11>','<20>'])
    elif d_firstname == email_name[0] and d_lastname.split(' ')[1] == email_name[1]:
        pattern = ''.join([pattern, '<11>','<21>'])
elif d_firstname == email_name[0] and d_lastname == '' and email_name[1] in lastname:
    pattern = ''.join([pattern, '<11>','<20><21>'])
else:
    print('error')
