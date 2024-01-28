from setuptools import find_packages, setup

setup(
    name='mongo-helper',
    packages=find_packages(),
    version='0.1.0',
    description='library that simplifies MongoDB operations',
    author='ABED ALWAHAB ALKHANJI',
    platforms=["Any"],
    author_email='a.w.khanji@hotmail.com',
    install_requires=["pymongo","mongoengine"],
)