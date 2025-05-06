from web3 import Web3
import os
from dotenv import load_dotenv

#Load env 
load_dotenv()
api_key = os.getenv("INFURA_API_KEY")
endpoint = os.getenv("INFURA_ENDPOINT")

#Connect to Ethereum Node
w3=Web3(Web3.HTTPProvider(endpoint))
assert w3.is_connected()

#Subscribe to Pending Transactions

print(w3.is_connected())

# w3 = Web3(Web3.HTTPProvider())