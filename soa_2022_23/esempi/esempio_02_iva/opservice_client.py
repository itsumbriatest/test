import utils

class OpService:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8080/"
        self.somma = self.op_binaria("somma")
        self.sottrazione = self.op_binaria("sottrazione")
        self.moltiplicazione = self.op_binaria("moltiplicazione")
        self.divisione = self.op_binaria("divisione")
        self.potenza = self.op_binaria("potenza")
        self.log10 = self.op_unaria("log10")
        self.sqrt = self.op_unaria("sqrt")
    
    def op_binaria(self, nome):
        def f(a, b):
            url = self.base_url + f"{nome}?x={a}&y={b}"
            return float(utils.get(url))
        return f
    
    def op_unaria(self, nome):
        def f(a):
            url = self.base_url + f"{nome}?x={a}"
            return float(utils.get(url))
        return f