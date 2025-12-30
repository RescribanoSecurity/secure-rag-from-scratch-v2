import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Secure RAG v2",
    layout="wide"
)

st.title("🔐 Secure RAG v2 – Visual Client")
st.markdown(
    """
    Interactive client to query the Secure RAG v2 system and
    **inspect security decisions, sources, and traceability**.
    """
)

st.divider()

# -------------------------------------------------
# Session state
# -------------------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# -------------------------------------------------
# Query input
# -------------------------------------------------
query = st.text_input(
    "Enter your query",
    placeholder="e.g. What is a RAG system?"
)

col1, col2 = st.columns([1, 1])

with col1:
    run = st.button("🚀 Run Query", use_container_width=True)

with col2:
    clear = st.button("🧹 Clear", use_container_width=True)

# -------------------------------------------------
# Clear
# -------------------------------------------------
if clear:
    st.session_state.result = None
    st.rerun()

# -------------------------------------------------
# Run query (STATE UPDATE ONLY)
# -------------------------------------------------
if run and query:
    with st.spinner("Querying Secure RAG..."):
        response = requests.post(API_URL, json={"query": query})

    if response.status_code != 200:
        st.error(f"API error: {response.status_code}")
    else:
        st.session_state.result = response.json()

# -------------------------------------------------
# Render result
# -------------------------------------------------
def render_result(data: dict):
    input_sec = data.get("security_flags", {})
    output_sec = data.get("output_security")
    block_reason = data.get("block_reason")

    in_action = input_sec.get("action", "unknown")
    out_action = output_sec.get("action") if output_sec else None

    # -----------------------------
    # INPUT SECURITY BANNER
    # -----------------------------
    if in_action == "allow":
        st.success("✅ Input allowed by security policy")
    elif in_action == "warn":
        st.warning("⚠️ Input allowed with warnings (potential risk detected)")
    elif in_action == "block":
        st.error("⛔ Input blocked by security policy")
    else:
        st.info("ℹ️ Input security decision unknown")

    # -----------------------------
    # OUTPUT SECURITY BANNER
    # -----------------------------
    if output_sec:
        if out_action == "allow":
            st.success("✅ Output allowed by security policy")
        elif out_action == "warn":
            st.warning("⚠️ Output allowed with warnings")
        elif out_action == "redact":
            st.warning("🟡 Output redacted due to sensitive data detection")
        elif out_action == "block":
            st.error("⛔ Output blocked due to sensitive data detection")

    # -----------------------------
    # Answer
    # -----------------------------
    st.subheader("🧠 Answer")
    st.write(data.get("answer", ""))

    if block_reason:
        st.caption(f"🔒 Block reason: `{block_reason}`")

    # -----------------------------
    # Security Analysis
    # -----------------------------
    st.markdown("---")
    st.subheader("🔐 Security Analysis")

    left, right = st.columns([1, 1])

    # LEFT – Security details
    with left:
        st.markdown("### 🛠️ Security Details")

        subl, subr = st.columns(2)

        with subl:
            st.markdown("**Input Security**")
            st.metric("Action", in_action.upper())
            st.metric("Risk score", input_sec.get("risk_score", 0))

            st.markdown("**Reasons:**")
            reasons = input_sec.get("reasons", [])
            if not reasons:
                st.write("- none")
            else:
                for r in reasons:
                    st.write(f"- {r}")

        with subr:
            st.markdown("**Output Security**")
            if not output_sec:
                st.write("Not executed")
            else:
                st.metric("Action", out_action.upper())
                st.metric("Risk score", output_sec.get("risk_score", 0))

                st.markdown("**Findings:**")
                findings = output_sec.get("findings", [])
                if not findings:
                    st.write("- none")
                else:
                    for f in findings:
                        st.write(
                            f"- {f.get('category')} "
                            f"(severity {f.get('severity')}, count {f.get('count')})"
                        )

    # RIGHT – OWASP mapping
    with right:
        st.markdown("### 🛡️ OWASP LLM Top 10 Mapping")

        violations = data.get("policy_violations", [])

        if not violations:
            st.success("✅ No OWASP policy violations detected.")
            if output_sec and out_action in ("redact", "block"):
                st.warning(
                    "Output Security triggered (PII/secret detection). "
                    "This maps conceptually to OWASP LLM02."
                )
        else:
            for v in violations:
                with st.expander(
                    f"🔴 {v['owasp_id']} – {v['owasp_name']} ({v['risk_level']})",
                    expanded=True,
                ):
                    st.write(v["description"])
                    st.markdown(
                        "**Detected by:** "
                        + ", ".join(v.get("detected_by", []))
                    )
                    st.markdown("**Controls applied:**")
                    for c in v.get("controls_applied", []):
                        st.write(f"- {c['control_id']}: {c['name']}")

    # -----------------------------
    # Retrieved sources
    # -----------------------------
    st.subheader("📚 Retrieved Sources")

    sources = data.get("sources", [])
    if not sources:
        st.info("No sources returned.")
    else:
        for idx, source in enumerate(sources, start=1):
            with st.expander(f"Source {idx}"):
                st.write(source.get("text", ""))

    # -----------------------------
    # Request ID
    # -----------------------------
    st.subheader("🆔 Request ID")
    st.code(data.get("request_id", ""))


# -------------------------------------------------
# FINAL RENDER ANCHOR (DO NOT MOVE)
# -------------------------------------------------
st.divider()
st.markdown("## 📤 Query Result")

if st.session_state.result is not None:
    render_result(st.session_state.result)
