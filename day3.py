import os
import os.path
import shutil
#os.mkdir('ne1')
#a = os.listdir('.')
#print(a)

file = open('t1')
#file = open('murali.txt', 'r')
#content = file.read()
#lines = file.readline()
lines = file.readlines()
#print(content)
#print("**************")
print(lines)
x = os.path.exists('t2')
print(' the existens of file  is: ',x)
#os.rmdir('new1')
#a = os.listdir('.')
#print(a)
#x = os.remove('t12')
#print(x)
##shutil.rmtree('test')
a = os.listdir('.')
print(a)
file.close()