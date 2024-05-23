from setuptools import setup, find_packages


setup(
  name='PasswordGenerator',
  version='0.0.1',
  author='chadee',
  author_email='esurginet2011@gmail.com',
  description='This is module generates passwords',
  long_description='',
  long_description_content_type='text/markdown',
  url='home_link',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)