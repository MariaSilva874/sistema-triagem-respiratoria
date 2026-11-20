import streamlit as st
from regras import analisar_respostas

st.set_page_config(
    page_title="Sistema de Triagem Respiratória",
    layout="centered"
)

st.title("Sistema Especialista para Triagem Inicial de Sintomas Respiratórios")

st.warning(
    "Este protótipo não realiza diagnóstico, não recomenda medicamentos "
    "e não substitui avaliação de um profissional de saúde."
)

st.markdown(
    "Preencha as informações abaixo. O sistema verificará primeiro sinais de alerta e, "
    "em seguida, apresentará padrões de sintomas que podem estar associados a algumas "
    "condições respiratórias."
)

with st.form("formulario_sintomas"):
    st.header("1. Informações gerais")
    idade = st.number_input("Idade", min_value=18, max_value=120, value=18, step=1)
    historico_asma = st.checkbox("Possui histórico de asma?")
    historico_rinite = st.checkbox("Possui histórico de rinite ou alergias?")
    historico_dpoC = st.checkbox("Possui histórico de DPOC ou bronquite crônica?")
    tabagismo = st.selectbox(
        "Histórico de tabagismo",
        ["Não", "Sim, atualmente", "Sim, no passado", "Prefiro não informar"]
    )

    st.header("2. Sintomas principais")
    tosse = st.checkbox("Tosse")
    tipo_tosse = st.selectbox(
        "Tipo de tosse",
        ["Não se aplica", "Seca", "Com secreção", "Mista"]
    )
    falta_ar = st.selectbox(
        "Falta de ar",
        ["Não", "Ao realizar esforço", "Em atividades leves", "Mesmo em repouso"]
    )
    dor_peito = st.selectbox(
        "Dor ou aperto no peito",
        ["Não", "Ao tossir", "Ao respirar profundamente", "Durante esforço", "Em repouso ou persistente"]
    )
    cansaco = st.checkbox("Cansaço ou fadiga")
    chiado = st.checkbox("Chiado no peito")

    st.header("3. Sintomas de vias aéreas superiores")
    coriza = st.checkbox("Coriza (nariz escorrendo)")
    congestao = st.checkbox("Nariz entupido")
    espirros = st.checkbox("Espirros frequentes")
    coceira = st.checkbox("Coceira no nariz, garganta ou olhos")
    dor_garganta = st.checkbox("Dor de garganta")
    olhos_lacrimejando = st.checkbox("Olhos lacrimejando ou irritados")

    st.header("4. Sintomas gerais")
    febre = st.checkbox("Febre")
    calafrios = st.checkbox("Calafrios")
    dores_musculares = st.checkbox("Dores musculares")
    dor_cabeca = st.checkbox("Dor de cabeça")

    st.header("5. Duração e evolução")
    duracao = st.selectbox(
        "Há quanto tempo os sintomas começaram?",
        ["Hoje", "Há 2 a 3 dias", "Há 4 a 7 dias", "Há 8 a 14 dias", "Há mais de 14 dias"]
    )
    evolucao = st.selectbox(
        "Como os sintomas estão evoluindo?",
        ["Melhorando", "Sem alterações", "Piorando", "Pioraram rapidamente", "Melhoraram e depois voltaram"]
    )
    gatilho_alergico = st.checkbox("Os sintomas aparecem ou pioram com poeira, pólen, mofo ou contato com animais?")
    sintomas_recorrentes = st.checkbox("Já teve episódios semelhantes anteriormente?")

    st.header("6. Sinais de esforço respiratório")
    dificuldade_falar = st.checkbox("Está com dificuldade para completar frases curtas por falta de ar?")
    respiracao_rapida = st.checkbox("Está respirando muito rápido mesmo em repouso?")
    retracoes = st.checkbox("Percebe afundamento entre as costelas ou na região abaixo delas ao respirar?")
    uso_musculos_pescoco = st.checkbox("Percebe esforço dos músculos do pescoço para respirar?")
    batimento_nasal = st.checkbox("Percebe abertura excessiva das narinas ao respirar?")

    st.header("7. Sinais de alerta")
    cianose = st.checkbox("Lábios, rosto ou língua azulados/arroxeados")
    confusao = st.checkbox("Confusão mental, desorientação ou sonolência fora do normal")
    estridor = st.checkbox("Ruído agudo ao inspirar (ao puxar o ar)")
    pressao_persistente = st.checkbox("Pressão ou dor forte e persistente no peito")
    piora_rapida = st.checkbox("Piora rápida e importante do estado geral")

    st.header("8. Informações complementares")
    possui_oximetro = st.radio("Possui oxímetro?", ["Não", "Sim"], horizontal=True)
    spo2 = None
    if possui_oximetro == "Sim":
        spo2 = st.number_input(
            "Saturação indicada pelo aparelho (%) — opcional",
            min_value=50, max_value=100, value=98, step=1,
            help="O valor será exibido como informação. Este protótipo não o usa para definir diagnóstico ou urgência."
        )

    enviado = st.form_submit_button("Analisar respostas", use_container_width=True)

