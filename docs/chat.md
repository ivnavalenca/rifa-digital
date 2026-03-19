# 🤖 AI Chat Assistant

<div id="chat-box" style="border:1px solid #ccc; padding:10px; height:300px; overflow:auto;"></div>

<input id="input" placeholder="Digite sua pergunta..." style="width:80%;">
<button onclick="send()">Enviar</button>

<script>

async function send(){

const input = document.getElementById("input").value;
const box = document.getElementById("chat-box");

box.innerHTML += `<p><b>Você:</b> ${input}</p>`;

// 🔥 CHAMANDO A API
const res = await fetch("http://localhost:5000/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ question: input })
});

const data = await res.json();

box.innerHTML += `<p><b>AI:</b> ${data.answer}</p>`;

}

</script>
