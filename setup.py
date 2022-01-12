from setuptools import setup, find_packages


setup(
    name='aio_qiwi_transactions',
    version='0.0.1',

    url='https://github.com/RubbishCode/aio_qiwi_transactions',
    author='Rubbish Code',
    author_email='rubbishcode@gmail.com',
    install_requires=['requests-async'],
    packages=find_packages()

)
