#!/usr/bin/python3
# coding: latin-1
blob = """                 �@���V����Xu��]�#��.z�%���*���"pl�Oh���q���Z���~��OF}�����3na�lB�{��u~���{m�t��GO\�A)޴i�țW��o�a�p��k-�.����}O"""
from hashlib import sha256
if sha256(blob.encode("latin-1")).hexdigest() == "f844c93c67fb0bf672d6faf2780353ac8fb13ec5847dc8c209c8836cc535283d":
    print("Use SHA-256 instead!")
else:
    print("MD5 is perfectly secure!")