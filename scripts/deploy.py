from brownie import Faucet, network, config, MockV3Aggregator
from scripts.helpful import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIROMENTS


def deploy():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    print(price_feed_address)
    faucet = Faucet.deploy(price_feed_address, {"from": account})
    print(f"contract deployed to {faucet.address}")

    return faucet


def main():
    deploy()
