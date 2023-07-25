from setuptools import setup, find_packages
##need improvement
setup(
    name='kubesys_operators',
    version='0.0.1',
    description='kubesys operators',
    author='zal-orz',
    author_email='zhangaoluo22@otcaix.iscas.ac.cn',
    url='https://github.com/kubesys/operators',
    packages=find_packages(),
    install_requires=[
        'kubesys-client @ git+ssh://github.com/kubesys/client-python.git',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
