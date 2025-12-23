// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FraudScoreRegistry {
    address public owner;
    mapping(address => uint256) public fraudScore;

    event ScoreUpdated(address indexed wallet, uint256 score);

    constructor() { owner = msg.sender; }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function setScore(address wallet, uint256 score) external onlyOwner {
        require(score <= 100, "Score must be 0-100");
        fraudScore[wallet] = score;
        emit ScoreUpdated(wallet, score);
    }

    function getScore(address wallet) external view returns (uint256) {
        return fraudScore[wallet];
    }
}