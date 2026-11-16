*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Can move from home page to add reference page
	Go To  ${HOME_URL}
	Click  button >> text=Lisää viite tästä!
	Get Title  ==  Lisää uusi viite
