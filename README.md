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


# Deployment

### About the deploymnet

1. Build Docker image
2. Push docker image to ECR
3. Launch EC2 Instance
4. Pull image from ECR to your EC2
5. Launch docker image in EC2 Instance

# Policy:
IAM User policies: AmazonEC2ContainerRegistryFullAccess, AmazonEC2FullAccess

## Create ECR repo to store docker image
    ECR_REPO: 282245150475.dkr.ecr.eu-central-1.amazonaws.com/mlflow-demo

## Create EC2 instance (Ubuntu)

## Open EC2 and install docker in EC2:

    ```bash
        sudo apt-get update -y
    ```
    ```bash
        sudo apt-get upgrade
    ```

    ```bash
        curl -fsSL https://get.docker.com -o get-docker.sh
    ```
    ```bash
        sudo sh get-docker.sh
    ```

    ```bash
        sudo usermod -aG docker ubuntu
    ```
    ```bash
        newgrp docker
    ```

## Configure EC2 as self hosted runner 
In your github:
```
    settings>actions>runner>new self hosted runner> choose os> run commands one by one on your EC2 machine

    When asking for name of the runner, type: self-hosted
    Skip adding additional labels
    For name of the working folder press Enter
```

## Setup Gitlab secrets 
How to get them:
1. Go to your github repo
2. Click settings> Secrets and variables>Actions> New repository secret
3. For all the keys bellow add values
4. Get the values from files downloaded from creating EC2 instance Access keys
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=eu-central-1
AWS_ECR_LOGIN_URI= 282245150475.dkr.ecr.eu-central-1.amazonaws.com
ECR_REPOSITORY_NAME=mlflow-demo
```