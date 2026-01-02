import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Manual Saipos Balança",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stDeployButton {display:none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título Principal
st.title("⚖️ Assistente de Balanças")
st.markdown("---")

# NAVEGAÇÃO POR ABAS
tab_oraculo, tab_mercado, tab_drivers, tab_incomp = st.tabs([
    "📘 Manual Oráculo", 
    "🛠️ Outras Config de Mercado", 
    "💾 Instalação de Drivers (Guia)",
    "🚫 Incompatíveis"
])

# ABA 1: MANUAL ORÁCULO (Procedimentos Detalhados)
with tab_oraculo:
    st.header("📋 Procedimentos Oficiais")
    st.caption("Baseado estritamente na documentação interna do Oráculo.")
    
    modelo_oficial = st.selectbox(
        "Selecione o modelo do cliente:",
        ["Selecione...", "Toledo (Prix 3 Fit, 3 Plus, 4)", "Urano (Pop, Top)"]
    )

    if modelo_oficial == "Toledo (Prix 3 Fit, 3 Plus, 4)":
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("🔧 **1. Configuração Física (Botões da Balança)**")
            st.markdown("""
            **Senha Padrão:** `2011`
            
            1. Tecle `MODO` ➡️ Digite `2011` ➡️ Tecle `MODO`.
            2. **Parâmetro C11 (Filtro):** Mude para **F3**.
               * *Motivo:* F1 é muito sensível (instável), F9 é muito lento.
            3. **Parâmetro C14 (Protocolo):** Mude para **PRT2**.
            4. **Parâmetro C15 (Baud):** Mude para **4800**.
            5. **Parâmetro C16 (Transmissão):** Mude para **L**.
               * *Motivo:* Ativa transmissão contínua.
            6. Tecle `CÓDIGO` para salvar e sair.
            """)
            
        with col2:
            st.success("🖥️ **2. No Software Saipos**")
            st.markdown("""
            * **Modelo:** `Toledo2180` (Recomendado) ou `Toledo`
            * **Baud Rate:** `4800`
            * **Data Bits:** `7`
            * **Parity:** `Even` (Par)
            * **Stop Bits:** `1`
            * **Timeout:** `6` segundos
            """)

    elif modelo_oficial == "Urano (Pop, Top)":
        st.error("⚠️ **Erro Comum: TimeOut**")
        st.markdown("""
        **Causa:** Protocolo incorreto na balança envia dados de validade/código que travam o sistema.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("🔧 **1. Configuração Física**")
            st.markdown("""
            Verifique o protocolo digitando `[F]` + `[3]` na balança.
            * O visor deve mostrar **PROT 1**.
            * Se estiver diferente, pressione `[P]` para alterar e `[E]` para salvar.
            """)
            
        with col2:
            st.success("🖥️ **2. No Software Saipos**")
            st.markdown("""
            * **Modelo:** `Urano` ou `UranoPOP`
            * **Baud Rate:** `9600`
            * **Data Bits:** `8`
            * **Parity:** `None`
            * **Stop Bits:** `1`
            * **Timeout:** `6` segundos
            """)

# ABA 2: OUTRAS CONFIG DE MERCADO (Alternativas)
with tab_mercado:
    st.header("🛠️ Configurações Genéricas e Alternativas")
    st.markdown("Use estas opções para marcas que não estão no manual oficial ou quando o padrão falhar.")
    
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        st.subheader("Elgin / Filizola")
        st.caption("Padrão da Linha DP")
        st.markdown("""
        * **Modelo:** `Filizola`
        * **Baud Rate:** `9600`
        * **Data Bits:** `8`
        * **Parity:** `None` (Nenhuma)
        * **Stop Bits:** `1`
        * **Timeout:** `6` segundos
        """)
        
    with col_b:
        st.subheader("Urano (Alternativa)")
        st.caption("Opção de Contorno")
        st.markdown("""
        * **Modelo:** `Filizola`
        * **Baud Rate:** `9600`
        * **Data Bits:** `8`
        * **Parity:** `None` (Nenhuma)
        * **Stop Bits:** `1`
        * **Timeout:** `6` segundos
        """)

    with col_c:
        st.subheader("Genéricas / China")
        st.caption("Balmak, Ramuza, Micheletti")
        st.markdown("""
        * **Modelo:** `Generica`
        * **Baud Rate:** `9600`
        * **Data Bits:** `8`
        * **Parity:** `None` (Nenhuma)
        * **Stop Bits:** `1`
        * **Timeout:** `6` segundos
        """)

    with col_d:
        st.subheader("Toledo (Legado)")
        st.caption("Padrão Antigo")
        st.markdown("""
        * **Modelo:** `Toledo`
        * **Baud Rate:** `2400` ou `9600`
        * **Data Bits:** `7`
        * **Parity:** `Even` (Par)
        * **Stop Bits:** `1`
        * **Timeout:** `6` segundos
        """)

    st.divider()

    # MENU RETÁTIL: MAIS OPÇÕES
    with st.expander("❓ Não deu certo? Verifique mais opções (Combinações Extras)"):
        st.markdown("Teste estas combinações caso as principais falhem. Útil para adaptadores USB antigos ou balanças desconfiguradas.")
        
        col_alt1, col_alt2, col_alt3 = st.columns(3)
        
        with col_alt1:
            st.markdown("### 1. Toledo (8 Bits / Sem Paridade)")
            st.markdown("*Útil quando o adaptador USB não suporta 7 bits/Par.*")
            st.code("""
Modelo: Toledo2180 (ou Toledo)
Baud Rate: 9600
Data Bits: 8  <-- Mudança
Parity: None  <-- Mudança
Stop Bits: 1
Timeout: 6
            """, language="text")

        with col_alt2:
            st.markdown("### 2. Genéricas (Lentas)")
            st.markdown("*Para balanças chinesas antigas ou cabos ruins.*")
            st.code("""
Modelo: Generica
Baud Rate: 4800 (ou 2400)
Data Bits: 8
Parity: None
Stop Bits: 1
Timeout: 6
            """, language="text")

        with col_alt3:
            st.markdown("### 3. Filizola/Elgin (Variação)")
            st.markdown("*Alguns modelos antigos da Elgin usam essa config.*")
            st.code("""
Modelo: Filizola
Baud Rate: 2400
Data Bits: 8
Parity: None
Stop Bits: 1
Timeout: 6
            """, language="text")

# ABA 3: DRIVERS 
with tab_drivers:
    st.header("💾 Solução de Problemas: Driver CH340")
    st.warning("⚠️ Sintomas: Erro 'Time Out', 'Communication Error 31' ou a Porta COM não aparece.")
    
    st.markdown("### 🚀 Passo a Passo de Instalação (Método Manual)")
    
    st.markdown("""
    **1. Baixar e Extrair:**
    - Baixe o driver **CH341SER**.
    - Extraia a pasta em um local fácil (ex: Área de Trabalho).
    """)
    st.write("") # Espaço em branco
    
    st.markdown("""
    **2. Abrir Gerenciador:**
    - Pressione `Win + R` no teclado.
    - Digite `devmgmt.msc` e dê Enter.
    - Vá em **Outros Dispositivos** ou **Portas (COM e LPT)** e ache o dispositivo com erro (ex: *USB-SERIAL CH340*).
    """)
    st.write("") 
    
    st.markdown("""
    **3. Atualizar Driver:**
    - Clique com o botão **direito** no dispositivo > **Atualizar Driver**.
    - Selecione: **"Procurar drivers no meu computador"**.
    """)
    st.write("") 
    
    st.markdown("""
    **4. Selecionar da Lista (Importante!):**
    - Clique em: **"Permitir que eu escolha em uma lista de drivers disponíveis em meu computador"**.
    """)
    st.write("") 
    
    st.markdown("""
    **5. Usar Disco:**
    - Clique no botão **"Com Disco..."**.
    - Clique em **"Procurar..."** e vá até a pasta onde você extraiu o driver.
    - Selecione o arquivo `.inf` e clique em OK.
    """)
    st.write("") 
    
    st.markdown("""
    **6. Finalizar:**
    - O Windows mostrará o modelo (ex: *USB-SERIAL CH340 Versão...*).
    - Clique em **Avançar** e depois **Fechar**.
    """)
    
    st.divider()
    
    st.markdown("### 🛡️ Passo 2: Bloquear Atualização Automática (Obrigatório)")
    st.error("Se não fizer isso, o Windows vai atualizar o driver sozinho e a balança vai parar de funcionar amanhã.")
    
    st.markdown("""
    1. Pressione `Win + R`, digite `sysdm.cpl` e dê Enter.
    2. Vá na aba **Hardware**.
    3. Clique no botão **Configurações de Instalação do Dispositivo**.
    4. Marque a opção **NÃO (o dispositivo poderá não funcionar...)**.
    5. Clique em **Salvar Alterações**.
    """)

# ABA 4: INCOMPATÍVEIS
with tab_incomp:
    st.header("🚫 Balanças Não Homologadas")
    st.error("Estes modelos NÃO funcionam com o Saipos Balança (Serial).")
    
    st.markdown("""
    De acordo com o documento 'Oráculo', os motivos da incompatibilidade são:

    ### ❌ Toledo Prix 5, Prix 6 e Atena II
    * **Motivo:** Estas balanças etiquetadoras não costumam usar cabo serial para conexão e, quando utilizam, **somente comunicam com o seu sistema próprio** da fabricante, bloqueando integrações externas.

    ### ❌ Toledo Prix 4 Uno (Versão 8)
    * **Motivo:** A configuração desta balança depende exclusivamente de um aplicativo da Toledo que **não é compatível com a Saipos**.
    
    ### ⚠️ Sistemas Antigos Instalados (Erro Comum)
    * **Sintoma:** "COMMUNICATION ERROR 5: ACESSO NEGADO".
    * **Motivo:** Clientes que usavam outros sistemas de balança podem ter a porta COM "sequestrada" pelo driver antigo. É necessário desinstalar os programas de pesagem anteriores.
    """)
    
    st.divider()
    
    st.info("💡 **Orientação Final:** Nesses casos, o cliente deve utilizar a pesagem manual.")