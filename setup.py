from setuptools import setup, find_packages

with open('README.rst','r') as f:
    long_desc = f.read()
setup(
    name='wikitable',
    version='0.0.6',
    description='Converts Wikipedia tables to dataframes and CSVs',
    py_modules=["wikitable"],
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'beautifulsoup4'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',],
        long_description = long_desc,
        long_description_content_type = 'text/x-rst',
        url = 'https://github.com/jaredmeyers/wikitable',
        author = 'Jared Meyers',
        author_email = 'jaredehren@verizon.net',
        )
