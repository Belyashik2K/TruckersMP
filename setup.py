from setuptools import setup, find_packages

version = '1.0.0'

with open('README.md', 'r') as f:
      long_description = f.read()

setup(name='TruckersMP',
      version=version,

      author='Belyashik2K',
      author_email='lovelybelyashik@gmail.com',

      license='Apache License, Version 2.0',

      long_description=long_description,
      long_description_content_type='text/markdown',

      description='Fully async python wrapper for TruckersMP API',
      url='https://github.com/Belyashik2K/TruckersMP',
      packages=find_packages(),
      install_requires=['certifi', 'aiohttp', 'pydantic'],
      zip_safe=False)