import sys
import os
import hashlib

if len(sys.argv) < 3:
    print "You need to specify two directories:"
    print sys.argv[0], "<directory1> <directory2>"
else:
    directory1 = sys.argv[1]
    directory2 = sys.argv[2]

    print "Comparing:"
    print directory1
    print directory2
    print

    for directory in [directory1, directory2]:
        if not os.access(directory, os.F_OK):
            print directory, "isn't a valid directory!"
            sys.exit()

        print "Directory", directory
        for item in os.walk(directory):
            print item,"\n"
        print

read_file = file(os.path.join("e:\\python\\dir1", "comp1.txt"))
file_contents = list(read_file.readlines())
print "The first line reads:", file_contents[0]

write_file = file(os.path.join("e:\\python\\dir1", "newfile.txt"), "w")
write_file.write("This is the first line of the file\n")
write_file.writelines(["and the second\n", "and the third!\n"])
write_file.close()

file_name = sys.argv[1]
print "file:",file_name
read_file = file(file_name)
the_hash = hashlib.md5()
for line in read_file.readlines():
    the_hash.update(line)
print the_hash.hexdigest()

test_dictionary = {}
test_dictionary = {'one':1, 'two':2}
test_dictionary = {'list':[1,2,3], 'dict':{'one':1, 'two':2},}
print test_dictionary['list']
print test_dictionary['dict']
del test_dictionary['list']
print test_dictionary.keys()
print test_dictionary.values()
print test_dictionary.items()
