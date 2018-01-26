# -*- coding: robot -*-
*** Settings ***
Library		HttpLibrary.HTTP
Documentation	blah blah blah
...		blah blah blah
Resource	resource.robot

*** Variables ***

*** Test Cases ***
Submit App
	[Tags]	submit blast
	Create Session  agave    ${AGAVE_BASE_URL}  verify=true
	${document}=	Catenate
	...	{
	...     "name": "ohana-blast-test",
	...     "appId": "ohana-blast-0.0.8",
	...     "archive": true,
	...     "inputs": {
	...         "QUERY": "agave://data.iplantcollaborative.org/mbomhoff/pov_test/POV_GD.Spr.C.8m_reads.fa" 
	...     }
	...	}
	Should Be Valid JSON	${document}
	${content}=	Parse Json	${document}
	Log	${content}	console=yes
	${headers}=    Create Dictionary       Authorization=Bearer ${AUTH_TOKEN}
	${resp}=	Post Request	agave	${JOBS}	data=${content}	headers=${headers}
	Log     ${resp.json()}      console=yes
	Should Be Equal As Strings	${resp.status_code}	201
	Dictionary Should Contain Item  ${resp.json()}  status	"success"	
