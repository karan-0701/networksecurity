'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used to setuptools
(or disutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more 
'''

from setuptools import find_packages, setup
from typing import List 

def get_requirements()->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #Read lines from file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found.')
    return requirements_list

                
setup(
    name="NetworkSecurity",
    version="0.0.0.1",
    author="Karandeep Singh",
    author_email="karandeep07012004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()  
)