## Example

```python
class MyClass(object):
    """Brief summary
    
    Detailed description.

    Parameters
    ----------
    init_arg1: int
               | Description
               | DEFAULT= 5

    init_arg2: real | str
               | Always use "line blocks" (denoted with a "|") to document parameters
               | Each "|" is a newline when rendered to HTML. It always look neat and
                 just works


    :ivar  init_arg1: see above Parameters, note that exactly 2 empty lines above this is required
    :ivar  init_arg2: see above Parameters
    :ivar attribute1: brief description of instance variable
    :ivar attribute2: brief description of instance variable
    """
    def __init__(self, init_arg1= 5, init_arg2):
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
```
