import json
import struct
import subprocess

obj = subprocess.Popen(
    "ls",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

stdout = obj.stdout.read()
stderr = obj.stderr.read()

print(stdout+stderr)
