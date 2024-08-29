from django.conf import settings
from django.db import transaction
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from web3 import Web3

from .models import Token
from .serializers import TokenCreateSerializer, TokenSerializer
from .services import create_token_in_blockchain
from .swagger_schemas import token_create_schema, total_supply_schema
from .utils import generate_unique_hash


class TokenCreateView(APIView):
    """Create new token"""

    @token_create_schema()
    @transaction.atomic()
    def post(self, request):
        serializer = TokenCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        media_url = serializer.validated_data.get("media_url")
        owner = serializer.validated_data.get("owner")
        unique_hash = generate_unique_hash()

        token = Token.objects.create(
            unique_hash=unique_hash, media_url=media_url, owner=owner
        )

        try:
            token = create_token_in_blockchain(token)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(TokenSerializer(token).data, status=status.HTTP_201_CREATED)


class TokenListView(ListAPIView):
    """Get all tokens from db"""

    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class TotalSupplyView(APIView):
    """Get total amount of tokens from blockchain"""

    @total_supply_schema()
    def get(self, request):
        web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))

        try:
            contract = web3.eth.contract(
                address=settings.CONTRACT_ADDRESS, abi=settings.CONTRACT_ABI
            )
            total_supply = contract.functions.totalSupply().call()
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response({"result": total_supply}, status=status.HTTP_200_OK)
