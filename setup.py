from setuptools import setup, find_packages


requirements = ["requests-async"]

setup(
    name="notebookc",
    version="0.0.1",
    author="Rubbish Code",
    author_email="rubbishcode@gmail.com",
    description="lib for working with qiwi for telegram async bots",
    url="https://https://github.com/RubbishCode/aio_qiwi_transactions/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8.8",
    ],
)
