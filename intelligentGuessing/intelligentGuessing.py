import pandas as pd
import re
df=pd.read_csv(r'C:\Users\GGMU\Desktop\Data Engineer\TEST\March12FinalTest\intelligentGuessing\intelligentGuessingDataSet',encoding='latin-1')
df=df.set_index('rownum')
print(df)
h = re.findall('[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*', str(df))
email_users = [ x.split('@')[0] for x in h ]
email_name=[x.split('.')[0] for x in email_users]
