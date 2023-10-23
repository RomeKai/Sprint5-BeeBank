def buscarDniCliente(fdni,fClientes):
    if len(fClientes)>0:
        for cliente in fClientes:
            if cliente.getDni()==fdni:
                return [True,fClientes.index(cliente)]
    return [False,0]