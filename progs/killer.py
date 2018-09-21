import subprocess

lines = subprocess.check_output('tasklist', shell=True).split('\r\n')

chrome = filter(lambda x : 'chrome.exe' in x , lines)

pids = [line.split()[1] for line in chrome]

for pid in pids:
    subprocess.call('taskkill /pid ' + pid)