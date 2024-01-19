# Python program to show pyplot module 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='password',database='revature')

inflation_id=[]
inflation_name=[]
c=db.cursor()
st='''select * from inflation_type'''
c.execute(st)
res=c.fetchall()
for i in res:
    inflation_id.append(i[0])
    inflation_name.append(i[1])
country_name=[]
country_code=[]
country_id=[]
c=db.cursor()
st='''select * from country'''
c.execute(st)
res=c.fetchall()
for i in res:
    country_id.append(i[0])
    country_code.append(i[1])
    country_name.append(i[2])
def show_country_all_years():
    n=int(input('Enter Country code to show all years inflation types:: '))
    while n  in country_code:
        n=int(input('Enter  Correct Country code to show all years inflation types:: '))
    try:
        c=db.cursor()
        st='''select * from inflation_rate where country_id={}'''.format(n)
        c.execute(st)
        res=c.fetchall()
        l=[]
        for i in res:
            l.append(i[2:])
        data=[]
        count=0
        for i in l:
            a=[]
            a.append(inflation_name[count])
            count+=1
            a.extend(i)
            data.append(a)
        col=['Inflation Type']
        for i in range(2001,2023):
            col.append(str(i))
        df=pd.DataFrame(data,columns=col)
        df.plot(x='Inflation Type',y=col[1:],kind='bar',title='{} country inflation rate from year::{} to year::{}'.format(country_name[n-1],2001,2022))
        plt.show()
        return 1
    except Exception as e:
        return e
def show_country_particular_years():
    n=int(input('Enter Country code to show all years inflation types:: '))
    while n  in country_code:
        n=int(input('Enter  Correct Country code to show all years inflation types:: '))
    startyear=int(input('Enter starting year in range 2001-2022:: '))
    while startyear<2000 or startyear>2022:
        startyear=int(input('Enter correct starting year in range 2001-2022:: '))
    endyear=int(input('Enter end year in range 2001-2022:: '))
    while endyear<2000 or endyear>2022:
        endyear=int(input('Enter correct end year in range 2001-2022:: '))
    try:
        c=db.cursor()
        st='''select * from inflation_rate where country_id={}'''.format(n)
        c.execute(st)
        res=c.fetchall()
        l=[]
        e1=startyear%1999
        e2=endyear%1999+1
        for i in res:
            l.append(i[e1:e2])
        data=[]
        count=0
        for i in l:
            a=[]
            a.append(inflation_name[count])
            count+=1
            a.extend(i)
            data.append(a)
        col=['Inflation Type']
        for i in range(startyear,endyear+1):
            col.append(str(i))
        df=pd.DataFrame(data,columns=col)
        df.plot(x='Inflation Type',y=col[1:],kind='bar',title='{} country inflation rate from year::{} to year::{}'.format(country_name[n-1],startyear,endyear))
        plt.show()
        return 1
    except Exception as e:
        return e

def compare_countries():
    n1=int(input('Enter one country id:: '))
    while n1 in country_code:
        n1=int(input('Enter correct one country id:: '))
    n2=int(input('Enter second country id:: '))
    while n2 in country_code:
        n2=int(input('Enter correct second country id:: '))
    year=int(input('Enter  year in range 2001-2022:: '))
    while year<2000 or year>2022:
        year=int(input('Enter correct  year in range 2001-2022:: '))
    try:
        c=db.cursor()
        st='''select * from inflation_rate where country_id={}'''.format(n1)
        c.execute(st)
        res1=c.fetchall()
        l1=[]
        year=year%1999
        for i in res1:
            l1.append(year)
        
        c=db.cursor()
        st='''select * from inflation_rate where country_id={}'''.format(n2)
        c.execute(st)
        res2=c.fetchall()
        l2=[]
        for i in res2:
            l2.append(i[year])
        df1=pd.DataFrame({
            country_name[n1-1]:l1,
            country_name[n2-1]:l2
        })
        df2=pd.DataFrame({
            'Inflation Type':inflation_name,
            'year':[year+1999]*len(inflation_name)
        })
        ax=df1.plot(x=country_name[n1-1],y=country_name[n2-1])
        df2.plot(ax=ax,x='Inflation Type',y='year')
        plt.show()
        return 1
    except Exception as e:
        return e
    
def compare_avg():
    n=int(input('Enter inflation id:: '))
    while n not in range(len(inflation_name)):
        n=int(input('Enter correct inflation id:: '))
    try:
        c=db.cursor()
        st='''select * from inflation_rate where inflation_id={}'''.format(n)
        c.execute(st)
        res=c.fetchall()
        #print(res)
        l1=[]
        for i in res:
            l1.append(sum(i[2:])//len(i))
        #print('l1 is:: ',l1,'country_name length is:: ',len(country_name))
        #print('length of l1 is:: ',len(l1))
        df=pd.DataFrame({
            'country_name':country_name,
            'avg values':l1
        })
        df.plot(x='country_name',y='avg values',kind='bar',title='avg values for inflation type {} of all countries'.format(inflation_name[n-1]))
        plt.show()
        return 1
    except Exception as e:
        return e
def find_max_min():
    pass



#show_country_all_years()
#show_country_particular_years() 
#compare_countries()  
#compare_avg()
    