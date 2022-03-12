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
email_name
email_users