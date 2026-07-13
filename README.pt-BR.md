<div align="center">

# create-course

**Uma skill do Claude Code que transforma um tema de pesquisa num curso pronto.**

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-6366f1)](https://github.com/renatodpaula/create-course)
[![Docs](https://img.shields.io/badge/docs-wiki-6366f1)](https://github.com/renatodpaula/create-course/wiki)
[![Autor](https://img.shields.io/badge/autor-Renato%20dPaula-6366f1)](https://renatodpaula.ai)

*[Read in English](README.md)*

</div>

---

A `create-course` entrevista você sobre escopo e público, pesquisa o tema a
fundo com agentes paralelos, mantém tudo em PRDs vivos, e entrega um curso em
HTML único e autossuficiente — o mesmo processo usado para montar o curso
"Clone Digital".

## Como funciona

| Etapa | O que acontece |
|---|---|
| **1. Entrevista** | `AskUserQuestion` fecha tema, público, profundidade, idioma, marca e o provedor de geração de imagem. |
| **2. Pesquisa** | 4–8 agentes em paralelo cobrem WebSearch/firecrawl (+ `/watch` para vídeos), verificando afirmações antes de escrever. |
| **3. PRDs vivos** | Os achados vão para quatro documentos estruturados — visão, estrutura, matriz de referências, log de pesquisa — atualizados a cada rodada. |
| **4. Construir o HTML** | Um único `curso.html`: CSS inline, tema escuro ou claro, componente-assinatura `.why-box`, foto de hero. |
| **5. Passada de consistência** | Releitura completa caçando contradições, regras absolutas que o próprio curso desmente, e padding. |
| **6. Verificar** | Checks estruturais + render real em viewport desktop e mobile. |
| **7. Publicar** *(opcional)* | Deploy no Cloudflare Pages com domínio próprio. |

## Princípios

- **Explicar o "porquê"** — toda regra vem com o motivo por trás.
- **Honestidade acima de hype** — custos, limites e fontes reais e datadas.
- **Caminhos, não ferramentas** — organizar pela decisão do aluno.
- **Documento vivo** — o curso é versionado, nunca "pronto".
- **Enxuto** — sem padding, sem números-espantalho, sem caixa de enchimento.
- **Coerente internamente** — nenhuma seção contradiz outra.

## Instalar

Link ou copie a pasta para onde o Claude Code lê skills:

```bash
ln -s ~/Projetos/skills/create-course ~/.claude/skills/create-course
```

Depois invoque com `/create-course`, ou peça "criar um curso sobre X".

## Requisitos

A skill orquestra outras skills e CLIs (lista completa, com alternativas e
degradação graciosa, na seção **Dependências** da `SKILL.md`):

```bash
brew install yt-dlp ffmpeg              # YouTube (Fase 2b) + /watch
pip3 install playwright && playwright install chromium   # render check (Fase 5)
npm i -g wrangler                       # só para publicar (Fase 6)
```

- **Skill `/watch`** (para analisar vídeos com tela + fala):
  [bradautomates/claude-video](https://github.com/bradautomates/claude-video) —
  `git clone` para `~/.claude/skills/watch`.
- **firecrawl** *(opcional)* — busca/scrape com extração completa
  (`brew install firecrawl` + `FIRECRAWL_API_KEY`); sem ele, o WebSearch nativo cobre.
- **Provedor de imagem** *(opcional, para o hero)* — API OpenAI/Gemini/OpenRouter/
  Higgsfield ou MCP de imagem; sem nenhum, o curso sai com hero de texto.

## Arquivos

| Caminho | Para quê serve |
|---|---|
| `SKILL.md` | O guia completo — entrevista → pesquisa → PRDs → HTML/ilustrações/consistência → verificar → publicar. |
| `assets/course-theme.css` | Tema completo (colar no `<style>`); presets escuro/claro, fontes e hero como variáveis CSS. |
| `assets/html-template.html` | Esqueleto com todo componente documentado, incluindo o hero full-bleed com foto. |
| `assets/build_helpers.py` | Renumeração, correção segura de acentos, checks estruturais (`--check`, `--assets`, `--anchors`, `--renumber`). |
| `templates/*.md` | Os quatro PRDs vivos. |

Documentação completa, incluindo referência dos componentes HTML e o guia de
publicação: **[wiki do projeto](https://github.com/renatodpaula/create-course/wiki)**.

## Autor

**Renato dPaula** — [@renatodpaula.ai](https://renatodpaula.ai)
