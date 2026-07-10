from django.conf import settings
from web3 import Web3
from web3.types import TxParams, Wei


def create_token_in_blockchain(token_data: dict[str, str]) -> str:
    assert settings.INFURA_URL, "INFURA_URL is not configured"
    assert settings.PUBLIC_ADDRESS, "PUBLIC_ADDRESS is not configured"
    assert settings.PRIVATE_KEY, "PRIVATE_KEY is not configured"

    web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))
    contract_address = Web3.to_checksum_address(settings.CONTRACT_ADDRESS)
    contract = web3.eth.contract(address=contract_address, abi=settings.CONTRACT_ABI)
    public_address = Web3.to_checksum_address(settings.PUBLIC_ADDRESS)
    nonce = web3.eth.get_transaction_count(public_address)

    base_fee_per_gas = web3.eth.get_block("pending")["baseFeePerGas"]
    max_priority_fee_per_gas = web3.to_wei("1", "gwei")
    max_fee_per_gas = Wei(base_fee_per_gas + web3.to_wei("2", "gwei"))

    tx_params: TxParams = {
        "chainId": 11155111,
        "gas": 300000,
        "maxFeePerGas": max_fee_per_gas,
        "maxPriorityFeePerGas": max_priority_fee_per_gas,
        "nonce": nonce,
    }
    txn = contract.functions.mint(
        token_data["owner"], token_data["unique_hash"], token_data["media_url"]
    ).build_transaction(tx_params)

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=settings.PRIVATE_KEY)

    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return web3.to_hex(tx_hash)
