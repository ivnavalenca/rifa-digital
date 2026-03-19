# Rifa Digital

## 🚀 Engineering Command Center

Painel central do sistema.

---

<div class="grid cards">

<div>
<h3>⚙️ Engineering Dashboard</h3>
<p>Monitoramento da arquitetura e serviços.</p>
<a href="engineering/engineering-map/">👉 Abrir</a>
</div>

<div>
<h3>📊 Agile Dashboard</h3>
<p>Métricas das sprints (Velocity e Burndown).</p>
<a href="agile/agile-dashboard/">👉 Abrir</a>
</div>

<div>
<h3>🧪 Quality Dashboard</h3>
<p>Indicadores de qualidade e testes.</p>
<a href="testing/quality-dashboard/">👉 Abrir</a>
</div>

<div>
<h3>📈 Project Health</h3>
<p>Saúde do projeto.</p>
<a href="process/project-health/">👉 Abrir</a>
</div>

<div>
<h3>🌐 System Digital Twin</h3>
<p>Visualização interativa da arquitetura.</p>
<a href="engineering/system-digital-twin/">👉 Abrir</a>
</div>

<div>
<h3>🧭 Architecture Navigator</h3>
<p>Navegação entre requisitos, testes e arquitetura.</p>
<a href="engineering/architecture-navigator/">👉 Abrir</a>
</div>

</div>

---

## 📊 Project Metrics

<div id="metrics"></div>

<script>
fetch("./assets/engineering-metrics.json")
.then(r => r.json())
.then(data => {
document.getElementById("metrics").innerHTML = `
<ul>
<li><b>Documents:</b> ${data.documents}</li>
<li><b>Requirements:</b> ${data.requirements}</li>
<li><b>User Stories:</b> ${data.user_stories}</li>
<li><b>Tests:</b> ${data.tests}</li>
<li><b>Services:</b> ${data.services}</li>
</ul>`
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
