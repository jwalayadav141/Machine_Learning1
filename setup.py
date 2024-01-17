
from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Jwala Yadav"
DISCRIPTION="This is a first FSDS Nov batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

# this method will execute the requirements.txt and return list of that
def get_requirements_list()->List[str]:
    """
    Discription: This function is going to return list of requirement
    mention in requirements.txt file

    return: This function is going to return a list which contain name of
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DISCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
#we can also specify python requirement it will behave same like as requirement.txt
) 
