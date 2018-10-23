# python py2exe.py py2exe

from distutils.core import setup
import py2exe

setup(console=['target.py'], options ={'py2exe' : { 'bundle_files' : 1, 'compressed' : True}}, zipfile = None)