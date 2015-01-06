'''
Created on 28/11/2014

@author: matsu
'''

class IntKBase: 
    def intKbase(self, x,b):
        alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
        'convert an integer to its string representation in a given base'
        if b<2 or b>len(alphabet):
            if b==64: # assume base64 rather than raise error
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            else:
                raise AssertionError("int2base base out of range")
        if isinstance(x,complex): # return a tuple
            return ( self.intKbase(x.real,b,alphabet) , self.intKbase(x.imag,b,alphabet) )
        if x<=0:
            if x==0:
                return alphabet[0]
            else:
                return  '-' + self.intKbase(-x,b,alphabet)
        # else x is non-negative real
        rets=''
        while x>0:
            x,idx = divmod(x,b)
            rets = alphabet[idx] + rets
        return rets
    
