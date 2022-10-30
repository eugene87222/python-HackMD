import setuptools


def readme():
    with open('README.md', 'r') as fp:
        return fp.read()


setuptools.setup(
    name='pythonHackMD',
    version='1.0.1',
    description='A Python interface for HackMD API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Eugene Yang',
    author_email='eugene87222@gmail.com',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='HackMD API',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    url='https://github.com/eugene87222/pythonHackMD',
)