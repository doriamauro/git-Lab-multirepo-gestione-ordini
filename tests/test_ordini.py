from app.ordini import aggiungi_ordine
from app.totali import totale_ordine


def test_ordine_e_totale():
    ordine = aggiungi_ordine("P01", 3)
    assert ordine["quantita"] == 3
    assert totale_ordine(12.5, 3) == 37.5
