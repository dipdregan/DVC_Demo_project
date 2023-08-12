from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirement_list: List[str] = ['pymongo', 'dvc', 'dvc-gdrive', 'scikit-learn', 'ipykernel']
    return requirement_list

setup(
    name="Winequality_project",
    version="0.0.1",
    author="dipendra_pratap",
    author_email="dipendrapratap155@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
