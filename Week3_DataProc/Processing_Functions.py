def Load_Data(Data_Dir=None,Type='Raw'):
    Base_Dir = os.getcwd()
    Data = {}
    if Base_Dir:
        os.chdir(Data_Dir)
        
    os.chdir(Type)
    for file in os.listdir(os.getcwd()):
        Name = file[:-4]
        Data[Name] = np.load(file)
    os.chdir(Base_Dir)
    return Data

### File Ops    
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def Clip_Data(Data,x_s,x_f):
    for I in Data:
        Data[I] = Data[I][x_s:x_f]
        
def Save_Data(Data,Type,Data_Dir=None):
    Base_Dir = os.getcwd()
    if Data_Dir:
        os.chdir(Data_Dir)
        
    mkdir_p(Type)
    os.chdir(Type)
    
    for Item in Data:
        np.save(Item,Data[Item])
    os.chdir(Base_Dir)