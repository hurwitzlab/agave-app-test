import os

import pytest

from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


@pytest.fixture
def cyverse_oauth_session():
    # grab client_id and client_secret:
    client_id, client_secret = os.environ['AGAVE_CREDENTIALS'].split(':')
    token_url = 'https://agave.iplantc.org/token'

    # generate HTTPBasicAuth Header
    basic_auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)

    # start oauth session
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, auth=basic_auth)

    return oauth