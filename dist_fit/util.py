import numpy as np
from .common import FakeFunc
from .cdist_func import Normalize

#decorators
#@normalized_function(xmin,xmax)
#def function_i_have_no_idea_how_to_normalize(x,y,z)
#   return complicated_function(x,y,z)
#
class normalized_function:
    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
    def __call__(self,f):
        return Normalize(f,(self.xmin,self.xmax))

class rename_parameters:
    def __init__(self,*arg):
        self.arg = arg
    def __call__(self,f):
        return FakeFunc(f,self.arg)

#useful for highlight some xrange
def vertical_highlight(x1,x2=None,color='g',alpha=0.3):
    from matplotlib import pyplot as plt
    if x2 is None:
        x1,x2=x1
    ylim = plt.gca().get_ylim()
    y = np.array(ylim)
    plt.fill_betweenx(y,np.array(x1,x1),np.array(x2,x2),color=color,alpha=alpha)