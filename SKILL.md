---
name: create-course
description: >-
  Cria um curso completo do zero: entrevista o usuário para definir escopo e
  público, faz pesquisa profunda na internet com múltiplos agentes paralelos
  (WebSearch/firecrawl + skill /watch para vídeos), documenta tudo em PRDs
  estruturados (PRD, estrutura, matriz de referências, log de pesquisa) e entrega
  um arquivo HTML único, escuro e navegável, com todo o curso. Use quando o
  usuário quiser "criar um curso", "montar um tutorial/guia completo", "produzir
  material didático sobre X", "transformar uma pesquisa em curso", ou invocar
  /create-course. Nasceu do processo que criou o curso "Clone Digital".
---

# Create Course

Skill para **criar um curso completo** sobre qualquer tema, do jeito que o curso
"Clone Digital" foi feito: entrevista → pesquisa profunda → PRDs vivos → um HTML
único e bonito. O papel dela é **fazer as perguntas certas, pesquisar a fundo em
muitas fontes, destilar o conhecimento não-óbvio, e entregar um artefato pronto**.

Entregável final: uma pasta de projeto com um `curso.html` autossuficiente
(CSS inline, tema escuro OU claro, hero com foto de abertura) + quatro documentos
de PRD que são o cérebro vivo do curso. Opcionalmente publicado na web
(Cloudflare Pages) com domínio próprio.

## Princípios que definem a qualidade (não negociáveis)

1. **Explicar o "porquê" é o coração.** Todo passo/regra do curso traz o objetivo
   E o motivo por trás — componente `.why-box`. O aluno entende, não decora. Isso
   também deixa o curso pronto para virar roteiro de vídeo (a narração explica a
   causa, não só o procedimento).
2. **Honestidade acima de hype.** Sempre incluir limitações reais, custos reais e
   avisos legais. Cada número no HTML tem que rastrear até uma fonte no
   `research-log.md`.
3. **Organizar por CAMINHOS/CONCEITOS, não por ferramentas.** A espinha é a
   decisão que o aluno precisa tomar; ferramentas entram a serviço dela. Uma
   seção-mapa/GPS no início ajuda a escolher antes de aprofundar.
4. **Documento vivo.** Os PRDs são atualizados a cada rodada de pesquisa. O curso
   nunca está "pronto" — está numa versão.
5. **Ortografia completa** no idioma-alvo (todos os acentos, nunca ASCII).
6. **Rigor de fonte.** Preços/recursos mudam rápido: datar a pesquisa e avisar
   "verifique o site oficial". Nunca inventar preço, recurso ou estatística.
7. **Enxuto, sem padding.** Cada box existe para ensinar, não para encher. Evite:
   (a) números "espantalho" que não aparecem em nenhum outro lugar (ex.: comparar
   "30 g vs 120 g" quando o curso só usa 30 g) — o leitor percebe como invenção;
   (b) caixas que só documentam uma pergunta pontual do usuário em vez de ensinar
   um conceito. Se um box não sobreviveria sem o contexto de uma conversa, corte.
