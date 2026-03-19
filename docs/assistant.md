# 🤖 AI Assistant

Assistente inteligente do sistema **Rifa Digital**.

---

## 🧠 O que este assistente faz?

Este assistente utiliza:

- 📚 documentação do projeto
- 🔗 rastreabilidade
- 📊 métricas de engenharia
- 🤖 inteligência artificial (OpenAI)

Para responder perguntas sobre o sistema.

---

## 💬 Faça uma pergunta

<div id="chat-box" style="border:1px solid #ccc; padding:10px; height:300px; overflow:auto; border-radius:8px;"></div>

<br>

<input id="input" placeholder="Digite sua pergunta..." style="width:80%; padding:8px;">
<button onclick="send()" style="padding:8px;">Enviar</button>

---

## 🧪 Exemplos de perguntas

- Quantos requisitos o sistema possui?
- Quais testes foram implementados?
- Como funciona a arquitetura?
- Existe rastreabilidade entre requisitos e testes?
- Qual o nível de qualidade do sistema?

---

## 🚀 Como funciona

Usuário → Chat → API → IA → Base de conhecimento → Resposta

---

<script>

async function send(){

  const inputField = document.getElementById("input");
  const box = document.getElementById("chat-box");

  const question = inputField.value;

  if (!question) return;

  box.innerHTML += `<p><b>Você:</b> ${question}</p>`;
  inputField.value = "";

  try {

    const res = await fetch("https://rifa-api-4vj2.onrender.com/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    });

    const data = await res.json();

    box.innerHTML += `<p><b>AI:</b> ${data.answer}</p>`;
    box.scrollTop = box.scrollHeight;

  } catch (err) {
    box.innerHTML += `<p><b>Erro:</b> Não foi possível conectar à IA.</p>`;
    console.error(err);
  }

}

</script>
