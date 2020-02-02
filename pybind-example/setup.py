
import os, sys

from setuptools import setup, Extension

# cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']
cpp_args = ['-std=c++11']

ext_modules = [
    Extension(
    'wrap',
        ['funcs.cpp', 'wrap.cpp'],
        include_dirs=['pybind11/include'],
    language='c++',
    extra_compile_args = cpp_args,
    ),
]

setup(
    name='wrap',
    version='0.0.1',
    author='Cliburn Chan',
    author_email='cliburn.chan@duke.edu',
    description='Example',
    ext_modules=ext_modules,
)
