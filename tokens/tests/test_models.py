import pytest
from django.db import IntegrityError

from tokens.models import Token


@pytest.mark.django_db
def test_str_representation():
    token = Token.objects.create(
        unique_hash="abc123",
        tx_hash="0x" + "1" * 64,
        media_url="https://example.com/image.png",
        owner="0x" + "2" * 40,
    )

    assert str(token) == f"Token {token.id} - Owner: {token.owner}"


@pytest.mark.django_db
def test_unique_hash_must_be_unique():
    Token.objects.create(
        unique_hash="duplicate",
        tx_hash="0x" + "1" * 64,
        media_url="https://example.com/image.png",
        owner="0x" + "2" * 40,
    )

    with pytest.raises(IntegrityError):
        Token.objects.create(
            unique_hash="duplicate",
            tx_hash="0x" + "3" * 64,
            media_url="https://example.com/other.png",
            owner="0x" + "4" * 40,
        )
