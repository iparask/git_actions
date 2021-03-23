import requests
from datetime import datetime

def main():

    resp = requests.get('https://api.github.com/repos/iparask/git_actions/actions/workflows/dispatch.yml/runs?event=repository_dispatch')
    print(resp.status_code)
    workflow_json = resp.json()
    print(workflow_json)
    if workflow_json['total_count'] > 0:
        last_run = workflow_json['workflow_runs'][0]
        finished = last_run['updated_at']
        status = last_run['conclusion']
        diff = datetime.now() - datetime.strptime(finished, '%Y-%m-%dT%H:%M:%SZ')
        
        print(diff, status)
        if status == 'success' and diff.seconds > 7:
            return 1
        else:
            return 0
    return 1


if '__name__' == '__main__':
    main()
