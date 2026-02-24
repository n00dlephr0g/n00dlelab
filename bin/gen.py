#!/bin/python3

import yaml
import subprocess
import sys

# important variables
definitionFile = "/lab/definition.yml"
composePath = "/lab/compose"
envPath = "/lab/env"
dockerPath = "/lab/docker"

# read file
try:
    with open(definitionFile, "r") as file:
        content = file.read()
        definition = yaml.safe_load(content)
except FileNotFoundError:
    print(f"{definitionFile} doesn't exist")
    print("exiting...")
    exit()

# helpers
def filecheck(filePath: str):
    try:
        with open(filePath, 'r') as f:
            return None
    except FileNotFoundError:
        print(f"{filePath} doesn't exist, please check {definitionFile}")
        print("exiting...")
        exit()

for service in definition:
    serviceFile = f"{composePath}/{service}.yml"
    filecheck(serviceFile)
    
    # create required directory
    servicePath = f"{dockerPath}/{service}"
    os.system(f"mkdir {servicePath}")

    # link docker compose
    os.system(f"ln -s {serviceFile} {servicePath}/docker-compose.yml")

    # generate env files
    os.system(f"echo {envPath}/ports.env > {servicePath}/.env")
    envs = envs if isinstance(envs, list) else [envs]
    for env in envs:
        envFile = f"{envPath}/{env}"
    