if enviado:
    respostas = {
        "idade": idade,
        "historico_asma": historico_asma,
        "historico_rinite": historico_rinite,
        "historico_dpoc": historico_dpoC,
        "tabagismo": tabagismo,
        "tosse": tosse,
        "tipo_tosse": tipo_tosse,
        "falta_ar": falta_ar,
        "dor_peito": dor_peito,
        "cansaco": cansaco,
        "chiado": chiado,
        "coriza": coriza,
        "congestao": congestao,
        "espirros": espirros,
        "coceira": coceira,
        "dor_garganta": dor_garganta,
        "olhos_lacrimejando": olhos_lacrimejando,
        "febre": febre,
        "calafrios": calafrios,
        "dores_musculares": dores_musculares,
        "dor_cabeca": dor_cabeca,
        "duracao": duracao,
        "evolucao": evolucao,
        "gatilho_alergico": gatilho_alergico,
        "sintomas_recorrentes": sintomas_recorrentes,
        "dificuldade_falar": dificuldade_falar,
        "respiracao_rapida": respiracao_rapida,
        "retracoes": retracoes,
        "uso_musculos_pescoco": uso_musculos_pescoco,
        "batimento_nasal": batimento_nasal,
        "cianose": cianose,
        "confusao": confusao,
        "estridor": estridor,
        "pressao_persistente": pressao_persistente,
        "piora_rapida": piora_rapida,
        "spo2": spo2,
    }

    resultado = analisar_respostas(respostas)

    st.divider()
    st.header("Resultado da análise")

    if resultado["alertas"]:
        st.error("Foram identificados sinais de alerta")
        st.markdown(
            "Os sinais selecionados podem indicar uma situação que precisa de avaliação "
            "imediata. **Procure um serviço de emergência, conforme "
            "a gravidade.**"
        )
        for alerta in resultado["alertas"]:
            st.write(f"- {alerta}")
    else:
        st.success("Nenhum dos sinais de alerta cadastrados foi selecionado.")
        st.info(
            "Isso não garante que a situação seja segura nem exclui a necessidade de "
            "avaliação profissional. Procure atendimento se houver piora, preocupação "
            "ou sintomas persistentes."
        )

    if resultado["associacoes"]:
        st.subheader("Padrões de sintomas identificados")
        st.write(
            "As condições abaixo são apenas associações possíveis entre sintomas "
            "informados e padrões descritos na base de regras. Não representam diagnóstico."
        )
        for item in resultado["associacoes"]:
            with st.container(border=True):
                st.markdown(f"**{item['condicao']}**")
                st.write(item["explicacao"])
                st.caption("Regras acionadas: " + ", ".join(item["regras"]))
    else:
        st.subheader("Resultado inconclusivo")
        st.write(
            "As respostas não corresponderam de forma suficiente aos padrões cadastrados. "
            "Isso não significa ausência de doença. Considere avaliação profissional."
        )
