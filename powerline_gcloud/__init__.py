import subprocess

def project(pl):
    return u'\u2601 ' + subprocess.Popen(['sh', '-c', 'cat ~/.config/gcloud/configurations/config_default | grep "project =" | cut -d" " -f3'], stdout=subprocess.PIPE).communicate()[0].strip().decode('utf8')
    return subprocess.Popen(['gcloud', 'config', 'get-value', 'project'], stdout=subprocess.PIPE).communicate()[0].strip().decode('utf8')
