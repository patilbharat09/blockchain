from web3 import Web3
#  note this is called python-decouple for pip
# if you have installed decouple
# you might need to uninstall decouple and python-decouple
# and reinstall decouple to get everything working again

from decouple import config

#  print some hello worlds
print('hello world')
print('hello another world')

# okay, let's pull in some values from .env
#  copy infura url from me, but best to set up your own (http://infura.io)
infuraUrl= config('INFURA_URL')

# this is the address of your ERC20 contract (0xblahblahbutcontract)
contractAddress = Web3.toChecksumAddress(config('CONTRACT_ADDRESS'))

# this is your primary metamask address (0xblahblah)
# toChecksumAddress added because of some random errors people were getting
ownerAddress = Web3.toChecksumAddress(config('OWNER_ADDRESS'))

# this is your private key (from metamask - large hex number)
privateKey = config('SUPER_SECRET_PRIVATE_KEY')

# okay, let's get the contract ABI
# this is like its API, but blockchain
# check out the verified contract screen on etherscan and you should see it...
abi='[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

# connect to infura
web3 = Web3(Web3.HTTPProvider(infuraUrl))

if web3.isConnected():
    print('CONNECTED TO WEB3!!!!')
    #  connect to your contract, using its address and ABI
    contractInstance = web3.eth.contract(address=contractAddress, abi=abi)
    # query your contract
    symbol = contractInstance.functions.symbol().call()
    # print your success
    print ('Bharats contract symbol is ' + symbol)