8. **Coerência interna.** O curso não pode se contradizer entre seções nem cravar
   uma regra absoluta que ele mesmo desmente depois (ex.: "a massa é sempre mole,
   não dá pra moldar" numa seção e "modele a bola" em outra). Regras têm nuance;
   contradições confundem e destroem a confiança. Ver a passada de consistência (Fase 4c).

## Fluxo (fases)

Entrevista → Pesquisa → PRDs → HTML (4) + Ilustrações (4b) + Consistência (4c) →
Verificar/render (5) → Publicar (6, opcional).

### Fase 1 — Entrevista (SEMPRE primeiro; use `AskUserQuestion`)

Nunca comece a pesquisar sem definir o escopo. Faça as perguntas em 1-2 rodadas
de `AskUserQuestion` (agrupe; não faça uma pergunta por vez). O que precisa saber:

- **Tema e ângulo** — sobre o quê exatamente, e qual recorte/tese. (Se o usuário
  já deu um tema vago, proponha 2-3 ângulos e deixe escolher.)
- **Público e nível** — para quem, do iniciante ao avançado; contexto (técnico?).
- **Idioma** — do curso (default: idioma do usuário).
- **Objetivo/transformação** — o que o aluno consegue fazer ao terminar.
- **Profundidade/escopo** — tamanho alvo (ex.: ~10, ~20, ~25 seções) e se é
  documento vivo para expansão contínua.
- **Fontes especiais** — há vídeos (YouTube) para analisar via `/watch`? Sites,
  PDFs, docs proprietários, contas/assinaturas que o usuário já tem?
- **Marca/visual** — nome/título, **cor de acento** (default roxo `#6366f1`;
  ofereça a paleta pronta da Fase 4 ou aceite um hex), **tema** (escuro padrão ou
  claro "editorial creme"), **par tipográfico** (neutro Inter, ou editorial
  Fraunces+Manrope+DM Mono), regras de estilo (ex.: sem emojis em texto corrido).
  Se o usuário citar um site de referência, extraia a paleta/fontes dele (firecrawl
  `scrape --format rawHtml` → grep de `--var`/hex/`font-family`).
- **Foto de abertura (hero)** — o curso vai ter uma imagem grande de abertura?
  (recomendado; é a tese visual). Se sim, o estilo dela DERIVA do tema (Fase 4b).
- **Publicação** — fica só como arquivo local ou vai pro ar? Se web: domínio
  desejado (Cloudflare Pages — Fase 6).

Registre as respostas — elas viram a Seção 1 do `PRD.md`. Se o usuário diser
"decida você", assuma defaults sensatos e siga; não trave.

### Fase 2 — Pesquisa profunda (fan-out paralelo)

Este é o motor. Faça pesquisa larga e verificada, não um resumo de memória.

- **Decomponha o tema em 4-8 ângulos** e dispare agentes em paralelo (uma única
  mensagem, múltiplos `Agent`/Workflow). Cada agente busca um ângulo distinto via
  **WebSearch** e/ou **firecrawl** (`firecrawl search` + `scrape` de fontes
  oficiais). Ângulos típicos: panorama do tema, ferramentas/players, preços e
  tiers, comparativos, casos reais/números, comunidade (Reddit/fóruns), armadilhas
  e limitações, aspectos legais/éticos.
- **Vídeos:** se o usuário indicou vídeos, use a skill **`/watch`** (passe a URL)
  para "assistir" — extrai frames + transcript e permite destilar fala + tela.
- **Verifique afirmações** antes de escrever: preço, recurso, estatística, status
  (vivo/morto). Prefira múltiplas fontes. Para review comprovadamente cético de
  achados importantes, um segundo agente pode tentar refutar.
- **Salve os achados brutos** em `research-log.md` conforme chegam (por rodada),
  com as URLs. É a bibliografia e a trilha de retomada.
- **Destile o não-óbvio** para o `PRD.md` §6 (Aprendizados-chave): o que um leigo
  não acharia sozinho. Esse é o valor do curso.

### Fase 3 — Documentar os PRDs (o cérebro vivo)

Crie a pasta do projeto e, a partir de `templates/`, preencha:

- `PRD.md` — visão, público, princípios, decisões editoriais e o porquê, resumo
  das referências, aprendizados-chave, roadmap. (`templates/PRD.md`)
- `course-structure.md` — o mapa seção a seção, agrupado em Partes, com o que cada
  seção entrega. Fonte de verdade da estrutura. (`templates/course-structure.md`)
- `reference-matrix.md` — matriz de ferramentas/fontes: preço, prós, contras,
  disponibilidade no idioma-alvo. (`templates/reference-matrix.md`)
- `research-log.md` — log por rodada, fontes, vídeos, achados brutos.
  (`templates/research-log.md`)

Antes de gerar o HTML, feche a **estrutura**: Partes → seções, na ordem
início→fim, com uma seção-mapa cedo se o tema tiver caminhos. Confirme a estrutura
com o usuário se ele quis participar; senão, siga com a proposta.

### Fase 4 — Construir o HTML (arquivo único)

Monte `curso.html` a partir de `assets/html-template.html`, **colando o conteúdo
inteiro de `assets/course-theme.css` dentro do `<style>`** (entregável de arquivo
único).

**Tema (escuro ou claro):** o CSS traz DOIS presets no topo do `:root` — escuro
(padrão) e claro "editorial creme" (comentado logo abaixo). Para o claro, troque o
bloco `:root` inteiro pelo preset claro E ajuste os textos de `.callout.green/
.yellow/.red` e `.tag-*` para tons escuros (o padrão é claro e some no creme — o
CSS lista os overrides). Não misture os dois presets.

**Fontes (parametrizáveis):** três variáveis — `--font-display` (títulos),
`--font-body` (corpo), `--font-mono` (kickers/rótulos). Troque-as + o `<link>` do
Google Fonts juntos. Um display serif (ex.: Fraunces) + corpo humanista (Manrope)
dá ar de revista; Inter em tudo é o neutro seguro.

**Cor de acento (parametrizável):** para reskinar o curso, edite só os 4 valores
de acento no `:root` — `--accent` (hex), `--accent-rgb` (a MESMA cor em triplet
RGB, ex.: `99,102,241`), `--accent-light` (tom claro p/ texto sobre fundo soft) e
`--accent-lighter` (mais claro p/ números de destaque). Paleta pronta:

| Cor | `--accent` | `--accent-rgb` | `--accent-light` | `--accent-lighter` |
|---|---|---|---|---|
| Roxo (default) | `#6366f1` | `99,102,241` | `#a5b4fc` | `#c7d2fe` |
| Azul | `#3b82f6` | `59,130,246` | `#93c5fd` | `#bfdbfe` |
| Verde-esmeralda | `#10b981` | `16,185,129` | `#6ee7b7` | `#a7f3d0` |
| Âmbar | `#f59e0b` | `245,158,11` | `#fcd34d` | `#fde68a` |
| Rosa | `#ec4899` | `236,72,153` | `#f9a8d4` | `#fbcfe8` |
| Ciano | `#06b6d4` | `6,182,212` | `#67e8f9` | `#a5f5fc` |

Para um hex arbitrário: use a cor no `--accent`+`--accent-rgb` e escolha `light`/
`lighter` clareando ~30% e ~50% (misturar com branco). Evite acento com pouco
contraste sobre `#0a0a0a`.

O template documenta cada componente:

- `nav` (âncoras das seções-chave) + `.hero` como **tese visual**: full-bleed com
  foto (`.hero-bg` + `.hero-scrim` + `.hero-content > .hero-inner`), texto à
  esquerda (badge, título com `<em>`, promessa, 3-4 `.hero-stat` honestos). Sem
  foto, remova `.hero-bg`/`.hero-scrim` e vira hero de texto. As imagens desktop
  (landscape) e mobile (vertical) vêm das vars `--hero-img`/`--hero-img-mobile`.
- `.toc` agrupado por `.toc-part` — um cabeçalho por Parte, `.toc-item` por seção.
- `.part-divider` antes da primeira seção de cada Parte.
- `section` com `.section-label` ("Seção NN"), `<h2>`, `.section-intro`.
- **`.why-box`** em toda etapa instrucional (o diferencial).
- `.callout` para destaques honestos: default (accent), `.green` (ganho),
  `.yellow` (cuidado), `.red` (legal/risco).
- `.platform-grid` + `.platform-card` para grades; `.filming-card` para pares;
  `<table>` para comparativos (sempre com coluna de idioma-alvo quando relevante).
- `<figure>`+`<figcaption>` só se houver ilustração gerada (ver Fase 4b).

**Regras de produção de HTML (aprendidas na dor — ver `PRD.md` §7):**
- **Grids com colunas FIXAS** `repeat(N,1fr)` batendo a contagem de itens. Nunca
  `auto-fill` que gera linha órfã.
- **Separadores só no nível de PARTE.** `<section>` NÃO leva `border-top` — uma
  linha de ponta a ponta em cada seção lê como "fim de bloco", não abertura. O
  espaço vertical já separa; a linha fica só no `.part-divider` (as 4-5 Partes).
- **Âncoras únicas**; `id` da seção == href na TOC e no nav.
- **Numeração** zero-padded (01, 02…), consistente entre `section-label`, TOC e
  ordem do DOM.
- Para arquivos grandes, edições estruturais (inserir/mover/renumerar seções,
  reconstruir TOC/nav, corrigir acentos em massa) devem usar o helper Python
  `assets/build_helpers.py` — nunca corrigir acento com regex que toque em nomes
  de classe/atributo (só texto entre tags).

### Fase 4b — Ilustrações (opcional, mas o hero vale muito)

Gerar via MCP do Magnific (`images_generate` → `creations_wait` → baixar a `url`)
ou OpenRouter (`google/gemini-2.5-flash-image`). Sempre **16:9** para figuras,
**sem texto renderizado** (modelos erram letras — legenda vai no `<figcaption>`).

**O estilo DERIVA do tema — nunca hardcode "escuro".** Monte um "estilo-base" que
casa com a paleta e cole no fim de cada prompt. É o erro nº 1: gerar imagens de
fundo escuro e depois o curso virar tema claro → tudo destoa. Exemplos:
- Tema escuro: `moody dark background (near-black), warm rim lighting, shallow
  depth of field, high detail, no text/letters/logos`.
- Tema claro: `bright airy editorial photography, soft natural daylight, clean
  cream background, generous negative space, modern high-end aesthetic, no
  text/letters/logos`.

**Hero = duas imagens dedicadas** (a foto de abertura é a que mais importa):
- **Desktop** landscape 16:9, objeto de um lado e MUITO espaço negativo do outro
  (onde o texto vai). Salve `assets/img/hero.jpg`.
- **Mobile** VERTICAL 9:16 — objeto ancorado embaixo, dois terços de cima arejados
  p/ o texto. Salve `assets/img/hero-mobile.jpg`. (Landscape cortada no retrato
  fica horrível; por isso a vertical dedicada.) Gere 2-3 variantes de cada e
  ESCOLHA vendo (Read no arquivo, não confie no prompt).

**Fluxo:** gerar em paralelo (uma mensagem, vários `images_generate`) →
`creations_wait` → baixar → **otimizar** (`sips -Z 1600 -s formatOptions 82`, ou
~2200px p/ o hero) → conferir **< ~300 KB** por imagem → salvar em `assets/img/` →
embutir em `<figure>` (ou nas vars do hero). Rode `build_helpers.py --assets`.

### Fase 4c — Passada de consistência (crítica, não pule)

Depois de escrever, releia o curso inteiro caçando o que destrói confiança:
- **Contradições entre seções** — uma seção crava o oposto de outra. Reconcilie
  com nuance (ex.: "massa mole" é um extremo do espectro; com mais ligante ela
  modela). Se um vídeo/fonte externa contradiz o consenso, apresente como método
  do praticante e aponte a divergência — não copie a afirmação frouxa.
- **Regras absolutas que o próprio curso desmente** — troque "sempre/nunca X" por
  a condição real ("X quando Y").
- **Padding e espantalhos** (Princípio 7) — corte números que não aparecem em
  outro lugar e caixas que só documentam uma pergunta pontual.
- **Confusões previsíveis do leitor** — onde dois conceitos se parecem (ex.:
  temperatura do forno vs interna), adicione um callout curto que os separa.
- **Voz impessoal/didática** — o curso é COMPARTILHADO com terceiros, não é uma
  resposta ao usuário da conversa. Nunca escreva "você lembrou certo", "como você
  perguntou", "no seu caso". O "você" instrucional genérico ("você alimenta o
  starter") é ok; referência à conversa/memória do usuário, não. Se um achado veio
  de uma pergunta do usuário, ensine o conceito — não documente o diálogo.
Um subagente cético ("liste toda contradição e todo número sem fonte") acha o que
você não vê relendo o próprio texto.

### Fase 5 — Verificar (sanity checks + render real)

Rode `assets/build_helpers.py --check curso.html`. Confirme:
- nº de `<section>` == nº de `.section-label` == nº de `.toc-item`.
- `<section>` abre == fecha; `<div>` balanceados.
- âncoras únicas; toda âncora da TOC/nav existe como `id`.
- toda imagem referenciada (`src`/`url()`) existe em disco (`--check`/`--assets`).
- nenhuma referência cruzada "Seção NN" quebrada após renumeração.
- acentos corretos (sem ASCII no lugar de acentuado).

**Render real (não confie só no HTML):** tire screenshots em DESKTOP (1440) e
MOBILE (390) e OLHE. O hero e os grids quebram diferente por viewport.
- Use **playwright** ou `chrome --headless=new` — o `chrome --headless` ANTIGO
  ignora `--window-size`/viewport e MENTE (renderiza ~800px e reporta como mobile).
  Snippet playwright: `chromium.launch({executablePath: <Chrome instalado>})` →
  `newPage({viewport:{width:390,height:844}})` → `screenshot()`.
- Se algo "vazar"/cortar, meça no navegador (`document.body.scrollWidth`,
  `getBoundingClientRect().width`) antes de mexer no CSS às cegas.

Depois, entregue: resuma o que foi criado, onde está, e as pendências/incertezas
que ficaram no `research-log.md` (o que testar/verificar antes de usar).

### Fase 6 — Publicar (opcional — Cloudflare Pages)

Se o usuário quiser o curso no ar:
1. **Monte a pasta de deploy** `dist/`: `index.html` (cópia do `curso.html`) +
   `assets/` inteiro. **Sincronize TODOS os assets a cada deploy** — o bug clássico
   é copiar só o HTML e esquecer uma imagem nova (ex.: `hero.jpg`) → 404 no ar,
   header sem foto. Rode `build_helpers.py --assets dist/index.html` antes de subir.
2. **Deploy:** `wrangler pages project create <nome> --production-branch main` (1×)
   e `wrangler pages deploy dist --project-name <nome> --branch main --commit-dirty=true`.
   Precisa de `wrangler` logado (`wrangler whoami`).
3. **Domínio próprio:** anexe pela API de Pages
   (`POST /accounts/{acc}/pages/projects/{proj}/domains {"name":"sub.dominio.com"}`)
   — mas o CNAME NÃO é criado sozinho. O usuário precisa criar 1 registro DNS no
   zone certo: `CNAME  <sub>  →  <proj>.pages.dev  (Proxied 🟠)`. O token do
   `wrangler` normalmente NÃO tem escopo de DNS; se for automatizar, peça um token
   com **Zone→DNS→Edit** e crie via API. Verifique no NS autoritativo, não no cache.
4. **Verifique HTTPS 200** forçando a edge (o DNS local demora a propagar):
   `curl --resolve sub.dominio.com:443:<IP-Cloudflare> https://sub.dominio.com`.
   O cert (Google CA) provisiona em minutos; status via a mesma API de domains.

## Expansão contínua (chamadas seguintes)

Quando o curso já existe e o usuário pede para expandir: leia os PRDs primeiro
(evita duplicar), abra uma **rodada nova** no `research-log.md`, pesquise só o
delta, atualize `reference-matrix.md`/`course-structure.md`, insira/renumere via
helper, e registre a decisão. O curso avança em versões.

## Arquivos desta skill
- `SKILL.md` — este guia.
- `assets/course-theme.css` — o tema completo (cole no `<style>` do HTML).
- `assets/html-template.html` — esqueleto + todos os componentes documentados.
- `assets/build_helpers.py` — renumeração, correção de acentos segura, sanity checks.
- `templates/PRD.md`, `course-structure.md`, `reference-matrix.md`, `research-log.md`.
