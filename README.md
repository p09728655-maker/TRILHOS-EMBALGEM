# Dimensionamento dos trilhos — Embalagem

Ferramenta de simulação da ocupação dos trilhos da Embalagem da Patrimar Móveis,
dentro do alcance das duas esteiras.

## O que faz

- Calcula quantas pistas cabem em cada esteira conforme o arranjo dos trilhos.
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
| Esteira 2 | 850 × 28.975 mm, defasada 7.850 mm | DWG: 23.975 mm; defasagem medida no eixo da esteira 1; aumento de +5.000 mm no final (`E2_AUMENTO`), desenhado hachurado |
| Vão entre as colunas C2 e C3 | 2.100 mm | medido no DWG · fixo no código, não ajustável na tela |
| Trilho de abastecimento (carrinho) | 2.100 mm de largura | faixa acima da C1 e no vão C2–C3, informado pela Produção (no DWG os rails ocupam 1.570 mm no vão e 2.100 mm acima da C1) |
| Trilho de abastecimento lateral | 2.100 mm de largura, a 800 mm da esteira 1 | mesma largura dos outros, informada pela Produção; distância lida do DWG; ambos editáveis |
| Posição da esteira 2 | como no DWG (defasada 7.850 mm) | "Alinhada com a esteira 1" ou "Encostada no trilho lateral" deslocam a esteira 2 e a C3 para perto da parede esquerda; não muda a contagem de pistas |
| Posição do conjunto | como no DWG | "Encostado na parede esquerda" zera o afastamento esquerdo e joga a folga para o fim da esteira 2 |
| Barracão | 55.210 × 24.900 mm · parede esquerda a 3.570 mm da borda externa do trilho lateral (6.470 mm até a esteira 1, cotado no DWG) e trilho de abastecimento a 700 mm da parede do lado da C1 | comprimento e afastamento esquerdo cotados no DWG; largura e afastamento superior são hipótese (linha de pilares a 11,0 m da esteira 1). Com afastamento 0 a parede encosta no conjunto |

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
| Conjunto dentro do barracão | sobra ≥ 0 nos dois sentidos | O conjunto ultrapassa a parede; o aviso diz quantos mm faltam. |

Os campos da tela têm mínimo e máximo declarados no HTML (`min`/`max`). Valores
fora da faixa, inclusive os que chegam pelo link compartilhado, são limitados a ela.

## Pendências

- O passo executado no chão de fábrica ainda não foi medido. Todos os cenários de
  referência vêm do desenho e podem estar desatualizados.
- No DWG a coluna C1 aparece com trilhos de 7.000 mm e a C3 com 3.000 mm, divergindo
  da informação de campo (6.000 e 4.000 mm).
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada.
- Barracão: o DWG cota 55.210 mm no sentido das esteiras, a partir de 6.470 mm antes do início
  da esteira 1, e a parede do lado da esteira 2 está a 1.380 mm dela. A cota de 23.570 mm do
  DWG não fecha com o trilho de abastecimento acima da C1 (rails a 10,3 m da esteira 1), então
  a largura de 24.900 mm e o afastamento de 700 mm foram tomados na linha de pilares a 11,0 m
  da esteira 1 e precisam ser confirmados.
- A defasagem da esteira 2 (7.850 mm) foi medida no eixo da esteira 1. A diferença bruta de
  coordenadas no DWG é 8.170 mm porque o conjunto está girado 1,5° e as esteiras não são
  exatamente paralelas entre si.
- O aumento de 5 m da esteira 2 foi desenhado no final da esteira (lado oposto ao início),
  mantendo a defasagem de 7.850 mm. Se o acréscimo for no início, a defasagem muda e
  o código precisa ser ajustado (`E2.ini`).
- O trilho de abastecimento lateral começa 800 mm antes da esteira 1 (lido do DWG, precisão de
  uns 300 mm, porque as linhas dessa região estão fora de esquadro).
- A largura da faixa do trilho de abastecimento (carrinho) está em 2.100 mm nas três posições,
  informada pela Produção, editável na tela. Só o desenho usa esse valor; ele não entra na contagem de pistas
  nem na metragem. A simulação avisa se a largura passar do vão de 2.100 mm entre C2 e C3.
- O vão entre C2 e C3 (2.100 mm, medido no DWG) e a largura da esteira 1 (850 mm; DWG: 840)
  não são editáveis na tela. Ambos afetam só o desenho e as cotas verticais, não a contagem
  de pistas nem a metragem.

## Stack

HTML autocontido, arquivo único, sem etapa de build e sem dependência externa.
PWA com service worker para uso offline. Publicado na Vercel.

Coordenação de PPCP — Patrimar Móveis.
