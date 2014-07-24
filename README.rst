================================================================================
                                deproulette
================================================================================


.. image:: http://skymovies.sky.com/image/unscaled/2008/12/9/Forrest-Gump.jpg
   :align: center
   :alt: Forrest Gump sitting on a bench waiting for the bus

.. pull-quote::

   Mama always said life was like a box of chocolates. You never know what you're gonna get.
   
   -- Forrest Gump, 1994

Do you ever get tired of knowing what you get? Have you ever felt you needed
to spice up your deployments?

With deproulette, you get what you wish for approximately none of the times.
This imprecision is achieved through "creative" use of the python package
distribution framework.

--------------------------------------------------------------------------------
                                 Usage
--------------------------------------------------------------------------------

Think of one or more packages, no need for unique packages,
but at most 5 packages, then run

.. code-block:: bash

    pip install deproulette

Once this has run, you have probably installed something else than what you
were thinking of. If not: please shoot me an email.

--------------------------------------------------------------------------------
                         How does it work?
--------------------------------------------------------------------------------

To achieve maximum discomfort for its users, deproulette downloads a list of
packages from https://pypi.python.org/simple/, then selects a random amount
of packages a random amount of times.

For all the details,
see https://github.com/joar/deproulette/blob/master/setup.py.
