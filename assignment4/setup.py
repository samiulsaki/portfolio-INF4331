from distutils.core import setup
from Cython.Build import cythonize

name = "integrators"
setup(
    name = name,
    packages = [name],
    ext_modules = cythonize(name + "/cython_integrator.pyx")
)


''' from distutils.core import setup, Extention
from Cython.Build import build_ext

setup(
    cmdclass={'build ext': build_ext},
    ext_modules = [Extention("integral", ["cython_integrator.pyx"])]
) '''