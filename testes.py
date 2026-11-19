import unittest
from regras import analisar_respostas

class TesteRegrasTriagem(unittest.TestCase):
    def base(self):
        return {
            "falta_ar": "Não",
            "dor_peito": "Não",
            "tipo_tosse": "Não se aplica",
            "tabagismo": "Não",
        }

    def test_alerta_cianose(self):
        respostas = self.base()
        respostas["cianose"] = True
        resultado = analisar_respostas(respostas)
        self.assertTrue(any("Coloração azulada" in a for a in resultado["alertas"]))

    def test_padrao_rinite(self):
        respostas = self.base()
        respostas.update({
            "espirros": True,
            "coriza": True,
            "coceira": True
        })
        resultado = analisar_respostas(respostas)
        self.assertTrue(any("rinite alérgica" in a["condicao"] for a in resultado["associacoes"]))

    def test_sem_resposta_nao_gera_associacao(self):
        resultado = analisar_respostas(self.base())
        self.assertEqual(resultado["associacoes"], [])

if __name__ == "__main__":
    unittest.main()
