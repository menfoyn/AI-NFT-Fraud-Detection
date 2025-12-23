# AI-Powered NFT Fraud Detection (Proof of Concept)

Course: SEN0401 – Special Topics in Software Engineering (Blockchain)  
Instructor: Yusuf Altunel  
Domain: AI4NFT / AI4Blockchain  

## Project Overview
This project is a proof-of-concept system that demonstrates how artificial intelligence
can be integrated with blockchain technology to detect and record fraudulent NFT-related
activities. The system uses a machine learning model to generate a fraud risk score and
stores this score on-chain using a Solidity smart contract.

The main goal of the project is to show a minimal but working AI + Blockchain integration
rather than a full-scale production system.

---

## System Architecture
The project consists of two main components:

1. **AI Component (Python)**
   - Trains a simple machine learning model using transaction-related features
   - Produces a fraud risk score between 0 and 100

2. **Blockchain Component (Solidity)**
   - Stores fraud scores on-chain
   - Restricts write access to the contract owner
   - Emits events when scores are updated