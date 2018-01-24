import json
import os
import sys
import time

from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


def test_puca():
    # grab client_id and client_secret:
    client_id, client_secret = os.environ['AGAVE_CREDENTIALS'].split(':')
    print(client_id)
    print(client_secret)
    token_url = 'https://agave.iplantc.org/token'

    # generate HTTPBasicAuth Header
    basic_auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)

    # start oauth session
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, auth=basic_auth)
    print(token)

    # submit a job
    job_json = json.loads("""\
    {
      "name": "ohana-blast-test",
      "appId": "ohana-blast-0.0.8",
      "archive": true,
      "inputs": {
        "QUERY": "agave://data.iplantcollaborative.org/jklynch/data/muscope/blast/test.fa"
      },
      "parameter": {
      }
    }
    """)

    submit_job_response = oauth.post(url='https://agave.iplantc.org/jobs/v2?pretty=true', json=job_json)
    print(submit_job_response.json())

    # ask for status on the job
    job_id = submit_job_response.json()['result']['id']
    job_status_url = 'https://agave.iplantc.org/jobs/v2/{}/status'.format(job_id)

    job_status = None
    for i in range(20):
        job_status_response = oauth.get(url=job_status_url)
        job_status = job_status_response.json()['result']['status']

        print(job_status)
        if job_status == 'FINISHED':
            break
        else:
            print('sleeping 60 seconds')
            for j in range(6):
                sys.stdout.write('.')
                time.sleep(10)

    assert job_status == 'FINISHED'
