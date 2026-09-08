# Dimensionamento dos trilhos — Embalagem

Ferramenta de simulação da ocupação dos trilhos da Embalagem da Patrimar Móveis,
dentro do alcance das duas esteiras.

> **Origem das medidas.** O DWG foi a referência inicial, mas **está desatualizado** na região da
> parede esquerda. Onde há medição de campo, ela prevalece sobre o desenho: distâncias da parede ao
> trilho lateral e à esteira 1, e a defasagem entre as esteiras. O que ainda vem só do DWG —
> comprimento do barracão, comprimentos das esteiras, passo dos trilhos — continua sujeito ao mesmo
> erro e está listado em Pendências.

## O que faz

- Calcula quantas pistas cabem em cada esteira conforme o arranjo dos trilhos.
- Recomenda explicitamente um dos arranjos e diz por que descartou os outros.
- Imprime uma folha de conferência em campo com o que ainda precisa de trena.
- Desenha a planta em escala das três colunas (C1, C2 e C3) e das duas esteiras.
- Desenha o trilho de abastecimento com carrinho: uma faixa acima da C1, outra no vão entre C2 e C3 e uma lateral, à esquerda do início da esteira 1, no sentido dos trilhos.
- Destaca o aumento de 5 m da esteira 2 na planta e mostra quantas pistas ele acrescenta.
- Desenha o contorno do barracão com cotas e avisa quando o conjunto não cabe nele.
- Compara os cenários pela metragem linear de trilho.
- Gera as cotas acumuladas em CSV e a planta em SVG.
- Imprime em A4 paisagem com cabeçalho de parâmetros.

## Parâmetros

| Parâmetro | Padrão | Origem |
|---|---:|---|
| Largura do trilho | 500 mm | medido no DWG |
| Largura da prancha | 450 mm | informado pela Produção |
| Vão dentro do par | 200 mm | medido no DWG |
| Vão entre pares | 500 mm | proposta em estudo |
| Comprimento C1 / C2 / C3 | 6.000 / 4.000 / 4.000 mm | informado pela Produção |
| Esteira 1 | 850 × 23.940 mm | largura ajustada para 850 mm (DWG: 840); comprimento medido no DWG |
| Esteira 2 | 850 × 28.975 mm, defasada 5.550 mm | comprimento do DWG: 23.975 mm; defasagem medida em campo (9.800 mm da parede até a esteira 2, menos os 4.250 mm até a esteira 1) — o DWG traz 7.850 mm, guardados em `E2.iniDwg`; aumento de +5.000 mm no final (`E2_AUMENTO`), desenhado hachurado |
| Vão entre as colunas C2 e C3 | 2.100 mm | medido no DWG · fixo no código, não ajustável na tela |
| Trilho de abastecimento (carrinho) | 2.100 mm de largura | faixa acima da C1 e no vão C2–C3, informado pela Produção (no DWG os rails ocupam 1.570 mm no vão e 2.100 mm acima da C1) |
| Trilho de abastecimento lateral | 2.100 mm de largura, encostado na parede (850 mm) e a 1.300 mm da esteira 1 | mesma largura dos outros, informada pela Produção; as duas distâncias foram medidas em campo e somam 4.250 mm da parede à esteira 1, contra 6.470 mm no DWG — **o DWG está desatualizado nessa região e o campo prevalece**; ambas editáveis |
| Posição da esteira 2 | como está hoje (defasada 5.550 mm) | "Alinhada com a esteira 1" ou "Encostada no trilho lateral" deslocam a esteira 2 e a C3 para perto da parede esquerda; não muda a contagem de pistas |
| Posição do conjunto | como no DWG | "Encostado na parede esquerda" zera o afastamento esquerdo e joga a folga para o fim da esteira 2 |
| Barracão | 55.210 × 24.900 mm · parede esquerda a 850 mm da borda externa do trilho lateral (4.250 mm até a esteira 1) e parede do lado da esteira 2 a 1.450 mm dela | comprimento cotado no DWG; os dois afastamentos digitados foram medidos em campo; a largura é hipótese (linha de pilares). Com afastamento 0 a parede esquerda encosta no conjunto |
| Afastamento da parede do lado da C1 | derivado | Não é digitado: é `largura do barracão − altura do conjunto − afastamento do lado da esteira 2`. Sai negativo quando o conjunto não cabe na largura, e é assim que o erro aparece do lado que ninguém mediu, em vez de sumir |

