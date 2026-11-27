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

    def regras_acionadas(self, resultado):
        regras = set()

        for associacao in resultado["associacoes"]:
            regras.update(associacao["regras"])

        return regras

    # GRUPO 1 - TESTES DAS REGRAS DE ASSOCIAÇÃO
    def test_CT01_resfriado(self):
        respostas = self.base()
        respostas.update({
            "coriza": True,
            "espirros": True
        })

        resultado = analisar_respostas(respostas)

        self.assertIn("R01", self.regras_acionadas(resultado))

    def test_CT02_sindrome_gripal(self):
        respostas = self.base()
        respostas.update({
            "febre": True,
            "tosse": True,
            "dores_musculares": True
        })

        resultado = analisar_respostas(respostas)

        self.assertIn("R02", self.regras_acionadas(resultado))

    def test_CT03_asma(self):
        respostas = self.base()
        respostas.update({
            "chiado": True,
            "falta_ar": "Ao realizar esforço",
            "historico_asma": True
        })

        resultado = analisar_respostas(respostas)

        self.assertIn("R03", self.regras_acionadas(resultado))

    def test_CT04_bronquite_aguda(self):
        respostas = self.base()
        respostas.update({
            "tosse": True,
            "tipo_tosse": "Com secreção",
            "cansaco": True
        })

        resultado = analisar_respostas(respostas)

        self.assertIn("R04", self.regras_acionadas(resultado))

    def test_CT05_rinite_e_sobreposicao(self):
        respostas = self.base()
        respostas.update({
            "espirros": True,
            "coriza": True,
            "coceira": True
        })

        resultado = analisar_respostas(respostas)

        regras = self.regras_acionadas(resultado)

        # O comportamento atual aciona R01 e R05.
        # A sobreposição está documentada na avaliação do CT05.
        self.assertIn("R01", regras)
        self.assertIn("R05", regras)

    def test_CT06_historico_dpoc(self):
        respostas = self.base()
        respostas["historico_dpoc"] = True

        resultado = analisar_respostas(respostas)

        self.assertIn("R06", self.regras_acionadas(resultado))

    # GRUPO 2 - TESTES NEGATIVOS E MULTIPLAS REGRAS
    def test_CT07_sindrome_gripal_sem_criterios_completos(self):
        respostas = self.base()
        respostas.update({
            "febre": True,
            "tosse": True
        })

        resultado = analisar_respostas(respostas)

        self.assertNotIn("R02", self.regras_acionadas(resultado))
        self.assertEqual(resultado["associacoes"], [])

    def test_CT08_multiplas_associacoes(self):
        respostas = self.base()
        respostas.update({
            "espirros": True,
            "coriza": True,
            "coceira": True,
            "febre": True,
            "tosse": True,
            "dores_musculares": True
        })

        resultado = analisar_respostas(respostas)

        regras = self.regras_acionadas(resultado)

        self.assertTrue({"R01", "R02", "R05"}.issubset(regras))
        self.assertEqual(len(resultado["associacoes"]), 3)

    def test_CT09_respiracao_rapida_sem_esforco(self):
        respostas = self.base()
        respostas["respiracao_rapida"] = True

        resultado = analisar_respostas(respostas)

        self.assertFalse(
            any("esforço respiratório" in alerta
                for alerta in resultado["alertas"])
        )

    def test_CT10_tosse_seca_nao_ativa_bronquite(self):
        respostas = self.base()
        respostas.update({
            "tosse": True,
            "tipo_tosse": "Seca",
            "cansaco": True
        })

        resultado = analisar_respostas(respostas)

        self.assertNotIn("R04", self.regras_acionadas(resultado))

    # GRUPO 3 - TESTES DAS REGRAS DE SEGURANÇA
    def test_RA01_dificuldade_respiratoria(self):
        # Verifica as duas possibilidades previstas na regra.
        casos = [
            {"dificuldade_falar": True},
            {"falta_ar": "Mesmo em repouso"}
        ]

        for respostas_adicionais in casos:
            with self.subTest(respostas=respostas_adicionais):
                respostas = self.base()
                respostas.update(respostas_adicionais)

                resultado = analisar_respostas(respostas)

                self.assertTrue(
                    any("Falta de ar intensa" in alerta
                        for alerta in resultado["alertas"])
                )

    def test_RA02_cianose(self):
        respostas = self.base()
        respostas["cianose"] = True

        resultado = analisar_respostas(respostas)

        self.assertTrue(
            any("Coloração azulada" in alerta
                for alerta in resultado["alertas"])
        )

    def test_RA03_confusao_mental(self):
        respostas = self.base()
        respostas["confusao"] = True

        resultado = analisar_respostas(respostas)

        self.assertTrue(
            any("Confusão mental" in alerta
                for alerta in resultado["alertas"])
        )

    def test_RA04_estridor(self):
        respostas = self.base()
        respostas["estridor"] = True

        resultado = analisar_respostas(respostas)

        self.assertTrue(
            any("estridor" in alerta
                for alerta in resultado["alertas"])
        )

    def test_RA05_pressao_persistente(self):
        respostas = self.base()
        respostas["pressao_persistente"] = True

        resultado = analisar_respostas(respostas)

        self.assertTrue(
            any("Pressão ou dor forte" in alerta
                for alerta in resultado["alertas"])
        )

    def test_RA06_piora_rapida(self):
        respostas = self.base()
        respostas["piora_rapida"] = True

        resultado = analisar_respostas(respostas)

        self.assertTrue(
            any("Piora rápida" in alerta
                for alerta in resultado["alertas"])
        )

    def test_RA07_esforco_respiratorio(self):
        respostas = self.base()
        respostas.update({
            "respiracao_rapida": True,
            "retracoes": True
        })

        resultado = analisar_respostas(respostas)

        self.assertTrue(
            any("esforço respiratório" in alerta
                for alerta in resultado["alertas"])
        )

    # GRUPO 4 - TESTES COMPLEMENTARES DE SEGURANÇA
    def test_alertas_simultaneos(self):
        respostas = self.base()
        respostas.update({
            "dificuldade_falar": True,
            "cianose": True,
            "confusao": True
        })

        resultado = analisar_respostas(respostas)

        self.assertGreaterEqual(len(resultado["alertas"]), 3)

        self.assertTrue(
            any("Falta de ar intensa" in alerta
                for alerta in resultado["alertas"])
        )
        self.assertTrue(
            any("Coloração azulada" in alerta
                for alerta in resultado["alertas"])
        )
        self.assertTrue(
            any("Confusão mental" in alerta
                for alerta in resultado["alertas"])
        )

    def test_alerta_e_associacao_simultaneos(self):
        respostas = self.base()
        respostas.update({
            "cianose": True,
            "coriza": True,
            "espirros": True
        })

        resultado = analisar_respostas(respostas)

        self.assertTrue(len(resultado["alertas"]) > 0)
        self.assertIn("R01", self.regras_acionadas(resultado))

    def test_entrada_sem_sintomas_resultado_inconclusivo(self):
        resultado = analisar_respostas(self.base())

        self.assertEqual(resultado["alertas"], [])
        self.assertEqual(resultado["associacoes"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
