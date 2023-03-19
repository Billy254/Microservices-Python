[![Python application test with Github Actions](https://github.com/Billy254/Microservices-Python/actions/workflows/devops_workflow.yml/badge.svg)](https://github.com/Billy254/Microservices-Python/actions/workflows/devops_workflow.yml)

# Microservices-Python
creating microservices using Python 

## Scaffold.
    - Makefile
    - requirements.txt
    - source
    - Test
    - Dockerfile
    - Build process : Infrastructure As Code

1. Create Virtual environment:

    python3 -m venv ~/.venv or virtualenv ~/.venv


#### Note: to activate the virtual environment when we start shell , add the source  virtaul environment command in bashrc file.

    source ~/.venv/bin/activate

2. Create empty files :

    touch requirements.txt Dockerfile Makefile main.py 
    mkdir mylib/__init__.py 
3. Populate Makefile.
4. Setup continous intergration , i.e check code for issues like lint errors.
5. Build command line tool using python fire library `./cli-fire.py --help` to test the logic



