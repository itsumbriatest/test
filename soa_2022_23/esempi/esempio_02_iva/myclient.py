import opservice_client
import utils

op = opservice_client.OpService()
print("Test del servizio OpService")
print(op.somma(-15.5, 12.3))
print(op.log10(1239432432.432432432))

print("Test del servizio IVA")
prezzo = 10
iva = utils.get(f"http://127.0.0.1:8081/iva?prezzo={prezzo}")
print(f"L'IVA su {prezzo} € è di {iva} €")
