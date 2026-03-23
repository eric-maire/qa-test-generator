# 🧪 QA Test Generator — Journal de bord (Plan 90 jours)

---

## Infos projet
- **Début du plan** : 15/03/2026
- **Objectif 90 jours** : 100-500 utilisateurs réels + retours terrain exploitables
- **Fin Phase 1** : 14/04/2026 (Jour 30)
- **URL app** : https://app-test-generator.streamlit.app
- **Repo** : https://github.com/TesteurGenAI/qa-test-generator

---

## Phase 1 — Jours 1 à 30 : Prototype (15/03 → 14/04/2026)

### Jours 1-2 (15-16/03/2026) — ✅ FAIT
- [x] Prompt QA qui génère cas de test, edge cases, risques
- [x] App Streamlit déployée sur Streamlit Cloud
- [x] API Gemini 2.5 Flash connectée (secret Streamlit)
- [x] Clé API masquée — zéro config pour les testeurs
- [x] Lien envoyé à 8 testeurs
- [x] Retours projet précédent : 8/8 n'avaient pas testé (trop de friction)
- [x] 4 testeurs ont testé la v1 et donné des retours
- [x] Itération v2 : ajout champ "Contexte applicatif" + prompt amélioré
- [x] .gitignore ajouté
- [x] Journal de bord créé

### Jour 3 (17/03/2026) — ✅ FAIT
- [x] 11 testeurs au total — 10 retours exploitables
- [x] Post LinkedIn carrousel (2407 impressions, 48 réactions, 18 commentaires)
- [x] Prompt corrigé : plus de données inventées
- [x] Export CSV compatible Jira/Xray ajouté + import Jira validé
- [x] Fix boutons d'export (session_state)
- [x] Newsletter LinkedIn "Le Testeur Augmenté" configurée

### Jour 4 (18/03/2026) — ✅ FAIT
- [x] 9 commentaires "QA" sur LinkedIn — tous contactés en DM
- [x] Export Gherkin / BDD ajouté
- [x] 4 formats d'export : Markdown, TXT, CSV Jira, Gherkin
- [x] 5 itérations produit en 4 jours

### Jours 5-6 (19-20/03/2026) — ✅ FAIT
- [x] Newsletter #1 publiée — 928 abonnés en 24h
- [x] Karima SORIANO (Test Manager Bforbank) — lead enterprise
- [x] Luis reteste : [À DÉFINIR PAR LE TESTEUR] improductif, veut un dialogue interactif
- [x] Bouton "Voir une démo" ajouté
- [x] Performance optimisée : CSV et Gherkin à la demande (~30s au lieu de 1min30)
- [x] Design épuré : icônes SVG émeraude, suppression des emojis

