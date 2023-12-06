word= open('Movies.txt','r+')
for i in word.readlines():
    print(i)
    if (i == 'Stranger Things '):
        print('Best')
word.close()