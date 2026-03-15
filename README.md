# 🧪 QA Test Generator — MVP Phase 1

Un agent IA qui transforme vos User Stories en cas de tests structurés.
Collez une User Story → Obtenez vos cas de test en 30 secondes.

## Ce que ça génère

- ✅ Cas de test fonctionnels (titre, préconditions, étapes, résultat attendu, priorité)
- ⚠️ Cas limites / Edge cases
- 🔴 Suggestions de risques (fonctionnels, perf, sécu, intégration)

## Lancer en local

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Lancer l'app
streamlit run app.py
```

L'app s'ouvre dans ton navigateur sur http://localhost:8501

## Déployer gratuitement sur Streamlit Cloud

1. Crée un repo GitHub et pousse ces fichiers
2. Va sur [share.streamlit.io](https://share.streamlit.io)
3. Connecte ton repo GitHub
4. Sélectionne `app.py` comme fichier principal
5. Clique "Deploy"

**C'est tout.** Tu obtiens une URL publique que tu peux partager à tes testeurs.

## Clé API Gemini (gratuite)

1. Va sur [aistudio.google.com](https://aistudio.google.com)
2. Clique "Get API Key"
3. Copie la clé
4. Colle-la dans la sidebar de l'app

## Structure

```
qa_test_generator/
├── app.py              # L'application Streamlit
├── requirements.txt    # Dépendances Python
└── README.md           # Ce fichier
```

## Roadmap Phase 1

- [x] Génération de cas de test fonctionnels
- [x] Génération d'edge cases
- [x] Suggestions de risques
- [ ] Scénarios BDD (Given/When/Then)
- [ ] Export CSV structuré
- [ ] Historique des générations

---

*QA Test Generator — MVP Phase 1 · Fait pour la communauté QA*
