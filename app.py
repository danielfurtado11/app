import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise da Reunião", layout="wide")

row = st.columns(1)

row[0].image("nexi.jpg", width=250)
row[0].markdown("## 👋 Bem-vindo, Diogo!")

st.write("")
st.write("")
st.write("")



st.title("📊 Análise da Reunião (11-02-2025)")

st.write("")
st.write("##### Participantes: <span style='font-weight:normal;'>André Neiva, Daniel Furtado, Diogo Feio, Francisco Falcão.</span>", unsafe_allow_html=True)
st.write("##### Duração: <span style='font-weight:normal;'>15:55 - 17:05 (70 minutos)</span>", unsafe_allow_html=True)


st.write("")

st.header("📅 Temas da Reunião", divider="gray")

st.markdown("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Início da reunião e demonstração do projeto. <span style='font-weight:normal;'>(15:55 - 16:02)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Apresentação de um sistema para transcrição automática e análise de reuniões/aulas.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Introdução das funcionalidades do sistema.
""", unsafe_allow_html=True)

st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Discussão sobre a transcrição e sumário automático. <span style='font-weight:normal;'>(16:02 - 16:08)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Explicação sobre como o sistemam captura e resume reuniões.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Aplicação em reuniões corporativas, aulas e até em ambientes desportivos.
""", unsafe_allow_html=True)


st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Utilização na área educacional. <span style='font-weight:normal;'>(16:08 - 16:14)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Benefícios para os professores e alunos.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Possibilidade de criar materiais didáticos a partir de transcrições
""", unsafe_allow_html=True)


st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Análise do engagement e participação. <span style='font-weight:normal;'>(16:14 - 16:22)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Monitorização da atenção dos participantes.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Identificação de momentos de maior e menor interação.
""", unsafe_allow_html=True)


st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Futuro do projeto e melhorias. <span style='font-weight:normal;'>(10:25- 10:30)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Criação de um portal para professores e alunos.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Melhorias na interface e na apresentação dos dados
""", unsafe_allow_html=True)



st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Planeamento de testes futuros e apresentação dos resultados. <span style='font-weight:normal;'>(10:30 - 10:37)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Refinamento dos modelos para detecção automática de padrões de engajamento.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Geração de gráficos e indicadores a partir dos dados capturados.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Planejamento para apresentação dos primeiros resultados na segunda-feira.
""", unsafe_allow_html=True)

st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Automação e disponibilidade da plataforma. <span style='font-weight:normal;'>(16:34 - 16:37)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Recolha e processamento automático de dados.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Manutenção da plataforma online 24 horas por dia.<br>
""", unsafe_allow_html=True)

st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Demonstração de relatórios e dashboards. <span style='font-weight:normal;'>(16:37 - 16:45)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Apresentação dos relatórios gerados a partir das aulas.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Explicação sobre a medição de engajamento e cansaço.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Comparação entre métodos de análise offline e online.<br>
""", unsafe_allow_html=True)

st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Refinamento dos indicadores de engajamento. <span style='font-weight:normal;'>(16:45 - 16:52)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Criação de um índice de scoring para facilitar interpretação.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Simplificação dos relatórios para tornar os insights mais práticos.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Identificação de padrões como cansaço e distração dos alunos.<br>
""", unsafe_allow_html=True)

st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Possíveis melhorias e expansão do projeto. <span style='font-weight:normal;'>(16:52 - 17:00)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Discussão sobre otimização da plataforma.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Organização de um painel com professores e profissionais.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Exploração do uso da ferramenta em diferentes áreas, como desporto.<br>
""", unsafe_allow_html=True)

