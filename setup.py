from setuptools import find_packages, setup
from typing import List

hypen_e = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [r.strip() for r in requirements]  # Strip newlines and spaces

        if hypen_e in requirements:
            requirements.remove(hypen_e)
    return requirements


setup (
    name = 'MLPROJECT',
    version = '0.0.1',
    author = 'Preetham',
    author_email = 'gollapallipreethamreddy@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )