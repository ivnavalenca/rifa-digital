document.addEventListener("DOMContentLoaded", function(){

fetch("./assets/engineering-metrics.json")
.then(r => r.json())
.then(data => {

document.getElementById("metrics").innerHTML = `

<div class="grid cards">

<div>
<h3>📄 Documents</h3>
<p>${data.documents}</p>
</div>

<div>
<h3>📋 Requirements</h3>
<p>${data.requirements}</p>
</div>

<div>
<h3>🧩 User Stories</h3>
<p>${data.user_stories}</p>
</div>

<div>
<h3>🧪 Tests</h3>
<p>${data.tests}</p>
</div>

<div>
<h3>⚙️ Services</h3>
<p>${data.services}</p>
</div>

</div>

<br>

<h2>📊 Engineering Distribution</h2>
<canvas id="chart1"></canvas>

`

const ctx = document.getElementById('chart1');

new Chart(ctx, {
type: 'bar',
data: {
labels: ['Documents','Requirements','User Stories','Tests','Services'],
datasets: [{
label: 'Quantidade',
data: [
data.documents,
data.requirements,
data.user_stories,
data.tests,
data.services
]
}]
}
});

})
.catch(err => {
document.getElementById("metrics").innerHTML = "Erro ao carregar métricas"
console.error(err)
})

});
