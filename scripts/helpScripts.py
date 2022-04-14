from lib2to3.pgen2.token import STAR
#from os import fork
from brownie import accounts, network , config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS =["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-dev-fork,mainnet-fork"]
def getAccount():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        print("getting account from ganache")
        return accounts[0]
    else:
        print("getting account from wallet")
        return accounts.add(config["wallets"]["from_key"])
def deploy_mocks():
    print(f"The active network is { network.show_active() }")
    print("Deploying mocks ... ")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE,{"from":getAccount()})
    print("deploy a mock")
    #price_feed_address = MockV3Aggregator[-1].address
