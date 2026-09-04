# Dimensionamento dos trilhos — Embalagem

Ferramenta de simulação da ocupação dos trilhos da Embalagem da Patrimar Móveis,
dentro do alcance das duas esteiras.

## O que faz

- Calcula quantas pistas cabem em cada esteira conforme o arranjo dos trilhos.
- Desenha a planta em escala das três colunas (C1, C2 e C3) e das duas esteiras.
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
| Esteira 1 | 840 × 23.940 mm | medido no DWG |
| Esteira 2 | 850 × 23.975 mm, defasada 8.170 mm | medido no DWG |
| Corredor entre C2 e C3 (circulação de carrinho) | 1.590 mm | DWG · confirmado pela Produção · fixo no código |

## Regras de aviso

A simulação avisa quando o cenário fere uma destas regras. Os limites ficam
como constantes nomeadas no início do script e valem para todos os cenários.

| Regra | Limite | O que acontece abaixo dele |
|---|---:|---|
| Vão entre pares (`GE_MIN`) | 500 mm | Não há circulação entre as vias. |
| Passagem para retirar prancha (`PASS_MIN`) | 800 mm | Não passa uma pessoa carregando prancha. |
| Folga da prancha no trilho (`FOLGA_MIN`) | 30 mm | Sem guia lateral, a prancha desalinha e trava. |
| Apoio da peça larga hoje (`APOIO_HOJE`) | 1.200 mm | Referência do arranjo atual para comparar a base da peça apoiada em dois trilhos. |

Os campos da tela têm mínimo e máximo declarados no HTML (`min`/`max`). Valores
fora da faixa, inclusive os que chegam pelo link compartilhado, são limitados a ela.

## Pendências

- O passo executado no chão de fábrica ainda não foi medido. Todos os cenários de
  referência vêm do desenho e podem estar desatualizados.
- No DWG a coluna C1 aparece com trilhos de 7.000 mm e a C3 com 3.000 mm, divergindo
  da informação de campo (6.000 e 4.000 mm).
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada.
- O corredor de 1.590 mm entre C2 e C3 é a circulação do carrinho e não pode ser
  reduzido. Com C2 = 4.000 e C3 = 4.000 (Produção) a distância entre as esteiras
  seria 9.590 mm; com C3 = 3.000 (DWG) é 8.590 mm. As esteiras são fixas, então
  uma das duas informações está errada: medir a distância entre as esteiras
  (borda a borda) para saber qual — se for 8.590 e a C3 tiver 4.000, o corredor
  real é de 590 mm e o carrinho não passa.

## Stack

HTML autocontido, arquivo único, sem etapa de build e sem dependência externa.
PWA com service worker para uso offline. Publicado na Vercel.

Coordenação de PPCP — Patrimar Móveis.
