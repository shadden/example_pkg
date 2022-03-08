# This file controls what happens when
# you execute 'import example_pkg'
from .example import foo
from ctypes import cdll
libdir="/Users/shadden/Projects/00_Codes_And_Data/00_example_python_package/src/c_extension/"
clibexample=cdll.LoadLibrary(libdir+"libexample.so")
from .std_map import standard_map_trajectory
__all__ = ["foo"]
