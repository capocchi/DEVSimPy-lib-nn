from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext
setup(
  name = "Utilities",
  ext_modules=[ 
    Extension("utils", ["utils.pyx"], libraries = ["scipy"])
    ],
  cmdclass = {'build_ext': build_ext}
)
