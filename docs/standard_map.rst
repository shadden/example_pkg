.. standard_map:

The Standard Map
----------------

The standard map takes a point :math:`(\theta,p)` and returns a new point :math:`(\theta',p')` 
according to the formula

.. math::
        \begin{align}
        p' &= p + K\sin\theta \\
        \theta' &= \theta + p'
        \end{align}

where :math:`K` is a paramter.
We'll use sphinx's automodule to create an API documentation
below. 
The function :func:`~example_pkl.std_map.standard_map_trajectory`
can be used to compute trajectories of the standard map.

API
---
.. automodule:: example_pkg.std_map
   :members:

