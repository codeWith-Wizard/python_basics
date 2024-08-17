#reading multiple lines

f = open("Chapter9/file.txt")

line = f.readline()
lines = f.readlines()
print(line, type(line))   #file pointer plays a major role
print(lines, type(lines))
f.close()