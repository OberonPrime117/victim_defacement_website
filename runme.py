import subprocess

process = subprocess.Popen(['python', '-m', 'http.server', '8000'])
try:
    process.communicate()
except KeyboardInterrupt:
    process.kill()