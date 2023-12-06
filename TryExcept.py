try:
    x= int(input('Enter an integer: '))
    print(x)
except:
    print('Something is wrong')
else:
    print('Nothing went wrong')
finally:
    print('TRY and Except Block Done')