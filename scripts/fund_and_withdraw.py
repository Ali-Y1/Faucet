from brownie import Faucet
from scripts.helpful import get_account


def fund():
    faucet = Faucet[-1]
    account = get_account()
    entrance_fee = faucet.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    faucet.fund({"from": account, "value": entrance_fee})


def withdraw():
    faucet = Faucet[-1]
    account = get_account()
    faucet.withdraw({"from": account})


def clean():
    faucet = Faucet[-1]
    account = get_account()
    faucet.clean({"from": account})


def main():
    fund()
