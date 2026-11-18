*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Can move from home page to add reference page
	Go To  ${HOME_URL}
	Click  button >> text=Lisää viite tästä!
	Get Title  ==  Lisää uusi viite

Can add a book referenve
	Go To  ${ADDREFERENCE_URL}
	Click  text=Book
	Get Title  ==  Lisää uusi kirjaviite
	Fill Text  input[name="author"]  Maija Meikäläinen
	Fill Text  input[name="editor"]  Matti Meikäläinen
	Fill Text  input[name="title"]  Hei hei
	Fill Text  input[name="publisher"]  Bantam
	Fill Text  input[name="year"]  2002
	Fill Text  input[name="volume"]  5
	Fill Text  input[name="number"]  190
	Fill Text  input[name="pages"]  384
	Fill Text  input[name="month"]  Heinäkuu
	Fill Text  textarea[name="note"]  Eipä mitään erityistä
	Fill Text  input[name="doi"]  https://doi.org/xxxx
	Fill Text  input[name="issn"]  12345678
	Fill Text  input[name="isbn"]  1234567891234
	Click  button >> text=Lisää viite
	Get Title  ==  Tallennetut viitteet
