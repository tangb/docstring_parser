from setuptools import setup, find_packages
from pathlib import Path

setup(
    author='Marcin Kurczewski',
    author_email='rr-@sakuya.pl',
    name='docstring_parser',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    version='0.1',
    url='https://github.com/rr-/docstring_parser',
    packages=find_packages(),

    classifiers=[
        'Environment :: Other Environment',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing :: Markup',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
