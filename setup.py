from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the given file,
    excluding '-e .'
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Abhinay',
    author_email='bhargavasaiabhinay.b@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
