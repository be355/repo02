# Gerenciador e Modificador de Batalhões

## Do código e suas funcionalidades.

O código "Mecajun2.py" contém um sistema para facilitar o gerenciamento e modificação de Batalhões que estão ativamente lutando.

O código permite:
  Visualizar as divisões de guerra existentes
  Adiconar uma nova divisão
  Remover uma divisão
  Modificar o número de Dobradores e não Dobradores de uma divisão
  Consultar as modificações realizadas

Primeiramente, o código define as funções que serão utilizadas no projeto, acessa os batalhões previamente definidos e cria um local para interação com o usuário. Após isso, cabe ao usário decidir quais modificações serão feitas. O programa conta com 5 funções que serão responsáveis pelas funcionalidades citadas anteriormente.

A função "show_bat" é responsável pela visualização dos batalhões existentes. Com isso em vista, ela mostra ao usuário todos os batalhões presentes e seus respectivos números de Dobradores e Não Dobradores, permitindo fácil acesso a estas informações.

Já o código "add_bat" permite ao usuário adiconar uma nova divisão de combate e informar seus números de Dobradores e Não Dobradores (O código contém medidas para evitar números negativos e divisões duplicadas).

A função "exclude_bat" faz o oposto a anterior e remove batalhões da lista de ativos, contém uma breve exibição das opções existentes.

O código "mod_bat" possibilita a modificação dos números de qualquer divisão de combate ativa, há a distinção entre Dobradores e Não Dobradores e medidas para evitar números negativos.

Por fim, a função "show_mod" descreve ao usuário quais modificações foram realizadas e em que ordem, visando fácil acesso a estes dados e a possibilidade de envios de relatórios detalhados para superiores.

## Modificações futuras

Para melhorar o programa enviado, existe a possibilidade de criar uma base de dados para estas informações. Deste modo, informações podem ser mantidas e atualizadas de diferentes locais. Além disso, a adição de um sistema para criptografar, da maneira desejada, os dados permitirá um fácil e seguro envio a diferentes indivíduos.
