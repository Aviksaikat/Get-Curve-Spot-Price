// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import {IERC20} from "./IERC20.sol";

// Adding only the ERC-20 function we need
interface IMATIC is IERC20 {
    function transfer(address dst, uint256 wad) external returns (bool);

    function balanceOf(address guy) external view returns (uint256);

    function decimals() external view returns (uint256);
}
