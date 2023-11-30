#!/usr/bin/python3
from ape import project

from scripts.constants import *


def approve(token, _from, to: str, amount: str):
    token.approve(to, amount, sender=_from)


def getDAI():
    return project.IDAI.at(DAI_Address)


def getUSDC():
    return project.IUSDC.at(USDC_Address)


def getWETH():
    return project.IWETH.at(WETH_Address)


def getWBTC():
    return project.IWBTC.at(WBTC_Address)


def getMATIC():
    return project.IMATIC.at(MATIC_Address)


# it will create a ERC20 object from a given address
def getERC20Token(address: str):
    return project.IERC20.at(address)


TOKENS = {
    "WETH": getWETH(),
    "DAI": getDAI(),
    "USDC": getUSDC(),
    "WBTC": getWBTC(),
    "MATIC": getMATIC(),
}


def main():
    pass
