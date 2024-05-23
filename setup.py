from setuptools import setup, find_packages


setup(
  name='PasswordGenerator',
  version='0.0.1',
  author='chadee',
  author_email='esurginet2011@gmail.com',
  description='This is module generates passwords',
  packages=find_packages(),
  install_requires=['loguru'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='password generator',
  python_requires='>=3.7'
)