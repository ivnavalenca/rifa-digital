fetch("../assets/quality-metrics.json")
  .then(res => res.json())
  .then(data => {

    document.getElementById("quality-metrics").innerHTML = `
      <div class="grid cards">

        <div>
          <h3>🧪 Test Cases</h3>
          <p>${data.test_cases}</p>
        </div>

        <div>
          <h3>📊 Test Reports</h3>
          <p>${data.test_reports}</p>
        </div>

        <div>
          <h3>🔗 Traceability</h3>
          <p>${data.traceability}</p>
        </div>

        <div>
          <h3>🧠 Strategy</h3>
          <p>${data.strategies}</p>
        </div>

        <div>
          <h3>⚙️ Process</h3>
          <p>${data.process_docs}</p>
        </div>

        <div>
          <h3>🚀 Quality Score</h3>
          <p><strong>${data.quality_score}</strong></p>
        </div>

      </div>
    `;
  })
  .catch(() => {
    document.getElementById("quality-metrics").innerHTML =
      "Erro ao carregar métricas";
  });
