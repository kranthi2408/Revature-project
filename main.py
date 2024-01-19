import service
import aop
while True:
    try:
        reg=int( input('1.Press 1 for register \n2.Press 2 for login:: '))
        while reg not in range(1,3):
            print('Enter correct value:: ')
            reg=int( input('1.Press 1 for register \n2.Press 2 for login:: '))
        
        break
    except ValueError:
        print('enter correct value')
if reg==1:
    while True:
        name=input('Enter Name:: ')
        password=input('Enter Password:: ')
        if service.register(name,password):
            print('Registered successfully')
            break
        else:
            print('Registration failed register once again')
elif reg==2:
    while True:
        name=input('Enter name:: ')
        password=input('Enter password:: ')
        if service.login(name,password):
            print('Login Success')
            break
        else:
            print('Login Failure Try Again')

country_name=service.print_country()
country_id=service.print_country_id()
country_code=service.print_country_code()
print('      COUNTRIES AVALAIBLE ARE AND THEIR CODES     ')
print('COUNTRY_ID COUNTRY_CODE COUNTRY_NAME')
for i in range(len(country_name)):
    print('{}             {}             {}'.format(country_id[i],country_code[i],country_name[i]))
inflation_id=service.print_inflation_id()
inflation_name=service.print_inflation_name()
print('INFLATION_ID       INFLATION_NAME')
for i in range(len(inflation_id)):
    print('{}          {}'.format(inflation_id[i],inflation_name[i]))
while True:
    print('1.Press 1 for CURD operations')
    print('2.Press 1 for additional operations on data')
    print('3.Press 3 for Exit:: ',end=' ')
    n=int(input())
    if n==1:
        print('1.Press 1 for creating')
        print('2.Press 2 for updating')
        print('3.Press 3 for reading')
        print('4.Press 4 for deleting:: ',end=' ')
        h=int(input())
        if h==1:
            print('1.Press 1 for creating new country')
            print('2.Press 2 for creating new inflation type:: ',end=' ')
            h1=int(input())
            if h1==1:
                if service.create_new_country():
                    print('SUccessfully added new country')
                else:
                    print('Failed in creating new country')
            elif h1==2:
                if service.create_new_inflation_type():
                    print('Succesfully added new inflation type')
                else:
                    print('failed in inserting new inflation type')
            else:
                print('Enter correct Input')
        elif h==2:
            print('1.press 1 for updating country related details')
            print('2.Press 2 for updating inflation type details')
            print('3.Press 3 for updating inflation rate details:: ',end=' ')
            h1=int(input())
            if h1==1:
                if service.update_country():
                    print('Successfully updated country name')
                else:
                    print('Failed to update country name')
            elif h1==2:
                if service.update_inflation_type():
                    print('Sucessfully changed inflation type')
                else:
                    print('Failed to update INflation type')
            elif h1==3:
                if service.update_inflation_rate():
                    print('Sucessfully updated inflation rate')
                else:
                    print('Failed to update inflation rate')
            else:
                print('WRONG INPUT ENTER CORRECT INPUT AGAIN')
        elif h==3:
            l=service.read_country()
            for i in l:
                print(*i)
        elif h==4:
            hh=service.delete()
            if hh==1:
                print('deletion sucessfull')
            else:
                print(hh)
        else:
            print('Enter correct input')
    elif n==2:
        print('1.Press 1 to show country all years inflation rates')
        print('2.Press 2 to show country particular years inflation rates')
        print('3.press 3 to compare inflation rates of countries')
        print('4.Press 4 for finding all countries avg inflation rates:: ',end=' ')
        h1=int(input())
        if h1==1:
            e=aop.show_country_all_years()
            if e!=1:
                print(e)
        elif h1==2:
            e=aop.show_country_particular_years()
            if e!=1:
                print(e)
        elif h1==3:
            e=aop.compare_countries()
            if e!=1:
                print(e)
        elif h1==4:
            e=aop.compare_avg()
            if e!=1:
                print(e)
        else:
            print('Enter correct input')
    elif n==3:
        break
    else:
        print('Enter correct input')
