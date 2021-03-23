import requests
from datetime import datetime

if '__name__' == '__main__':
    resp = requests.get('https://api.github.com/repos/iparask/git_actions/actions/workflows/dispatch.yml/runs?event=repository_dispatch')

    workflow_json = resp.json()

    if workflow_json['total_count']:
        last_run = workflow_json['workflow_runs'][0]
        finished = last_run['updated_at']
        status = last_run['conclusion']
        diff = datetime.now() - datetime.strptime(finished, '%Y-%m-%dT%H:%M:%SZ')
        if status == 'success' and diff.days > 7:
            return 1
        else:
            return 0
