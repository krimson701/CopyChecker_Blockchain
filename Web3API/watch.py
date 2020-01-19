
import json
import sys
import time
from web3 import Web3, HTTPProvider
from solc import compile_standard

# Solidity source code
# web3.py instance


f1=open("./contract.abi",'r')
f2=open("./contract.adr",'r')
#Load contract ABI, Address
abi=eval(f1.read())
adr=f2.read().rstrip('\n')
f2.close()
f1.close()

#Set Account Password, RPC geth URL
rpc_url = "http://localhost:8545"


w3 = Web3(HTTPProvider(rpc_url))
checker = w3.eth.contract(address=adr, abi=abi)

def handle_event(event):
    receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
    result1 = checker.events.MakeFileId().processReceipt(receipt)
    print("FileId: "+result1[0]['args']['FileId'])
def log_loop(event_filter, poll_interval):
	while True:
		print(event_filter.get_new_entries())
		for event in event_filter.get_new_entries():
			handle_event(event)
			time.sleep(poll_interval)

block_filter = w3.eth.filter({'fromBlock':'latest', 'address':adr})
log_loop(block_filter, 10)

