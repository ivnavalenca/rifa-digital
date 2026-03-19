document.addEventListener("DOMContentLoaded", function(){

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
</ul>
`

})
.catch(err => {
document.getElementById("metrics").innerHTML = "Erro ao carregar métricas"
console.error(err)
})

})
