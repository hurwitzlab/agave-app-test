import json

import pytest

from agave_app_test import submit_job, wait_for_job_to_finish


def test_muscope_last_private(cyverse_oauth_session):
    job_json = json.loads("""\
        {
          "name": "muscope-last-test",
          "appId": "muscope-last-0.0.3",
          "archive": true,
          "inputs": {
            "QUERY": "agave://data.iplantcollaborative.org/jklynch/data/muscope/last/test.fa"
          },
          "parameter": {
            "USE_TEST_DB": true
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
