import streamlit as st
from core.parser import parse_file
from core.classifier import classify_contract
from core.clause_extractor import extract_clauses
from core.risk_engine import score_clause
from core.llm_engine import explain_clause

st.set_page_config(page_title="LegalLens AI", layout="wide")

st.title("⚖️ LegalLens AI")
st.caption("GenAI-powered contract risk analyzer for Indian SMEs")

uploaded = st.file_uploader(
    "Upload a contract (PDF, DOCX, or TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded:
    text = parse_file(uploaded, uploaded.type.split("/")[-1])
    contract_type = classify_contract(text)
    clauses = extract_clauses(text)

    st.success(f"Detected Contract Type: {contract_type}")
    total_score = 0

    for clause in clauses[:5]:
        score, level = score_clause(clause["text"])
        total_score += score

        with st.expander(f"Clause {clause['id']} — Risk: {level}"):
            st.write(clause["text"])
            st.markdown("**Plain-English Explanation & Advice**")
            st.write(explain_clause(clause["text"]))

    st.metric("Overall Contract Risk Score", total_score)
