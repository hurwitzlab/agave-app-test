import json
import os
import sys
import time

import requests.auth
import oauthlib.oauth2
import requests_oauthlib

from robot.api import logger


class agave_library():

    def __init__(self, agave_base_url):
        self._agave_base_url = agave_base_url
        self._oauth = None
        self._job_response = None


    def oauth_login(self):
        client_id, client_secret = os.environ['AGAVE_CREDENTIALS'].split(':')
        token_url = '{}/token'.format(self._agave_base_url)

        # generate HTTPBasicAuth Header
        basic_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
        client = oauthlib.oauth2.BackendApplicationClient(client_id=client_id)

        # start oauth session
        self._oauth = requests_oauthlib.OAuth2Session(client=client)
        self._oauth.fetch_token(token_url=token_url, auth=basic_auth)

        return self._oauth


    def submit_job(self, job_json):
        self._job_response = self._oauth.post(
            url='{}/jobs/v2?pretty=true'.format(self._agave_base_url),
            json=job_json)

        print(self._job_response)
        return self._job_response


    def wait_for_job_to_finish(self, job_id):
        job_status_url = '{}/jobs/v2/{}/status'.format(self._agave_base_url, job_id)

        job_status_response = self._oauth.get(url=job_status_url)
        job_status = job_status_response.json()['result']['status']
        logger.console(job_status + ' ' + job_id)
        while not (job_status == 'FINISHED' or job_status == 'FAILED'):
            logger.console('sleeping 60 seconds')
            for j in range(3):
                logger.console('.')
                time.sleep(20)
            job_status_response = self._oauth.get(url=job_status_url)
            job_status = job_status_response.json()['result']['status']

            logger.console(job_status + ' ' + job_id)

        return job_status
