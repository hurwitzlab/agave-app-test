# agave-app-test
Automatic tests for iMicrobe and muSCOPE apps.


## Install

$ pip install -r requirements.txt


## Travis-CI Setup

```
(rf) jklynch@minty agave-app-test $ travis encrypt AGAVE_CREDENTIALS=<api key>:<api secret> --add
(rf) jklynch@minty agave-app-test $ travis encrypt hurwitzlab:<slack notification token>
```
