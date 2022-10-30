from setuptools import setup, find_packages

setup(
    name='pyHackMD',
    version='1.0',
    license='MIT',
    author='Eugene Yang',
    author_email='eugene87222@gmail.com',
    packages=find_packages('pyHackMD'),
    url='https://github.com/eugene87222/python-HackMD',
    keywords='HackMD API',
    install_requires=[
        'requests',
    ],

)