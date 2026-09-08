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
- Recebe outras máquinas e áreas demarcadas do barracão, desenha na planta e avisa quando invadem o conjunto.
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
| Vão dentro do par | 50 mm | limite informado pela Produção; no DWG são 200 mm |
| Vão entre pares | 500 mm | proposta em estudo |
| Comprimento C1 / C2 / C3 | 7.000 / 4.000 / 3.000 mm | C1 e C3 medidas em campo, ambas confirmando o DWG; C2 ainda vem da Produção, a fonte que errou as outras duas |
| Esteira 1 | 850 × 23.940 mm | largura ajustada para 850 mm (DWG: 840); comprimento medido no DWG |
| Esteira 2 | 850 × 28.975 mm, defasada 5.550 mm | comprimento do DWG: 23.975 mm; defasagem medida em campo (9.800 mm da parede até a esteira 2, menos os 4.250 mm até a esteira 1) — o DWG traz 7.850 mm, guardados em `E2.iniDwg`; aumento de +5.000 mm no final (`E2_AUMENTO`), desenhado hachurado |
| Vão entre as colunas C2 e C3 | 2.100 mm | medido no DWG · fixo no código, não ajustável na tela |
| Trilho de abastecimento (carrinho) | 2.100 mm de largura | faixa acima da C1 e no vão C2–C3, informado pela Produção (no DWG os rails ocupam 1.570 mm no vão e 2.100 mm acima da C1) |
| Trilho de abastecimento lateral | 2.100 mm de largura, encostado na parede (850 mm) e a 1.300 mm da esteira 1 | mesma largura dos outros, informada pela Produção; as duas distâncias foram medidas em campo e somam 4.250 mm da parede à esteira 1, contra 6.470 mm no DWG — **o DWG está desatualizado nessa região e o campo prevalece**; ambas editáveis |
| Posição da esteira 2 | como está hoje (defasada 5.550 mm) | "Alinhada com a esteira 1" ou "Encostada no trilho lateral" deslocam a esteira 2 e a C3 para perto da parede esquerda; não muda a contagem de pistas |
| Posição do conjunto | como no DWG | "Encostado na parede esquerda" zera o afastamento esquerdo e joga a folga para o fim da esteira 2 |
| Barracão — comprimento | 55.210 mm | cotado no DWG, desenho desatualizado. Com 0, o contorno não é desenhado |
| Barracão — largura | 21.850 mm | deduzida das três medidas de campo com o arranjo de hoje (500 + 19.900 + 1.450) e tratada como parede fixa. A hipótese antiga de 24.900 mm, tirada da linha de pilares, foi abandonada |
| Afastamentos das paredes | 850 mm (esquerda, até o trilho lateral) · 500 mm (lado da C1, até o trilho de abastecimento) | medidos em campo. O conjunto está ancorado no lado da C1: é de lá que ele cresce |
| Parede do lado da esteira 2 → esteira 2 | **calculado: 1.450 mm** | Não é digitado: `largura − afastamento da C1 − altura do conjunto`. Alongar um trilho reduz este número, que é o espaço sendo consumido. Negativo = não cabe |

## Recomendação de arranjo

A tela nomeia um dos arranjos como recomendado, acima do comparativo, e marca o botão dele com
um ponto verde na barra de cenários. O critério é
explícito e está impresso junto com a resposta:

> **Mais pistas entre os arranjos que respeitam os limites declarados.** Empate em pistas, vence o
> de menor metragem.

Os limites são os das regras de aviso: `GE_MIN` (500 mm de circulação entre pares), `GI_MIN`
(50 mm dentro do par, informado pela Produção), `PASS_MIN` (800 mm de passagem) e `FOLGA_MIN`
(30 mm da prancha no trilho). Cada arranjo descartado aparece com o motivo. Com os valores atuais:

| Arranjo | Pistas | Metragem | Apoio | Passagem | Situação |
|---|---:|---:|---:|---:|---|
| Versão 1 · par 200 · vão 500 | 90 | 410 m | 1.200 mm | 1.140 mm | apto, 8 pistas a menos |
| Versão 2 · par encostado · vão 500 | 102 | 466 m | 1.000 mm | 940 mm | fora: par de 0 mm |
| Versão 3 · sem par · vão 500 | 77 | 351 m | 1.500 mm | 940 mm | apto, 21 pistas a menos |
| Versão 4 · par 50 · vão 500 | 98 | 444 m | 1.050 mm | 1.690 mm | **recomendado** |
| Passo do DWG · par 200 · vão 400 | 96 | 438 m | 1.200 mm | 740 mm | fora: vão 400 e passagem 740 |

Os botões seguem a sequência das versões, não o ranking — a Versão 4 é a quarta na barra mesmo
sendo a recomendada.

**O apoio da peça larga não é limite, é comparação.** A largura da peça mais larga apoiada em dois
trilhos nunca foi levantada, e os 1.200 mm do arranjo de hoje são só o que ele entrega — não um
requisito. Usá-lo como corte reprovaria arranjos por um número que ninguém confirmou. Ele aparece
no comparativo para a decisão ser tomada com ele à vista.

Quando o arranjo com mais pistas cai por um único limite, a tela diz qual é e quanto custa
mantê-lo. Hoje é a Versão 2: 4 pistas a mais, fora só pelo par de 0 mm.

## Áreas e máquinas

Aba ao lado das cotas. Cadastra outras máquinas e espaços demarcados do barracão com nome,
posição e tamanho; eles aparecem na planta e a simulação avisa quando algum entra na área do
conjunto. O aviso separa dois casos, porque só um deles custa capacidade:

