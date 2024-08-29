import json

from django.conf import settings
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web3 import Web3

from .models import Token
from .serializers import TokenSerializer, TokenCreateSerializer
from .utils import generate_unique_hash


class TokenCreateView(APIView):
    def post(self, request):
        serializer = TokenCreateSerializer(data=request.data)

        if serializer.is_valid():
            media_url = serializer.validated_data.get('media_url')
            owner = serializer.validated_data.get('owner')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        unique_hash = generate_unique_hash()

        token = Token.objects.create(
            unique_hash=unique_hash,
            media_url=media_url,
            owner=owner
        )

        web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))
        contract_address = settings.CONTRACT_ADDRESS

        with open('config/contract_abi.json') as file:
            contract_abi = json.load(file)

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        nonce = web3.eth.get_transaction_count(settings.PUBLIC_ADDRESS)

        txn = contract.functions.mint(
            token.owner,
            token.unique_hash,
            token.media_url
        ).buildTransaction({
            'chainId': 11155111,
            'gas': 70000,
            'maxPriorityFeePerGas': web3.to_wei('1', 'gwei'),
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=settings.PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        token.tx_hash = web3.to_hex(tx_hash)
        token.save()

        return Response(TokenSerializer(token).data, status=status.HTTP_201_CREATED)


class TokenListView(ListAPIView):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class TotalSupplyView(APIView):
    def get(self, request):
        web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))
        contract_address = settings.CONTRACT_ADDRESS

        with open('config/contract_abi.json') as file:
            contract_abi = json.load(file)

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        total_supply = contract.functions.totalSupply().call()

        return Response({"result": total_supply})