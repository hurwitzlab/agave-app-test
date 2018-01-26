# -*- coding: robot -*-
*** Settings ***
Documentation	blah blah blah
...		blah blah blah
Resource	resource.robot

*** Variables ***

*** Test Cases ***
Submit Ap
	[Tags]	submit blast
	Create Session  agave    ${AGAVE_BASE_URL}  verify=true
	${content}=    Load JSON From File	./data/ohana-blast-0.0.8.json
	${headers}=    Create Dictionary       Content-Type=application/json	Authorization=Bearer ${AUTH_TOKEN}
	${resp}=	Post Request	agave	${JOBS}	data=${content}	headers=${headers}
	Log     ${resp.json()}      console=yes
	Should Be Equal As Strings	${resp.status_code}	201
	Dictionary Should Contain Item  ${resp.json()}  status	success	
	${id}=	Get From Dictionary   ${resp.json()["result"]}  id 
	Log	"Job ID:" ${id}	console=yes