st.write("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 Marcação de novas reuniões e próximos passos. <span style='font-weight:normal;'>(17:00 - 17:05)</span>", unsafe_allow_html=True)
st.write("""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Planejamento de uma nova reunião com a Cátia da PBS.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Discussão sobre uma apresentação para a Nova SBE em março.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Organização de reuniões para potenciais parceiros e investidores.<br>
""", unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

st.header("📝 Resumo",divider="gray")

st.text = """
A reunião iniciou-se com os participantes André Neiva, Daniel Furtado, Francisco Falcão e Diogo Feio discutindo detalhes operacionais e técnicos sobre o funcionamento do sistema que estavam desenvolvendo. 
André Neiva começou por mencionar a necessidade de verificar se todos os participantes estavam prontos para a sessão e se os dispositivos estavam a funcionar corretamente. 
Em seguida, discutiu-se a importância de obter permissão para gravar a reunião, uma vez que os dados capturados seriam processados posteriormente para gerar um relatório detalhado. 
A transcrição e a análise automática das reuniões eram um dos principais focos do projeto, permitindo não apenas a captura do conteúdo da discussão, mas também a avaliação da eficácia da reunião ou aula.

Após a introdução e os preparativos técnicos, os participantes passaram a discutir o funcionamento do sistema. 
André explicou que a ferramenta era capaz de gravar e transcrever automaticamente as reuniões, fornecendo um sumário do que foi dito, identificando os principais pontos abordados e categorizando as tarefas e responsabilidades de cada participante. 
Esse recurso poderia ser especialmente útil em ambientes educacionais, pois permitiria aos alunos acessarem rapidamente um resumo da aula, em vez de dependerem apenas de suas próprias anotações. 
Diogo Feio questionou se a transcrição ocorria em tempo real, ao que André explicou que, no momento, a gravação era processada após a reunião para gerar os relatórios, mas que havia planos para aprimorar a tecnologia e permitir uma análise em tempo real.

Francisco Falcão destacou que essa ferramenta poderia revolucionar a maneira como professores e alunos interagem com o conteúdo das aulas. 
Para os professores, o sistema permitiria gerar um resumo estruturado de cada aula, auxiliando na organização do conteúdo e facilitando a criação de materiais didáticos. 
Para os alunos, representaria um recurso essencial para revisar o que foi discutido em aula e identificar tópicos que poderiam necessitar de mais estudo. 
Além disso, Francisco enfatizou que a tecnologia também poderia ser aplicada a outros contextos, como treinamentos corporativos ou desportivos, onde as instruções dadas por um treinador ou gestor poderiam ser registradas e distribuídas de forma organizada aos participantes.

Durante a reunião, foi apresentada uma demonstração do sistema, na qual Daniel Furtado partilhou o ecrã para exibir um protótipo do relatório gerado automaticamente. 
O relatório continha uma lista dos tópicos abordados na reunião, organizados cronologicamente, com indicações de quando cada tema foi discutido. 
Diogo Feio mostrou-se interessado em como os tópicos eram extraídos automaticamente do conteúdo falado, perguntando se os pontos eram definidos previamente ou se eram identificados pelo modelo. 
André Neiva explicou que o sistema analisava a transcrição da reunião e identificava os temas principais com base nos padrões linguísticos e no contexto da conversa. 
Francisco complementou, dizendo que o modelo conseguia associar os temas discutidos a um horário específico dentro da reunião, o que permitiria aos utilizadores navegar rapidamente para os momentos mais relevantes.

Outro aspeto debatido foi a possibilidade de medir o nível de atenção e engajamento dos participantes. 
Francisco explicou que estavam a desenvolver métricas que poderiam indicar se um aluno estava atento ou distraído durante uma aula, analisando variáveis como expressões faciais, postura corporal e padrões de interação. 
A primeira versão do relatório era muito extensa e continha informações detalhadas sobre cada participante, mas percebeu-se que um resumo mais simplificado, baseado num índice de "engagement score", seria mais útil. 
Esse índice permitiria que professores ou gestores identificassem momentos em que a atenção do grupo diminuiu e ajustassem sua abordagem para manter o interesse dos participantes.

Diogo Feio sugeriu que essa tecnologia poderia ser útil não apenas para o meio acadêmico, mas também para outros setores, como reuniões empresariais, treinamentos para profissionais que exigem alta concentração (como controladores de tráfego aéreo) e até mesmo para técnicos desportivos que precisam registrar e analisar instruções dadas a suas equipas. 
Ele enfatizou que o sistema tinha um grande potencial e poderia ter aplicações muito amplas, desde a educação até o setor corporativo.

Nos momentos finais da reunião, discutiu-se a necessidade de realizar novos testes e coletar feedback de diferentes utilizadores. 
Diogo sugeriu organizar uma nova reunião com a Cátia da PBS para apresentar os avanços do projeto e perceber sua reação às melhorias feitas desde o último encontro. 
Além disso, propôs reunir um painel de especialistas de diferentes áreas, incluindo professores, treinadores desportivos e gestores empresariais, para observar como cada um interpretaria os relatórios gerados pela ferramenta e quais funcionalidades considerariam mais úteis.

A reunião encerrou com um consenso sobre a importância de continuar aprimorando a tecnologia, tornando-a mais intuitiva e acessível. 
Os participantes concordaram que o design e a apresentação dos dados ainda precisavam de melhorias, mas que a funcionalidade central do sistema já estava bem encaminhada. 
O projeto prometia trazer grandes benefícios para a gestão do conhecimento, otimizando a forma como reuniões e aulas são documentadas, analisadas e utilizadas para melhorar a aprendizagem e a eficiência dos encontros.
"""

with st.container(height=500, border=True):
    st.write(st.text)

st.write("")
st.write("")
st.write("")


st.header("✅ Destaques", divider="gray")
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Objetivo principal da tecnologia: <span style='font-weight:normal;'> A reunião focou no desenvolvimento de um sistema capaz de transcrever, resumir e analisar reuniões e aulas, ajudando na gestão do conhecimento e no acompanhamento do engajamento dos participantes</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Demonstração do Protótipo: <span style='font-weight:normal;'>Daniel Furtado apresentou um protótipo do sistema, mostrando como ele gera automaticamente um relatório com os tópicos discutidos e a cronologia da reunião.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Medir Engagement e Atenção: <span style='font-weight:normal;'>O sistema está a evoluir para medir o nível de participação dos indivíduos através da análise de expressões faciais, postura e padrões de interação. Foi mencionado que a primeira versão dos relatórios era extensa e técnica, mas que agora se está a simplificar a informação através de um \"engagement score\".</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Aplicações da Tecnologia: <span style='font-weight:normal;'>Diogo Feio destacou que a ferramenta pode ser usada além do setor acadêmico, incluindo reuniões empresariais, treinamentos de alto desempenho e até para técnicos desportivos.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Testes Futuros: <span style='font-weight:normal;'>Foi sugerido que se organizasse uma nova reunião com a Cátia da PBS para avaliar os avanços do projeto e também a realização de um painel de especialistas de diferentes áreas para testar a utilidade da ferramenta em diferentes contextos.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Desafios e Melhorias: <span style='font-weight:normal;'>Houve uma discussão sobre a necessidade de aprimorar a interface do sistema, tornando-o mais acessível e intuitivo. Além disso, foi mencionado que o processamento das reuniões atualmente ocorre após a gravação, mas a meta é conseguir transcrições e análises em tempo real.</span>", unsafe_allow_html=True)



