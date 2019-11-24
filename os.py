#! python3

import os

os.path.join('folder1', 'folder2', 'folder3', 'file.png')   # join using appropriate separator for each OS

os.getcwd()     # get current working directory
#os.chdir('c:\\')     # change working directory


totalSize = 0
for filename in os.listdir('c:\\python'):
    if not os.path.isfile(os.path.join('c:\\python', filename)):
                          continue

    totalSize = totalSize + os.path.getsize(os.path.join('c:\\python', filename))


# reading and writing files

##textFile = open('C:\\Users\\i823857\\Desktop\\0000284264.txt')
##content = textFile.read()
##textFile.close()

textFile = open('C:\\Users\\i823857\\Desktop\\hello.txt', 'w')
content = textFile.write('Hello world!')
textFile.close()

textFile = open('C:\\Users\\i823857\\Desktop\\hello.txt', 'a')
content = textFile.write('\n\nGoodbye!')
textFile.close()

print(content)

# storing variables in files

import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

print(list(shelfFile.keys()))
print(list(shelfFile.values()))


import shutil
#shutil.copy('c:\\source.txt', 'c:\\destination directory')
#shutil.copy('c:\\source.txt', 'c:\\destination directory\\destination file.txt')

# copy the whole directory
#shutil.copytree('c:\\source', 'c:\\destination')

#shutil.move('c:\\source.txt', 'c:\\destination')

# to rename, move file to same folder


#import send2trash
#send2trash.send2trash('c:\\filename.txt')  # sends to recycling bin instead of removing file permanently


# walking a directory tree

for folderName, subfolders, filenames in os.walk('c:\\users\\i823857\\desktop\\i823857\\music'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))

