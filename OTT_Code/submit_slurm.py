#!/usr/bin/python

import sys
import requests
from os.path import normpath, basename

current_user = "onetwotree"
api_key = "Kp0mPtWDyVE1jf-WbCmE9Qwt8NpqKaXyW7yGWHbVRlJO1b7gtT3dUeywbi2Citrqh7M"

# Job submission endpoint
job_submit_url = "https://saw.tau.ac.il/slurmapi/job/submit/"


def submit_job_to_Q(wd, cmd):
    # current_user = getpass.getuser()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "X-USERNAME": current_user,
    }

    jobID = basename(normpath(wd))
    jobName = f'onetwotree_{jobID}'
    payload = {
        "script": f"{cmd}\n",
        "partition": "pupko-pool",
        "tasks": 1,
        "name": jobName,
        "account": "pupko-users_v2",
        "nodes": 1,
        "qos": "owner",
        "cpus_per_task": 8,
        "memory_per_node": 6144,
        "standard_output": f"{wd}/output.txt",
        "standard_error": f"{wd}/error.txt",
        "current_working_directory": wd,
        "environment": [
            "PATH=/powerapps/share/rocky9/mamba/miniforge3/envs/guidance-env/bin:/powerapps/share/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local.cc/bin:/mathematica/vers/11.2",
            "LD_LIBRARY_PATH=/usr/lib64/atlas:/usr/lib64/mysql:/lib:/lib64:/lib/sse2:/lib/i686:/lib64/sse2:/lib64/tls:/powerapps/share/rocky9/mamba/miniforge3/envs/guidance-env/lib",
        ],
    }

    jobs_request = requests.post(job_submit_url, headers=headers, json=payload)
    jobs_request.raise_for_status()

    jobs_result = jobs_request.json()
    if 'job_id' in jobs_result:
        return str(jobs_result['job_id'])

    return ''

cmd = sys.argv[1]
job_id = sys.argv[2]
wd = f'/onetwotree/results/{job_id}'
ans = submit_job_to_Q(wd, cmd)
print(ans, end='')