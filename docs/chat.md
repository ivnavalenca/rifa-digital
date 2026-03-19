# 🤖 AI Chat Assistant

<div id="chat-box" style="border:1px solid #ccc; padding:10px; height:300px; overflow:auto;"></div>

<input id="input" placeholder="Digite sua pergunta..." style="width:80%;">
<button onclick="send()">Enviar</button>

<script>

async function send(){

const input = document.getElementById("input").value;
const box = document.getElementById("chat-box");

box.innerHTML += `<p><b>Você:</b> ${input}</p>`;

const res = await fetch("../assets/assistant-api.json");
const data = await res.json();

let response = "Não sei responder ainda.";

for (const key in data){
  if(input.toLowerCase().includes(key)){
    response = data[key];
  }
}

box.innerHTML += `<p><b>AI:</b> ${response}</p>`;

}

</script>
