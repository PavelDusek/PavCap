from setuptools import setup

setup(
        name='PavCap',
        version='1.0',
        description="Pavel Dusek's simple library for REDCap (https://www.project-redcap.org/) API communication in Python.",
        author='Pavel Dusek',
        author_email='pavel.dusek@gmail.com',
        packages=['PavCap'],
        install_requires=['requests'],
)
