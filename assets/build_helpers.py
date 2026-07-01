#!/usr/bin/env python3
"""build_helpers.py — utilidades para produzir/manter o HTML do curso com segurança.

Nasceu das lições da produção do curso "Clone Digital" (ver PRD §7/§8):
edições estruturais em HTML grande (renumerar seções, reconstruir TOC/nav,
corrigir acentos) precisam ser feitas por script determinístico, nunca por
regex que toque em nomes de classe/atributo.

Uso:
    python build_helpers.py --check curso.html
        Roda sanity checks (contagens, balanço de tags, âncoras, imagens em disco).

    python build_helpers.py --assets curso.html
        Confere que toda imagem local referenciada (src / url()) existe em disco.
        Rode ANTES de publicar e depois de montar a pasta de deploy (dist/).

    python build_helpers.py --renumber curso.html
        Renumera todos os `.section-label` por ordem do DOM (01, 02, ...) e
        imprime o mapa old->new (âncoras não mudam; refs cruzadas você atualiza).

    python build_helpers.py --anchors curso.html
        Lista âncoras (id de <section>) e verifica que toda href #... existe.

Correção de acentos em massa: use `fix_accents_in_text()` importando este módulo,
passando um dicionário {errado: certo}. Ele SÓ altera texto entre tags.
"""
import os
import re
import sys


def split_tags(html):
    """Divide em pedaços alternando (texto, tag, texto, tag...) preservando tudo.
    Índices ímpares são tags <...>; pares são texto entre tags."""
    return re.split(r'(<[^>]+>)', html)


def fix_accents_in_text(html, replacements):
    """Aplica {errado: certo} SOMENTE no texto entre tags (nunca em atributos/classes)."""
    parts = split_tags(html)
    for i in range(0, len(parts), 2):  # só os pedaços de texto
        for wrong, right in replacements.items():
            parts[i] = parts[i].replace(wrong, right)
    return ''.join(parts)


def renumber_section_labels(html):
    """Reescreve o conteúdo de cada <div class="section-label">...</div> como
    'Seção NN' na ordem em que aparecem no DOM. Retorna (novo_html, n)."""
    counter = {'n': 0}
    # detecta o prefixo usado (Seção/Section/Seccao...) a partir do primeiro label
    m = re.search(r'class="section-label"[^>]*>\s*([A-Za-zÀ-ÿ]+)', html)
    prefix = m.group(1) if m else 'Seção'

    def repl(match):
        counter['n'] += 1
        return f'{match.group(1)}{prefix} {counter["n"]:02d}{match.group(3)}'

    pattern = re.compile(r'(<div class="section-label"[^>]*>)(.*?)(</div>)', re.S)
    new_html = pattern.sub(repl, html)
    return new_html, counter['n']


def referenced_assets(html):
    """Retorna caminhos de imagens locais citados em src="..." e em url(...) do CSS/estilo."""
    refs = set(re.findall(r'src="([^"]+\.(?:jpe?g|png|webp|avif|gif|svg))"', html, re.I))
    refs |= set(re.findall(r"url\(['\"]?([^)'\"]+\.(?:jpe?g|png|webp|avif|gif|svg))['\"]?\)", html, re.I))
    # ignora http(s)/data:
    return {r for r in refs if not r.startswith(('http://', 'https://', 'data:', '//'))}


def assets_check(html, base_dir):
    """Confere que toda imagem local referenciada existe em disco (relativo ao HTML).
    Pega a classe de bug que quebrou o header no deploy: referência a arquivo ausente."""
    problems = []
    for rel in sorted(referenced_assets(html)):
        if not os.path.exists(os.path.join(base_dir, rel)):
            problems.append(f"imagem referenciada não existe em disco: {rel}")
    return problems


def check(html, base_dir=None):
    problems = []
    n_sections = len(re.findall(r'<section\b', html))
    n_close = len(re.findall(r'</section>', html))
    n_labels = len(re.findall(r'class="section-label"', html))
    n_toc = len(re.findall(r'class="toc-item"', html))
    n_div_open = len(re.findall(r'<div\b', html))
    n_div_close = len(re.findall(r'</div>', html))

    print(f"<section> abre: {n_sections}  fecha: {n_close}")
    print(f".section-label: {n_labels}")
    print(f".toc-item: {n_toc}")
    print(f"<div> abre: {n_div_open}  fecha: {n_div_close}")

    if n_sections != n_close:
        problems.append("section abre != fecha")
    if not (n_sections == n_labels == n_toc):
        problems.append(f"contagens divergem: section={n_sections} label={n_labels} toc={n_toc}")
    if n_div_open != n_div_close:
        problems.append(f"div desbalanceado: {n_div_open} != {n_div_close}")

    # âncoras
    ids = re.findall(r'<section id="([^"]+)"', html)
    dup = {x for x in ids if ids.count(x) > 1}
    if dup:
        problems.append(f"âncoras duplicadas: {dup}")
    hrefs = set(re.findall(r'href="#([^"]+)"', html))
    missing = hrefs - set(ids)
    if missing:
        problems.append(f"href sem <section id> correspondente: {missing}")

    # imagens referenciadas existem?
    if base_dir is not None:
        asset_problems = assets_check(html, base_dir)
        n_refs = len(referenced_assets(html))
        print(f"imagens locais referenciadas: {n_refs}")
        problems += asset_problems

    if problems:
        print("\nPROBLEMAS:")
        for p in problems:
            print("  -", p)
        return 1
    print("\nOK — todos os checks passaram.")
    return 0


def anchors(html):
    ids = re.findall(r'<section id="([^"]+)"', html)
    print("Âncoras (ordem do DOM):")
    for i, a in enumerate(ids, 1):
        print(f"  {i:02d}  #{a}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    mode, path = sys.argv[1], sys.argv[2]
    with open(path, encoding='utf-8') as f:
        html = f.read()
    base_dir = os.path.dirname(os.path.abspath(path))
    if mode == '--check':
        return check(html, base_dir)
    if mode == '--assets':
        problems = assets_check(html, base_dir)
        for p in problems:
            print("  -", p)
        print("OK — todas as imagens existem." if not problems else f"\n{len(problems)} imagem(ns) ausente(s).")
        return 1 if problems else 0
    if mode == '--anchors':
        anchors(html)
        return 0
    if mode == '--renumber':
        new_html, n = renumber_section_labels(html)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Renumerado: {n} seções. Reescreva TOC/nav e refs cruzadas conforme necessário.")
        return 0
    print(__doc__)
    return 1


if __name__ == '__main__':
    sys.exit(main())
