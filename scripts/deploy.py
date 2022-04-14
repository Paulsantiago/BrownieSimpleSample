from distutils.command.config import config
import os
from brownie import FundMe, network,config, MockV3Aggregator
from scripts.helpScripts import (
    getAccount ,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)


def deploy_fundme():
    #If we are on a persistent network like rinnkeby
    #use the associate addressotherwise , deploy mocks
    account = getAccount()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        print("Deploying mocks ... ",len(MockV3Aggregator))
        price_feed_address = MockV3Aggregator[-1].address
    fundMe = FundMe.deploy(price_feed_address, 
    {"from":account},publish_source = config["networks"][network.show_active()].get("verify"),)
    print("contract deployed " ,fundMe)
    print("contract deployed address", fundMe.address)
    return fundMe
def main():
    deploy_fundme()