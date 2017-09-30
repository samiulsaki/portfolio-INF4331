# The setup file for creating a module named integrators before running the
# integators for unit testing. The setup must run before any integrators to 
# be run on the machine. Please follow the instructions provided on assignment 4
# Readme file.

from distutils.core import setup
from Cython.Build import cythonize
import numpy

name = "integrators"
setup(
    name = name,
    packages = [name],
    ext_modules = cythonize(name + "/cython_integrator.pyx"),
    include_dirs=[numpy.get_include()]
)
