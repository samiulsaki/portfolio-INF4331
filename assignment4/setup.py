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
