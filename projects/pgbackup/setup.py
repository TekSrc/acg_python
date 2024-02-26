from setuptools import find_packages, setup

with open('README.md', 'r') as f:
  long_description = f.read()

setup(
  name='pgbackup',
  version='0.1.0',
  author='Frank Carvajal',
  author_email='frankacarv@gmail.com',
  description='A utility for backing up PostgreSQL databases.',
  long_description=long_description,
  long_descritipn_content_type='text/markdown',
  url="https://github.com/TekSrc/acg_python",
  packages=find_packages('src'),
  )
