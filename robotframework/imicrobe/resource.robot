*** Settings ***
Documentation	Blah blah blah
Library		RequestsLibrary
Library		Collections
Library		JSONLibrary
Library     robotframework.imicrobe.agave_library  https://agave.iplantc.org

*** Variables ***
${AGAVE_BASE_URL}	https://agave.iplantc.org
${JOBS}			/jobs/v2
