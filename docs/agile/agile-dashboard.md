# Agile Dashboard

Painel automático de métricas ágeis do projeto.

---

## Métricas do Backlog

<div id="agile-metrics"></div>

<script>

fetch("../assets/agile-metrics.json")
.then(r => r.json())
.then(data => {

document.getElementById("agile-metrics").innerHTML = `
<ul>
<li>Total User Stories: ${data.total_user_stories}</li>
<li>Concluídas: ${data.done}</li>
<li>No Backlog: ${data.backlog}</li>
</ul>
`

})

</script>
