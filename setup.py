from setuptools import setup, find_packages

def get_requirements(path='requirements.txt'):
    with open(path) as f:
        return f.read().splitlines()
    
setup(
    name='extractor',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
)