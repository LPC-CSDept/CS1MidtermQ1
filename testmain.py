
try:
    f = open('main.cpp')
except Exception as e:
    print('False')
    # print (e)
else:
    lines = f.read()

if 'if' in lines:
    print('False')
else:
    print('True')
