'''
Trabalho - Jogo de Ficção Interativa 
SME0827 - Estruturas de Dados
Beatriz Proença Carvalho - 10408302
Caio Henrique Mendes Schiavo - 11810602
Filipe Vasconcelos Ferreira - 7286339
 Vikson Gianotti Andrade dos Santos - 10733900
'''

'''
codigo dos acessorios
6 chaves: 1, 2, 3, 4, 5, 6
cola  0
blusa  7
chave do carro 8
manual 9
'''

# inventario de coisas para carregar
bag = []
#conjunto de chaves, se tiver todas pode ir embora
chaves = []

class Object:
  def __init__(self, name, story_piece, key=-1):
    self.name = name
    self.story_piece = story_piece
    self.key = key # identifica se o objeto possui umas das chaves, -1 nao possui chave

# cada no é um lugar para se visitar
class TreeNode :
  def __init__(self, name, story_piece, objects=[]):
    self.story_piece = story_piece
    self.name = name
    self.objects = objects
    self.children = []
  
#Adiciona um nó filho
  def add_child(self, child_node):
    self.children.append(child_node)

#Adiciona o objeto no inventário
  def get_obj(self, id):
    bag.append(self.objects.pop(id))

def end_game(current_node):
  # verifica se todas as condiçoes para o jogo acabar são satisfeitas
  # tem todas as chaves:
  if len(chaves) < 6: return False
  #esta no ultimo comodo
  if current_node.name != "Porta": return False

  # possui o manual e a cola
  tem_manual = False
  tem_cola = False
  for object in bag:
    if object.key == 9: tem_manual = True
    if object.key == 0: tem_cola = True

  # possui todas as condicoes para acabar
  return tem_cola and tem_manual

class Tree:
  def __init__(self, root):
    self.root = root
    
  def traverse(self):
    story_node = self.root
    print(story_node.story_piece)

    # fazer um loop o fim do jogo
    # isto é, até o final do percurso
    while not end_game(story_node):
      print("Escolha para onde você quer ir:\n")

      for place_index in range(len(story_node.children)):
        print(" Escolha "+str(place_index)+" para ir ate "+story_node.children[place_index].name)

      choice = int(input("Insira sua escolha: "))
      if choice not in range(len(story_node.children)):
        print("Por favor insira um valor dentro do intervalo válido!\n")
      else:
        chosen_index = choice 
        chosen_place = story_node.children[chosen_index]
        print(chosen_place.story_piece+"\n")

        is_searching = True
        while is_searching :
          if len(chosen_place.objects) == 0:
              print("Não há nada de novo para se ver.")
              break

          print("Você pode ver:\n")
          for obj_index in range(len(chosen_place.objects)):
            print(" Escolha "+str(obj_index)+" para ir interagir com "+chosen_place.objects[obj_index].name)
          
          obj_index = int(input("Insira sua escolha: "))

          if obj_index not in range(len(chosen_place.objects)):
            print("Por favor insira um valor dentro do intervalo válido!\n")
          else:
            chosen_obj = chosen_place.objects[obj_index]
            print(chosen_obj.story_piece+"\n")

            deve_quardar = input("Você quer guardar esse objeto? (s/n) \n")
            if deve_quardar == "s":
              if chosen_obj.key >= 1 and chosen_obj.key <= 6 :
                chaves.append(chosen_place.objects.pop(obj_index))
              elif chosen_obj.key >= 0:
                bag.append(chosen_place.objects.pop(obj_index))
              else: print("Não se pode guardá-lo\n")
            
            deve_continuar = input("Você quer continuar procurando? (s/n) \n")
            if deve_continuar == "n":
              is_searching = False
            

        story_node = chosen_place
    
    print("Você conseguiu tudo o que precisava para montar a chave e destrancar a nova fechadura!!\n")
    print("Finalmente a porta se abriu, está um dia lindo la fora, porque não sai um pouco hoje ;)")


             


