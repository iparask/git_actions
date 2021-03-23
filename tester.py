import requests
import sys

from datetime import datetime

def main():
    resp = requests.get('https://api.github.com/repos/iparask/git_actions/actions/workflows/dispatch.yml/runs?event=repository_dispatch')
    workflow_json = resp.json()
    if workflow_json['total_count'] > 0:
        last_run = workflow_json['workflow_runs'][0]
        finished = last_run['updated_at']
        status = last_run['conclusion']
        diff = datetime.now() - datetime.strptime(finished, '%Y-%m-%dT%H:%M:%SZ')
        if status == 'success' and diff.seconds > 7:
            sys.exit(1)
        else:
            sys.exit(0)
    sys.exit(1)

main()