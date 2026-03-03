#!/usr/bin/env python3
import requests

headers = {
    "Authorization": "Bearer Kp0mPtWDyVE1jf-WbCmE9Qwt8NpqKaXyW7yGWHbVRlJO1b7gtT3dUeywbi2Citrqh7M",
    "X-USERNAME": "onetwotree"
}

payload = {
    "script": "echo Hello, world!",
    "partition": "pupkoweb",
    "tasks": 1,
    "name": "test_job",
    "nodes": 1,
    "cpus_per_task": 2,
    "memory_per_node": 1024,
    "standard_output": "/tmp/job.out",
    "standard_error": "/tmp/job.err",
    "current_working_directory": "/tmp",
    "environment": [
        "PATH=/usr/local/bin:/usr/bin",
        "LD_LIBRARY_PATH=/lib:/lib64"
    ]
}

r = requests.post("https://saw.tau.ac.il/slurmapi/job/submit/", json=payload, headers=headers)
print(r.json())
