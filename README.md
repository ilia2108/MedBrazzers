# eLEKsir project

Hello. This is a repository of team MedBrazzers that has created a project eLEKsir - a brand new way of coopeeration between HPC, pharmacists and patients. It uses WR codes to access medeical data which is sotred in blockchain based on Ethereum. In the following chapters we'll describe all components of our solution. Here's a demo (click on the picture)

[![Full demo](https://img.youtube.com/vi/6VadtWG0G4M/0.jpg)](https://youtu.be/6VadtWG0G4M "Full demo")

## Frontend

We have created the frontend based on **Bootstrap**. Its main advantage is **scalability** to both desktop and mobile devices. So all types of users can use simple UI to make their treatment as comfortable as possible.

We have implemented an authentocation and authorizarion with three roles: **patient, HCP** and **pharmacist**. Doctor and pharmacist roles are mostly the same, but doctor has unique feature to initially add user to the blockchain.  

![alt text](https://github.com/ilia2108/MedBrazzers/blob/master/screenshots/land.png)

## QR codes

That's the basic entity that we're working with. After doctor has added a user into blockchain the **only thing required from patient** is **valid QR code**. It contains an information about patients in plaintext, however, this solution stands for demo reasons only. You can check the contents of QR with your smartphone.

![alt text](https://github.com/ilia2108/MedBrazzers/blob/master/screenshots/qr.png)

Also, there's a feature to print a QR


## Adding a drug

After scanning QR doctor or pharmacist can create a new block based on alreeady existing one. All sides (patient, HPC, pharmacist) can edit this data, but we assuming that the most of the data will be changed not by patient.

![alt text](https://github.com/ilia2108/MedBrazzers/blob/master/screenshots/add.png)

## Blockchain

That's the core of the solution. Unfortunately, because of it you can't try it yourself, becuase it's quite intensive technical process to set it up. There're several reasons to have blockchain-based solution:
- The technology itself is the **third most impactful technology**;
- **Healthcare** is the **second biggest industry** that uses blockchain;
- **Demand** on blockchain in healthcare **has increased by 26%** since start of COVID-19 crisis;
- There's a success story from Japan where a hospital created a **digital health passport** of their patients based on blockchain.

The main technology advantage is a combination of both **transparency** and **security**. The added element can never be deleted or edited, only new one can be created.

We have implemented a real-world blockchain scenario using smart contracts written in Solidity programming language. We use [Ethereum Ganache](https://www.trufflesuite.com/ganache) to review local blockchain in verify it. The example of our existing node of smart contract is below:

![alt text](https://github.com/ilia2108/MedBrazzers/blob/master/screenshots/blockchain.png)
