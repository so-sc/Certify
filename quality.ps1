# Install required packages (make sure pip is installed)
pip install pylint black pytest pytest-cov

# If the reports directory does not exist, create it
if (!(Test-Path -Path "./reports")) {
    New-Item -ItemType Directory -Path "./reports"
}

# Lint all Python files in the current directory and specific subfolders (utils and router)
pylint .\*.py .\utils\*.py .\router\*.py > ./reports/pylint_report.txt
Write-Host "Pylint report generated in reports/pylint_report.txt"

# Format all Python files in the current directory and specific subfolders (utils and router) with black (optional)
black .\*.py .\utils\*.py .\router\*.py
Write-Host "Code formatted with Black"

# Run tests with pytest (assuming your tests are in a 'tests' directory)
pytest tests > ./reports/pytest_report.txt
Write-Host "Pytest report generated in reports/pytest_report.txt"

# Check for code coverage (optional)
pytest --cov=. tests > ./reports/coverage_report.txt
Write-Host "Coverage report generated in reports/coverage_report.txt"