######
# Lugares da historia
######
inicio = TreeNode("Inicio", "Voce acaba de acordar sozinho dentro de casa, sua aventura aqui é encontrar todas as 6 chaves para poder sair. Boa sorte ;)\n")
quarto = TreeNode("Quarto", "Voce esta dentro de seu quarto, um pouco de luz atravessa a janela e voce sabe que já amanheceu\n",
  [
    Object("Cama", "Você vê sua cama desarrumada, embaixo de seu cobertor tem um volume, você o puxa e encontra umas das chaves.\n", 1),
    Object("Prateleira", "Você vê sua prateleira e de relance percebe um pequeno brilho, encontra mais uma chave.\n", 2),
    Object("Mesa", "Observa sua mesa e ela esta do jeito que você a deixou ontem.\n"),
    Object("Embaixo da cama", "Você empurra sua cama para verificar se havia esquecido algo lá mas não encontra nada.\n"),
    Object("Armário", "Decide abrir seu armário, não ve nada além das suas roupas penduradas, inclusive lembra que precisa por seu casaco de couro para lavar.\nA última vez que usou ele voltou sujo de terra.\n"),
    Object("Janela", "Vai até a janela, vê que o dia está ensolarado, o que de da mais vontade de encontrar as chaves para sair logo de casa.\n")
  ])
inicio.add_child(quarto)


sala = TreeNode("Sala", "Você entra na sala, está um pouco escura, você ascende a luz e logo se depara com algumas coisas: \n",
  [
    Object("Caixa de sapato", "Seu pai é um cara meio distraído, você vê a caixa de sapatos sociais dele jogada meio aberta no chão. Você vai guardá-la e vê que ele deixou um dos pedaços lá dentro\n", 3),
    Object("Caixa de ferramentas", "Seu pai adora construir coisas por conta própria, vive deixando sua caixa de ferramentas em todo canto.\n Você pega para guardar e acha outro pedaço da chave", 4),
    Object("Chão", "A sala está organizada, apesar do seu pai, sua mãe adora manter tudo em ordem, está limpo, com excessão de outro pedaço da chave jogado perto da porta.\n", 5),
    Object("Ratoeira", "Sua mãe tem pavor de certos animais, só de ouvir alguns barulhos de noite, já deixou a casa cheia de ratoiras armadas, uma delas está no seu pé, você quase esbarra nela.\n")    
  ]
)
quarto.add_child(sala)
sala.add_child(quarto)

escritorio = TreeNode("Escritorio", "Entrou no escritorio do seu pai", 
  [
    Object("Gavata de cima", "A primeira gaveta esta semi-aberta, você abre e acha a cola especial de seu pai, pode usá-la para juntar os pedaços", 0),
    Object("Gavate de baixo", "A segunda gaveta esta fechada, mas sem tranca, você abre e encontra outra chave", 6),
    Object("Chaveiro", "Você vê em cima da mesa principal o chaveiro"),
    Object("Porta do lado da mesa", "Essa é a porta onde seu pai guarda suas ferramentas mais valiosas, você tenta abri-lá, mas verifica que está fechada.\n"),
    Object("Computador", "Seu pai como um amante de tecnologia sempre deixa o computador ligado, você que a última aba aberta era um manual de uso de um novo tipo de motor elétrico.\n")
  ])
sala.add_child(escritorio)
escritorio.add_child(sala)


sala_principal = TreeNode("Sala principal", "Esta agora na sala de visitas, a manha já se estendeu e a luz do dia a ilumina completamente.",
  [
    Object("Arara", "Próximo da porta há uma arara para se pedurar roupas, sua blusa da faculdade esta jogada em um dos braços", 7),
    Object("Sofa", "O sofá esta arrumado, com todas as almofadas posicionas, no braço você encontra a chave do carro da sua mãe", 8),
    Object("Estante", "Na estande próxima da porta estão todas as fotos de familia, com recordações da férias. Atras de um desses quadros a um pequeno livro."+
          "\nO manual de como de montar a chave para a fechadurra tecnologica que seu pai instalou.\nPrecisa apenas ter todas os pedaços e a cola para montar a chave final.\n", 9),
    Object("Tapete", "A sala possui um tapete felpudo, você se ajoelha para tentar encontrar algo de interessante nele, mas sem sucesso.\n")
  ])

sala_principal.add_child(escritorio)
escritorio.add_child(sala_principal)

fim = TreeNode("Porta", "Você esta diante da porta de casa, pode tentar abri-lá, mas para isso precisa montar a chave tecnológica que seu pai criou."
      +"\nVocê sabe que existe uma manual dentro da casa pra construi-la com as partes da chave e que vai precisar de uma cola especifica pra por todas juntas e sair.")
sala_principal.add_child(fim)
fim.add_child(sala_principal)


######
# TESTING AREA
######

historia = Tree(inicio)

historia.traverse()