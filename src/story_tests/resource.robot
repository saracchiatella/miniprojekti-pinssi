*** Settings ***
Library  Browser

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      500ms
${HOME_URL}   http://${SERVER}
${ADDREFERENCE_URL}  http://${SERVER}/add_reference
${BROWSER}    chromium
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $HEADLESS == 'true'
        New Browser  browser=${BROWSER}  headless=True
    ELSE
        New Browser  browser=${BROWSER}  headless=False  slowMo=${DELAY}
    END
    New Context
    New Page  about:blank
