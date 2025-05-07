from web3 import Web3
import os
from dotenv import load_dotenv
load_dotenv()

wss_rpc_url = os.getenv("CHAINSTACK_WSS_RPC_URL")
w3= Web3(Web3.LegacyWebSocketProvider(wss_rpc_url))

pending_filter= w3.eth.filter('pending')
pending_tx_hashes=pending_filter.get_new_entries()

for tx_hash in pending_tx_hashes:
    try:
        tx = w3.eth.get_transaction(tx_hash)
        print(f'{tx["to"]}')
        if tx['to'] is None:  # Contract creation
            print(f"📦 Contract creation tx detected: {tx_hash.hex()}")
    except Exception:
        continue
    
#wait for tx to be mined
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = receipt.contractAddress

# Check for ERC-20 functions
code = w3.eth.get_code(contract_address)
if code and b'totalSupply' in code:
    print(f"🪙 Likely ERC-20 token deployed at: {contract_address}")