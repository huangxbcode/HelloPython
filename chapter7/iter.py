import os

my_list = [1,2,3]
foo =  iter(my_list)
print foo
print foo.next()

print "counter----------------------------------------"
def counter(value):
    print "Starting at", value
    while value > 0:
        yield value
        value -= 1

foo = counter(5)
foo
for x in foo:
    print x

foo = [x**2 for x in range(10000)]

print "dir_name----------------------------------------"
dir_name = 'E:\workspace\HelloPython\chapter7'
file_type = '.py'

for path, dirs, files in os.walk(dir_name):
    print "path:", path
    print "dirs:", dirs
    print "file_type:", [f for f in files if f.endswith(file_type)]
    print "end:", '_'*42

print "log_files----------------------------------------"
def log_files(dir_name, file_type):
    if not os.path.exists(dir_name):
        print "dir_name:", dir_name
        raise ValueError(dir_name + "not found!")
    if not os.path.isdir(dir_name):
        raise ValueError(dir_name + "is not a directory!")
    for path, dirs, files in os.walk(dir_name):
        log_files = [f for f in files if f.endswith(file_type)]
        for each_file in log_files:
            yield os.path.join(path, each_file)

def log_lines(dir_name, file_type):
    for each_file in log_files(dir_name, file_type):
        for each_line in file(each_file).readlines():
            yield (each_file, each_line.strip())

def list_errors(dir_name, file_type):
    return (each_file + ': ' + each_line.strip()
        for each_file, each_line in
            log_lines(dir_name, file_type)
        if 'error' in each_line.lower())

if __name__ == '__main__':
    dir_name = 'E:/workspace/test'
    file_type = '.log'
    for each_file in log_files(dir_name, file_type):
        print each_file
    print "======================================="
    for each_error in list_errors(dir_name, file_type):
        print each_error