### Jours 7-8 (21-23/03/2026) — ✅ FAIT
- [x] Testeur 13 — Rezika D : "ça marche très bien, résultat similaire à Copilot mais c'est bien d'avoir un outil spécialisé"
- [x] Vidéo démo 30 secondes tournée et publiée sur LinkedIn
- [x] Post LinkedIn #2 vidéo publié
- [x] Post LinkedIn #3 préparé (hallucinations IA)
- [x] Newsletter #2 rédigée (hallucinations IA + dialogue interactif)
- [x] Julien Botella (Smartesting/Lynqa) a contacté — décliné, reste focus
- [x] MODE GUIDÉ LIVRÉ : dialogue interactif IA/testeur — l'IA pose des questions avant de générer
- [x] 2 modes disponibles : Guidé (questions d'abord) et Direct (génération immédiate)
- [x] Message envoyé à Luis pour tester le mode guidé

### Leçons apprises
- La friction tue l'adoption : Ollama + API tokens + install = personne ne teste
- Zéro installation = condition non négociable
- Le contexte applicatif change tout (retour Luis)
- Les retours terrain > la réflexion solo — itérer en < 24h crée de la confiance
- L'export CSV Jira est la feature la plus demandée (3 testeurs)
- Les LLM inventent des données si on ne l'interdit pas explicitement
- Streamlit : session_state pour persister les résultats
- Jira : champs texte court limités à 255 caractères
- CTA "commente QA" génère des leads qualifiés
- 928 abonnés newsletter en 24h — le marché QA + IA a une demande forte
- Engagement LinkedIn ≠ utilisation réelle
- Le [À DÉFINIR PAR LE TESTEUR] est une demi-solution — le dialogue interactif est la vraie réponse
- "Résultat similaire à Copilot" — la spécialisation et les exports sont les différenciateurs actuels
- Les acteurs établis (Smartesting) repèrent ta newsletter — signal de crédibilité
- Varier les hooks LinkedIn — ne pas réutiliser le même plus de 2 fois

### En attente
- [ ] Retour de Luis sur le mode guidé
- [ ] Publier le post LinkedIn #3 (hallucinations IA)
- [ ] Publier la newsletter #2
- [ ] Retour de Karima (Bforbank) — relancer semaine du 27/03
- [ ] Retour de Diawando avec VPN
- [ ] Retour d'Elodie — relancer début avril
- [ ] Résultats du post vidéo LinkedIn
- [ ] Convertir les 928 abonnés newsletter en utilisateurs actifs

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **A testé ?** : Oui (v1 + v2 + v4-v5)
- **Retour v1 :** Manque de contexte, cas de test trop génériques
- **Retour v2 :** Mieux, mais l'IA invente des données
- **Retour v4-v5 :** [À DÉFINIR PAR LE TESTEUR] improductif, veut un dialogue interactif
- **Actions** : v2 contexte, v3 prompt strict, MODE GUIDÉ livré (Jour 8). En attente retour.

### Testeur 2 — Moez Ben Khaled
- **Retour :** "c'est vraiment top", demande génération TA → backlog

### Testeur 3 — Romain De Page
- **Retour :** "vraiment bien", a exporté en .txt

### Testeur 4 — Diawando DIAWARA
- **Retour :** Restriction géo API Gemini (Guinée-Conakry). En attente VPN.

### Testeur 5 — Ken Defossez
- **Retour :** Bug PixelConnect corrigé. Signal B2B : "on nous demande des initiatives AI"

### Testeur 6 — Aymen Ismail
- **Retour :** Demande CSV Jira et Gherkin → les deux livrés

### Testeur 7 — Tasnim Ferchichi
- **Retour :** "cohérent avec contexte", demande matrice de test → backlog

### Testeur 8 — Kalidou BA
- **Retour :** "super APP", demande analyse par URL/APK → vision long terme

### Testeur 9 — Nicolas Trzcinski
- **Retour :** Projet similaire Jira/Xray, propose collaboration → déclinée

### Testeur 10 — Lyne Voctabah
- **Retour :** Demande historique et BDD → Gherkin livré, historique au backlog

### Testeur 11 — Elodie Juino
- **Retour :** "après notre recette" → relancer début avril

### Testeur 12 — Karima SORIANO
- **Retour :** Lead enterprise Bforbank, "faut tester sur une vraie US" → relancer semaine du 27/03

### Testeur 13 — Rezika D
- **Retour :** "ça marche très bien, similaire à Copilot mais bien d'avoir un outil spécialisé"

### Leads LinkedIn
- Lewis Dieu Ne Dort BABE YAKA — Senior QA Engineer — DM envoyé
- Ali KAR — Ingénieur Testing Agile ISTQB — DM envoyé
- Ahlem Ayari — Étudiante ISITCOM — DM envoyé
- Abdoulahi DIABY — Consultant QA SAP — DM envoyé
- Ala Eddine Benna — Testeur logiciel ISTQB — DM envoyé
- Abdelkrim BOUHRAOUA — QA Testeur ISTQB — DM envoyé
- Abdessamad Nacih — Ingénieur QA — DM envoyé

### Contact industrie
- Julien Botella (Smartesting/Lynqa) — décliné, reste focus

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel | Jour |
|----------|-----------------|--------|------|
| Prototype utilisable | ✅ | ✅ | J2 |
| Testeurs confirmés | 10+ | 13 ✅ | J8 |
| Leads LinkedIn | - | 7 | J4 |
| Testeurs qui ont testé | 5+ | 11 ✅ | J8 |
| Retours exploitables | 3+ | 12 ✅ | J8 |
| Itérations produit | - | 8 | J8 |
| Formats d'export | - | 4 | J4 |
| Modes de génération | - | 2 (Guidé + Direct) | J8 |
| Posts LinkedIn | 3 | 3 | J8 |
| Newsletter publiée | 1 | 1 ✅ | J6 |
| Abonnés newsletter | - | 928 | J6 |
| Import Jira validé | - | ✅ | J3 |
| Temps de génération | 30s | ~30s ✅ | J6 |
| Vidéo démo | - | ✅ | J8 |
| Jours écoulés / 30 | - | 8/30 (27%) | - |
| Utilisateurs actifs | 100-500 | ~20 | J8 |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash
2. **Architecture** : 1 appel LLM principal, CSV et Gherkin à la demande
3. **Go-to-market** : PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Contexte applicatif** : ajouté (v2, retour Luis)
6. **Prompt strict** : ne jamais inventer de données (v3)
7. **Export CSV Jira/Xray** : retours Aymen, Nicolas, Moez
8. **Export Gherkin/BDD** : retours Aymen, Lyne
9. **Collaboration Nicolas** : déclinée
10. **Repo GitHub public** : nécessaire pour Streamlit Cloud gratuit
11. **Formation** : en mode maintenance
12. **Newsletter** : "Le Testeur Augmenté" — hebdomadaire
13. **Performance** : CSV et Gherkin à la demande
14. **Mode guidé** : dialogue interactif IA/testeur (v8, retour Luis)
15. **Smartesting/Lynqa** : contact décliné
16. **Migration Next.js** : prévue Phase 2

## Backlog
- [x] Prompt strict (Luis v2)
- [x] Export CSV Jira/Xray (Aymen, Nicolas, Moez)
- [x] Import Jira + config sauvegardée
- [x] Export Gherkin / BDD (Aymen, Lyne)
- [x] Bouton démo pré-rempli
- [x] Optimisation performance
- [x] Vidéo démo
- [x] Mode guidé — dialogue interactif (Luis v4-v5)
- [ ] Historique / sauvegarde des générations (Lyne)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Matrice de test (Tasnim)
- [ ] Analyse d'app par URL/APK (Kalidou) — vision long terme
- [ ] Gestion restrictions géo API (Diawando)
- [ ] Migration Next.js (Phase 2)

---

## Phase 2 — Jours 31 à 60 : Validation marché (15/04 → 14/05/2026)
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 61 à 90 : Produit (15/05 → 13/06/2026)
*(à compléter quand Phase 2 terminée)*
