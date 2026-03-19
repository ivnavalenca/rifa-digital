name: AI Pipeline

on:
  push:
    branches:
      - main

jobs:

  ai:
    runs-on: ubuntu-latest

    steps:

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install openai requests

      # 🔥 INGESTÃO (RAG)
      - name: Ingest project knowledge
        run: python copilot/ingest.py

      # 🔥 (opcional) gerar respostas automáticas
      - name: Generate AI responses
        run: python scripts/generate_ai_responses.py || true

      # 💾 salvar arquivo gerado
      - name: Commit knowledge
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "actions@github.com"
          git add copilot/knowledge.json
          git commit -m "update: knowledge base" || echo "No changes"
          git push
