import pandas as pd
df=pd.read_csv(r'C:\Users\GGMU\Desktop\Data Engineer\TEST\March12FinalTest\intelligentGuessing\intelligentGuessingDataSet',encoding='latin-1')
print(df)

def remove_spaces(a):
    if "'" in a:
        a=a.split("' ")
        b=''
        for i in a:
            b=b+i
        return b
    
    a=a.split()
    b=''
    for i in a:
        b=b+i
    return b

for i in range(20,53):
    fname=df.loc[i,"firstname"]
    lname=df.loc[i,"lastname"]
    email_content=df.loc[i,"email"]
    email_content=email_content.split("@")[0]
    
    #For <11>:
    if email_content==fname:
        df.loc[i,"Email Pattern"]='<11>'
    
    #For <22>:
    if email_content==lname:
        df.loc[i,"Email Pattern"]='<22>'
        
    #For <1>.<21> ,<1>.<22> ,<1><22>,<1><20><21>:
    if len(str(lname).split())>1:
        
        if str(email_content)==str(fname)[0]+'.'+str(str(lname).split()[1]):
            df.loc[i,"Email Pattern"]='<1>.<21>'
        
        if str(email_content)==str(fname)+'.'+str(str(lname).split()[1]):
            df.loc[i,"Email Pattern"]='<11>.<21>'
            
        if str(email_content)==str(fname)[0]+'.'+str(str(lname).split()[0]):
            df.loc[i,"Email Pattern"]='<1>.<20>'
        
        if str(email_content)==str(fname)+'-'+str(str(lname).split()[0]):
            df.loc[i,"Email Pattern"]='<11-<20>'
        
        if str(email_content)==str(fname)[0]+str(remove_spaces(str(lname))):
            df.loc[i,"Email Pattern"]='<1><20><21>'
            
        if str(email_content)==str(fname)+'.'+str(remove_spaces(str(lname))):
            df.loc[i,"Email Pattern"]='<11>.<20><21>'
        
            
        lnameupdated=str(lname).split()
        if str(email_content)==str(fname)+'.'+lnameupdated[0]+"-"+ lnameupdated[1]:
            df.loc[i,"Email Pattern"]='<11>.<20>-<21>'
        if str(email_content)==str(fname)+lnameupdated[0]+"."+ lnameupdated[1]:
            df.loc[i,"Email Pattern"]='<11><20>.<21>'
            
            
        if str(email_content)==str(fname)+'.'+lnameupdated[0]+ lnameupdated[1][0:6]:
            df.loc[i,"Email Pattern"]='<11>.<20><21-l6|>'
        
        
        
        
    else:
        if str(email_content)==str(fname)[0]+'.'+str(lname):
            df.loc[i,"Email Pattern"]='<1>.<22>'
            
        if str(email_content)==str(fname)[0]+str(lname):
            df.loc[i,"Email Pattern"]='<1><22>'
            
        if str(email_content)==str(fname)+'.'+str(lname):
            df.loc[i,"Email Pattern"]='<11>.<22>'
        
            
    #For <11>,<22>:
    if str(email_content)==str(fname)+'.'+str(lname):
        df.loc[i,"Email Pattern"]='<11>.<22>'
        
    #For <1-f31>_<22>:
    if str(email_content)==str(fname)[0:3]+"_"+ str(lname):
        df.iloc[i,"Email Pattern"]='<11-f3|>_<22>'
        
    #For <1-f21>_<22>:
    if str(email_content)==str(fname)[0:2]+"_"+ str(lname):
        df.iloc[i,"Email Pattern"]='<11-f2|>_<22>'
     
    if len(str(lname).split("'"))>1:
        lnamesplitted = str(lname).split("'")
        if  str(email_content)==str(fname)[0:4]+"."+lnamesplitted[0]+lnamesplitted[1]:
            df.loc[i, "Email Pattern"] = '<11-f4|>.<20><21>'
            
    if len(str(lname).split("'"))>1:
        lnamesplitted = str(lname).split("'")
        if  str(email_content)==str(fname)+"."+lnamesplitted[0]+lnamesplitted[1].split(' ')[0]:
            df.loc[i, "Email Pattern"] = '<11>.<20><23>'
    
    if len(str(fname).split("-"))>1:
        fnamesplitted = str(fname).split('-')
        if  str(email_content)==fnamesplitted[0]+fnamesplitted[1]+"."+str(lname):
            df.loc[i, "Email Pattern"] = '<10><11>.<22>'
            

print(df)

df.to_csv('intelligentGuessing/problemset1_submission.csv')