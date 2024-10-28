ipsum_file = open('files/ipsum.txt')
for line in ipsum_file:
    print(line)
    # when you want to removethe gap of each line we can use .rstrip() method
    # print(line.rstrip())
    
# or we can use 
ipsum_file.seek(0)
# seek() used to indecat the change the cuurent file position 0 default or beginning 1 the current file position 2 the end of the file or set to other number in which charactor it starts
lines = ipsum_file.readlines()
print(lines)
# also read limited charactors using seek
ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)
ipsum_file.close()
  