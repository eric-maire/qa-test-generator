import streamlit as st
import requests
import json
import time
import csv
import io
import re

# --- SVG Icons (Emerald, 20px, inline) ---
ICON_CHECK = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>'
ICON_ZAP = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
ICON_FILE = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>'
ICON_CLIPBOARD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'
ICON_LAYERS = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
ICON_DOWNLOAD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'
ICON_CODE = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
ICON_BOOK = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'
ICON_SETTINGS = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>'
ICON_SHIELD = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'

# --- Page Config ---
st.set_page_config(
    page_title="QA Test Generator",
    page_icon="✓",
    layout="wide"
)

# --- Custom CSS - Emerald Theme ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

.stApp { font-family: 'DM Sans', sans-serif; }

/* === HEADER === */
.main-header { text-align: center; padding: 2.5rem 0 1.5rem 0; }
.main-header h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.4rem; font-weight: 700;
    background: linear-gradient(135deg, #059669, #10B981, #34D399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.main-header .tagline { font-size: 1.15rem; color: #6b7280; margin-top: 0; margin-bottom: 1rem; }
.badge {
    display: inline-block; background: #ecfdf5; color: #059669;
    font-size: 0.7rem; font-weight: 700; padding: 0.3rem 0.9rem;
    border-radius: 999px; border: 1px solid #a7f3d0; margin-bottom: 0.8rem;
    letter-spacing: 1px; text-transform: uppercase;
}
.badge svg { vertical-align: -3px; margin-right: 4px; }
.welcome-stats { display: flex; justify-content: center; gap: 2.5rem; margin-top: 1.2rem; margin-bottom: 0.5rem; }
.stat-item { text-align: center; }
.stat-number { font-family: 'JetBrains Mono', monospace; font-size: 1.5rem; font-weight: 700; color: #059669; }
.stat-label { font-size: 0.78rem; color: #9ca3af; margin-top: 0.15rem; }

/* === SECTION TITLES === */
.section-title {
    font-family: 'JetBrains Mono', monospace; font-size: 0.95rem;
    font-weight: 600; color: #374151; letter-spacing: 0.3px; margin-bottom: 0.5rem;
}
.section-title svg { vertical-align: -4px; margin-right: 6px; }

/* === SIDEBAR === */
section[data-testid="stSidebar"] { background-color: #f0fdf4; }
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: #059669; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; letter-spacing: 0.3px;
}

/* === BUTTONS === */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #059669, #10B981) !important;
    color: white !important; border: none !important; font-weight: 600 !important;
    padding: 0.6rem 1.5rem !important; border-radius: 8px !important;
    font-size: 1rem !important; transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #047857, #059669) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
}

/* === DOWNLOAD BUTTONS === */
.stDownloadButton > button {
    border: 1px solid #d1fae5 !important; color: #059669 !important;
    font-weight: 600 !important; border-radius: 8px !important;
    transition: all 0.2s ease !important;
}
.stDownloadButton > button:hover {
    background-color: #ecfdf5 !important; border-color: #059669 !important;
}

/* === TEXT AREA === */
.stTextArea textarea {
    border-radius: 8px !important; border: 1px solid #d1d5db !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextArea textarea:focus {
    border-color: #10B981 !important;
    box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.15) !important;
}

/* === FOOTER === */
.footer {
    text-align: center; color: #9ca3af; font-size: 0.8rem;
    padding: 2rem 0 1rem 0; border-top: 1px solid #e5e7eb; margin-top: 3rem;
}
.footer svg { vertical-align: -3px; margin: 0 3px; }
</style>
""", unsafe_allow_html=True)

# --- System Prompt ---
SYSTEM_PROMPT = """Tu es un expert QA senior avec 15 ans d'expérience en test logiciel.

Tu génères des cas de test CONCRETS et EXÉCUTABLES. Un testeur junior qui ne connaît pas l'application doit pouvoir exécuter chaque cas de test sans poser de question.

=== RÈGLE ABSOLUE SUR LES DONNÉES ===

Si un contexte applicatif est fourni :
- Utilise UNIQUEMENT les informations données (noms de pages, boutons, URLs, rôles, règles métier)
- Ne complète pas, n'invente pas, n'extrapole pas au-delà de ce qui est fourni
- Si certaines données manquent malgré le contexte, marque-les [À DÉFINIR PAR LE TESTEUR]

Si AUCUN contexte applicatif n'est fourni :
- N'INVENTE AUCUN contexte. Pas de nom d'application fictif, pas d'URL inventée, pas de nom de bouton supposé, pas de nom de page imaginaire
- N'écris JAMAIS de section "Contexte Applicatif Inventé" ou "Contexte supposé" ou similaire
- Pour CHAQUE donnée non fournie, écris exactement : [À DÉFINIR PAR LE TESTEUR]
- Cela inclut : URLs, noms de boutons, noms de pages, messages d'erreur, emails, mots de passe, identifiants, durées de session, règles de validation

=== FIN RÈGLE ABSOLUE ===

RÈGLES DE RÉDACTION :
- Chaque étape doit être SPÉCIFIQUE et détaillée
- Chaque précondition doit décrire exactement comment atteindre l'état initial

À partir de la User Story (et du contexte applicatif si fourni), génère :

## 1. CAS DE TEST FONCTIONNELS
Pour chaque cas de test, fournis :
- **Titre** : nom court et clair
- **Préconditions** : état initial requis avec les étapes pour y arriver
- **Données de test** : valeurs fournies par le contexte OU [À DÉFINIR PAR LE TESTEUR] si non fournies
- **Étapes** : actions numérotées, spécifiques et détaillées
- **Résultat attendu** : ce qui doit se passer, avec les messages exacts si fournis dans le contexte, sinon [À DÉFINIR PAR LE TESTEUR]
- **Priorité** : Haute / Moyenne / Basse

## 2. CAS LIMITES (EDGE CASES)
Identifie les scénarios aux frontières :
- Valeurs limites (min, max, vide, null)
- Cas d'erreur et comportements inattendus
- Concurrence, timeout, données corrompues
- Pour chaque edge case : titre + données de test + description + résultat attendu

## 3. SUGGESTIONS DE RISQUES
Identifie les risques potentiels :
- Risques fonctionnels
- Risques de performance
- Risques de sécurité
- Risques d'intégration
- Pour chaque risque : titre + description + impact (Critique / Majeur / Mineur) + mitigation suggérée

RÈGLES GÉNÉRALES :
- Sois exhaustif mais pertinent — pas de cas de test inutiles
- Adapte le niveau de détail à la complexité de la User Story
- Utilise un langage clair, compréhensible par un testeur junior
- Réponds en français sauf pour les termes techniques standards
- Structure ta réponse en Markdown clair avec les 3 sections ci-dessus
"""

# --- CSV Conversion Prompt ---
CSV_CONVERSION_PROMPT = """Tu es un assistant qui convertit des cas de test en format JSON strict pour import Azure DevOps.

À partir des cas de test fournis, extrais UNIQUEMENT les cas de test fonctionnels et les cas limites (PAS les risques) et retourne un tableau JSON.

Chaque objet du tableau doit avoir exactement ces champs :
- "Test Case ID": identifiant unique (TC-001, TC-002, etc.)
- "Summary": le titre du cas de test
- "Description": description courte du cas de test
- "Preconditions": les préconditions, chaque précondition sur une ligne séparée avec un numéro (1. xxx\\n2. xxx\\n3. xxx)
- "Test Steps": les étapes, CHAQUE ÉTAPE SUR UNE LIGNE SÉPARÉE avec un numéro (1. xxx\\n2. xxx\\n3. xxx). Utilise \\n pour séparer les lignes.
- "Expected Result": les résultats attendus, CHAQUE RÉSULTAT SUR UNE LIGNE SÉPARÉE avec un numéro (1. xxx\\n2. xxx). Utilise \\n pour séparer les lignes.
- "Priority": "Haute", "Moyenne" ou "Basse" (en français)

RÈGLES STRICTES :
- Retourne UNIQUEMENT le tableau JSON, rien d'autre
- Pas de backticks, pas de commentaires
- Le JSON doit être valide et parsable directement
- Supprime tout formatage Markdown dans les valeurs
"""

# --- Gherkin Conversion Prompt ---
GHERKIN_CONVERSION_PROMPT = """Tu es un expert QA qui convertit des cas de test en scénarios Gherkin (BDD).

À partir des cas de test fournis, génère des scénarios au format Gherkin strict.

FORMAT OBLIGATOIRE :

Feature: [Titre dérivé de la User Story]

  Scenario: [Titre du cas de test]
    Given [précondition 1]
    And [précondition 2]
    When [action utilisateur 1]
    And [action utilisateur 2]
    Then [résultat attendu 1]
    And [résultat attendu 2]

RÈGLES STRICTES :
- Mots-clés Gherkin en ANGLAIS, contenu en FRANÇAIS
- Chaque cas de test fonctionnel ET chaque cas limite devient un Scenario
- NE PAS inclure les risques
- Pour les scénarios avec plusieurs jeux de données, utilise Scenario Outline avec Examples
- Pas de formatage Markdown — du texte brut Gherkin uniquement
"""

# --- Header ---
st.markdown(f"""
<div class="main-header">
    <div class="badge">{ICON_ZAP} Propuls&eacute; par l'IA</div>
    <h1>QA Test Generator</h1>
    <p class="tagline">Transformez vos User Stories en cas de test complets en 30 secondes.</p>
    <div class="welcome-stats">
        <div class="stat-item">
            <div class="stat-number">4</div>
            <div class="stat-label">Formats d'export</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">30s</div>
            <div class="stat-label">Temps de g&eacute;n&eacute;ration</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">0</div>
            <div class="stat-label">Config requise</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- API Key (from secrets) ---
api_key = st.secrets.get("MAMMOUTH_API_KEY", "")

with st.sidebar:
    st.markdown("### QA Test Generator")
    st.markdown("---")
    st.markdown("### Guide rapide")
    st.markdown("""
    1. Collez votre User Story
    2. *(Optionnel)* Ajoutez le contexte de votre app
    3. Cliquez sur **Générer**
    4. Exportez en Markdown, TXT, CSV Azure DevOps ou Gherkin
    """)

    st.markdown("---")

    # Modèles disponibles configurables via secrets (clé MAMMOUTH_MODELS)
    default_models = ["claude-sonnet-4-6", "claude-opus-4-6", "gemini-3.1-pro-preview", "gpt-4o", "gpt-5.2"]
    models = st.secrets.get("MAMMOUTH_MODELS", default_models)

    if not isinstance(models, (list, tuple)) or len(models) == 0:
        models = default_models

    model_choice = st.selectbox(
        "Modèle LLM",
        options=models,
        index=0,
        help="Choisir le modèle utilisé pour générer les cas de test et les conversions."
    )

    st.markdown("### Exemple de User Story")
    st.code("""En tant qu'utilisateur,
je veux pouvoir réinitialiser
mon mot de passe via email,
afin de récupérer l'accès
à mon compte.""", language=None)

    st.markdown("---")
    st.markdown("### Exemple de contexte")
    st.code("""App : MonBanquier.fr
Type : app bancaire web
URL : https://app.monbanquier.fr
Pages : Login, Dashboard, Profil
Rôles : Client, Conseiller, Admin
Techno : React + API REST
Règles mot de passe : 
min 8 caractères, 1 majuscule, 
1 chiffre, 1 caractère spécial""", language=None)

    st.markdown("---")
    st.markdown("### Exports disponibles")
    st.markdown("Markdown · TXT · CSV Azure DevOps · Gherkin")

# --- Helper: Convert JSON to CSV ---
def json_to_azure_csv(test_cases_json):
    output = io.StringIO()
    fieldnames = ["Title", "Step Action", "Step Expected"]
    writer = csv.DictWriter(output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    def parse_numbered_list(text):
        text = (text or "").replace('\r\n', '\n').replace('\r', '\n').strip()
        if not text:
            return []
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        parsed = []
        for line in lines:
            m = re.match(r'^\s*\d+\.\s*(.*)$', line)
            if m:
                parsed.append(m.group(1).strip())
            else:
                parsed.append(line)
        return parsed

    for tc in test_cases_json:
        title = tc.get("Summary", "").strip()
        test_steps = parse_numbered_list(tc.get("Test Steps", ""))
        expected_results = parse_numbered_list(tc.get("Expected Result", ""))

        # 1st line: only title
        writer.writerow({"Title": title, "Step Action": "", "Step Expected": ""})

        # remaining rows: step/action mapping
        max_rows = max(len(test_steps), len(expected_results))
        for i in range(max_rows):
            action = test_steps[i] if i < len(test_steps) else ""
            expected = expected_results[i] if i < len(expected_results) else ""
            writer.writerow({"Title": "", "Step Action": action, "Step Expected": expected})

    return output.getvalue()

# --- Mamouth API helper ---
def mamouth_generate(user_message, api_key, model="gpt-4.1", temperature=0.2, max_tokens=1200):
    url = "https://api.mammouth.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    }

    response = requests.post(url, headers=headers, json=payload, timeout=90)
    response.raise_for_status()
    data = response.json()

    if not data.get("choices") or not data["choices"]:
        raise ValueError("Mammouth API returned empty choices")

    # Compatible OpenAI-style response
    content = data["choices"][0].get("message", {}).get("content")
    if content is None:
        raise ValueError("Mammouth API response missing message content")

    return content

# --- Main Inputs ---
st.markdown(f'<p class="section-title">{ICON_CLIPBOARD} Votre User Story</p>', unsafe_allow_html=True)
user_story = st.text_area(
    "User Story",
    height=150,
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...\n\nVous pouvez aussi coller des critères d'acceptance, des règles métier, ou toute description fonctionnelle.",
    label_visibility="collapsed"
)

with st.expander("Contexte applicatif (optionnel — recommandé pour des tests plus précis)"):
    app_context = st.text_area(
        "Décrivez votre application",
        height=120,
        placeholder="Nom de l'app, type (web/mobile), URL, pages principales, rôles utilisateurs, règles métier, stack technique, contraintes spécifiques...\n\nPlus vous donnez de contexte, plus les cas de test seront précis et exécutables.",
        label_visibility="collapsed"
    )

# --- Generate Button ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate = st.button("Générer les cas de test", use_container_width=True, type="primary")

# --- Generation Logic ---
if generate:
    if not api_key:
        st.error("Configuration API manquante. Contactez l'administrateur.")
    elif not user_story.strip():
        st.error("Collez une User Story pour commencer.")
    else:
        try:
            if app_context and app_context.strip():
                user_message = f"CONTEXTE APPLICATIF :\n{app_context}\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"
            else:
                user_message = f"AUCUN CONTEXTE APPLICATIF FOURNI. Tu DOIS utiliser [À DÉFINIR PAR LE TESTEUR] pour toute donnée spécifique à l'application. N'invente RIEN.\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"

            with st.spinner("Analyse et génération des tests..."):
                result = mamouth_generate(user_message, api_key, model=model_choice)

            st.session_state['result'] = result
            st.session_state['user_story'] = user_story
            st.session_state['app_context'] = app_context if app_context else ""

            with st.spinner("Préparation de l'export CSV Azure DevOps..."):
                try:
                    csv_response_text = mamouth_generate(f"Convertis ces cas de test en JSON :\n\n{result}", api_key, model=model_choice)
                    raw_json = csv_response_text.strip()
                    if raw_json.startswith("```"): raw_json = raw_json.split("\n", 1)[1]
                    if raw_json.endswith("```"): raw_json = raw_json.rsplit("```", 1)[0]
                    raw_json = raw_json.strip()
                    test_cases = json.loads(raw_json)
                    st.session_state['csv_data'] = json_to_azure_csv(test_cases)
                    st.session_state['csv_count'] = len(test_cases)
                except Exception:
                    st.session_state['csv_data'] = None
                    st.session_state['csv_count'] = 0

            with st.spinner("Génération des scénarios Gherkin..."):
                try:
                    gherkin_text = mamouth_generate(f"Convertis ces cas de test en scénarios Gherkin :\n\n{result}", api_key, model=model_choice).strip()
                    if gherkin_text.startswith("```"): gherkin_text = gherkin_text.split("\n", 1)[1]
                    if gherkin_text.endswith("```"): gherkin_text = gherkin_text.rsplit("```", 1)[0]
                    st.session_state['gherkin_data'] = gherkin_text.strip()
                except Exception:
                    st.session_state['gherkin_data'] = None

        except Exception as e:
            st.error(f"Erreur : {str(e)}")

# --- Display results from session_state ---
if st.session_state.get('result'):
    result = st.session_state['result']
    us = st.session_state.get('user_story', '')
    ctx = st.session_state.get('app_context', '')

    st.markdown("---")

    tab_results, tab_gherkin = st.tabs(["Cas de test", "Gherkin / BDD"])

    with tab_results:
        st.markdown(result)

    with tab_gherkin:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.code(gherkin_data, language="gherkin")
        else:
            st.info("Gherkin non disponible pour cette génération.")

    # --- Export Options ---
    st.markdown("---")
    st.markdown(f'<p class="section-title">{ICON_DOWNLOAD} Exporter les résultats</p>', unsafe_allow_html=True)

    col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)

    with col_exp1:
        export_header = f"# QA Test Generator\n\n## User Story\n{us}"
        if ctx.strip(): export_header += f"\n\n## Contexte applicatif\n{ctx}"
        markdown_content = f"{export_header}\n\n---\n\n{result}"
        st.download_button(label="Markdown", data=markdown_content, file_name="test_cases.md", mime="text/markdown", use_container_width=True, key="dl_markdown")

    with col_exp2:
        txt_header = f"User Story:\n{us}"
        if ctx.strip(): txt_header += f"\n\nContexte applicatif:\n{ctx}"
        txt_content = f"{txt_header}\n\n---\n\n{result}"
        st.download_button(label="TXT", data=txt_content, file_name="test_cases.txt", mime="text/plain", use_container_width=True, key="dl_txt")

    with col_exp3:
        csv_data = st.session_state.get('csv_data')
        csv_count = st.session_state.get('csv_count', 0)
        if csv_data:
            st.download_button(label=f"CSV Azure DevOps ({csv_count})", data=csv_data, file_name="test_cases_azure_devops.csv", mime="text/csv", use_container_width=True, key="dl_csv")
        else:
            st.warning("CSV indisponible")

    with col_exp4:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.download_button(label="Gherkin", data=gherkin_data, file_name="test_cases.feature", mime="text/plain", use_container_width=True, key="dl_gherkin")
        else:
            st.warning("Gherkin indisponible")

# --- Footer ---
st.markdown(f"""
<div class="footer">
    QA Test Generator {ICON_SHIELD} Propuls&eacute; par l'IA · Fait pour la communaut&eacute; QA<br>
    <span style="font-size: 0.7rem; color: #d1d5db;">Un outil par Amadou FOFANA — Le Testeur Augment&eacute;</span>
</div>
""", unsafe_allow_html=True)