st.write("")
st.write("")
st.write("")


st.header("👣 Próximos Passos", divider="gray")

st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Organizar uma reunião com a Cátia da PBS para apresentar as melhorias feitas no sistema desde a última reunião.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Criar um painel de especialistas (professores, treinadores desportivos e gestores) para testar a ferramenta e recolher feedback sobre suas necessidades específicas.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Otimizar o sistema para ser mais intuitivo, refinando o design da interface e melhorando a apresentação dos dados gerados.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Aprimorar o \"engagement score\", garantindo que seja um indicador útil para professores e gestores na análise da atenção dos participantes.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Continuar desenvolvendo a transcrição e análise em tempo real, para que os utilizadores possam acompanhar e reagir aos dados durante as reuniões.")

st.write("")
st.write("")
st.write("")

st.header("✍🏻 Tarefas Atribuídas", divider="gray")


# Dicionário de tarefas atribuídas a cada pessoa
tasks = {
    "André Neiva": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Agendar a reunião com a Cátia da PBS.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Trabalhar na melhoria da apresentação dos dados no relatório.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Garantir que a nova versão do sistema possa ser demonstrada de forma clara na próxima reunião."
    ],
    "Daniel Furtado": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Melhorar o processamento do engagement e atenção dentro do sistema.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Implementar otimizações para que a ferramenta seja capaz de processar transcrições em tempo real.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Trabalhar na estabilidade da plataforma e na integração com diferentes formatos de reunião."
    ],
    "Diogo Feio": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Auxiliar na identificação de potenciais parceiros e utilizadores para testar o sistema.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Acompanhar a evolução do projeto e fornecer sugestões de aplicação prática para diferentes áreas.",
    ],
    "Francisco Falcão": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Coordenar a organização do painel de especialistas para avaliar a ferramenta em diferentes setores.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Ajustar a estrutura dos relatórios gerados para torná-los mais acessíveis e úteis para os utilizadores finais.",
    ]
}

