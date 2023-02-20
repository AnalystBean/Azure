trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- script: |
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
  displayName: 'Install dependencies'

- script: |
    python main.py
  displayName: 'Run application'