import time
import hashlib
import json
import requests
import base64
from flask import Flask, request
from multiprocessing import Process, Pipe
import ecdsa
from miner_config import MINER_ADDRESS, MINER_NODE_URL, PEER_NODES

node = Flask(__name__)
#définition de la forme générale d'un bloc
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """Renvoie un nouvel objet Bloc. Chaque bloc est" chaîné "à son précédent en appelant
            son hachage unique.
        Args:
            index (int): numéro de bloc.
            timestamp (int): horodatage de création de bloc.
            data (str): données à envoyer.
            previous_hash (str): Chaîne représentant le hachage unique du bloc précédent.
        Attrib:
            index (int): numéro de bloc.
            timestamp (int): horodatage de création de bloc.
            data (str): données à envoyer.
            previous_hash (str): Chaîne représentant le hachage unique du bloc précédent.
            hash (str): hachage unique du bloc actuel.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    #fonction de hashage; hacher l'ensemble des inforations que le bloc contient (index+ timestamp...)
    def hash_block(self):
        """Creates the unique hash for the block. It uses sha256."""
        val_sha = hashlib.sha256()
        val_sha.update((str(self.index)
                    + str(self.timestamp)
                    + str(self.data)
                    + str(self.previous_hash)).encode('utf-8'))
        return val_sha.hexdigest()
        #Retourne le hash en hexadecimal
    #creation de tout premier block
    @staticmethod
    def create_genesis_block():
            """Pour créer chaque bloc, il a besoin du hachage du précédent.
            Premierement le bloc n'a pas de précédent, il doit donc être créé manuellement
            (avec un index zéro et un hachage précédent arbitraire)"""
        return Block(0, time.time(), {"proof-of-work": 9,"transactions": None}, "0")
    # Node's blockchain copy
    BLOCKCHAIN = [create_genesis_block()]
        """ Stocke les transactions de ce nœud dans une liste.
        Si le nœud auquel on a envoyé la transaction ajoute un bloc
        il sera accepté, mais il y a une chance que se soit
        rejetée et la transaction revient comme si elle n'avait jamais été
        traité"""
    NODE_PENDING_TRANSACTIONS = []

    # preuve de travail
    def proof_of_work(last_proof, blockchain):
        # Creation d'une variable qui va trouver la prochaine proof of work
    incrementer = last_proof + 1
    # on incremente tant que le numéro n'est pas divisible par 9
    # and the proof of work of the previous block in the chain
    start_time = time.time()
    while not (incrementer % 7919 == 0 and incrementer % last_proof == 0):
        incrementer += 1
        # Check if any node found the solution every 60 seconds
        if int((time.time()-start_time) % 60) == 0:
            # If any other node got the proof, stop searching
            new_blockchain = consensus(blockchain)
            if new_blockchain:
                # (False: another node got proof first, new blockchain)
                return False, new_blockchain
    # Once that number is found, we can return it as a proof of our work
    return incrementer, blockchain
    # Keep incrementing the incrementer until it's equal to a number divisible by 9
    # and the proof of work of the previous block in the chain
    start_time = time.time()
    while not (incrementer % 7919 == 0 and incrementer % last_proof == 0):
        incrementer += 1
        # Check if any node found the solution every 60 seconds
        if int((time.time()-start_time) % 60) == 0:
            # If any other node got the proof, stop searching
            new_blockchain = consensus(blockchain)
            if new_blockchain:
                # (False: another node got proof first, new blockchain)
                return False, new_blockchain
    # Once that number is found, we can return it as a proof of our work
    return incrementer, blockchain