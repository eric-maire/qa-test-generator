# 🧪 QA Test Generator — Journal de bord (Plan 90 jours)

---

## Infos projet
- **Début du plan** : 15/03/2026
- **Objectif 90 jours** : 100-500 utilisateurs réels + retours terrain exploitables
- **URL app** : https://app-test-generator.streamlit.app
- **Repo** : https://github.com/TesteurGenAI/qa-test-generator

---

## Phase 1 — Jours 1 à 30 : Prototype

### Jour 1 (15-16/03/2026) — ✅ FAIT
- [x] Prompt QA qui génère cas de test, edge cases, risques
- [x] App Streamlit déployée sur Streamlit Cloud
- [x] API Gemini 2.5 Flash connectée (secret Streamlit)
- [x] Clé API masquée — zéro config pour les testeurs
- [x] Lien envoyé à 8 testeurs
- [x] Retours projet précédent : 8/8 n'avaient pas testé (trop de friction)
- [x] 4 testeurs ont testé la v1 et donné des retours
- [x] Itération v2 : ajout champ "Contexte applicatif" + prompt amélioré pour des cas de test exécutables
- [x] Message envoyé à Luis pour retester la v2
- [x] .gitignore ajouté
- [x] Journal de bord créé

### Leçons apprises
- La friction tue l'adoption : Ollama + API tokens + install = personne ne teste
- Zéro installation = condition non négociable
- "Pas eu le temps" = "trop compliqué pour que je fasse l'effort"
- Le contexte applicatif change tout : sans contexte, les cas de test sont génériques et inexécutables (retour Luis)
- Les retours terrain sont plus utiles que la réflexion solo — itérer en < 24h crée de la confiance
- Bug Diawando = restriction géo API Gemini (Guinée-Conakry), pas un bug de code

### En attente
- [ ] Retour de Luis sur la v2 (contexte applicatif)
- [ ] Relancer les 4 testeurs restants (dans 48h)
- [ ] Retour de Diawando avec VPN

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> Je sais que c'est un prototype mais je vois 2 grandes limitations :
> 1. Comment passer le contexte de la User Story
> 2. Comment generer les données de test
> Pour les quelques cas que j'ai essayé, je ne vois pas un user delta etre capable d'executer les cas de tests sans une bonne connaissance de l'application. Pour moi, un bon cas de test doit contenir suffisamment d'information que "mr tout le monde" peut l'executer sans poser de question...

- **Action prise** : Ajout champ contexte applicatif + prompt amélioré (v2). Message envoyé pour retester.

### Testeur 2 — Moez Ben Khaled
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé l'outil cet aprem et c'est vraiment top.
> Juste une question : Des fois les PO rédigent mal les tests d'acceptation et c'est très important pour la synchro Squash/Jira et l'automatisation par exemple, y a t'il un moyen d'évoluer l'outil pour la création des TA avec les cas de test stp?

- **Action prise** : Noté pour Phase 2 — génération de tests d'acceptance (TA).

### Testeur 3 — Romain De Page
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé ton outil il est vraiment bien. Tu l'as fait avec quoi?
> Oui niquel j'ai bien eu les case de tests et je les ai même exportés en .txt pour voir c'est vraiment bien

- **Action prise** : Aucune — retour positif, export fonctionne.

### Testeur 4 — Diawando DIAWARA
- **A testé ?** : Partiellement
- **Date** : 16/03/2026
- **Retour :**

> Je constate que les cas de tests ne sont pas générés après soumission de la user story.
> Je vais activer mon vpn et reprendre.

- **Action prise** : Restriction géographique API Gemini (Guinée-Conakry). En attente retour avec VPN.

### Testeurs 5-8
- **A testé ?** : Non
- **Relance prévue** : 18/03/2026

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel |
|----------|-----------------|--------|
| Prototype utilisable | ✅ | ✅ |
| Testeurs contactés | 10+ | 8 |
| Testeurs qui ont testé | 5+ | 4 |
| Retours exploitables | 3+ | 3 ✅ |
| Itérations basées sur feedback | - | 1 (v2 contexte) |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash (pas Ollama)
2. **Architecture** : 1 seul appel LLM (pas 3 agents)
3. **Go-to-market** : Option A — PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Champ contexte applicatif** : ajouté suite retour Luis — améliore drastiquement la qualité des tests générés
6. **Tests d'acceptance (TA)** : demandé par Moez — reporté à Phase 2

## Backlog (demandé par les testeurs, pas encore planifié)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Gestion des restrictions géographiques API (Diawando)

---

## Phase 2 — Jours 30 à 60 : Validation marché
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 60 à 90 : Produit
*(à compléter quand Phase 2 terminée)*
