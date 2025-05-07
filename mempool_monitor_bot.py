from web3 import Web3
import os
from dotenv import load_dotenv

#Load env 
load_dotenv()
api_key = os.getenv("INFURA_API_KEY")
endpoint = os.getenv("CHAINSTACK_ENDPOINT")
flashbots_rpc_url = os.getenv("FLASHBOTS_RPC_URL")
private_key = os.getenv("PRIVATE_KEY")

#Connect to Ethereum Node
w3=Web3(Web3.HTTPProvider(endpoint))


def use_flahsbots():
    flahsbots=Web3(Web3.HTTPProvider(flashbots_rpc_url))
    ACCOUNT = flahsbots.eth.account.from_key(private_key)
    ADDRESS = ACCOUNT.address
  
    tx = {
        "from": ADDRESS,
        "to": "0x4D5fA74E995aacf8Dd01fe634BD449be2775d5Db",  # Replace this!
        "value": flahsbots.to_wei(0.01, "ether"),
        "gas": 21000,
        "maxFeePerGas": flahsbots.to_wei(100, "gwei"),
        "maxPriorityFeePerGas": flahsbots.to_wei(2, "gwei"),
        "nonce": flahsbots.eth.get_transaction_count(ADDRESS),
        "chainId": 1,  # Ethereum Mainnet
        "type": 2,
    }
   
    # Sign the transaction
    signed_tx = flahsbots.eth.account.sign_transaction(tx, private_key)
    print(f'Sign: {signed_tx} \n')
    tx_hash = flahsbots.eth.send_raw_transaction(signed_tx)
    print("🔒 Protected TX sent:", tx_hash.hex())
    
def monitor_mempool():
    while True:
        current_block = w3.eth.block_number
        confirmed_block_number = current_block-1
        confirmed_block = w3.eth.get_block(confirmed_block_number, full_transactions=True)
        
        for i, tx in enumerate(confirmed_block['transactions']):
            print(f"{i+1}: 'From: ' {tx['from']} 'To:' {tx['to']}")
        
        print('\n')
        # pending_block=w3.eth.get_block('pending')
        # pending_transactions=pending_block['transactions']
        # print(f"Current block: {current_block}. Pending transactions: {len(pending_transactions)}")


# monitor_mempool()
# w3 = Web3(Web3.HTTPProvider())
use_flahsbots()