st.write("")
st.write("")
st.write("")


# Criar checkboxes para cada pessoa
selected_people = []
for person in tasks.keys():
    if st.checkbox(person, value=True):  # Começa marcado por padrão
        selected_people.append(person)

# Exibir as tarefas das pessoas selecionadas
for person in selected_people:
    st.write(f"#### {person}")

    for task in tasks[person]:
        st.write(f" {task}")

st.write("")
st.write("")
st.write("")

st.header("❔ Questões Relevantes", divider="gray")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 A transcrição ocorre em tempo real ou apenas após a reunião? <span style='font-weight:normal;'>(Diogo Feio)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Atualmente, o sistema processa os dados após a reunião, mas a meta é oferecer transcrição e análise em tempo real.</span>", unsafe_allow_html=True)


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como o sistema identifica os tópicos principais da reunião? <span style='font-weight:normal;'>(Diogo Feio)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>A ferramenta analisa a transcrição automaticamente e extrai os principais pontos com base nos padrões linguísticos e no contexto da conversa.</span>", unsafe_allow_html=True)


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 O sistema pode ser útil para além do contexto acadêmico? <span style='font-weight:normal;'>(Diogo Feio)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Sim, pode ser aplicado em reuniões empresariais, treinamentos técnicos, formações desportivas e outros cenários que exigem documentação e análise de interações.</span>", unsafe_allow_html=True)


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como o engagement score é calculado? <span style='font-weight:normal;'>(Francisco Falcão)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>Inicialmente, o sistema analisava múltiplas variáveis, como expressões faciais e postura, mas agora está sendo refinado para gerar um índice mais simples e interpretável para os utilizadores.</span>", unsafe_allow_html=True)


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como a informação deve ser organizada para não sobrecarregar os utilizadores? <span style='font-weight:normal;'>(Diogo Feio)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>O sistema está a evoluir para apresentar um resumo mais conciso, em vez de um relatório muito técnico e extenso.</span>", unsafe_allow_html=True)


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Como garantir que a ferramenta seja aplicável a diferentes públicos e necessidades? <span style='font-weight:normal;'>(Diogo Feio)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Resposta: <span style='font-weight:normal;'>A ideia de criar um painel de especialistas surgiu para testar a ferramenta em diferentes cenários e recolher sugestões de melhoria.</span>", unsafe_allow_html=True)



topics = {
    "Global": None,
    "Início da reunião e demonstração do projeto": ("15:55", "16:02"),
    "Discussão sobre a transcrição e sumário automático": ("16:02", "16:08"),
    "Utilização na área educacional": ("16:08", "16:14"),
    "Análise do engagement e participação": ("16:14", "16:22"),
    "Futuro do projeto e melhorias": ("10:25", "10:30"),
    "Planeamento de testes futuros e apresentação dos resultados": ("10:30", "10:37"),
    "Automação e disponibilidade da plataforma": ("16:34", "16:37"),
    "Demonstração de relatórios e dashboards": ("16:37", "16:45"),
    "Refinamento dos indicadores de engajamento": ("16:45", "16:52"),
    "Possíveis melhorias e expansão do projeto": ("16:52", "17:00"),
    "Marcação de novas reuniões e próximos passos": ("17:00", "17:05")
}


st.header("📈 Engagement", divider="gray")

data = pd.read_csv("online_new.csv")
data["datetime"] = pd.to_datetime(data["datetime"])

time_adjust = "1min" 


plot_data = []

data_global = data.set_index('datetime').resample(time_adjust)["engagement1"].mean().reset_index()
data_global['person'] = 'Média Global' 

data["person"] = data["person"].replace({0: "Francisco Falcão", 1: "Daniel Furtado", 2: "Diogo Feio", 3: "André Neiva"})

selected_topic = st.selectbox("🔍 Filtrar Tema:", list(topics.keys(),), key="engagement")
if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (data['datetime'].dt.strftime("%H:%M") >= start_time) & (data['datetime'].dt.strftime("%H:%M") <= end_time)
    mask_time1 = (data_global['datetime'].dt.strftime("%H:%M") >= start_time) & (data_global['datetime'].dt.strftime("%H:%M") <= end_time)
    data_filtered = data[mask_time]
    data_filtered_global = data_global[mask_time1]
