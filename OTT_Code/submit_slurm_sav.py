#!/usr/bin/env python

import sys
import requests
from os.path import normpath, basename

current_user = "onetwotree"
api_key = "Kp0mPtWDyVE1jf-WbCmE9Qwt8NpqKaXyW7yGWHbVRlJO1b7gtT3dUeywbi2Citrqh7M"

# Base URL for authentication and token generation
base_url = 'https://saw.tau.ac.il'


def submit_job_to_Q(wd, cmd):

    # job submission url
    job_url = f'{base_url}/slurmapi/job/submit/'
    # Auth Headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "X-USERNAME": current_user,
    }

    job_id = basename(normpath(wd))
    job_name = f'onetwotree_{job_id}'
    environment = [
        "PATH=/powerapps/share/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local.cc/bin",
        "MODULEPATH=/powerapps/share/Modules/Centos7/modulefiles:/powerapps/share/Modules/Rocky8/modulefiles:/powerapps/share/Modules/Rocky9/modulefiles:/etc/modulefiles:/usr/share/modulefiles:/usr/share/modulefiles/Linux:/usr/share/modulefiles/Core:/usr/share/lmod/lmod/modulefiles/Core",
    ]

    payload = {
        "script": f"{cmd}\n",
        "partition": "pupkoweb",
        "tasks": 1,
        "name": job_name,
        "account": "pupkoweb-users",
        "nodes": "1",
        "cpus_per_task": 4,
        "memory_per_node": 6144,
        "time_limit": {
            "number": 10080,
            "set": True,
            "infinite": False,
        },
        "current_working_directory": wd,
        "standard_output": f"{wd}/output.txt",
        "standard_error": f"{wd}/error.txt",
        "environment": environment,
    }

    jobs_request = requests.post(job_url, headers=headers, json=payload)

    if jobs_request.status_code == 200:
        job_result = jobs_request.json()
        return job_result['job_id']

    return

cmd = sys.argv[1]
job_id = sys.argv[2]
wd = f'/onetwotree/results/{job_id}'
ans = submit_job_to_Q(wd, cmd)
print(ans, end='')

