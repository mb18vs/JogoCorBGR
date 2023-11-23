import random
pontos_seus = 0
pontos_deles = 0
while(True):
  cor_secreta = random.choice (['R','G','B' ])
  palpite = input("Adivinhe a cor (R,G,B): ").upper()
  if palpite not in ['R', 'G', 'B']:
     print("Entrada inválida, Escolha R, G, B.")
  elif palpite == cor_secreta:
      print("Parabéns! Você ACERTOU!")
      pontos_seus = pontos_seus +1
  elif palpite != cor_secreta:
      print(" Você Errou!!")
      pontos_deles = pontos_deles +1
  print('Acor era', cor_secreta)

  print(f'VOCỄ {pontos_seus} X PC {pontos_deles}')