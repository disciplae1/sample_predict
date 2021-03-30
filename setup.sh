mkdir -p ~/.samplepredict/

echo "[server]
headless = true
port = process.env.PORT || 8000
enableCORS = false
" > ~/.samplepredict/config.toml
