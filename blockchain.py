import datetime
import hashlib
import JSON
from flask import Flask, jsonify
class Block:
  def __init__(self, index,timestamp,data,previousHash=""):
    self.index = index
    self.timestamp = timestamp
    self.data=data
    self.previousHash=previousHash
    self.hash=self.calculateHash()

  def calculateHash(self):
      return hashlib.sha256(self.index+self.previousHash+self.timestamp+JSON.stringify(self.data)).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain=[self.createGenesisBlock()]
    def createGenesisBlock():
        return Block(0,"26/05/2022","Genesis block","0")

    def getLatestBlock(self):
        return self.chain[self.chain.length-1]
    
    def addBlock(newBlock):
        newBlock.previousHash=self.getLatestBlock().hash
        newBlock.hash=newBlock.calculateHash
        self.chain.push(newBlock)
        
plot1 = Blockchain()
plot1.addBlock(Block(1,))



