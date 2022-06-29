from random import choice

def remover_porta_escolhida(porta,portas):
    removida=0
    for i in range(len(portas)):
        if portas[i]==porta:
            removida=i
    del portas[removida]
    return portas

def trocar_porta(porta_atual,portas):
    for porta in portas:
        if porta_atual != porta:
            porta_atual = porta
    return porta_atual


def monty_hall(bool_troca):
  portas = [1,2,3]
  escolhas_portas = [1,2,3]
  premio = choice(escolhas_portas)
  jogador = choice(escolhas_portas)
  escolhas_portas = remover_porta_escolhida(jogador,escolhas_portas)
  escolhas_portas = remover_porta_escolhida(premio,escolhas_portas)
  # Aqui está a dica do negócio, o apresentador não escolhe o prêmio e nem a sua porta, logo há uma alta chance da troca dar certo
  apresentador = choice(escolhas_portas)
  portas = remover_porta_escolhida(apresentador,portas)
  if bool_troca:
      jogador = trocar_porta(jogador,portas)
  if jogador == premio:
      return "Ganhou"
  else:
      return "Perdeu"
      
i=0
taxa_acerto_troca=0
taxa_acerto_manter=0
max_iteracoes=5
while(i<max_iteracoes):
    # Com troca
    resultado = monty_hall(True)
    if resultado=="Ganhou":
        taxa_acerto_troca+=1
    # Sem troca
    resultado = monty_hall(False)
    if resultado=="Ganhou":
        taxa_acerto_manter+=1
    i+=1

acerto_porcentagem_troca=(taxa_acerto_troca/max_iteracoes)*100
acerto_porcentagem_manter=(taxa_acerto_manter/max_iteracoes)*100
print('Taxa de acerto com troca é de {}%'.format(acerto_porcentagem_troca))
print('Taxa de acerto sem troca é de {}%'.format(acerto_porcentagem_manter))