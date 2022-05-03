from scripts.helpful import get_account
from scripts.deploy import deploy
from brownie import exceptions, Wei, accounts
import pytest


def test_can_fund():
    account = get_account()
    faucet = deploy()
    entrance_fee = faucet.getEntranceFee() + 100
    print(entrance_fee)
    tx = faucet.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert faucet.addressToAmountFunded(account.address) == entrance_fee


# account balance should be greater or equals to 1 ether
def test_withdraw_error():
    account = get_account()
    faucet = deploy()
    entrance_fee = faucet.getEntranceFee()
    faucet.fund({"from": account, "value": entrance_fee})
    with pytest.raises(exceptions.VirtualMachineError):
        faucet.withdraw({"from": account})


def test_can_withdraw():
    account = get_account()
    faucet = deploy()
    faucet.fund({"from": account, "value": Wei("1 ether")})
    before = account.balance()
    faucet.withdraw({"from": account})
    after = account.balance()
    assert after - before == Wei("0.1 ether")


# clean function send all ether in contract to the owner
def test_clean():
    account = get_account()
    faucet = deploy()
    faucet.fund({"from": account, "value": Wei("1 ether")})
    assert faucet.balance() == Wei("1 ether")
    faucet.clean({"from": account})
    assert faucet.balance() == 0


def test_clean_for_non_owners():
    account = get_account()
    faucet = deploy()
    faucet.fund({"from": account, "value": Wei("1 ether")})
    assert faucet.balance() == Wei("1 ether")
    with pytest.raises(exceptions.VirtualMachineError):
        faucet.clean({"from": accounts[1]})
    assert faucet.balance() != 0
