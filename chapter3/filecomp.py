import sys
import os
import hashlib

if len(sys.argv) < 3:
    print "You need to specify two directories:"
    print sys.argv[0], "<directory1> <directory2>"
    sys.exit()
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

def md5(file_path):
    """Return an md5 checksum for a file"""
    print "file_path:",file_path
    if os.path.isdir(file_path):
        return '1'
    
    read_file = file(file_path)
    the_hash = hashlib.md5()
    for line in read_file.readlines():
        the_hash.update(line)
    return the_hash.hexdigest()

def directory_listing(dir_name):
    """Return all of the files in a directory."""
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for path, dirs, files in os.walk(dir_name):
        if dir_root is None:
            dir_root = path
        dir_trim = len(dir_root)
        print "dir", dir_name,
        print "root is", dir_root

    trimmed_path = path[dir_trim:]
    print "trimmed_path:", trimmed_path
    if trimmed_path.startswith(os.path.sep):
        trimmed_path = trimmed_path[1:]

    for each_file in files + dirs:
        file_path = os.path.join(trimmed_path, each_file)
        dir_file_list[file_path] = True

    print "dir_file_list",dir_file_list
    return (dir_file_list, dir_root)

dir1_file_list, dir1_root = directory_listing(directory1)
dir2_file_list, dir2_root = directory_listing(directory2)
results = {}

print "dir2_file_list---", dir2_file_list
for file_path in dir2_file_list.keys():
    
    if file_path not in dir1_file_list:
        results[file_path] =  "not found in directory 1"
    else:
        print file_path, "found in directory 1 and 2"
        file1 = os.path.join(dir1_root, file_path)
        file2 = os.path.join(dir2_root, file_path)
        if md5(file1) != md5(file2):
            results[file_path] = "is different in directory 2!"
        else:
            results[file_path] = "is the same in both!"

for file_path, value in dir1_file_list.items():
    if file_path not in results:
        results[file_path] = "not found in directory 2!"

print
for file_path, result in sorted(results.items()):
    if os.path.sep not in file_path and "same" not in result:
        print file_path, result

for path, result in sorted(results.items()):
    if os.path.sep in file_path and "same" not in result:
        print path, result
        
