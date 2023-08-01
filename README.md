# ml-flow-demo

# Workflows:
1. Update config.yml
2. Update schema.yml (all columns of our data)
3. Update params.yml
4. Update the entity
5. Update the configuration manager and src config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update app.py

# How to run?

### Steps:

Clone the repository: 
```bash
https://github.com/dimoynwa/ml-flow-demo
```

### Step 1: Create a conda environment
```bash
conda create -n mlproj python=3.9 -y
```

```bash
conda activate mlproj
```

### Step 2: Install the requirements

```bash
pip install -r requirements.txt
```

### Run the following:
```bash
python app.py
```


## MLFlow:
[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[Dagshub](https://dagshub.com/)
MLFLOW_TRACKING_URI=https://dagshub.com/dimoynwa/ml-flow-demo.mlflow \
MLFLOW_TRACKING_USERNAME=dimoynwa \
MLFLOW_TRACKING_PASSWORD=b438e26f2c75bb68347e97b2096330de3ad1e94f  \
python script.py

To export as environment variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/dimoynwa/ml-flow-demo.mlflow
export MLFLOW_TRACKING_USERNAME=dimoynwa
export MLFLOW_TRACKING_PASSWORD=b438e26f2c75bb68347e97b2096330de3ad1e94f
```


