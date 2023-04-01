"""
包
"""

import my_package.mymodule1
import my_package.mymodule2

my_package.mymodule1.add(1, 2)
my_package.mymodule2.sub(1, 2)

from my_package import mymodule1
from my_package import mymodule2

mymodule1.add(3, 4)
mymodule2.sub(3, 4)

from my_package.mymodule1 import add
from my_package.mymodule2 import sub

add(1, 2)
sub(2, 3)

from my_package import *  # 只会导入__all__限定的
# mymodule2.sub(1, 2)


# import numpy
