#!/usr/bin/env python3
# coding: utf-8
from pykakasi import kakasi

kakasi = kakasi()

kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')

conv = kakasi.getConverter()

filename = '豚.jpg'

print(type(filename))
print(conv.do(filename))
