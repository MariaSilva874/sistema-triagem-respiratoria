def analisar_respostas(r):
    alertas = []
    associacoes = []

    # 1. Regras de segurança: avaliadas antes das associações.
    if r.get("dificuldade_falar") or r.get("falta_ar") == "Mesmo em repouso":
        alertas.append(
            "Falta de ar intensa ou dificuldade para falar por falta de ar."
        )

    if r.get("cianose"):
        alertas.append("Coloração azulada/arroxeada em lábios, rosto ou língua.")

    if r.get("confusao"):
        alertas.append("Confusão mental, desorientação ou sonolência anormal.")

    if r.get("estridor"):
        alertas.append("Ruído agudo ao inspirar (estridor).")

    if r.get("pressao_persistente"):
        alertas.append("Pressão ou dor forte e persistente no peito.")

    if r.get("piora_rapida"):
        alertas.append("Piora rápida e importante do estado geral.")

    if r.get("respiracao_rapida") and (
        r.get("retracoes") or r.get("uso_musculos_pescoco") or r.get("batimento_nasal")
    ):
        alertas.append(
            "Respiração rápida associada a sinais de esforço respiratório."
        )

    # 2. Regras de associação.
    # Resfriado / infecção de vias aéreas superiores
    if (
        (r.get("coriza") or r.get("congestao"))
        and (r.get("espirros") or r.get("dor_garganta") or r.get("tosse"))
    ):
        associacoes.append({
            "condicao": "Padrão compatível com resfriado ou infecção de vias aéreas superiores",
            "explicacao": (
                "A combinação de sintomas nasais com espirros, dor de garganta "
                "ou tosse pode ocorrer em infecções das vias aéreas superiores."
            ),
            "regras": ["R01"]
        })

    # Síndrome gripal / padrão semelhante à influenza
    if r.get("febre") and r.get("tosse") and (
        r.get("dores_musculares") or r.get("calafrios") or r.get("dor_cabeca")
    ):
        associacoes.append({
            "condicao": "Padrão semelhante à síndrome gripal",
            "explicacao": (
                "Febre e tosse associadas a dores musculares, calafrios ou dor de cabeça "
                "podem compor um quadro semelhante à síndrome gripal."
            ),
            "regras": ["R02"]
        })

    # Padrão associado à asma
    if r.get("chiado") and (
        r.get("falta_ar") in ["Ao realizar esforço", "Em atividades leves", "Mesmo em repouso"]
        or r.get("dor_peito") == "Não"
    ) and (r.get("historico_asma") or r.get("sintomas_recorrentes")):
        associacoes.append({
            "condicao": "Padrão de sintomas que pode estar associado à asma",
            "explicacao": (
                "Chiado, falta de ar ou sintomas recorrentes, especialmente com histórico "
                "de asma, podem ser observados em quadros asmáticos."
            ),
            "regras": ["R03"]
        })

    # Padrão associado à bronquite aguda
    if r.get("tosse") and r.get("tipo_tosse") in ["Com secreção", "Mista"] and (
        r.get("cansaco") or r.get("dor_peito") == "Ao tossir" or r.get("chiado")
    ):
        associacoes.append({
            "condicao": "Padrão de sintomas que pode estar associado à bronquite aguda",
            "explicacao": (
                "Tosse com secreção ou mista acompanhada de cansaço, desconforto ao tossir "
                "ou chiado pode ocorrer em quadros de bronquite. A causa precisa de avaliação."
            ),
            "regras": ["R04"]
        })

    # Padrão associado à rinite alérgica
    if r.get("espirros") and (r.get("coriza") or r.get("congestao")) and (
        r.get("coceira") or r.get("olhos_lacrimejando") or r.get("gatilho_alergico")
    ):
        associacoes.append({
            "condicao": "Padrão compatível com rinite alérgica",
            "explicacao": (
                "Espirros, coriza ou congestão associados a coceira, irritação ocular "
                "ou exposição a possíveis alérgenos podem ocorrer na rinite alérgica."
            ),
            "regras": ["R05"]
        })

    # Acrescenta contexto de histórico sem inferir uma condição.
    if r.get("historico_dpoc") or r.get("tabagismo") in ["Sim, atualmente", "Sim, no passado"]:
        associacoes.append({
            "condicao": "Fator de histórico relevante",
            "explicacao": (
                "O histórico informado de DPOC/bronquite crônica ou tabagismo é um dado "
                "importante para a avaliação profissional, mas não permite classificação "
                "automática neste protótipo."
            ),
            "regras": ["R06"]
        })

    return {
        "alertas": alertas,
        "associacoes": associacoes
    }
