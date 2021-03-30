mkdir -p ~/.sample_predict/

echo "[server]
headless = true
port = process.env.PORT || 8000
enableCORS = false
" > ~/.sample_predict/config.toml
