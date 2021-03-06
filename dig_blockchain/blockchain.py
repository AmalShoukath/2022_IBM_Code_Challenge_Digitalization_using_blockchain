import datetime
import hashlib
import flask 
import sys
from flask import Flask
from flask import json
class Block:
  def __init__(self, index,timestamp,data,previousHash=""):
    self.index = index
    self.timestamp = timestamp
    self.data=data
    self.previousHash=previousHash
    self.hash=self.calculateHash()

  def calculateHash(self):
        string= str(self.index)+str(self.previousHash)+str(self.timestamp)+ str(json.dumps(self.data))
        return hashlib.sha256(string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain=[self.createGenesisBlock()]
    def createGenesisBlock(self):
        return Block(0,"26/05/2022","Genesis block","0")

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]
    
    def addBlock(self,newBlock):
        newBlock.previousHash=self.getLatestBlock().hash
        newBlock.hash=newBlock.calculateHash()
        self.chain.append(newBlock)
    def __str__(self) -> str:
        return self.data
    def isChainValid(self):
        for i in range(1,len(self.chain)):
            currentBlock= self.chain[i]
            previousBlock=self.chain[i-1]
        if(currentBlock.hash != currentBlock.calculateHash()):
            return False
        if(currentBlock.previousHash != previousBlock.hash):
            return False
        return True
        


        
#plot1 = Blockchain()
#B1=Block(1,"23/05/2022",{"amount": 4})
#plot1.addBlock(B1)
#B2=Block(1,"24/05/2022",{"amount": 10})
#plot1.addBlock(B2)
#for items in plot1.chain:
    #print(str(items.data))
#print(plot1.isChainValid())
#plot1.chain[1].data["amount"]=100
#print(plot1.chain[1].data)
#print(plot1.isChainValid())
