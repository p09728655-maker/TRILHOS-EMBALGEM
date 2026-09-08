#!/usr/bin/env python3
"""Extrai as outras máquinas e áreas demarcadas do layout, em coordenadas do app.

O DWG original é AC1032 (AutoCAD 2018) e não abre em ferramenta comum. Foi convertido
uma vez com o LibreDWG compilado do fonte:

    git clone --depth 1 https://github.com/LibreDWG/libredwg.git
    cd libredwg && sh autogen.sh && ./configure --disable-bindings --disable-shared && make -j
    ./programs/dwg2dxf -o layout-embalagem.dxf "Layout Produção Patrimar - Embalagem - Oderli.dwg"

O DXF resultante está versionado ao lado deste script, então rodar isto basta:

    pip install ezdxf && python3 extrai-maquinas.py layout-embalagem.dxf

Como funciona: reconstrói retângulos ligando as LINEs que compartilham ponta, ancora na
esteira 1 (que no desenho aparece deitada — o eixo Y do DWG é o X do app) e descarta o que
já é modelado pelo app: trilhos, esteiras, paredes, cotas e hachuras.

ATENÇÃO: a posição no sentido dos trilhos herda o erro do desenho, que já se mostrou
deslocado nessa direção em relação ao campo. Conferir antes de decidir layout.
"""
import sys, math, collections, ezdxf

CENTRO = (642495.8, 7675208.2)   # perto da Grampeadora, em UTM; o desenho é georreferenciado
RAIO   = 140.0                   # metros
SNAP   = 0.02                    # 2 cm, para juntar pontas que o CAD deixou com folga
E1_CENTRO_APP = 9525             # centro da esteira 1 no eixo Y do app: 2.100 + 7.000 + 425


def caixas_do_dxf(caminho):
    """Agrupa as LINEs em componentes conexas e devolve a caixa de cada uma."""
    msp = ezdxf.readfile(caminho).modelspace()
    cx, cy = CENTRO
    segs, pontos = [], collections.defaultdict(set)
    for e in msp.query("LINE"):
        a, b = e.dxf.start, e.dxf.end
        if max(abs(a.x - cx), abs(b.x - cx)) > RAIO or max(abs(a.y - cy), abs(b.y - cy)) > RAIO:
            continue
        A, B = (a.x - cx, a.y - cy), (b.x - cx, b.y - cy)
        if math.dist(A, B) < 1e-6:
            continue
        i = len(segs)
        segs.append((A, B, e.dxf.layer))
        for P in (A, B):
            pontos[(round(P[0] / SNAP), round(P[1] / SNAP))].add(i)

    pai = list(range(len(segs)))

    def raiz(x):
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    for ids in pontos.values():
        ids = list(ids)
        for j in ids[1:]:
            ra, rb = raiz(ids[0]), raiz(j)
            if ra != rb:
                pai[ra] = rb

    grupos = collections.defaultdict(list)
    for i in range(len(segs)):
        grupos[raiz(i)].append(i)

    saida = []
    for ids in grupos.values():
        pts = [p for i in ids for p in (segs[i][0], segs[i][1])]
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        saida.append(dict(x0=min(xs), y0=min(ys), x1=max(xs), y1=max(ys),
                          w=max(xs) - min(xs), h=max(ys) - min(ys), lay=segs[ids[0]][2]))
    return saida, msp


def main(caminho):
    caixas, msp = caixas_do_dxf(caminho)
    e1 = min((c for c in caixas if 23.5 <= c["h"] <= 24.3 and c["w"] < 3 and c["lay"] == "0"),
             key=lambda c: c["x0"])
    dx, dy = (e1["x0"] + e1["x1"]) / 2, e1["y0"]

    def para_app(x, y):
        return round((y - dy) * 1000), round((x - dx) * 1000 + E1_CENTRO_APP)

    cx, cy = CENTRO
    textos = []
    for e in msp.query("TEXT MTEXT"):
        t = (e.plain_text() if e.dxftype() == "MTEXT" else e.dxf.text).strip()
        p = e.dxf.insert
        if t and abs(p.x - cx) <= RAIO and abs(p.y - cy) <= RAIO:
            textos.append((p.x - cx, p.y - cy, t))

    alvos = [c for c in caixas if c["lay"] == "0"
             and 0.8 <= c["w"] <= 13 and 0.8 <= c["h"] <= 13 and c["w"] * c["h"] >= 1.5]

    print("Máquinas e áreas do DWG, em coordenadas do app (mm):\n")
    for c in sorted(alvos, key=lambda c: para_app(c["x0"], c["y0"])[0]):
        x, y = para_app(c["x0"], c["y0"])
        nome = next((t for tx, ty, t in textos
                     if c["x0"] - .6 <= tx <= c["x1"] + .6 and c["y0"] - .6 <= ty <= c["y1"] + .6), "")
        print(f'  {{ nome:"{nome or "sem nome no DWG"}", x:{x}, y:{y}, '
              f'w:{round(c["h"] * 1000)}, h:{round(c["w"] * 1000)} }},')


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "layout-embalagem.dxf")
