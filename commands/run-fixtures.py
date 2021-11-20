import os

def normalize(names):
    return list(map(lambda name: name.rstrip(), names))


lsStream = os.popen('ls fixtures/')
fixturesNames = normalize(lsStream.readlines())

for name in fixturesNames:
    loadStream = os.popen('python manage.py loaddata --skip-checks fixtures/' + name)
    print(name + ' ' + loadStream.read())