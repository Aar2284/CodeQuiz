Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Quiz Project - Starting Up..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Install all required packages
Write-Host "[1/3] Installing required packages..." -ForegroundColor Yellow
python3 -m pip install django reportlab matplotlib python-dotenv --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install packages. Make sure Python 3 is installed." -ForegroundColor Red
    pause
    exit
}
Write-Host "      Packages installed!" -ForegroundColor Green

# Step 2: Apply database migrations
Write-Host "[2/3] Setting up the database..." -ForegroundColor Yellow
python3 manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Migration failed." -ForegroundColor Red
    pause
    exit
}
Write-Host "      Database ready!" -ForegroundColor Green

# Step 3: Start the development server
Write-Host ""
Write-Host "[3/3] Starting the web server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Open your browser and go to:" -ForegroundColor White
Write-Host "   http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "   Press Ctrl+C to stop the server" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python3 manage.py runserver
