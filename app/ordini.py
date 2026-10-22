"""Gestione ordini: primo modulo del laboratorio."""

ORDINI = []

def aggiungi_ordine(codice, quantita):
    ordine = {"codice": codice, "quantita": quantita}
    ORDINI.append(ordine)
    return ordine
