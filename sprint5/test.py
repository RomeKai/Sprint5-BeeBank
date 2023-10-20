#from scriptDB import reconstruirCliente
from clientClass import ClienteClassic
from clientClass import ClienteGold
from clientClass import ClienteBlack
from scriptDB import buscarDniCliente

#c1 = ClienteClassic("Lucas","De Ameller",123456789,None,None,None,None,None,None,None,None,None,None,None,None,None,None,"creating")

#reconstruirCliente(123456789)
statePointer = buscarDniCliente(1234567809)
stateIndex = 0
print(statePointer[stateIndex])