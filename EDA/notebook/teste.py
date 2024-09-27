#from EDA.hello import ola
#import sys
import os
from pathlib import Path

root = Path().resolve().parent
t = os.path.realpath
#root = Path().resolve()
#ola('nivel acima')
print(root)
print(t)