import streamlit as st

st.set_page_config(
    page_title="Manual Saipos Balança",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_bar = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {
        visibility: hidden;
        display: none;
    }
    .block-container {
        padding-top: 1rem;
    }
    </style>
"""
st.markdown(hide_bar, unsafe_allow_html=True)

st.title("⚖️ Assistente de Balanças")
st.markdown("---")

# NAVEGAÇÃO
tab_oraculo, tab_mercado, tab_drivers, tab_incomp, tab_detalhes, tab_modelos = st.tabs([
    "📘 Manual Oráculo", 
    "🛠️ Outras Config de Mercado", 
    "💾 Instalação de Drivers",
    "🚫 Incompatíveis",
    "ℹ️ Detalhes Técnicos",
    "📂 Modelos Disponíveis"
])

# ABA 1: ORÁCULO
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

# ABA 2: OUTRAS CONFIG DE MERCADO
with tab_mercado:
    st.header("🛠️ Configurações Genéricas e Alternativas")
    st.markdown("Use estas opções para marcas que não estão no manual oficial ou quando o padrão falhar.")
    
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
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

    with col_d:
        st.subheader("Genéricas")
        st.caption("Balmak, Ramuza, Micheletti")
        st.markdown("""
        * **Modelo:** `Generica`
        * **Baud Rate:** `9600`
        * **Data Bits:** `8`
        * **Parity:** `None` (Nenhuma)
        * **Stop Bits:** `1`
        * **Timeout:** `6` segundos
        """)

    st.divider()

    with st.expander("❓ Não deu certo? Verifique mais opções (Combinações Extras)"):
        st.markdown("Teste estas combinações caso as principais falhem.")
        
        st.markdown("### 🎯 Toledo Prix 3 Fit (Variações)")
        
        col_prix1, col_prix2, col_prix3 = st.columns(3)
        
        with col_prix1:
            st.markdown("**1. Padrão de Fábrica (Sem Configurar)**")
            st.markdown("Tente esta se o cliente tirou da caixa agora.")
            st.code("""
Modelo: Toledo
Baud Rate: 9600
Data Bits: 7
Parity: Even
Stop Bits: 1
            """, language="text")
            st.caption("Se falhar, teste Baud Rate 2400.")

        with col_prix2:
            st.markdown("**2. Adaptador Genérico**")
            st.markdown("Use se o cabo USB não suportar 7 bits.")
            st.code("""
Modelo: Toledo2180
Baud Rate: 9600
Data Bits: 8
Parity: None
Stop Bits: 1
            """, language="text")
            
        with col_prix3:
            st.markdown("**3. Lenta/Estável (Requer ajuste)**")
            st.markdown("Na balança, mude C15 para `2400`.")
            st.code("""
Modelo: Toledo
Baud Rate: 2400
Data Bits: 7
Parity: Even
Stop Bits: 1
            """, language="text")

        st.divider()
        st.markdown("### 🔄 Outras Marcas")
        
        col_alt1, col_alt2 = st.columns(2)
        with col_alt1:
            st.markdown("**Genéricas (Lentas)**")
            st.code("""
Modelo: Generica
Baud Rate: 4800
Data Bits: 8
Parity: None
Stop Bits: 1
            """, language="text")

        with col_alt2:
            st.markdown("**Filizola (Lenta)**")
            st.code("""
Modelo: Filizola
Baud Rate: 2400
Data Bits: 8
Parity: None
Stop Bits: 1
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
    st.write("")
    
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

# ABA 5: DETALHES
with tab_detalhes:
    st.header("ℹ️ Glossário Técnico: Entendendo o Saipos Balança")
    st.markdown("Diagnóstico rápido e explicação dos campos.")
    
    st.subheader("1. Diagnóstico de Erros (Peso -9 ou 0)")
    
    col_err1, col_err2 = st.columns(2)
    
    with col_err1:
        st.error("📉 **Peso Negativo (-9 ou -9000)**")
        st.markdown("**Causa: Falha de Comunicação (Física ou Driver).**")
        st.markdown("""
        O sistema tentou abrir a porta, mas não achou nada.
        * **Verifique:**
            1. Porta COM incorreta (mudou sozinha?).
            2. Cabo USB desconectado ou com mal contato.
            3. Driver do cabo parou de funcionar (Windows 11).
        """)
        
    with col_err2:
        st.warning("0️⃣ **Peso Zerado (0)**")
        st.markdown("**Causa: Falha de Configuração.**")
        st.markdown("""
        A balança está conectada, mas o sistema não entende o que ela fala.
        * **Verifique:**
            1. **Protocolo:** Urano fora do `PROT 1` envia lixo (validade/preço).
            2. **Handshaking:** Deve estar em "Nenhum".
        """)

    st.divider()

    st.subheader("2. Significado dos Campos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("Modelo Balança (Protocolo)", expanded=False):
            st.markdown("""
            **O que é:** É o "idioma" que a balança fala (ex: a Toledo manda `STX 00.500kg`).
            * **Dica:** Se o peso aparece com caracteres estranhos, o modelo está errado.
            """)
            
        with st.expander("Porta Serial (COM)", expanded=False):
            st.markdown("""
            **O que é:** O endereço do USB no Windows (COM1, COM3, etc).
            * **Importante:** Se trocar o cabo de porta USB, esse número muda!
            """)

        with st.expander("Data Bits (Tamanho)", expanded=False):
            st.markdown("""
            **O que é:** O tamanho do "pacote" de informação que a balança envia por vez.
            * **7 Bits:** Padrão antigo (Toledo).
            * **8 Bits:** Padrão moderno (Geral).
            
            **Regra de Ouro:**
            * **Toledo:** Usa **7**.
            * **Todas as outras:** Usam **8**.
            """)

    with col2:
        with st.expander("Baud Rate (Velocidade)", expanded=False):
            st.markdown("""
            **O que é:** Velocidade da transmissão.
            * **Padrão:** 9600 (maioria), 4800/2400 (Toledo). Se errar, os dados chegam corrompidos.
            """)
            
        with st.expander("Parity (Paridade / Erro)", expanded=False):
            st.markdown("""
            **O que é:** Método de segurança para checar se a informação chegou corrompida.
            * **Even (Par):** Verifica se o número de bits é par.
            * **None (Nenhuma):** Sem verificação.
            
            **Regra de Ouro:**
            * **Toledo:** Usa **Even (Par)**.
            * **Todas as outras:** Usam **None (Nenhuma)**.
            """)
            
        with st.expander("Timeout Pesagem", expanded=False):
            st.markdown("""
            **O que é:** Tempo de espera antes de dar erro.
            * **Padrão:** 6 segundos. Aumente para balanças velhas.
            """)

# ABA 6: MODELOS
with tab_modelos:
    st.header("📂 Lista de Modelos Disponíveis")
    st.markdown("Guia rápido para saber qual opção selecionar na lista 'Modelo Balança' do software.")
    
    col_toledo, col_geral = st.columns(2)
    
    with col_toledo:
        st.subheader("🟢 Toledo")
        st.markdown("Opções específicas para balanças Prix.")
        
        st.markdown("""
        * **Toledo2180:** 🏆 **(Recomendado)** O driver mais moderno e estável para Prix 3, 3 Fit e 4. Melhor tratamento de erros.
        * **Toledo:** Versão "Legada" (Antiga). Use se a balança estiver com padrão de fábrica (P03).
        * **Toledo2090 / 2090N:** Para balanças industriais ou modelos específicos da série 2090.
        * **ToledoBCS21:** Específico para balanças contadoras (BCS).
        * **ToledoTi420:** Para indicadores de pesagem industrial Ti420.
        """)
        
        st.divider()
        
        st.subheader("🔵 Urano")
        st.markdown("""
        * **Urano:** Driver padrão. Exige balança configurada em `PROT 1`.
        * **UranoPOP:** Variação específica para a linha POP (às vezes tem formatação diferente).
        * **UranoUDC:** Para balanças de checkout (frente de caixa).
        """)

    with col_geral:
        st.subheader("🟠 Padrões de Mercado")
        st.markdown("Drivers compatíveis com múltiplas marcas.")
        
        st.markdown("""
        * **Filizola:** 🛠️ **(O Coringa)**. Além de balanças Filizola, este protocolo é usado pela **Elgin (Linha DP)** e muitas outras nacionais.
        * **Generica:** Tenta ler qualquer número que chegar na porta. Ideal para **Balmak**, **Ramuza** e balanças importadas da China.
        """)

        st.divider()
        
        st.subheader("🟣 Outras Marcas / Industriais")
        with st.expander("Ver lista completa de outros modelos"):
            st.markdown("""
            * **Weightech (WT1000, WT3000, etc):** Indicadores industriais pesados.
            * **Micheletti / Alfa:** Marcas nacionais comuns em açougues.
            * **Magna / LucasTec / Digitron:** Balanças regionais ou específicas.
            * **Rinnert / Muller / Saturno:** Geralmente equipamentos de chão ou industriais antigos.
            * **Libratek / Lider / Capital:** Marcas menos frequentes no varejo alimentar.
            """)
