import json

import pytest

from test import wait_for_job_to_finish


def test_ohana_blast_private(cyverse_oauth_session):
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

    submit_job_response = cyverse_oauth_session.post(
        url='https://agave.iplantc.org/jobs/v2?pretty=true', json=job_json)
    print(submit_job_response.json())

    job_status = wait_for_job_to_finish(
        job_id=submit_job_response.json()['result']['id'],
        cyverse_oauth_session=cyverse_oauth_session)

    assert job_status == 'FINISHED'
