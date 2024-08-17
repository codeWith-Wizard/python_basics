#reading from  file

f = open("Chapter9/file.txt")#used to open the file
'''
by default open is in read mode
''' 
data = f.read()  #reading the data
print(data)  
f.close()  #closing the opened file
