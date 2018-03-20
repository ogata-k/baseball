# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:48:56 2017

@author: Owner
"""


import sys
from cx_Freeze import setup, Executable

base = None

setup(name = "sample",
      version = "1.0",
      description = "converter",
      executables = [Executable("baseball.py", base=base)])
