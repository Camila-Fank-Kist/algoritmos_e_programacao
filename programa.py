def acertos(gab, res):
  num_acertos = 0
  for i in range(len(gab)):
    if gab[i] == res[i]:
      num_acertos += 1
  return num_acertos
gabarito = ['A', 'B', 'A', 'C', 'B', 'D', 'E', 'A', 'A', 'C']
respostas = ['C', 'B', 'B', 'C', 'A', 'A', 'E', 'A', 'A', 'C']
print(acertos(gabarito, respostas))