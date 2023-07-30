# This is a Python script that will generate folder structure and all files

import os
import pathlib as pl
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'mlflow_demo'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yml',
    'params.yml',
    'schema.yml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]

for filepath in list_of_files:
    filepath = pl.Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.log(level=logging.INFO, msg=f'Creating directory {file_dir} for file {file_name}')

    if (not os.path.exists(filepath)) or os.path.getsize(filepath)==0:
        with open(filepath, 'w') as f:
            pass
            logging.log(level=logging.INFO, msg=f'Create file {filepath}')

    else:
        logging.log(level=logging.INFO, msg=f'{filepath} already exists')