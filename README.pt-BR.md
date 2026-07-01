# create-course

*[Read in English](README.md)*

Skill do Claude Code que **cria um curso completo do zero** e entrega um HTML
único e navegável — do jeito que o curso "Clone Digital" foi produzido.

**Fluxo:** entrevista (`AskUserQuestion`) → pesquisa profunda com agentes
paralelos (WebSearch/firecrawl + `/watch` para vídeos) → PRDs vivos (PRD,
estrutura, matriz de referências, log de pesquisa) → `curso.html` (CSS inline,
tema **escuro ou claro**, **hero com foto de abertura**, componente-assinatura
`.why-box`) → passada de consistência → sanity checks + render real → publicar
opcional (Cloudflare Pages).

**Princípios:** explicar o porquê; honestidade (custos/limites/legal reais);
organizar por caminhos, não por ferramentas; documentos vivos; rigor de fonte;
enxuto (sem padding nem números-espantalho); coerência interna (sem contradições).

## Instalar
Link/copie para onde o Claude Code lê skills, ex.:
```
ln -s ~/Projetos/skills/create-course ~/.claude/skills/create-course
```
Depois invoque com `/create-course` ou peça "criar um curso sobre X".

## Arquivos
- `SKILL.md` — o guia (entrevista → pesquisa → PRDs → HTML/ilustrações/consistência → verificar → publicar).
- `assets/course-theme.css` — tema completo (colar no `<style>`); presets escuro/claro, fontes e hero como variáveis.
- `assets/html-template.html` — esqueleto + componentes documentados (hero full-bleed com foto).
- `assets/build_helpers.py` — renumeração, correção segura de acentos, checks (`--check`, `--assets`, `--anchors`, `--renumber`).
- `templates/*.md` — os quatro PRDs.

Documentação completa: [wiki deste repositório](https://github.com/renatodpaula/create-course/wiki).

## Autor
Renato dPaula — [@renatodpaula.ai](https://renatodpaula.ai)
