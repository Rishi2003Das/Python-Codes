#Simple Login and user Id check
username= input('Enter user name: ')
password= input('Enter Password: ')

print('Your account is created successfully')
print('Login now')

user= input('Enter user name: ')
password2= input('Enter Password: ')

if (username == user and password == password2):
    print('Login sucessful')
    print('Welcome to the site!!!')
else:
    print('Login is failed. Try again')