import hashlib

def countries_wiki(path):
  with open(path, 'r', encoding='utf-8') as f:
    for line in f:
      yield hashlib.md5(line.strip().encode('utf-8'))

if __name__ == '__main__':
  with open('result.txt', 'w') as f:
    for hesh in countries_wiki('try.txt'):
      code = hesh.hexdigest() + '\n'
      f.write(code)
