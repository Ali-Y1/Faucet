from brownie import network, config,accounts,MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_ENVIROMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORKED_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The network is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        print("Deploying AggregatorV3Interface Mock")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mock is deployed")
def main():
    deploy_mocks()