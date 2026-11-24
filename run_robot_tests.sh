#!/bin/bash

#pysäytetään skripti jos tietokannan luonti epäonnistuu

set -e

echo "Running tests"

# luodaan tietokanta
uv run python src/db_helper.py

echo "DB setup done"

#siivous onnistuneiden testien ja virheiden jälkeen

cleanup() {
  kill $(lsof -t -i:5001) 2>/dev/null || true
}
trap cleanup EXIT

# käynnistetään Flask-palvelin taustalle
uv run python3 src/index.py &

echo "started Flask server"

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5001)" != "200" ]];
  do sleep 1;
done

echo "Flask server is ready"

# suoritetaan testit
uv run robot --variable HEADLESS:true src/story_tests
