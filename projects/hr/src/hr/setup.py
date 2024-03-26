from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='CLI HR management application user export utility',
    long_description=readme,
    author='Frank Carvajal',
    author_email='frankacarv@gmailcom',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
