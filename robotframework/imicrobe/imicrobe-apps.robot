# -*- coding: robot -*-
*** Settings ***
Documentation	blah blah blah
...		blah blah blah
Resource	resource.robot

*** Variables ***

*** Test Cases ***
Test Those Apps
    [Template]  Test Agave App
    ./data/imicrobe-puca-0.0.2.json
    ./data/ohana-blast-0.0.8.json

*** Keywords ***
Test Agave App
    [Arguments]  ${jobs_json_file_path}
	Oauth Login
	${content}=                     Load JSON From File	   ${jobs_json_file_path}
	Log                             ${content}             console=yes
    ${resp}=                        Submit Job             ${content}
    Log                             ${resp.text}           console=yes
    ${id}=                          Get From Dictionary    ${resp.json()["result"]}  id
    Log Many                        "Job ID:"              ${id}
    Should Be Equal As Strings      ${resp.status_code}    201
    Dictionary Should Contain Item  ${resp.json()}         status  success
	Log Many                        ${resp.text}
	Wait For Job To Finish          ${id}
