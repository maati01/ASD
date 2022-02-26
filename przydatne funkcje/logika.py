while True:
  try:
    s = list(input())
  except:
    break

  d = {'¬': '~', '∧': '&','∨': 'v','⇒': '->','⇔': '<->'}
  for i in range(len(s)):
    if s[i] in d:
      s[i] = d[s[i]]

  s = ''.join(s)
  s = s.replace('=>', '->')

  print(s)