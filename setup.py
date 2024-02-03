from setuptools import find_packages, setup

setup(
    name='mongo-helper',
    packages=find_packages(),
    version='0.1.0',
    description='library that simplifies MongoDB operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ABED ALWAHAB ALKHANJI',
    license_files='LICENSE',
    platforms=["Any"],
    author_email='a.w.khanji@hotmail.com',
    install_requires=["pymongo","mongoengine"],
)