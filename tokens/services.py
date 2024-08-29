from django.conf import settings
from web3 import Web3


def create_token_in_blockchain(token_data):
    web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))
    contract = web3.eth.contract(
        address=settings.CONTRACT_ADDRESS, abi=settings.CONTRACT_ABI
    )
    nonce = web3.eth.get_transaction_count(settings.PUBLIC_ADDRESS)

    base_fee_per_gas = web3.eth.get_block('pending')['baseFeePerGas']
    max_priority_fee_per_gas = web3.to_wei("1", "gwei")
    max_fee_per_gas = base_fee_per_gas + web3.to_wei("2", "gwei")

    txn = contract.functions.mint(
        token_data['owner'], token_data['unique_hash'], token_data['media_url']
    ).build_transaction(
        {
            "chainId": 11155111,
            "gas": 300000,
            "maxFeePerGas": max_fee_per_gas,
            "maxPriorityFeePerGas": max_priority_fee_per_gas,
            "nonce": nonce,
        }
    )

    signed_txn = web3.eth.account.sign_transaction(
        txn, private_key=settings.PRIVATE_KEY
    )

    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return web3.to_hex(tx_hash)
