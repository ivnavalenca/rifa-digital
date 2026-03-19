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
<h3>🐞 Issues</h3>
<p>${data.open_issues}</p>
</div>

<div>
<h3>🔀 PRs</h3>
<p>${data.pull_requests}</p>
</div>

<div>
<h3>👥 Contributors</h3>
<p>${data.contributors}</p>
</div>

</div>

<br>

<h2>📊 Issues vs PRs</h2>
<canvas id="chart1"></canvas>

`

const ctx = document.getElementById('chart1');

new Chart(ctx, {
type: 'bar',
data: {
labels: ['Issues', 'Pull Requests'],
datasets: [{
label: 'Quantidade',
data: [data.open_issues, data.pull_requests]
}]
}
});

})
.catch(err => {
document.getElementById("metrics").innerHTML = "Erro ao carregar métricas"
console.error(err)
})

});
