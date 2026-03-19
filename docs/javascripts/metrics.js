document.addEventListener("DOMContentLoaded", function(){

fetch("./assets/engineering-metrics.json")
.then(r => r.json())
.then(data => {

document.getElementById("metrics").innerHTML = `
<div class="grid cards">

<div>
<h3>⭐ Stars</h3>
<p>${data.stars}</p>
</div>

<div>
<h3>🍴 Forks</h3>
<p>${data.forks}</p>
</div>

<div>
<h3>🐞 Issues Abertas</h3>
<p>${data.open_issues}</p>
</div>

<div>
<h3>🔀 Pull Requests</h3>
<p>${data.pull_requests}</p>
</div>

<div>
<h3>👥 Contributors</h3>
<p>${data.contributors}</p>
</div>

</div>
`

})
.catch(err => {
document.getElementById("metrics").innerHTML = "Erro ao carregar métricas"
console.error(err)
})

})
