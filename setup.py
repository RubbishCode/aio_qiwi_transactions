from setuptools import setup, find_packages

setup(
    name = 'aio_qiwi_transactions',
    version = '0.0.1',
    url = 'rubbishcode.ru',
    description = 'lib for working with qiwi for telegram async bots',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository
        'aio_qiwi_transactions @ git+ssh://git@github.com/RubbishCode/aio_qiwi_transactions.git'
    ]
)
