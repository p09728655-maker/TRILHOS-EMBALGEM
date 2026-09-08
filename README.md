# Dimensionamento dos trilhos — Embalagem

Ferramenta de simulação da ocupação dos trilhos da Embalagem da Patrimar Móveis,
dentro do alcance das duas esteiras.

## O que faz

- Calcula quantas pistas cabem em cada esteira conforme o arranjo dos trilhos.
- Desenha a planta em escala das três colunas (C1, C2 e C3) e das duas esteiras.
- Desenha o trilho de abastecimento com carrinho: uma faixa acima da C1 e outra no vão entre C2 e C3.
- Destaca o aumento de 5 m da esteira 2 na planta e mostra quantas pistas ele acrescenta.
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
| Esteira 2 | 850 × 28.975 mm, defasada 8.170 mm | DWG: 23.975 mm; aumento de +5.000 mm no final (`E2_AUMENTO`), desenhado hachurado |
| Vão entre as colunas C2 e C3 | 2.000 mm | ajustado para 2.000 mm (DWG: 1.590) · fixo no código, não ajustável na tela |
| Trilho de abastecimento (carrinho) | 1.000 mm de largura | faixa acima da C1 e centrada no vão C2–C3 · largura a confirmar com a Produção |

## Regras de aviso

A simulação avisa quando o cenário fere uma destas regras. Os limites ficam
como constantes nomeadas no início do script e valem para todos os cenários.

| Regra | Limite | O que acontece abaixo dele |
|---|---:|---|
| Vão entre pares (`GE_MIN`) | 500 mm | Não há circulação entre as vias. |
| Passagem para retirar prancha (`PASS_MIN`) | 800 mm | Não passa uma pessoa carregando prancha. |
| Folga da prancha no trilho (`FOLGA_MIN`) | 30 mm | Sem guia lateral, a prancha desalinha e trava. |
| Apoio da peça larga hoje (`APOIO_HOJE`) | 1.200 mm | Referência do arranjo atual para comparar a base da peça apoiada em dois trilhos. |
| Trilho de abastecimento no vão (`GAP_COL`) | 2.000 mm | A faixa do carrinho não cabe entre C2 e C3. |

Os campos da tela têm mínimo e máximo declarados no HTML (`min`/`max`). Valores
fora da faixa, inclusive os que chegam pelo link compartilhado, são limitados a ela.

## Pendências

- O passo executado no chão de fábrica ainda não foi medido. Todos os cenários de
  referência vêm do desenho e podem estar desatualizados.
- No DWG a coluna C1 aparece com trilhos de 7.000 mm e a C3 com 3.000 mm, divergindo
  da informação de campo (6.000 e 4.000 mm).
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada.
- O aumento de 5 m da esteira 2 foi desenhado no final da esteira (lado oposto ao início),
  mantendo a defasagem de 8.170 mm do DWG. Se o acréscimo for no início, a defasagem muda e
  o código precisa ser ajustado (`E2.ini`).
- A largura da faixa do trilho de abastecimento (carrinho) está em 1.000 mm por hipótese, editável na
  tela. Só o desenho usa esse valor; ele não entra na contagem de pistas nem na metragem. A simulação
  avisa se a largura passar do vão de 2.000 mm entre C2 e C3.
- O vão entre C2 e C3 (2.000 mm) e a largura da esteira 1 (850 mm) foram ajustados em
  relação ao DWG (1.590 e 840 mm) e não são editáveis na tela. Ambos afetam só o desenho
  e as cotas verticais, não a contagem de pistas nem a metragem.

## Stack

HTML autocontido, arquivo único, sem etapa de build e sem dependência externa.
PWA com service worker para uso offline. Publicado na Vercel.

Coordenação de PPCP — Patrimar Móveis.
