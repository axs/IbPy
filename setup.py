from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

import glob
import os
import sys

#python setup.py build_ext --inplace -c mingw32


setup(
    name = "Cython IbPy",
    ext_modules = cythonize([dirpath +'/*.pyx' for dirpath, directories, files in os.walk('ib')]),
)

