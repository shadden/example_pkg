# This file controls what happens when
# you execute 'import example_pkg'
##########################################
#### Getting the C extension #############
##########################################
from ctypes import cdll
import os

# Absolute path where module is installed
pymodulepath=os.path.dirname(__file__)

# Suffix of compiled shared libraries 
import sysconfig
suffix = sysconfig.get_config_var('EXT_SUFFIX')
if suffix is None:
    suffix = ".so"

# load the C libary
clibexample=cdll.LoadLibrary(pymodulepath+"/../libexample"+suffix)

##########################################
####### Unrealted to C extension #########
##########################################
# import 
from .example import foo
from .std_map import standard_map_trajectory
__all__ = ["foo","standard_map_trajectory"]
