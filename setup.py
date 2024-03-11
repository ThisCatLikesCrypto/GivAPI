from setuptools import setup, find_packages

setup(
    name='GivAPI',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='Wilbur Williams',
    description='Gets current data from the GivEnergy API',
    url='https://github.com/ThisCatLikesCrypto/GivAPI',
    long_description_content_type='text/markdown'
)
