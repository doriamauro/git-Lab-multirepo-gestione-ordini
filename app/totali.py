"""Calcolo importi ordini."""

def totale_ordine(prezzo_unitario, quantita):
    if prezzo_unitario < 0 or quantita <= 0:
        raise ValueError("Prezzo e quantita non validi")
    return round(prezzo_unitario * quantita, 2)
