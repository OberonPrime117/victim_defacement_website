import subprocess

process = subprocess.Popen(['python', '-m', 'http.server', '8080'])
try:
    process.communicate()
except KeyboardInterrupt:
    process.kill()