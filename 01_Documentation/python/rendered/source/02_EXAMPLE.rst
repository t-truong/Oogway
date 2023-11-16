Example Code
============

This page shows how the docstring style looks when rendered

Example Class
-------------

.. automodule:: codefile
    :members: MyClass
    :undoc-members:
    :show-inheritance:

Example Function
----------------

..
    Do not specify a member to document everything in a file

.. automodule:: codefile
    :members: doSomethingStandalone
    :undoc-members:
    :show-inheritance:

Example Code Block
------------------

:python:`a= [len(x)+1 for x in [[1, 2], [3, 4, 5]]]` is an in-line code which should be also be colored when rst_prolog variable is defined in conf.py
``this= len("mystring")+1`` is a literal which should not be colored, depending on your HTML theme

.. code::

    #file.py
    import sys
    import numpy as np

    print("This is a code block") #which should already have proper syntax highlighting
                                  #even without rst_prolog if the language is given
                                  #otherwise rst_prolog language is applied
    a= np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
    sys.exit()
