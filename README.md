# Dimensionamento dos trilhos — Embalagem

Ferramenta de simulação da ocupação dos trilhos da Embalagem da Patrimar Móveis,
dentro do alcance das duas esteiras.

> **Origem das medidas.** O DWG foi a referência inicial, mas **está desatualizado** na região da
> parede esquerda. Onde há medição de campo, ela prevalece sobre o desenho: distâncias da parede ao
> trilho lateral e à esteira 1, e a defasagem entre as esteiras. O que ainda vem só do DWG —
> comprimento do barracão, comprimentos das esteiras, passo dos trilhos — continua sujeito ao mesmo
> erro e está listado em Pendências. **O comprimento do barracão saiu dessa lista: foi conferido em
> campo e confirma o desenho.** Restam os comprimentos das esteiras.

> **Isto é projeto, não levantamento.** Os trilhos montados hoje na Embalagem **não seguem passo
> regular e não têm medida definida** — não estão encostados nem espaçados por uma regra. Não existe,
> portanto, "o arranjo de hoje" a medir ou a bater com a simulação. A planta que sai daqui é o
> **layout a executar**; os arranjos são comparados entre si e contra o DWG, nunca contra o que está
> montado. As medidas de campo que o app usa são das coisas fixas — paredes, esteiras e comprimentos
> de trilho —, não do espaçamento entre eles.

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
- Diz, em números, quantos metros e quantas pistas juntar os trilhos em par rende — e o que custa.
- Gera as cotas acumuladas em CSV e a planta em SVG.
- Imprime em A4 paisagem com cabeçalho de parâmetros, e tem uma impressão focada só no desenho,
  que aceita papel maior (A3 rende ~44% de desenho).

## Densidade da tela

A tela mostra o que decide e guarda a justificativa atrás de um clique. O que fica sempre visível:
planta, faixa de indicadores, avisos, arranjo recomendado com seus números e o limite que está
custando pistas, comparativo e cotas.

O que só aparece quando pedido:

| Camada | Onde | Como abre |
|---|---|---|
| Texto de apoio dos campos | barra lateral | aparece sozinho no campo em foco; o botão **Explicações** fixa todos e a escolha fica gravada no navegador |
| Critério da recomendação e arranjos descartados | bloco Comparativo | detalhe "Critério e arranjos descartados" |
| Procedência das áreas | barra lateral | detalhe "De onde vêm estas áreas" |
| Geometria e medidas | barra lateral | detalhe "Geometria e medidas" |
| Origem das medidas e ressalvas do DWG | rodapé | rodapé recolhido, com a ressalva que importa na linha visível |
| Cotas em CSV, planta em SVG, impressão só da planta e folha de conferência | topo | menu **Mais** |

**Na impressão nada fica escondido**: as camadas recolhidas abrem sozinhas antes de imprimir e
voltam a fechar depois.

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
| Trilho de abastecimento lateral | 2.100 mm de largura, encostado na parede (850 mm) e a 1.300 mm da esteira 1 | **cadeia conferida em campo: 850 + 2.100 + 1.300 = 4.250 mm da parede à esteira 1**, contra 6.470 mm no DWG — o desenho está errado nessa região e o campo prevalece. A largura de 2.100 mm, antes informada pela Produção, foi conferida dentro dessa cadeia; as três medidas seguem editáveis |
| Posição da esteira 2 | como está hoje (defasada 5.550 mm) | "Alinhada com a esteira 1" ou "Encostada no trilho lateral" deslocam a esteira 2 e a C3 para perto da parede esquerda; não muda a contagem de pistas |
| Posição do conjunto | como no DWG | "Encostado na parede esquerda" zera o afastamento esquerdo e joga a folga para o fim da esteira 2 |
| Barracão — comprimento | 55.210 mm | **conferido em campo, confirma a cota do DWG**. Com 0, o contorno não é desenhado |
| Barracão — largura | 21.850 mm | deduzida das três medidas de campo com os comprimentos de trilho atuais (500 + 19.900 + 1.450) e tratada como parede fixa. A hipótese antiga de 24.900 mm, tirada da linha de pilares, foi abandonada |
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

