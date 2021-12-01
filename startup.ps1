if (-Not (Test-Path -Path '.venvWin')) {
    python3 -m venv .venvWin
    .\.venvWin\Scripts\Activate
    python3 -m pip install -r .\requirements.txt
} else {
    .\.venvWin\Scripts\Activate
}

python3 main.py