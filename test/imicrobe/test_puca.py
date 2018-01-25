import json

import pytest

from test import wait_for_job_to_finish


def test_puca_private(cyverse_oauth_session):
    # submit a job
    job_json = json.loads("""\
        {
          "name": "imicrobe-puca-test",
          "appId": "imicrobe-puca-0.0.2",
          "archive": true,
          "inputs": {
            "inputDir": "test/imicrobe-puca"
          },
          "parameters": {
            "BC_NAME": "samtools_1.6--0.img",
            "CMD_LINE": "samtools quickcheck -v imicrobe-puca/test.bam"
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
