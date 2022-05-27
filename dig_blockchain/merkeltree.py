import hashlib

from numpy import block
class merkelTreeHash(object):
    def __init__(self) -> None:
        
    def findMerkelHash(self,fileHashes):
        blocks=[]
        if not fileHashes:
            raise ValueError("Missing required file hashes for computing merk tree")
        for m in sorted(fileHashes):
            blocks.append(m)
        listLen=len(blocks)
        while listLen % 2 !=0:
            blocks.extend(blocks[1:])
            listLen=len(blocks)
        secondary=[]
        for k in [blocks[x:x+2] for x in xrange(0,len(blocks),2)]:
            hasher=hashlib.sha256()
            hasher.update(k[0]+k[1])
            secondary.append(hasher.hexdigest())
        if(len(secondary)==1):
            return secondary[0][0:64]
        else:
            return self.findMerkelHash(secondary)

if __name__=='__main__':
    import uuid
    file_hashes=[]
    for i in range(0,13):
        file_hashes.append(str(uuid.uuid4().hex))
    print("Finding the Merkel tree hash of {0} random hashes".format(len(file_hashes)))
    cls=merkelTreeHash()
    mk=cls.findMerkelHash(file_hashes)
    print("The merkel tree hash of the hashes below is: {0} ".format(mk))
    print "...."
    print(file_hashes)
