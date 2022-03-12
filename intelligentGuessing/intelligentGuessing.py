import pandas as pd
import re
data=[]
df=pd.read_csv(r'C:\Users\GGMU\Desktop\Data Engineer\TEST\March12FinalTest\intelligentGuessing\intelligentGuessingDataSet',encoding='latin-1')
df=df.set_index('rownum')
for i in range(20,53):
    firstname=df.columns.get_loc('firstname')
    d_firstname=df.iloc[:,firstname:firstname+1]
    lastname=df.columns.get_loc('lastname')
    d_lastname=df.iloc[:,lastname:lastname+1]
    email=df.columns.get_loc('email')
    d_email=df.iloc[:,email:email+1]
    pattern=df.columns.get_loc('Email Pattern')
    d_Pattern=df.iloc[:,pattern:pattern+1]
    h = re.findall('[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*', str(df))
    email_users = [ x.split('@')[0] for x in h ]
    email_name=[x.split('.')[0] for x in email_users]
    if email_name==d_firstname:
            df.loc[i,"Email Pattern"]='<11>'
    if email_name==d_lastname:
            df.loc[i,"Email Pattern"]='<22>'
    if len(str(d_lastname).split())>1:
    if str(email_name)==str(d_firstname)[0]+'.'+str(str(d_lastname).split()[1]):
            df.loc[i,"Email Pattern"]='<1>.<21>'
        
        if str(email_name)==str(d_firstname)+'.'+str(str(d_lastname).split()[1]):
            df.loc[i,"Email Pattern"]='<11>.<21>'
            
        if str(email_name)==str(d_firstname)[0]+'.'+str(str(d_lastname).split()[0]):
            df.loc[i,"Email Pattern"]='<1>.<20>'
        
        if str(email_name)==str(d_firstname)+'-'+str(str(d_lastname).split()[0]):
            df.loc[i,"Email Pattern"]='<11-<20>'
        
        if str(email_name)==str(d_firstname)[0]+str(remove_spaces(str(d_lastname))):
            df.loc[i,"Email Pattern"]='<1><20><21>'
            
        if str(email_name)==str(d_firstname)+'.'+str(remove_spaces(str(d_lastname))):
            df.loc[i,"Email Pattern"]='<11>.<20><21>'
        
            
        d_lastnameupdated=str(d_lastname).split()
        if str(email_name)==str(d_firstname)+'.'+d_lastnameupdated[0]+"-"+ d_lastnameupdated[1]:
            df.loc[i,"Email Pattern"]='<11>.<20>-<21>'
        if str(email_name)==str(d_firstname)+d_lastnameupdated[0]+"."+ d_lastnameupdated[1]:
            df.loc[i,"Email Pattern"]='<11><20>.<21>'
            
            
        if str(email_name)==str(d_firstname)+'.'+d_lastnameupdated[0]+ d_lastnameupdated[1][0:6]:
            df.loc[i,"Email Pattern"]='<11>.<20><21-l6|>'
        
        
        
        
    else:
        if str(email_name)==str(d_firstname)[0]+'.'+str(d_lastname):
            df.loc[i,"Email Pattern"]='<1>.<22>'
            
        if str(email_name)==str(d_firstname)[0]+str(d_lastname):
            df.loc[i,"Email Pattern"]='<1><22>'
            
        if str(email_name)==str(d_firstname)+'.'+str(d_lastname):
            df.loc[i,"Email Pattern"]='<11>.<22>'
        
            
    #For <11>,<22>:
    if str(email_name)==str(d_firstname)+'.'+str(d_lastname):
        df.loc[i,"Email Pattern"]='<11>.<22>'
        
    #For <1-f31>_<22>:
    if str(email_name)==str(d_firstname)[0:3]+"_"+ str(d_lastname):
        df.iloc[i,"Email Pattern"]='<11-f3|>_<22>'
        
    #For <1-f21>_<22>:
    if str(email_name)==str(d_firstname)[0:2]+"_"+ str(d_lastname):
        df.iloc[i,"Email Pattern"]='<11-f2|>_<22>'
     
    if len(str(d_lastname).split("'"))>1:
        d_lastnamesplitted = str(d_lastname).split("'")
        if  str(email_name)==str(d_firstname)[0:4]+"."+d_lastnamesplitted[0]+d_lastnamesplitted[1]:
            df.loc[i, "Email Pattern"] = '<11-f4|>.<20><21>'
            
    if len(str(d_lastname).split("'"))>1:
        d_lastnamesplitted = str(d_lastname).split("'")
        if  str(email_name)==str(d_firstname)+"."+d_lastnamesplitted[0]+d_lastnamesplitted[1].split(' ')[0]:
            df.loc[i, "Email Pattern"] = '<11>.<20><23>'
    
    if len(str(d_firstname).split("-"))>1:
        fnamesplitted = str(d_firstname).split('-')
        if  str(email_name)==fnamesplitted[0]+fnamesplitted[1]+"."+str(d_lastname):
            df.loc[i, "Email Pattern"] = '<10><11>.<22>'
            

print(df)
df = pd.DataFrame([pattern])
data.append(df)
df = pd.concat(data)
df.to_csv("problemset1_submission.csv", index=False)
