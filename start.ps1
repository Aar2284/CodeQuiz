Write-Host "Starting Quiz System..." -ForegroundColor Cyan
    python -m pip install -r requirements.txt --quiet
    python manage.py migrate
    Write-Host "Opening http://127.0.0.1:8000" -ForegroundColor Green
    python manage.py runserver