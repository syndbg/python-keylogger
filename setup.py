from setuptools import setup
import os

VERSION = '0.0.1'
README = 'A multiplatform Python keylogger.'


# To be added

def read_requirements(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        requirements = f.readlines()
        for r in requirements:
            r = r.replace('\n', '')


setup(
    name='python-keylogger',
    author='Anton Antonov',
    author_email='anton.synd.antonov@gmail.com',
    url='https://github.com/syndbg/flask-robohash',
    download_url='https://github.com/syndbg/python-keylogger/archive/master.zip',
    version=VERSION,
    packages=['flask_robohash'],
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('test_requirements.txt'),
    test_suite='tests',
    include_package_data=True,
    license='MIT',
    description='A multiplatform Python keylogger.',
    long_description=README,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    platforms='any',
    keywords='python linux osx windows key keylogger logger',
    zip_safe=True,
)
