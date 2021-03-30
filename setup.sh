mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = process.env.PORT || 8000
enableCORS = false
" > ~/.streamlit/config.toml
