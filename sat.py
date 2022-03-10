import re
from itertools import product
import sys

f = open(sys.argv[1], "r")
input = f.read()
input = input.strip()

# despart fiecare clauza din string intr-o lista
clause_split = input[1:-1]
clause_split = clause_split.split(")^(")

# cel mai mare numar din input
res = re.findall(r'\d+', input)
val_max = max(list(map(int, res)))

FNC_SAT = []
variable = []
var_nr = 0
negativ = 0

# am luat un for pentru a parcurge toate clauzele
for i in range(len(clause_split)):
  # despart fiecare variabila din stringul unei clauze
  variable_split = clause_split[i].split("V")
  # setez lista de variabile cu 0
  variable = [0 for l in range(val_max)]

  # am luat un for pentru a parcurge toate variabilele din clauza
  for j in range(len(variable_split)):

    if variable_split[j][0] == "~":
      negativ = 1
      variable_split[j] = variable_split[j][1:]

    # fac cast din string in int la fiecare variabila
    var_nr = int(int(variable_split[j]) - 0)

    if negativ == 1:
      variable[var_nr-1] = -1
    else:
      variable[var_nr-1] = 1
    var_nr = 0
    negativ = 0

  # bag fiecare clauza cu variabile in FNC_SAT
  FNC_SAT.append(variable)

# creez matricea binara
matrix_bin = list(product([0,1], repeat=val_max))

# am luat un for pentru a parcurge toate cazurile din matricea binara
for i in range(len(matrix_bin)):

  # am luat un for pentru a parcurge toate clauzele
  for j in range(len(FNC_SAT)):
    out = 0

    # am luat un for pentru a parcurge toate variabilele dintr-o clauza
    # si am verificat daca formula de la input este satisfiabila
    for k in range(val_max):
      if FNC_SAT[j][k] == -1 and matrix_bin[i][k] == 0:
        out = 1
        break
      elif FNC_SAT[j][k] == -1 and matrix_bin[i][k] == 1:
        out = 0
      elif FNC_SAT[j][k] == 1 and matrix_bin[i][k] == 0:
        out = 0
      elif FNC_SAT[j][k] == 1 and matrix_bin[i][k] == 1:
        out = 1
        break
    if out == 0:
        break
  if out == 1:
    break

print(out)