import os,errno
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

print os.getcwd()
mkdir_p('TestTest')
os.chdir('TestTest')
mkdir_p('Test2')
os.chdir('Test2')
print os.getcwd()
os.chdir('../..')
print os.getcwd()