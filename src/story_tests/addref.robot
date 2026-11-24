*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***

Can add a book reference
	Go To  ${ADDREFERENCE_URL}
	Click  text=Kirjaviite
	Get Title  ==  book
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
	Get Title  ==  references

Can Add An Article Reference
	Click  text=Artikkeli
	Get Title  ==  article
	Fill Text  input[name="author"]  Maija Meikäläinen
	Fill Text  input[name="title"]  Hei hei
	Fill Text  input[name="journal"] Asiallinen Lehti
	Fill Text  input[name="year"]  2142
	Fill Text  input[name="volume"]  42
	Fill Text  input[name="number"]  999
	Fill Text  input[name="pages"]  5-55
	Fill Text  input[name="month"]  Hirmukuu
	Fill Text  textarea[name="note"]  Oli hyvä lehti
	Fill Text  input[name="doi"]  https://doi.org/xxxx
	Fill Text  input[name="issn"]  1122334455
	Fill Text  input[name="zblnumber"]  9898
	Fill Text  input[name="eprint"]  Asiallinen Lehti Mobiili
	Click  button >> text=Lisää viite
	Get Title  ==  references

Can Add An Inproceedings Reference
	Click  text=Konferenssijulkaisu
	Get Title  ==  inproceedings
	Fill Text  input[name="author"]  Aino Asiantuntija
	Fill Text  input[name="title"]  Tärkeä konferenssi koskien kaikkia asioita
	Fill Text  input[name="journal"]  Kaikkien asioiden konferenssi
	Fill Text  input[name="year"]  2042
	Fill Text  input[name="editor"]  Eija Eines
	Fill Text  input[name="volume"]  42
	Fill Text  input[name="number"]  999
	Fill Text  input[name="series"]  777
	Fill Text  input[name="pages"]  5-55
	Fill Text  input[name="month"]  Hirmukuu
	Fill Text  input[name="address"]  http://www.kaikkienasioidenkonferenssi.ym
	Fill Text  input[name="organization"]  Universaali Kaali
	Fill Text  input[name="publisher"]  Jämsä: Koivu
	Fill Text  textarea[name="note"]  Täällä sain tietää kaiken
	Fill Text  textarea[name="annote"]  Paitsi sen, meneekö testi läpi
	Click  button >> text=Lisää viite
	Get Title  ==  references

