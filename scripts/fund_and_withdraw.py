from threading import activeCount
from brownie import FundMe
from scripts.helpScripts import getAccount

def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"current entrance fee is {entrance_fee}")
    print("funding ...")
    fund_me.fund({"from":account,"value":entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    print("withdrawing ...")
    fund_me.withdraw({"from":account})
    print("withdrawn")
def main():
    fund()
    withdraw()