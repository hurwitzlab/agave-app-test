# -*- coding: robot -*-
*** Settings ***
Documentation	blah blah blah
...		blah blah blah
Resource	resource.robot

*** Variables ***

*** Test Cases ***
imicrobe puca
	[Tags]	imicrobe-puca
	Oauth Login
	${content}=                     Load JSON From File	  ./data/imicrobe-puca-0.0.2.json
	Log                             ${content}             console=yes
    ${resp}=                        Submit Job             ${content}
    ${id}=                          Get From Dictionary    ${resp.json()["result"]}  id
    Log Many                        "Job ID:"              ${id}
    Should Be Equal As Strings      ${resp.status_code}    201
    Dictionary Should Contain Item  ${resp.json()}         status  success
	Log Many                        ${resp.text}
	Wait For Job To Finish          ${id}
