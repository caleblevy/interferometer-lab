def New_Plot(*args):
    Fig = plt.figure()
    plt.plot(*args)
    return Fig
    
def Add_Labels(Fig,Title,xLabel,yLabel,Sci=True):
    plt.figure(Fig.number)
    plt.title(Title,fontsize=20)
    plt.xlabel(xLabel,fontsize=18)
    plt.ylabel(yLabel,fontsize=18)
    if Sci:
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        
    # Fix the axis fontsizes
    ax = plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(12)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12)

def Save_PNG_Plot(Fig,Name,Plot_Dir=None):
    Base_Dir = os.getcwd()
    if Plot_Dir:
        os.chdir(Plot_Dir) 
           
    plt.figure(Fig.number)
    plt.savefig(Name+'.png')   
    os.chdir(Base_Dir)