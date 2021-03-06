# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks_dev/MLE_01_serving.ipynb (unless otherwise specified).

__all__ = ['func', 'Class']

# Cell

#import ...

# Cell
def func(a,b):
    '''
    a function that subs a and b
    '''
    return a + b

# Cell
class Class:
    '''
    a class to apply a function through the apply method
    '''
    def __init__(self, func):
        assert callable(func), 'func should be callable type'
        self.func = func

    def apply(self, *args, **kwargs):
        return self.func(*args, **kwargs)


# Cell
##############
#we highly recommend you creating ccode from the notebook instead
#of creating from src and running nbdev_update_lib. Still, if you want
#to proceeed, please create your new code bellow this tag before running nbdev_update_lib
##############