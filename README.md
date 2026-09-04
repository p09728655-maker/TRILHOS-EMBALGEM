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

## Pendências

- O passo executado no chão de fábrica ainda não foi medido. Todos os cenários de
  referência vêm do desenho e podem estar desatualizados.
- No DWG a coluna C1 aparece com trilhos de 7.000 mm e a C3 com 3.000 mm, divergindo
  da informação de campo (6.000 e 4.000 mm).
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada.

## Stack

HTML autocontido, arquivo único, sem etapa de build e sem dependência externa.
PWA com service worker para uso offline. Publicado na Vercel.

Coordenação de PPCP — Patrimar Móveis.
