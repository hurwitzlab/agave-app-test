import json

import pytest

from agave_app_test import submit_job, wait_for_job_to_finish


def test_ohana_blast_private(cyverse_oauth_session):
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

    submit_job_response = submit_job(
        cyverse_oauth_session=cyverse_oauth_session,
        job_json=job_json)
    print(submit_job_response.json())

    job_status = wait_for_job_to_finish(
        job_id=submit_job_response.json()['result']['id'],
        cyverse_oauth_session=cyverse_oauth_session)

    assert job_status == 'FINISHED'
