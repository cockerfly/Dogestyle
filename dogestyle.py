import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
import random

r = int(input("Сколько генерим адресов: "))
def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

for i in range(r):
        ran = random.randrange(115792089237316195423570985008687,115792089237316195423570985008687907852837564279074904382605163141518161494336)
        pk = Key.from_int(ran)
        key = Key.from_int(ran)
        upub = pk._pk.public_key.format(compressed=False)
        cpub = pk._pk.public_key.format(compressed=True)
        crmd = HASH160(cpub)
        urmd = HASH160(upub)
        dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd)
        dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd)
        f=open(u"dooge.txt","a")
        print(key.to_hex())
        print(dogecaddr)
        print(dogeuaddr)
        f.write("priv: " + key.to_hex() + "\n")
        f.write("address_comp: " + dogecaddr + "\n")
        f.write("address_un: " + dogeuaddr + "\n")
        f.close
   
   
   #Donation 1CockerXJADMqEPbFSLgexwgJ8tYjA2xmH
   #dogecoin  D9PuW4uDXRKJnimpJfYz9jxgffdChKz3zs