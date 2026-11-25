import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


class TestBook:

    def test_book_page_opens(self, client):
        response = client.get("/book")

        assert response.status_code == 200


    def test_book_post_calls_add_book(self, client):

        with patch("app.cites.add_book") as mock_add_book:

            response = client.post(
                "/book",
                data={
                    "author": "Mörökölli",
                    "title": "Pökkelöpölli",
                    "year": "2026"
                }
            )

            mock_add_book.assert_called_once()

            assert response.status_code == 302


    def test_book_post_sends_correct_data(self, client):

        with patch("app.cites.add_book") as mock_add_book:

            client.post(
                "/book",
                data={
                    "author": "Källi Käärme",
                    "title": "Python-opas"
                }
            )

            mock_add_book.assert_called_once()

            sent_data = mock_add_book.call_args[0][0]

            assert sent_data["author"] == "Källi Käärme"
            assert sent_data["title"] == "Python-opas"

    def test_references_calls_get_references(self, client):

        with patch("app.cites.get_references") as mock_get:

            mock_get.return_value = []

            response = client.get("/references")

            mock_get.assert_called_once()

            assert response.status_code == 200
