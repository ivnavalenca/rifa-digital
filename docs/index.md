# Rifa Digital

## 🚀 Engineering Command Center

Painel central do sistema.

<div class="grid cards">

- **⚙️ Engineering Dashboard**

  Monitoramento da arquitetura e serviços.

  [Abrir](engineering/engineering-map/)

- **📊 Agile Dashboard**

  Métricas das sprints (Velocity e Burndown).

  [Abrir](agile/agile-dashboard/)

- **🧪 Quality Dashboard**

  Indicadores de qualidade e testes.

  [Abrir](testing/quality-dashboard/)

- **📈 Project Health**

  Saúde do projeto.

  [Abrir](process/project-health/)

- **🌐 System Digital Twin**

  Visualização interativa da arquitetura.

  [Abrir](engineering/system-digital-twin/)

- **🧭 Architecture Navigator**

  Navegação entre requisitos, testes e arquitetura.

  [Abrir](engineering/architecture-navigator/)

</div>

---

## 📊 Project Metrics

<div id="metrics"></div>

<script>

fetch("assets/engineering-metrics.json")
.then(r => r.json())
.then(data => {

document.getElementById("metrics").innerHTML = `
<ul>
<li><b>Documents:</b> ${data.documents}</li>
<li><b>Requirements:</b> ${data.requirements}</li>
<li><b>User Stories:</b> ${data.user_stories}</li>
<li><b>Tests:</b> ${data.tests}</li>
<li><b>Services:</b> ${data.services}</li>
</ul>
`

})

</script>

---

## 📘 Sobre o Projeto

O sistema **Rifa Digital** integra:

- Engenharia de Software  
- Arquitetura  
- Testes  
- DevOps  
- Gestão Ágil  

---

## 🧭 Navegação Rápida

- Product → visão do sistema  
- Requirements → funcionalidades  
- Agile → gestão das sprints  
- Engineering → mapas e grafos  
- Testing → validação  
