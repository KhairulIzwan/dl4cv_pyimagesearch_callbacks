from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(packages=['dl4cv_pyimagesearch_callbacks'], package_dir={'': 'src'})

setup(**d)
