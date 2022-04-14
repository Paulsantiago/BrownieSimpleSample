from setuptools import find_namespace_packages
from scripts.helpScripts import getAccount
from scripts.deploy import deploy_fundme, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network,accounts, exceptions
import pytest

def test_can_fund_withdraw():
    account = getAccount()
    fund_me = deploy_fundme()
    entrance_fee = fund_me.getEntranceFee()+1000000
    tx = fund_me.fund({"from":account,"value":entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==entrance_fee
    tx2 = fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==0
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print("skipping")
        pytest.skip("only for local testing")
    account = getAccount()
    fund_me = deploy_fundme()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})


