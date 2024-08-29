from django.db import models


class Token(models.Model):
    """NFT-token model"""
    unique_hash = models.CharField(max_length=20, editable=False, unique=True)
    tx_hash = models.CharField(max_length=66, unique=True)
    media_url = models.URLField()
    owner = models.Field(max_length=42)

    def __str__(self):
        return f"Token {self.id} - Owner: {self.owner}"

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
