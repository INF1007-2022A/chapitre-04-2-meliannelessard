#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	partie1 = name.split("-")[0] # liste -> ['Jean', 'Luc']
	print(partie1)
	nouveau = partie1[0].upper() + partie1[1:].lower()

	# mettre premiere lettre en majuscule
	
	
	return (f'Bonjour {nouveau}')

def get_random_sentence(animals, adjectives, fruits):
	
	#animal = animals[random.randrange(0, len(animals))]
	#adjectif = adjectives[random.randrange(0, len(adjectives))]
	#fruit = fruits[random.randrange(0, len(fruits))] 

	# plus facile de faire une boucle

	animals = animals[random.randrange(len(animals))]
	adjectives = adjectives[random.randrange(len(adjectives))]
	fruits = fruits[random.randrange(len(fruits))]
	return (f'Aujourd’hui, j’ai vu un {animals} s’emparer d’un panier {adjectives} plein de {fruits}.')
	

def encrypt(text, shift):

	return encrypt(text, shift)

def decrypt(encrypted_text, shift):
	return decrypt(encrypted_text, shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
