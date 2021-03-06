Keyword - Contextlib, __enter__ , __exit__ , exception
# EX1 
# No use with
file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1.\nContextlib Test1.')
finally:
    file.close()

# EX2
# Use with
with open('testfile2.txt', 'w') as f:
    f.write('Context Manager Test2.\nContextlib Test2.')

# EX3
# Use Class -> Context Manager with exception handling

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started: __init__')
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        print('MyFileWriter started: __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started: __exit__')
        if exc_type:
            print('Logging exception {}'. format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter('testfile3.txt', 'w') as f:
    f.write('Context Manager Test3.\nContextlib Test3.')