- **Pega trilho** — diz quantos, e que ou a máquina sai ou o conjunto perde essas pistas.
- **Está num vão** — dentro da caixa do conjunto, mas sem atrapalhar trilho nenhum; o aviso pede
  confirmação da folga em vez de tratar como conflito.

Sistema de coordenadas, o mesmo da planta: **X** no sentido das esteiras, zero no início da
esteira 1; **Y** no sentido dos trilhos, zero no trilho de abastecimento acima da C1. Valores
negativos ficam à esquerda e acima.

As áreas viajam no link junto com o resto (`areas=nome~x~y~w~h|...`) e entram na folha de
conferência com uma coluna para validar em campo.

O botão **"Carregar do DWG"** traz cinco áreas extraídas do desenho: a Grampeadora (única com
rótulo no arquivo), três máquinas sem nome e a área demarcada de 5,49 × 11,64 m. Elas podem ser
editadas ou apagadas como qualquer outra.

### Como o DWG foi lido

O arquivo é AC1032 (AutoCAD 2018) e não abre em ferramenta comum. Foi convertido uma vez com o
LibreDWG compilado do fonte, e o DXF resultante está versionado em `ferramentas/`:

```
git clone --depth 1 https://github.com/LibreDWG/libredwg.git
cd libredwg && sh autogen.sh && ./configure --disable-bindings --disable-shared && make -j
./programs/dwg2dxf -o layout-embalagem.dxf "Layout Produção Patrimar - Embalagem - Oderli.dwg"
```

`ferramentas/extrai-maquinas.py` reconstrói os retângulos ligando as LINEs que compartilham ponta,
ancora na esteira 1 — que no desenho aparece deitada, o eixo Y do DWG é o X do app — e descarta o
que o app já modela: trilhos, esteiras, paredes, cotas e hachuras. Duas cotas do próprio desenho
confirmam o resultado: 55,213 m de barracão e 5,49 × 11,64 m da área demarcada.

O desenho também confirma os comprimentos de trilho medidos em campo: as LINEs aparecem em grupos
de 7,0 / 4,0 / 3,0 / 5,0 m com 0,5 m de largura.

**A posição no sentido dos trilhos herda o erro do desenho**, que já se mostrou deslocado nessa
direção. Conferir em campo antes de decidir layout.

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
| Vão dentro do par (`GI_MIN`) | 50 mm | Abaixo do que a Produção aceita fechar o par. |
| Espaço até a parede da esteira 2 | ≥ 0 | O conjunto passa da parede; o aviso diz quantos mm. |
| Distância entre as esteiras (`DIST_E1E2`) | 9.100 mm | `C2 + corredor + C3` saiu da distância real entre as esteiras. O aviso diz quanto a esteira 2 teria que se deslocar, ou para quanto o corredor central fecharia. |
| Passagem para retirar prancha (`PASS_MIN`) | 800 mm | Não passa uma pessoa carregando prancha. |
| Folga da prancha no trilho (`FOLGA_MIN`) | 30 mm | Sem guia lateral, a prancha desalinha e trava. |
| Apoio da peça larga hoje (`APOIO_HOJE`) | 1.200 mm | Referência do arranjo atual para comparar a base da peça apoiada em dois trilhos. Não reprova arranjo: é comparação, não limite. |
| Trilho de abastecimento no vão (`GAP_COL`) | 2.100 mm | A faixa do carrinho não cabe entre C2 e C3. |
| Conjunto dentro do barracão | sobra ≥ 0 no comprimento | O conjunto ultrapassa a parede do fundo; o aviso diz quantos mm faltam. Na largura não há aviso: ela é calculada e fecha sempre. |

Os campos da tela têm mínimo e máximo declarados no HTML (`min`/`max`). Valores
fora da faixa, inclusive os que chegam pelo link compartilhado, são limitados a ela.

## Pendências

- O passo executado no chão de fábrica ainda não foi medido. Todos os cenários de
  referência vêm do desenho e podem estar desatualizados.
- **Nos comprimentos de trilho o DWG estava certo e a informação de campo anterior, errada.**
  A C1 é 7.000 mm e a C3 é 3.000 mm, as duas medidas e as duas iguais ao desenho; o app usava
  6.000 e 4.000 mm, vindos da Produção. Sobra a C2 de 4.000 mm, única cota de trilho ainda não
  medida e vinda dessa mesma fonte — está marcada na folha de conferência.
- O DWG erra na posição das coisas (parede, defasagem das esteiras) e acerta nos comprimentos de
  trilho. Vale como regra ao ler o desenho: desconfiar de onde ele coloca, não de quanto ele mede.
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada.
- **A largura do barracão passou a ser resultado, não entrada.** Os três afastamentos foram medidos
  (850, 500 e 1.450 mm) e, com a altura do conjunto, fecham em 21.850 mm. A hipótese anterior de
  24.900 mm, tirada da linha de pilares do DWG, sobrava 3.050 mm sem explicação e foi abandonada.
  Falta conferir com trena se o barracão tem mesmo essa largura: se tiver menos, o conjunto não
  cabe e algum trilho precisa encurtar; se tiver mais, sobra espaço que a simulação não mostra.
- **`C2 + corredor + C3` é a distância entre a esteira 1 e a esteira 2 — hoje 9.100 mm.** As duas
  esteiras são equipamento existente, então esse número não muda sozinho. Alongar um trilho sem
  encurtar outro obriga a esteira 2 a descer em direção à parede ou o corredor central a fechar; a
  simulação não trava, mas avisa qual é o preço em milímetros de cada saída. A distância de
  9.100 mm veio dos trilhos medidos, não de uma trena entre as esteiras — está na folha de
  conferência, e é uma medida fácil que valida a C2 de quebra.
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