| Arranjo | Pistas | Metragem | Passagem | Situação |
|---|---:|---:|---:|---|
| Versão 1 · par 200 · vão 500 | 90 | 410 m | 1.140 mm | apto, 8 pistas a menos |
| Versão 2 · par encostado · vão 500 | 102 | 466 m | 940 mm | fora: par de 0 mm |
| Versão 3 · sem par · vão 500 | 77 | 351 m | 940 mm | apto, 21 pistas a menos |
| Versão 4 · par 50 · vão 500 | 98 | 444 m | 1.690 mm | **recomendado** |
| Passo do DWG · par 200 · vão 400 | 96 | 438 m | 740 mm | fora: vão 400 e passagem 740 |

Os botões seguem a sequência das versões, não o ranking — a Versão 4 é a quarta na barra mesmo
sendo a recomendada.

**A base da peça larga apoiada em dois trilhos saiu da tela.** O campo informa que praticamente
toda peça entra num trilho só de 500 mm, então esse número não decidia nada e ocupava um indicador
fixo na faixa, uma linha em cada arranjo do comparativo e um pedaço do aviso do par fechado. Nunca
foi limite — a largura da peça mais larga também nunca foi levantada —, e agora nem comparação é.
O valor continua calculado e sai no **cabeçalho da impressão completa** e na **folha de conferência**,
e o critério da recomendação registra por que ele ficou de fora.

> **Ponto em aberto para a Produção.** O único efeito declarado do vão dentro do par era justamente
> a base da peça larga. Se ela não pesa, o limite de 50 mm fica sem justificativa escrita — e é ele,
> sozinho, que separa a Versão 4 da Versão 2 (**+4 pistas e +22 m**). Vale confirmar com a Produção
> se os 50 mm existem por outro motivo (montagem, limpeza, fixação, pé entre trilhos) antes de
> tratar a Versão 2 como disponível.

Quando o arranjo com mais pistas cai por um único limite, a tela diz qual é e quanto custa
mantê-lo, **em pistas e em metros**. Hoje é a Versão 2: 4 pistas e 22 m a mais, fora só pelo
par de 0 mm.

## Quanto juntar os trilhos rende

Juntar os trilhos é fechar o vão **dentro do par**: dois trilhos encostados ocupam menos banco que
dois soltos, e a esteira que sobra vira mais uma via. O comparativo sempre trouxe a metragem de
cada arranjo, mas a subtração ficava por conta de quem lia — e era ela que respondia à pergunta.
Agora o ganho sai pronto, numa linha fixa dentro do bloco Comparativo, logo abaixo da recomendação.

Só o vão dentro do par muda: largura do trilho, vão entre pares, passagem e os comprimentos de C1,
C2 e C3 vêm da tela. Misturar dois efeitos na mesma conta invalidaria o número.

A referência muda com o arranjo que estiver na tela, e o texto sempre a nomeia:

| Arranjo na tela | Número grande | Contra o quê |
|---|---|---|
| Par fechado ou aberto (vão ≠ 200 mm) | o que fechar o par rende sobre o passo do DWG | par de 200 mm, o passo que o DWG desenha |
| Par de 200 mm | o que o par rende sobre os trilhos soltos | mesmos trilhos, sem par |
| Sem par | o que juntar em par de 50 mm renderia | os trilhos soltos da própria tela |

Com os valores padrão, fechar o par de 200 para 0 mm rende **+56 m e +12 pistas** (466 m no lugar
de 410 m); contra trilhos soltos, o par rende **+115 m e +25 pistas**. Até os 50 mm que a Produção
aceita são **+34 m e +8 pistas**.

**O ganho vem com conta a pagar, e ela aparece na mesma linha:** metro de trilho a mais é
capacidade a mais, mas também trilho a instalar — não é economia, é investimento em ocupação.
A base da peça larga já esteve aqui como o outro lado da troca e saiu: com praticamente toda peça
entrando num trilho só, ela não é preço de nada.

## Áreas e máquinas

