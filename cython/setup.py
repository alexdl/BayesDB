import sys
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

virtual_env_dir = "~/.virtualenvs/tabular_predDB/"
numpy_rel_dir = "lib/python2.7/site-packages/numpy/core/include/"
numpy_include_full_dir = os.path.join(virtual_env_dir, numpy_rel_dir)
numpy_include_full_dir = os.path.expanduser(numpy_include_full_dir)
if not os.path.isdir(numpy_include_full_dir):
    error_message = 'numpy_include_full_dir doesn\'t exist: %s\n' \
        % numpy_include_full_dir
    sys.stderr.write(error_message)
    sys.exit()

setup(
  name = 'Demos',
  ext_modules=[
        Extension("ContinuousComponentModel",
              sources=["ContinuousComponentModel.pyx",
                       "../src/utils.cpp",
                       "../src/numerics.cpp",
                       "../src/RandomNumberGenerator.cpp",
                       "../src/ComponentModel.cpp",
                       "../src/MultinomialComponentModel.cpp",
                       "../src/ContinuousComponentModel.cpp"],
              include_dirs=["../include/CrossCat/",
                            numpy_include_full_dir],
              language="c++"),
        Extension("MultinomialComponentModel",
              sources=["MultinomialComponentModel.pyx",
                       "../src/utils.cpp",
                       "../src/numerics.cpp",
                       "../src/RandomNumberGenerator.cpp",
                       "../src/ComponentModel.cpp",
                       "../src/MultinomialComponentModel.cpp",
                       "../src/ContinuousComponentModel.cpp"],
              include_dirs=["../include/CrossCat/",
                            numpy_include_full_dir],
              language="c++"),
        Extension("State",
              sources=["State.pyx",
                       "../src/utils.cpp",
                       "../src/numerics.cpp",
                       "../src/RandomNumberGenerator.cpp",
                       "../src/DateTime.cpp",
                       "../src/State.cpp",
                       "../src/View.cpp",
                       "../src/Cluster.cpp",
                       "../src/ComponentModel.cpp",
                       "../src/MultinomialComponentModel.cpp",
                       "../src/ContinuousComponentModel.cpp"],
              include_dirs=["../include/CrossCat/",
                            numpy_include_full_dir],
              language="c++"),
    ],
  cmdclass = {'build_ext': build_ext},

)
