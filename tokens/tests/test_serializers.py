import pytest

from tokens.serializers import TokenCreateSerializer

VALID_OWNER = "0x" + "a" * 40


@pytest.mark.parametrize(
    "owner",
    [
        "not-an-address",
        "0x" + "a" * 39,
        "0x" + "a" * 41,
        "a" * 42,
    ],
)
@pytest.mark.django_db
def test_validate_owner_rejects_invalid_format(owner):
    serializer = TokenCreateSerializer(
        data={"media_url": "https://example.com/image.png", "owner": owner}
    )

    assert not serializer.is_valid()
    assert "owner" in serializer.errors


@pytest.mark.django_db
def test_validate_owner_accepts_valid_format():
    serializer = TokenCreateSerializer(
        data={"media_url": "https://example.com/image.png", "owner": VALID_OWNER}
    )

    assert serializer.is_valid(), serializer.errors
