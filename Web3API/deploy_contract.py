import json


from web3 import Web3, HTTPProvider
from solc import compile_standard

# web3.py instance
rpc_url = "http://localhost:8545"
w3 = Web3(HTTPProvider(rpc_url))
w3.geth.personal.unlockAccount(w3.eth.accounts[0],"jj",15000)
# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# get bytecode
bytecode="0x608060405234801561001057600080fd5b5061079f806100206000396000f300608060405260043610610078576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063092a5cce1461007d5780630bd3ec001461009457806315155bf3146100cf578063442890d51461011e578063c5b4200614610175578063fbc65775146101a2575b600080fd5b34801561008957600080fd5b506100926101cd565b005b3480156100a057600080fd5b506100cd600480360381019080803590602001909291908035600019169060200190929190505050610231565b005b3480156100db57600080fd5b50610108600480360381019080803590602001909291908035600019169060200190929190505050610311565b6040518082815260200191505060405180910390f35b34801561012a57600080fd5b5061013361061e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561018157600080fd5b506101a06004803603810190808035906020019092919050505061063a565b005b3480156101ae57600080fd5b506101b76106c7565b6040518082815260200191505060405180910390f35b731aae59f7d4eb5941eb0c9d9492566a8035aca00973ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561021857fe5b3373ffffffffffffffffffffffffffffffffffffffff16ff5b61023961072b565b731aae59f7d4eb5941eb0c9d9492566a8035aca00973ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561028457fe5b61028d836106d4565b151561029557fe5b4281600001818152505081816020019060001916908160001916815250508060008085815260200190815260200160002060030160008060008781526020019081526020016000206004015481526020019081526020016000206000820151816000015560208201518160010190600019169055905050505050565b600061031b610748565b600061032561072b565b731aae59f7d4eb5941eb0c9d9492566a8035aca00973ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561037057fe5b4291508560010285836001026040516020018084600019166000191681526020018360001916600019168152602001826000191660001916815260200193505050506040516020818303038152906040526040518082805190602001908083835b6020831015156103f657805182526020820191506020810190506020830392506103d1565b6001836020036101000a03801982511681845116808217855250505050505090500191505060405180910390206001900483600001818152505085836020018181525050600083604001901515908115158152505060008360600181815250508181600001818152505084816020019060001916908160001916815250508260008085600001518152602001908152602001600020600082015181600001556020820151816001015560408201518160020160006101000a81548160ff021916908315150217905550606082015181600401559050506001836000015190806001815401808255809150509060018203906000526020600020016000909192909190915055508060008085600001518152602001908152602001600020600301600080600087600001518152602001908152602001600020600401600081548092919060010191905055815260200190815260200160002060008201518160000155602082015181600101906000191690559050507fb06726cbf87caed16d4d7ff793e4d1221210febab866a4692908e072f9c553046040518080602001828103825260068152602001807f68692c206869000000000000000000000000000000000000000000000000000081525060200191505060405180910390a17f5c9d1274e817bc669b888c1f22d936dc6b011eefc5018941fb367d184d092ba083600001516040518082815260200191505060405180910390a18260000151935050505092915050565b6000731aae59f7d4eb5941eb0c9d9492566a8035aca009905090565b731aae59f7d4eb5941eb0c9d9492566a8035aca00973ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561068557fe5b61068e816106d4565b151561069657fe5b600160008083815260200190815260200160002060020160006101000a81548160ff02191690831515021790555050565b6000600180549050905090565b600080600090505b60018054905081101561072057826001828154811015156106f957fe5b906000526020600020015414156107135760019150610725565b80806001019150506106dc565b600091505b50919050565b604080519081016040528060008152602001600080191681525090565b60806040519081016040528060008152602001600081526020016000151581526020016000815250905600a165627a7a72305820f6b0f145b83e2d935da6734406fa1fa758fba13d7c4891bcf13f0decedb5cec80029"
# get abi
abi=[
	{
		"constant": False,
		"inputs": [],
		"name": "destroyContract",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "fileId",
				"type": "uint256"
			},
			{
				"name": "fileHash",
				"type": "bytes32"
			}
		],
		"name": "updateFile",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "userId",
				"type": "uint256"
			},
			{
				"name": "fileHash",
				"type": "bytes32"
			}
		],
		"name": "createFile",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getContractOwner",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "fileId",
				"type": "uint256"
			}
		],
		"name": "deleteFile",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getNumberOfFiles",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"name": "FileId",
				"type": "uint256"
			}
		],
		"name": "MakeFileId",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"name": "str",
				"type": "string"
			}
		],
		"name": "MakeString",
		"type": "event"
	}
]
copyChecker = w3.eth.contract(abi=abi, bytecode=bytecode)


# Submit the transaction that deploys the contract
tx_hash = copyChecker.constructor().transact()
print("Maked transaction")
print(tx_hash)
# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash,600)
print("deployed")
print(tx_receipt.contractAddress)
Checker = w3.eth.contract(
address=tx_receipt.contractAddress,
abi=abi)
print(Checker)
# insert use code