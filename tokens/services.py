from django.conf import settings
from web3 import Web3

from .models import Token


def create_token_in_blockchain(token: Token):
    web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))
    contract = web3.eth.contract(
        address=settings.CONTRACT_ADDRESS, abi=settings.CONTRACT_ABI
    )
    nonce = web3.eth.get_transaction_count(settings.PUBLIC_ADDRESS)

    txn = contract.functions.mint(
        token.owner, token.unique_hash, token.media_url
    ).build_transaction(
        {
            "chainId": 11155111,
            "gas": 70000,
            "maxPriorityFeePerGas": web3.to_wei("1", "gwei"),
            "nonce": nonce,
        }
    )

    signed_txn = web3.eth.account.sign_transaction(
        txn, private_key=settings.PRIVATE_KEY
    )

    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

    token.tx_hash = web3.to_hex(tx_hash)
    token.save()

    return token