## Recomendação de arranjo

A tela nomeia um dos quatro arranjos como recomendado, acima do comparativo. O critério é
explícito e está impresso junto com a resposta:

> **Mais pistas entre os arranjos que não pioram nenhum limite.** Empate em pistas, vence o de
> menor metragem.

Os limites são os mesmos das regras de aviso (`GE_MIN`, `PASS_MIN`, `FOLGA_MIN`) mais um: o apoio
da peça larga em dois trilhos não pode cair abaixo do que a fábrica já tem hoje (`APOIO_HOJE`,
1.200 mm). Cada arranjo descartado aparece com o motivo. Com os valores atuais:

| Arranjo | Pistas | Metragem | Apoio | Situação |
|---|---:|---:|---:|---|
| Versão 1 · par 200 · vão 500 | 90 | 416 m | 1.200 mm | **recomendado** |
| Versão 2 · par encostado · vão 500 | 102 | 472 m | 1.000 mm | fora: apoio abaixo do de hoje |
| Versão 3 · sem par · vão 500 | 77 | 356 m | 1.500 mm | apto, mas 13 pistas a menos |
| Passo do DWG · par 200 · vão 400 | 96 | 444 m | 1.200 mm | fora: vão de 400 mm e passagem de 740 mm |

**O `APOIO_HOJE` é o ponto fraco do critério.** A largura da peça mais larga apoiada em dois
trilhos nunca foi levantada; 1.200 mm é só o que o arranjo atual entrega. A Versão 2 dá 12 pistas
a mais e está fora só por isso. Quando a peça for medida, essa linha da recomendação muda ou se
confirma — a tela diz isso na cara, em vez de esconder atrás do número.

## Folha de conferência em campo

O botão "Conferir em campo" imprime a planta e, na página seguinte, uma tabela com cada medida,
o valor que a tela usa, a origem (campo, Produção, DWG, hipótese ou derivado) e uma coluna em
branco para anotar o que a trena disser. As linhas destacadas são as que ainda mudam alguma
decisão. A folha sai do estado atual da tela, então reflete o que estiver digitado na hora.

## Regras de aviso

A simulação avisa quando o cenário fere uma destas regras. Os limites ficam
como constantes nomeadas no início do script e valem para todos os cenários.

| Regra | Limite | O que acontece abaixo dele |
|---|---:|---|
| Vão entre pares (`GE_MIN`) | 500 mm | Não há circulação entre as vias. |
| Passagem para retirar prancha (`PASS_MIN`) | 800 mm | Não passa uma pessoa carregando prancha. |
| Folga da prancha no trilho (`FOLGA_MIN`) | 30 mm | Sem guia lateral, a prancha desalinha e trava. |
| Apoio da peça larga hoje (`APOIO_HOJE`) | 1.200 mm | Referência do arranjo atual para comparar a base da peça apoiada em dois trilhos. |
| Trilho de abastecimento no vão (`GAP_COL`) | 2.100 mm | A faixa do carrinho não cabe entre C2 e C3. |
| Conjunto dentro do barracão | sobra ≥ 0 no comprimento e afastamento do lado da C1 ≥ 0 | O conjunto ultrapassa a parede; o aviso diz quantos mm faltam. |

Os campos da tela têm mínimo e máximo declarados no HTML (`min`/`max`). Valores
fora da faixa, inclusive os que chegam pelo link compartilhado, são limitados a ela.

## Pendências

- O passo executado no chão de fábrica ainda não foi medido. Todos os cenários de
  referência vêm do desenho e podem estar desatualizados.
- No DWG a coluna C1 aparece com trilhos de 7.000 mm e a C3 com 3.000 mm, divergindo
  da informação de campo (6.000 e 4.000 mm).
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada.
- A largura do barracão (24.900 mm) e o afastamento do lado da C1 continuam sem medição. Como o
  afastamento do lado da esteira 2 (1.450 mm) veio de campo, é o lado da C1 que absorve o erro da
  largura: com 24.900 mm ele dá 3.550 mm, contra os 700 mm que a hipótese da linha de pilares
  indicava. Ou a largura não é 24.900 mm, ou a hipótese dos 700 mm estava errada — medir a largura
  interna resolve os dois.
