# Change directory to client
cd client
# Start Next.js development server
Start-Process -NoNewWindow -FilePath "npm" -ArgumentList "run dev"

# cd ../server
# Start Python application
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "../server/main.py"

# Wait for both processes to exit
Wait-Process -Name "node"
Wait-Process -Name "python"