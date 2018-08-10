"""
Detail see: https://github.com/pypa/sampleproject/blob/master/setup.py
"""
from setuptools import setup, find_packages

setup(
    name='qsnark-python-sdk',
    version='1.0.0',
    keywords='Qsnark, SDK',
    description='Qsnark SDK for Python',
    license='MIT License',
    url='https://github.com/hyperchaincn/qsnark-python-sdk',
    author='hyperchaincn',
    author_email='support.dev@hyperchain.cn',
    packages=find_packages(),
    install_requires=[
        'requests>=v2.19.0,<3'
    ],
    classifiers=[
        'Topic :: Software Development :: SDK',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent"
    ],
)
