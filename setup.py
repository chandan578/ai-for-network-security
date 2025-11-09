"""
Setup.py file  is an essential part of packaging and distributing the Python project. It is used to define the package metadata and dependencies and more.
"""

from setuptools import find_packages, setup  ## find_packages is used to find all __init__.py file
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements..
    """
    requirements_lst:List[str] = []
    try:
        ## open file
        with open('requirements.txt', 'r') as file:
            ## read lines
            lines = file.readlines()
            ## process each line
            for line in lines:
                ## remove white spaces
                requirement = line.strip()
                ## ignore empty line and -e. file
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found..')

    return requirements_lst


setup(
    name='ai-for-network-security',
    version='0.0.1',
    author='Chandan Kumar',
    author_email='chandankumar26102000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)