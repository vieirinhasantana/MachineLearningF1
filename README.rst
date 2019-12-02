=========
Bot Collector News from Google News
=========

**Index**
1. [Introduction](#intr)
2. [Environment Configuration](#cs1)
3. [Pre-Commit](#cs2)
4. [Unit Test](#cs5)
5. [Unit Test and Coverage](#cs3)
6. [Radon](#cs4)

First of all create and enable a workspace using virtualenv_ or anaconda_
then run these command in you virtual environment

::

  $ pip install pre-commit
  $ pre-commit
  $ pip install -r requirements.txt

The `Makefile` has steps to execute this application, you will need a rabbitmq

**Merge requests of new functions and fixes without tests will be declined**

.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _anaconda: https://www.anaconda.com
