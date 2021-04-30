import pyqrcode
import png

s = str(input('Link, nome ou palavra: --> '))
s = pyqrcode.create(s)
nome = str(input('Nome do arquivo: --> ')).split()
nome = '_'.join(nome)
s.png(f"{nome}.png", scale=6)