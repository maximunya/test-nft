import json
from unittest.mock import MagicMock, patch

import pytest
from django.urls import reverse

from tokens.models import Token

VALID_OWNER = "0x" + "a" * 40


def post_json(client, url, payload):
    return client.post(url, data=json.dumps(payload), content_type="application/json")


@pytest.mark.django_db
def test_create_token_success(client):
    url = reverse("tokens:create-token")
    payload = {"media_url": "https://example.com/image.png", "owner": VALID_OWNER}

    with patch("tokens.views.create_token_in_blockchain", return_value="0x" + "1" * 64) as mocked:
        response = post_json(client, url, payload)

    assert response.status_code == 201
    assert Token.objects.count() == 1
    token = Token.objects.get()
    assert response.json() == {
        "id": token.id,
        "unique_hash": token.unique_hash,
        "tx_hash": token.tx_hash,
        "media_url": payload["media_url"],
        "owner": payload["owner"],
    }
    mocked.assert_called_once()


@pytest.mark.django_db
def test_create_token_invalid_owner_returns_400(client):
    url = reverse("tokens:create-token")
    payload = {"media_url": "https://example.com/image.png", "owner": "not-an-address"}

    response = post_json(client, url, payload)

    assert response.status_code == 400
    assert Token.objects.count() == 0


@pytest.mark.django_db
def test_create_token_blockchain_failure_returns_500_and_rolls_back(client):
    url = reverse("tokens:create-token")
    payload = {"media_url": "https://example.com/image.png", "owner": VALID_OWNER}

    with patch("tokens.views.create_token_in_blockchain", side_effect=Exception("boom")):
        response = post_json(client, url, payload)

    assert response.status_code == 500
    assert response.json() == {"error": "boom"}
    assert Token.objects.count() == 0


@pytest.mark.django_db
def test_list_tokens(client):
    Token.objects.create(
        unique_hash="a" * 20,
        tx_hash="0x" + "1" * 64,
        media_url="https://example.com/image.png",
        owner=VALID_OWNER,
    )
    url = reverse("tokens:get-token-list")

    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["count"] == 1


@pytest.mark.django_db
def test_total_supply_success(client):
    mock_web3_instance = MagicMock()
    mock_contract = mock_web3_instance.eth.contract.return_value
    mock_contract.functions.totalSupply.return_value.call.return_value = 42
    url = reverse("tokens:get-total-supply")

    with patch("tokens.views.Web3", return_value=mock_web3_instance):
        response = client.get(url)

    assert response.status_code == 200
    assert response.json() == {"result": 42}


@pytest.mark.django_db
def test_total_supply_failure_returns_500(client):
    mock_web3_instance = MagicMock()
    mock_web3_instance.eth.contract.side_effect = Exception("rpc unavailable")
    url = reverse("tokens:get-total-supply")

    with patch("tokens.views.Web3", return_value=mock_web3_instance):
        response = client.get(url)

    assert response.status_code == 500
    assert response.json() == {"error": "rpc unavailable"}
