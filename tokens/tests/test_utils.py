import pytest

from tokens.models import Token
from tokens.utils import generate_unique_hash


@pytest.mark.django_db
def test_generate_unique_hash_length_and_charset():
    unique_hash = generate_unique_hash()

    assert len(unique_hash) == 20
    assert unique_hash.isalnum()


@pytest.mark.django_db
def test_generate_unique_hash_skips_existing_values(monkeypatch):
    existing_hash = "a" * 20
    Token.objects.create(
        unique_hash=existing_hash,
        tx_hash="0x" + "1" * 64,
        media_url="https://example.com/image.png",
        owner="0x" + "2" * 40,
    )

    calls = iter([existing_hash, "b" * 20])
    monkeypatch.setattr("random.choices", lambda *args, **kwargs: list(next(calls)))

    assert generate_unique_hash() == "b" * 20
