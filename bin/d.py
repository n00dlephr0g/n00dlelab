#!/bin/python3

import yaml
import subprocess

# important variables
definitionFile = "/lab/definition.yml"
composePath = "/lab/compose"
envPath = "/lab/env"
projectPath = "/lab/projects"

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
def namecheck(services: list):
    for service in services:
        if service not in definition:
            print(f"no service named \"{service}\" in {definitionFile} ")
            print("exiting...")
            exit()

def filecheck(filePath: str):
    try:
        with open(filePath, 'r') as f:
            return None
    except FileNotFoundError:
        print(f"{filePath} doesn't exist, please check {definitionFile}")
        print("exiting...")
        exit()



def up(services: list):
    namecheck(services)
    process = ["docker", "compose", "up", "-d"]

    for service in services:
        serviceFile = f"{composePath}/{service}.yml"
        filecheck(serviceFile)
        process.extend(["-f", serviceFile])

        process.extend(["--env-file", "/lab/env/ports.env"])

        envs = definition[service]
        envs = envs if isinstance(envs, list) else [envs]

        for env in envs:
            envFile = f"{envPath}/{env}.env"
            filecheck(serviceFile)
            process.extend(["--env-file", envFile])


def down(services: list):
    namecheck(services)
    process = ["docker", "compose", "down"]

    for service in services:
        serviceFile = f"{composePath}/{service}.yml"
        filecheck(serviceFile)
        process.extend(["-f", serviceFile])


up(["atm"])

    
    
