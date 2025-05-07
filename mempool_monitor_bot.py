from web3 import Web3
import os
from dotenv import load_dotenv

#Load env 
load_dotenv()
api_key = os.getenv("INFURA_API_KEY")
endpoint = os.getenv("CHAINSTACK_ENDPOINT")

#Connect to Ethereum Node
w3=Web3(Web3.HTTPProvider(endpoint))

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

monitor_mempool()
# w3 = Web3(Web3.HTTPProvider())