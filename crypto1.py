# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 04:03:06 2020

@author: samurai_shampoo
"""

from hashlib import sha256

def updatehash(*args):
    hashing_text = ""; h= sha256()
    for arg in args:
        hashing_text += str(arg)
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

#print(updatehash("hello world", "hello"))     

class Block():
    data=None
    hash=None
    nance=0
    previous_hash = "0"*64
    
    def __init__(self, data,number=1):
        self.data = data
        self.number=number
        
    def hash(self):
        return updatehash(self.previous_hash, self.number, self.data, self.nance)
     
    def __str__(self):
        return str("Block: %s\nHash: %s\nPrevious: %s\nData: %s\nNance: %s\n" %(self.number, self.hash(), self.previous_hash,self.data, self.nance))
        
class Blockchain():
    difficulty = 4
    def __init__(self, chain=[]):
        self.chain= chain
    
    def add(self, block):
        self.chain.append(block)
    
    def remove(self, block):
        self.chain.remove(block)
    
    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass
    
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nance +=1
        
    def isValid(self):
        for i in range(1, len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                return False
        return True
    

def main():
    blockchain = Blockchain()
    database = ["hello", "wassup", "okay", "bye"]
    
    num=0
    for data in database:
        num+=1
        blockchain.mine(Block(data,num))
        
    
    #print(blockchain.chain)
    for block in blockchain.chain:
        print(block)
    blockchain.chain[2].data = "NEW DATA"
    blockchain.mine(blockchain.chain[2])
    print(blockchain.isValid())
    
if __name__ == "__main__":
    main()
