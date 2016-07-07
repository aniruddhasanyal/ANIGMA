@echo off
echo Access at http://127.0.0.1:8000
python -m http.server --cgi 8000
pause>nul