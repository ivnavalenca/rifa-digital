# Architecture Navigator

Mapa interativo da engenharia do sistema.

Clique em um elemento para navegar pelas relações.

<div id="graph"></div>
<div id="details"></div>

<script src="https://d3js.org/d3.v7.min.js"></script>

<script>

fetch("../assets/engineering-knowledge-graph.json")
.then(r => r.json())
.then(graph => {

const width = 900
const height = 600

const svg = d3.select("#graph")
.append("svg")
.attr("width", width)
.attr("height", height)

const simulation = d3.forceSimulation(graph.nodes)
.force("link", d3.forceLink(graph.links).id(d => d.id).distance(120))
.force("charge", d3.forceManyBody().strength(-300))
.force("center", d3.forceCenter(width/2,height/2))

const link = svg.selectAll("line")
.data(graph.links)
.enter()
.append("line")

const node = svg.selectAll("circle")
.data(graph.nodes)
.enter()
.append("circle")
.attr("r",12)
.on("click",showInfo)

const label = svg.selectAll("text")
.data(graph.nodes)
.enter()
.append("text")
.text(d=>d.id)
.attr("font-size","11px")

simulation.on("tick",()=>{

link
.attr("x1",d=>d.source.x)
.attr("y1",d=>d.source.y)
.attr("x2",d=>d.target.x)
.attr("y2",d=>d.target.y)

node
.attr("cx",d=>d.x)
.attr("cy",d=>d.y)

label
.attr("x",d=>d.x+14)
.attr("y",d=>d.y)

})

function showInfo(node){

document.getElementById("details").innerHTML = `
<h3>${node.id}</h3>
<p>Tipo: ${node.type}</p>
`

}

})

</script>
