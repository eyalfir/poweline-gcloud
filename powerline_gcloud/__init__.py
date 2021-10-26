import subprocess

def project(pl, prefix, command):
    return prefix + (" " if prefix else "") + subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].strip().decode('utf8')
