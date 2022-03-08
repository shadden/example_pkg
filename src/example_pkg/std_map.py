import numpy as np
from . import clibexample
from ctypes import c_double, POINTER, pointer

_std_mp=clibexample.standard_map
_std_mp.argtypes=[POINTER(c_double),POINTER(c_double),c_double]
_std_mp.restypes=None

def standard_map_trajectory(p0,theta0,K,Npts):
    r"""
    Generator for a trajectory of the standard map
    with parameter `K` for initial point (`p0`,`theta0`).

    Arguments
    ---------
    p0 : float
        Initial value of map variable p
    theta0 : float
        Initial value o fmap variable theta
    K : float
        Value of map parameter K
    Npts : int
        Number of trajectory points to compute.

    Returns
    -------
    theta_vals : numpy array
        Theta values of the trajectory
    p_vals : numpy array
        P values of trajectory
    """
    p_ptr = pointer(c_double(p0))
    theta_ptr = pointer(c_double(theta0))
    p_vals,theta_vals = np.zeros((2,Npts))
    for i in range(Npts):
        p_vals[i] = p_ptr.contents.value
        theta_vals[i] = theta_ptr.contents.value
        _std_mp(theta_ptr,p_ptr,K)
    return theta_vals,p_vals
