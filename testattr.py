
# 当被访问的属性找不到时，才会调用__getattr__
class TestGetAttr(object):
    def __getattr__(self, name):
        print "Attribute '%s' not found!" % name
        return 42

    def __init__(self,
                 file_name = 'log.txt',
                 level = 1):
        self.level = 2
        self.file_name = file_name

if __name__ == '__main__':
    test_class = TestGetAttr()
    print test_class.something
    print "test_class.level:", test_class.level
    print "test_class.file_name:", test_class.file_name

    test_class.something =43
    print test_class.something

print "-------------------------------------------------------"
class TestSetAttr(object):
    def __init__(self):
        self.__dict__['things'] = {}

    def __setattr__(self, name, value):
        print "Settings '%s' to '%s'"%(name, value)
        self.things[name] = value
    
    def __getattr__(self, name):
        try:
            return self.things[name]
        except KeyError:
            raise AttributeError(
                "'%s' object has no attribute '%s'"%
                (self.__class__.__name__, name))

if __name__ == '__main__':
    test_class2 = TestSetAttr()
    test_class2.something = 42
    print "test_class2.something:", test_class2.something
    print "test_class2.things:", test_class2.things
    print "test_class2.something_else:", test_class2.something_else
