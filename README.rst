Podaga
=======

.. image:: https://cloud.githubusercontent.com/assets/8732474/14165527/f62d3f96-f6d7-11e5-8c34-dc28f70e2721.gif

What
~~~~

Weather forecast, location, and general information display for the terminal.

Requires
~~~~~~~~

Curses is used to display the output, react to user input, and update on window resizing.

Also needed:

::

    pip install pyowm pyspin


Run
~~~~

::

    python podaga.py

Controls
~~~~~~~~

+------------------------------------+-----------------------------+
| Keys                               | Actions                     |
+====================================+=============================+
| ``q`` or ``Q`` or ``Esc``          | quit                        |
+------------------------------------+-----------------------------+
| ``r`` or ``R``                     | refresh forecast            |
+------------------------------------+-----------------------------+

Command-line options
~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+---------------------------------+
| Options                                | Descriptions                    |
+========================================+=================================+
| ``-h`` or ``--help``                   | show help message               |
+----------------------------------------+---------------------------------+
| ``--version``                          | show current version            |
+----------------------------------------+---------------------------------+
| ``-k`` or ``--api-key``                | set OWM api key                 |
+----------------------------------------+---------------------------------+
| ``-t`` or ``temp_unit``                | set temperature unit            |
+----------------------------------------+---------------------------------+
| ``-s`` or ``--save-config``            | saves current changes to config |
+----------------------------------------+---------------------------------+

Configuration file
~~~~~~~~~~~~~~~~~~

Check out ``example.podaga.conf`` for details.
Using the save (-s) argument will automatically generate a config file in the default location.

Support
~~~~~~~

-  [x] Works on Linux completely

-  [x] Works on OSX completely

-  [ ] Windows not supported