else:
    data_filtered = data
    data_filtered_global = data_global



for person in data['person'].unique():
    data_person = data_filtered[data_filtered['person'] == person].set_index('datetime')
    grouped_data = data_person["engagement1"].resample(time_adjust).mean().reset_index()
    grouped_data['person'] = f'{person}'
    plot_data.append(grouped_data)


plot_data.append(data_filtered_global)
plot_df = pd.concat(plot_data)

fig = px.line(
    plot_df, 
    x="datetime", 
    y="engagement1", 
    color="person",
    title="Engagement ao Longo do Tempo",
    labels={"datetime": "Tempo", "engagement1": "Engagement (%)", "person": "Participantes"},
    template="plotly_white",
    line_dash="person",
    line_group="person",
    line_dash_map={"Média Global": "dash", "André Neiva": "solid", "Daniel Furtado": "solid", "Francisco Falcão": "solid", "Diogo Feio": "solid"},
    range_y=[0, 1]
)



st.plotly_chart(fig, use_container_width=True)


st.write("")
st.write("")
st.write("")


st.header("📈 Participação", divider="gray")
st.write("")

st.write("##### 🗣️ Participação Ativa:")
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  André Neiva: <span style='font-weight:normal;'>00:18:48 (26.86%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Daniel Furtado: <span style='font-weight:normal;'>00:11:03 (15.79%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Diogo Feio: <span style='font-weight:normal;'>00:17:42 (25.29%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Francisco Falcão: <span style='font-weight:normal;'>00:19:56 (28.48%)</span>", unsafe_allow_html=True )




df_resampled = pd.read_csv("intervencoes_por_minuto.csv", index_col=0, parse_dates=True)




participants = df_resampled.columns.tolist()

df_filtered = df_resampled[participants].reset_index()
df_melted = df_filtered.melt(id_vars=["time"], var_name="Participant", value_name="Interventions")

selected_topic = st.selectbox("🔍 Filtrar por Tema:", list(topics.keys(),), key="participation")
if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (df_melted['time'].dt.strftime("%H:%M") >= start_time) & (df_melted['time'].dt.strftime("%H:%M") <= end_time)
    data_filtered = df_melted[mask_time]
else:
    data_filtered = df_melted




fig = px.line(data_filtered, x="time", y="Interventions", color="Participant",
            labels={"time": "Horário", "Interventions": "Número de Intervenções"},
            title="Participação ao Longo do Tempo")
    
fig.update_xaxes(title="Tempo")
fig.update_yaxes(title="Nº ntervenções")
fig.update_layout(legend_title="Participantes")

st.plotly_chart(fig, use_container_width=True)



st.write("")
st.write("")
st.write("")


st.header("🎭 Expressão Facial", divider="gray")

time_adjust = '1 min'



people_list = data['person'].unique()
people_list = ["Global"] + list(people_list)

selected_topic = st.selectbox("🔍 Filtrar por Tema:", list(topics.keys()), key="facial_expression")
selected_person = st.selectbox("👤 Filtrar por Pessoa:", people_list)

if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (data['datetime'].dt.strftime("%H:%M") >= start_time) & (data['datetime'].dt.strftime("%H:%M") <= end_time)
    data_filtered = data[mask_time]
else:
    data_filtered = data

if selected_person != "Global":
    data_filtered = data_filtered[data_filtered['person'] == selected_person]

expression_counts = data_filtered.groupby(
    [pd.Grouper(key='datetime', freq=time_adjust), 'facial_expression']
).size().unstack(fill_value=0)

expression_normalized = expression_counts.div(expression_counts.sum(axis=1), axis=0).fillna(0)

expression_smoothed = expression_normalized.rolling(window=5, min_periods=1).mean()

plot_data = expression_smoothed.reset_index().melt(id_vars="datetime", var_name="Expression", value_name="Frequency")

# Criar o gráfico interativo com Plotly Express
fig = px.line(
    plot_data, 
    x="datetime", 
    y="Frequency", 
    color="Expression", 
    title=f"Variação da Expressão Facial - {selected_topic} ({selected_person})",
    labels={"datetime": "Tempo", "Frequency": "Expressão Facial (%)", "Expression": "Expressão Facial"},
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)
