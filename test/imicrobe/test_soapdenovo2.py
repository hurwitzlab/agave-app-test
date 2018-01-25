import json

import pytest

from test import wait_for_job_to_finish


def test_soapdenovo2_private(cyverse_oauth_session):
    # submit a job
    job_json = json.loads("""\
        {
          "name": "imicrobe-soapdenovo2-test",
          "appId": "imicrobe-soapdenovo2-0.0.3",
          "archive": true,
          "inputs": {
            "CONFIG_FILE": "jklynch/test/imicrobe-soapdenovo2/test.config",
            "FORWARD_FQ": "shared/iplant_training/genome_assembly_soapdenovo/A_Assemble_Reads/fragScSi_1.fq",
            "REVERSE_FQ": "shared/iplant_training/genome_assembly_soapdenovo/A_Assemble_Reads/fragScSi_2.fq"
          },
          "parameters": {
            "OUTPUT_GRAPH_PREFIX": "test-output-graph"
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
