import json
import sys

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
passwd="jj"
rpc_url = "http://localhost:8545"


w3 = Web3(HTTPProvider(rpc_url))
w3.geth.personal.unlockAccount(w3.eth.accounts[0],passwd,15000)
# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]
checker = w3.eth.contract(address=adr, abi=abi)

def createFile(userId,fileHash):
	tx_hash=checker.functions.createFile(userId,fileHash).transact()
	#tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash,600)
def updateFile(fileId,fileHash):
	tx_hash=checker.functions.updateFile(fileId,fileHash).transact()
	#tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash,600)
def deleteFile(fileId):
	tx_hash=checker.functions.deleteFile(fileId).transact()
	#tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash,600)

Mode=sys.argv[1]
fileId=int(sys.argv[2])
userId=int(sys.argv[3])
fileHash=sys.argv[4]

if Mode=="0":
	createFile(userId,fileHash)	

if Mode=="1":
	updateFile(fileId,fileHash)

if Mode=="2":
	deleteFile(fileId)	
