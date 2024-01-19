import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='password',database='revature')
def register(name,password):
    print(name,password)
    try:
        st='''insert into user_login values(%s,%s)'''
        t=(name,password)
        c=db.cursor()
        c.execute(st,t)
        db.commit()
        return 1
    except:
        return 0
def login(name,password):
    try:
        st='''select password from user_login where username=%s '''
        c=db.cursor()
        c.execute(st,(name,))
        result=c.fetchall()
        #print(result[0][0])
        if result[0][0]==password:
            return 1
        else:
            return 0
    except:
        return 0
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
def print_country():
    return country_name
def print_country_id():
    return country_id
def print_country_code():
    return country_code

inflation_id=[]
inflation_name=[]
c=db.cursor()
st='''select * from inflation_type'''
c.execute(st)
res=c.fetchall()
for i in res:
    inflation_id.append(i[0])
    inflation_name.append(i[1])
def print_inflation_id():
    return inflation_id
def print_inflation_name():
    return inflation_name
def create_new_country():
    new_country_name=input('Enter new country name:: ')
    while new_country_name in country_name:
        new_country_name=input('Enter new country name which is not available in past:: ')
    new_country_id=int(input('Enter new country id:: '))
    while new_country_id in country_id:
        new_country_id=input('Enter new country id which is not available in past:: ')
    new_country_code=input('Enter new country code:: ')
    while new_country_code in country_code:
        new_country_code=input('Enter new country code which is not available in past:: ')
    try:
        c=db.cursor()
        st='''insert into country values(%s,%s,%s)'''
        t=(new_country_id,new_country_code,new_country_name)
        c.execute(st,t)
        db.commit()
        return 1
    except:
        return 0
def create_new_inflation_type():
    new_inflation_id=int(input('Enter new inflation id:: '))
    while new_inflation_id in inflation_id:
        new_inflation_id=int(input('Enter new inflation id which is not avaliable in  past:: '))
    new_inflation_name=input('Enter new inflation name:: ')
    while new_inflation_name in inflation_name:
        new_inflation_name=input('Enter new inflation id which is not avaliable in  past:: ')
    try:
        c=db.cursor()
        st='''insert into inflation_type values(%s,%s)'''
        t=(new_inflation_id,new_inflation_name)
        c.execute(st,t)
        db.commit()
        return 1
    except:
        return 0
def update_country():
    n=int(input('1.Press 1 to update country name \n 2.Press 2 to update country code:: '))
    if n==1:
        countryname=input('Enter old country name to update country name:: ')
        ind=country_name.index(countryname)
        newcountryname=input('Enter new country name:: ')
        while countryname==newcountryname or newcountryname in country_name:
            newcountryname=input('Enter new country name not same as old country name:: ')
        try:
            c=db.cursor()
            st='''update country set country_name='{}'  where country_id={} '''.format(newcountryname,ind+1)
            #print(st)
            c.execute(st)
            db.commit()
            return 1
        except:
            return 0
    elif n==2:
        countryname=input('Enter old country name to update country code:: ')
        ind=country_name.index(countryname)+1
        newcountrycode=input('Enter new country code:: ')
        while countryname==newcountrycode or newcountrycode in country_name:
            newcountrycode=input('Enter new country code not same as old country code:: ')
        try:
            c=db.cursor()
            st='''update country set country_code='{}'  where country_id={} '''.format(newcountrycode,ind)
            #print(st)
            c.execute(st)
            db.commit()
            print('sucess')
            return 1
        except:
            print('failure')
            return 0

def update_inflation_type():
    oldinflationtype=input('Enter old inflation type:: ')
    newinflationtype=input('ENter new inflation type:: ')
    while oldinflationtype==newinflationtype or newinflationtype in inflation_name:
        newinflationtype=input('ENter new inflation type not present in inflation name:: ')
    ind=inflation_name.index(oldinflationtype)+1
    try:
        c=db.cursor()
        st='''update inflation_type set inflation_name='{}' where inflation_id={}'''.format(newinflationtype,ind)
        c.execute(st)
        db.commit()
        return 1
    except:
        return 0
def update_inflation_rate():
    countryname=input('Enter country name:: ')
    inflationtype=input('Enter Inflation type:: ')
    year=int(input('Enter year to change inflation rate in range between 2001-2022:: '))
    while countryname not in country_name:
        countryname=input('Enter country name present in database:: ')
    while inflationtype not in inflation_name:
        inflationtype=input('Enter inflation name present in database:: ')
    while year<2000 or year>2022:
        year=int(input('Enter year to change inflation rate in range between 2001-2022:: '))
    newinflationrate=float(input('Enter new inflation rate'))
    ind1=country_name.index(countryname)+1
    ind2=inflation_name.index(inflationtype)+1
    try:
        c=db.cursor()
        st='''update inflation_rate set {}={} where country_id={} and inflation_id={}'''.format('y'+str(year),newinflationrate,ind1,ind2)
        print(st)
        c.execute(st)
        db.commit()
        print('success')
    except:
        print('failed')
def read_country():
    countryname=input('Enter country name:: ')
    ind=country_name.index(countryname)+1
    try:
        c=db.cursor()
        st='''select inf.inflation_name,inf1.y2001,inf1.y2002,inf1.y2003,inf1.y2004,inf1.y2005,inf1.y2006,inf1.y2007,inf1.y2008,inf1.y2009,inf1.y2010,inf1.y2011,inf1.y2012,inf1.y2013,inf1.y2014,inf1.y2015,inf1.y2016,inf1.y2017,inf1.y2018,inf1.y2019,inf1.y2020,inf1.y2021,inf1.y2022 from inflation_type inf,inflation_rate inf1 where inf.inflation_id=inf1.inflation_id and country_id={}'''.format(ind)
        c.execute(st)
        res=c.fetchall()
        return res
    except:
        return 0
def delete():
    try:
        print('1.Press 1 to delete country')
        print('2.Press 2 to delete inflation type:: ',end=' ')
        h=int(input())
        if h==1:
            c=db.cursor()
            cid=int(input('Enter country id:: '))
            while cid not in country_id:
                cid=int(input('Enter correct country id:: '))
            st='''delete from inflation_rate where country_id={}'''.format(cid)
            c.execute(st)
            db.commit()
            st='''delete from country where country_id={}'''.format(cid)
            c=db.cursor()
            c.execute(st)
            db.commit
            return 1
        elif h==2:
            c=db.cursor()
            cid=int(input('Enter inflation type id:: '))
            while cid not in inflation_id:
                cid=int(input('Enter correct inflation type id id:: '))
            st='''delete from inflation_rate where country_id={}'''.format(cid)
            c.execute(st)
            db.commit()
            st='''delete from inflation_type where inflation_id={}'''.format(cid)
            c.execute(st)
            return 1
        else:
            print('Enter correct value')
    except Exception as e:
        return e


    





    



    
