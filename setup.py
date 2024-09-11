from setuptools import setup, find_packages
import os

def read_long_description():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

def read_requirements():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
        requirements = f.read()
    return requirements
    
setup(
    name="basic_test",
    version="0.1",
    description="python basic numpy and opencv test",
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    author="Dr. Amish Kumar",
    author_email="amishkumar562@gmail.com",
    url="https://github.com/VisioSphereAI/job_artifact",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)