Seção da barra lateral, ao lado da planta — é entrada, e entrada fica onde estão os outros
parâmetros. Cada máquina é um cartão com nome, X, Y, largura e altura; o cartão em foco tem a sua
máquina destacada com traço cheio no desenho, e quem invade o conjunto ganha barra âmbar à
esquerda. Digitar a medida e ver a máquina andar acontece na mesma tela, sem rolagem. Eles
aparecem na planta e a simulação avisa quando algum entra na área do conjunto. O aviso separa dois casos, porque só um deles custa capacidade:

- **Pega trilho** — diz quantos, e que ou a máquina sai ou o conjunto perde essas pistas.
- **Está num vão** — dentro da caixa do conjunto, mas sem atrapalhar trilho nenhum; o aviso pede
  confirmação da folga em vez de tratar como conflito.

Sistema de coordenadas, o mesmo da planta: **X** no sentido das esteiras, zero no início da
esteira 1; **Y** no sentido dos trilhos, zero no trilho de abastecimento acima da C1. Valores
negativos ficam à esquerda e acima.

As áreas viajam no link junto com o resto (`areas=nome~x~y~w~h|...`) e entram na folha de
conferência com uma coluna para validar em campo.

O botão **"Do DWG"** traz cinco áreas extraídas do desenho: a Grampeadora (única com
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

## Impressão focada no desenho

O botão **"Imprimir só a planta"**, no menu **Mais**, manda a planta sozinha para o papel: saem de
cena a faixa de indicadores, os avisos de regra, o comparativo e as cotas, e o desenho ocupa a
largura inteira da folha — **20% maior em escala** (43% em área) que na impressão completa em A4.
É a folha de levar ao chão de fábrica ou à reunião de layout.

O que fica, porque planta sem isso não se confere:

- o cabeçalho com o arranjo, a data e a versão do app;
- os parâmetros que o desenho mostra (trilho, vãos, passagem, comprimentos de C1/C2/C3,
  abastecimento, esteira 2, barracão e pistas por lado). Os que a planta não desenha — prancha,
  folga, apoio em dois trilhos e distância entre as esteiras — só saem na impressão completa;
- o **alerta de link antigo**, quando aparece. Os avisos de regra saem, mas esse fica: ele diz que
  a geometria na tela está desatualizada, e uma planta impressa sem ele vale como certa sendo
  errada;
- a legenda das cores;
- a ressalva do DWG, em uma linha no pé.

### O tamanho é limitado pela largura do papel, não pela altura

A planta tem cerca de **2,1:1** e a folha A4 paisagem, **1,45:1**. Quem limita o desenho é a
**largura**: ele já sai de ponta a ponta e sobra altura que a proporção não consegue usar. Esconder
os avisos deixa a folha limpa — **não aumenta o desenho**, e o mesmo vale para encolher o cabeçalho.
Girar para retrato também não adianta: o lado maior do A4 é o mesmo nas duas orientações.

Por isso a `@page` desta impressão fixa **só a orientação**, sem travar o tamanho do papel. Escolher
**A3** no diálogo rende um desenho **~44% maior em escala** (mais que o dobro em área), medido no PDF
gerado. A altura do palco acompanha a folha (`100vh`) em vez de ser fixa em milímetros — numa folha
maior ela precisa crescer junto, senão o desenho volta a ser limitado pela altura e o A3 não paga.

A margem continua em 8 mm, igual à das outras folhas: fechar para 5 mm renderia 2,3% e arrisca corte
de borda em impressora com margem física maior, já que o desenho vai de ponta a ponta.

A impressão completa (botão **Imprimir**) não mudou: A4 paisagem, planta na primeira página,
comparativo e cotas depois.

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
| Trilho de abastecimento no vão (`GAP_COL`) | 2.100 mm | A faixa do carrinho não cabe entre C2 e C3. |
| Conjunto dentro do barracão | sobra ≥ 0 no comprimento | O conjunto ultrapassa a parede do fundo; o aviso diz quantos mm faltam. Na largura não há aviso: ela é calculada e fecha sempre. |

Os campos da tela têm mínimo e máximo declarados no HTML (`min`/`max`). Valores
fora da faixa, inclusive os que chegam pelo link compartilhado, são limitados a ela.

## Pendências

- ~~O passo executado no chão de fábrica ainda não foi medido.~~ **Resolvida, e não por medição:**
  os trilhos montados hoje não têm medida definida e não seguem passo regular, então não há passo de
  campo a levantar. A comparação entre os arranjos é entre projetos, com o DWG como referência, e a
  folha de conferência deixou de pedir essa medida. Os cenários de referência continuam vindo do
  desenho — o que muda é que isso deixou de ser uma lacuna e passou a ser a única base possível.
- **Nos comprimentos de trilho o DWG estava certo e a informação de campo anterior, errada.**
  A C1 é 7.000 mm e a C3 é 3.000 mm, as duas medidas e as duas iguais ao desenho; o app usava
  6.000 e 4.000 mm, vindos da Produção. Sobra a C2 de 4.000 mm, única cota de trilho ainda não
  medida e vinda dessa mesma fonte — está marcada na folha de conferência.
- O DWG erra na posição das coisas (parede, defasagem das esteiras) e acerta nos comprimentos de
  trilho. Vale como regra ao ler o desenho: desconfiar de onde ele coloca, não de quanto ele mede.
- A largura da peça mais larga apoiada nos dois trilhos ainda não foi levantada, mas **deixou de
  pesar na escolha do arranjo**: o campo informa que praticamente toda peça entra num trilho só de
  500 mm. Continua na folha de conferência, sem destaque, para confirmar com trena antes de fechar
  o par. Com isso, **o limite de 50 mm dentro do par ficou sem justificativa escrita** — era a base
  da peça larga — e é ele que separa a Versão 4 da Versão 2. Confirmar com a Produção o motivo real.
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
- **A cadeia da parede até a esteira 1 está CONFERIDA em campo: 850 + 2.100 + 1.300 = 4.250 mm.**
  O trilho de abastecimento lateral corre encostado na parede esquerda. Os 2.100 mm da largura desse
  trilho eram informação da Produção e passaram a ser **medida de campo**, conferidos dentro da
  cadeia. O DWG cota 6.470 mm nesse mesmo trecho: a divergência de 2.220 mm **deixa de ser dúvida
  sobre qual lado está certo** — o campo está certo e o desenho, errado nessa região. Até uma versão
  anterior a ordem estava invertida no desenho (3.570 mm da parede e 800 mm da esteira 1, leitura do
  DWG numa região fora de esquadro).
  **O que isso não resolve:** o comprimento do barracão (55.210 mm) continua saindo do mesmo DWG e
  contado a partir dessa mesma parede, então a sobra no fim da esteira 2 segue herdando o erro — ver
  o item abaixo. Confirmar a cadeia da parede não confirma a outra ponta.
- ~~A sobra no fim da esteira 2 é o número menos confiável da simulação.~~ **Resolvida.** Era o
  número mais frágil porque as medidas de campo aproximaram o conjunto da parede esquerda e essa
  diferença reaparecia inteira como folga no outro extremo, com o comprimento do barracão vindo do
  mesmo desenho que errava a primeira ponta. **As duas pontas foram conferidas em campo:** a cadeia
  da parede esquerda (850 + 2.100 + 1.300 = 4.250 mm) e o comprimento interno do barracão
  (55.210 mm, que confirma a cota do DWG). A sobra de **16.435 mm** no cenário padrão passa a ser
  número derivado de medida, não de hipótese, e o aviso de "não cabe no comprimento" passa a ser
  confiável.
  **O que ela ainda herda do desenho:** o comprimento da esteira 2. É esse termo que governa a
  conta — `5.550 de defasagem + 28.975 de esteira` chega mais longe que a esteira 1 —, então medir a
  esteira 2 fecha o último furo da sobra. Está destacado na folha de conferência.
- **Os comprimentos das esteiras são a última medida de peso que vem só do DWG.** A esteira 1
  (23.940 mm) define quantas pistas cabem nela; a esteira 2 (23.975 mm antes do aumento) define as
  dela e ainda governa a sobra do fundo. As duas passaram a sair destacadas na folha de conferência.
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
