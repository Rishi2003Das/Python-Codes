file= open('Movies.txt','w')
file.write('Game Of Thrones, Stranger Things, The Freelancer')
file= open('Movies.txt','r')
print(file.read())
file.close()
file= open('Movies.txt','a')
file.write(', Genius')
file= open('Movies.txt','r')
print(file.read())
file.close()