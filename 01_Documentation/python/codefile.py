class MyClass(object):
    """Brief summary
    
    Detailed description.

    Parameters
    ----------
    init_arg1: int
               | Always use "line blocks" (denoted with a "|") to document parameters
               | Each "|" is a newline when rendered to HTML. It always look neat and
                 just works

    init_arg2: real | str
               | DEFAULT= 5


    :ivar  init_arg1: see above Parameters, note that exactly 2 empty lines above this is required
    :ivar  init_arg2: see above Parameters
    :ivar attribute1: brief description of instance variable
    :ivar attribute2: brief description of instance variable
    """
    def __init__(self, init_arg1, init_arg2= 5):
        self.init_arg1= init_arg1
        self.init_arg2= init_arg2
        self.attribute1= init_arg1
        self.attribute2= init_arg2/init_arg1


    def doSomething(self, arg1):
        """Brief summary

        Detailed description.

        Parameters
        ----------
        arg1: array_like[real]
              | Description


        :ivar arg1: see above Parameters
        """
        self.arg1= arg1
####################################################################################################
def doSomethingStandalone(arg1, arg2, **kwargs):
    """Brief summary

    Detailed description. This :ref:`links to a target <user target>`. This :meth:`~MyClass.doSomething` links to
    a function.

    Parameters
    ----------
    arg1  : dict(str, list(real))
            | Description
    
    arg2  : set(int, str)
            | Description
    
    kwarg1: int, optional
            | Optional arguments may or may not have a DEFAULT
            | DEFAULT= 5

    Returns
    -------
    out1: int
          | Description
    out2: str
          | Description
    """
    myvar= kwargs.get("kwarg1", 5)
    return out1, out2
