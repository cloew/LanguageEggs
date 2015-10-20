from distutils.core import setup

setup(name='leggs',
      version='0.3.00',
      description='Python Language Eggs',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['leggs'],
      install_requires=["kao_factory"]
     )