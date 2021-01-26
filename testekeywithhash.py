Private_key = bytes.fromhex("BF9795D3FCB4E2181B7B536C2247EA0001397C99BA94D4D4DD62801BB151B091")

import ecdsa

signing_key = ecdsa.SigningKey.from_string(Private_key, curve = ecdsa.SECP256k1)

verifying_key = signing_key.get_verifying_key()

print("this is the vk: " + verifying_key.to_string().hex())

public_key = bytes.fromhex("04") + verifying_key.to_string()

print ("this is the public key: " + public_key.hex())

import hashlib

sha256_1 = hashlib.sha256(public_key)

ripemd160 = hashlib.new("ripemd160")
ripemd160.update(sha256_1.digest())

hashed_public_key = bytes.fromhex("00") + ripemd160.digest()

print("this is the hashed public key: " + hashed_public_key.hex())

checksum_full = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()

print("this is my full checksum (32 bytes, I only need 4 bytes): " + checksum_full.hex())

checksum = checksum_full[:4]

print ("this is the real check sum only 4 bytes long: " + checksum.hex())

bin_addr = hashed_public_key + checksum

print("this is my bin_addr: " + bin_addr.hex())

import base58

FINALE_BTC_ADDRESS = base58.b58encode(bin_addr)

print ("this is my bitcoin address! " + str(FINALE_BTC_ADDRESS))