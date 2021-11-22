import os

fixturesNames = os.listdir('fixtures/')

for name in fixturesNames:
    loadStream = os.popen('python manage.py loaddata --skip-checks fixtures/' + name)
    print(name + ' ' + loadStream.read())