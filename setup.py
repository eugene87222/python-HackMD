from setuptools import setup, find_packages

setup(
    name='HackMD',
    version='1.0.0',
    license='MIT',
    author='Eugene Yang',
    author_email='eugene87222@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/eugene87222/pyHackMD',
    keywords='HackMD API',
    install_requires=[
        'requests',
    ],

)