- Barracão: o DWG cota 55.210 mm no sentido das esteiras, a partir de 6.470 mm antes do início
  da esteira 1, e a parede do lado da esteira 2 está a 1.380 mm dela. A cota de 23.570 mm do
  DWG não fecha com o trilho de abastecimento acima da C1 (rails a 10,3 m da esteira 1), então
  a largura de 24.900 mm e o afastamento de 700 mm foram tomados na linha de pilares a 11,0 m
  da esteira 1 e precisam ser confirmados.
- A defasagem da esteira 2 adotada é de **5.550 mm, medida em campo** (9.800 mm da parede até a
  esteira 2, menos 4.250 mm da parede até a esteira 1). O DWG traz 7.850 mm no eixo da esteira 1
  (8.170 mm na diferença bruta de coordenadas, porque o conjunto está girado 1,5° e as esteiras não
  são exatamente paralelas). São **2.300 mm de divergência**, somados aos 2.220 mm da parede à
  esteira 1: no DWG a esteira 2 começa 4.520 mm depois de onde está na fábrica.
- O aumento de 5 m da esteira 2 foi desenhado no final da esteira (lado oposto ao início),
  mantendo a defasagem de 5.550 mm. Se o acréscimo for no início, a defasagem muda e
  o código precisa ser ajustado (`E2.ini`).
- **Divergência aberta de 2.220 mm entre o campo e o DWG, no sentido do comprimento.** O trilho de
  abastecimento lateral corre encostado na parede esquerda. Medidas de campo: 850 mm da parede à
  borda externa do trilho e 1.300 mm do trilho até a esteira 1, o que dá 4.250 mm da parede à
  esteira 1 (850 + 2.100 + 1.300). O DWG cota 6.470 mm nesse mesmo trecho. A simulação adota o
  campo. Até a versão anterior a ordem estava invertida no desenho (3.570 mm da parede e 800 mm da
  esteira 1, leitura do DWG numa região fora de esquadro).
- **A sobra no fim da esteira 2 é o número menos confiável da simulação e é justamente o que
  justificaria o aumento de 5 m.** O comprimento do barracão (55.210 mm) foi cotado no DWG a partir
  da parede esquerda. As duas medidas de campo aproximaram o conjunto dessa parede — 2.220 mm na
  esteira 1 e 4.520 mm na esteira 2 — e essa diferença reaparece inteira como folga no outro
  extremo: a sobra no comprimento saiu de 11.915 mm (só DWG) para 16.435 mm no cenário padrão.
  **Nenhum desses 4.520 mm foi medido.** Antes de decidir o aumento da esteira 2, medir em campo a
  distância do fim da esteira 2 até a parede do fundo, ou o comprimento interno do barracão.
- A largura da faixa do trilho de abastecimento (carrinho) está em 2.100 mm nas três posições,
  informada pela Produção, editável na tela. Só o desenho usa esse valor; ele não entra na contagem de pistas
  nem na metragem. A simulação avisa se a largura passar do vão de 2.100 mm entre C2 e C3.
- O vão entre C2 e C3 (2.100 mm, medido no DWG) e a largura da esteira 1 (850 mm; DWG: 840)
  não são editáveis na tela. Ambos afetam só o desenho e as cotas verticais, não a contagem
  de pistas nem a metragem.

## Versão

O número da versão aparece no topo da tela, no título da aba e no cabeçalho de impressão.
Ele vem da constante `VERSAO` no `index.html` e **precisa ser alterado junto com o nome do cache
em `sw.js`** (`trilhos-embalagem-<versão>`) a cada publicação. Serve para conferir, no tablet do
chão de fábrica, se a tela está mostrando a versão publicada ou um cache antigo — se o número não
bater com a última alteração, atualizar a página com Ctrl+F5.

O link de compartilhamento guarda todos os parâmetros no `#` da URL e sobrescreve os padrões ao
abrir, então um link salvo antes de uma correção continua mostrando a geometria antiga na versão
nova. O `#` agora carrega também a chave `app` com a versão que o gravou. Ao abrir um link de
versão diferente, a tela compara os campos de medida (`MEDIDAS` no script) com os padrões atuais e,
se algum divergir, mostra um alerta nomeando o campo, o valor do link e o valor de hoje, com um
botão "Usar as medidas atuais". Link gravado nesta versão não dispara o alerta: ali o que estiver
diferente foi o usuário quem mudou.

## Stack

HTML autocontido, arquivo único, sem etapa de build e sem dependência externa.
PWA com service worker para uso offline. Publicado na Vercel.

Coordenação de PPCP — Patrimar Móveis.
