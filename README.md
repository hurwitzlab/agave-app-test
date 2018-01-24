# agave-app-test
Automatic tests for iMicrobe and muSCOPE apps.


## Install

$ pip install -r requirements.txt


## Travis-CI Setup

This procedure does not have to be repeated.

Travis-CI integration with Slack can be managed here: https://hurwitzlab.slack.com/apps/manage.

Encrypt Agave credentials to be used for submitting apps and the Slack notification token like this:

```
jklynch@minty agave-app-test $ travis encrypt AGAVE_CREDENTIALS=<api key>:<api secret> --add
jklynch@minty agave-app-test $ travis encrypt hurwitzlab:<Slack notification token>
```

The encrypted Slack notification has to be added to `.travis.yml` manually. The `.travis.yml` file
should include this:

```
env:
  global:
    secure: blahblahblah
notifications:
  slack:
    secure: blahblahblah
```
