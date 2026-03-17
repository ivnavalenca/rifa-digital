# Agile Dashboard

## Velocity por Sprint

<canvas id="velocityChart"></canvas>

## Burndown Chart

<canvas id="burndownChart"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>

fetch("../assets/agile-metrics.json")
.then(r => r.json())
.then(data => {

const velocityCtx = document.getElementById('velocityChart');

new Chart(velocityCtx, {
type: 'bar',
data: {
labels: data.sprints,
datasets: [{
label: 'Velocity',
data: data.velocity
}]
}
});


const burnCtx = document.getElementById('burndownChart');

new Chart(burnCtx, {
type: 'line',
data: {
labels: ["Day 1","Day 2","Day 3","Day 4","Day 5"],
datasets: [
{
label: "Planned",
data: data.burndown.planned
},
{
label: "Actual",
data: data.burndown.actual
}
]
}
});

});

</script>
