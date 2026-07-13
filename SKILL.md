---
name: create-course
description: >-
  Cria um curso completo do zero: entrevista o usuário para definir escopo e
  público, faz pesquisa profunda na internet com múltiplos agentes paralelos
  (WebSearch/firecrawl + skill /watch para vídeos), documenta tudo em PRDs
  estruturados (PRD, estrutura, matriz de referências, log de pesquisa) e entrega
  um arquivo HTML único, escuro e navegável, com todo o curso. TAMBÉM cuida de
  cursos já criados: qualquer alteração, expansão, correção ou nova aula/vídeo
  incorporado a um curso existente deve passar por esta skill (fluxo "Expansão
  contínua" — rodada no research-log, guardião da tese, renumeração segura,
  checklist de fechamento que mantém os PRDs sincronizados). Use quando o
  usuário quiser "criar um curso", "montar um tutorial/guia completo", "produzir
  material didático sobre X", "transformar uma pesquisa em curso", "adicionar/
  mudar/corrigir algo num curso existente", "incorporar um vídeo/aula ao curso",
  "revisar/reorganizar o curso", ou invocar /create-course. Nasceu do processo
  que criou o curso "Clone Digital".
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
9. **Guardião da tese.** Todo curso declara sua TESE em 1 linha no topo do `PRD.md`
   (ex.: "pão de fermento natural, sem ovos"; "use as ferramentas que você já paga").
   Todo conteúdo novo — na criação E em cada expansão — é checado contra ela:
   *isso contradiz a tese?* Se contradiz e mesmo assim vale entrar, entra com um
   callout de desvio explícito ("esta receita usa fermento biológico — foge da linha
   do curso porque...") ou rotulado como bônus fora da linha. Nunca em silêncio.
   É o erro nº 1 da expansão incremental: conteúdo de vídeo/fonte nova colado sem
   reconciliar com a espinha do curso.
10. **PRDs nunca mentem.** Uma rodada (criação ou expansão) só está FECHADA quando
   `PRD.md`, `course-structure.md` e o mapa de renumeração refletem o HTML real.
   Documento de planejamento desatualizado é pior que nenhum: a próxima expansão
   lê o mapa errado e duplica/desalinha conteúdo. Ver "Checklist de fechamento de
   rodada" no fim deste guia.

## Fluxo (fases)

Entrevista → Pesquisa (2) + Curadoria de vídeo (2b) → PRDs → HTML (4) +
Ilustrações (4b) + Consistência (4c) → Verificar/render (5) → Publicar (6, opcional).

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
- **Profundidade da pesquisa em vídeo** (`AskUserQuestion` com 3 opções — mais
  vídeo assistido = curso melhor, mas mais tokens e tempo; a escolha é do usuário):
  | Nível | Varredura | Transcrições lidas | `/watch` completo | Comentários | Idiomas |
  |---|---|---|---|---|---|
  | **Rápido** | ~15-20 vídeos | ~5 | 1-2 (só onde o visual importa) | top ~20 dos assistidos | idioma-alvo + EN |
  | **Equilibrado** (default) | ~40-60 | ~10-15 | 3-5 | top ~50 por vídeo lido | idioma-alvo + EN |
  | **Profundo** | ~100+ | ~25-40 | 8-15 | top ~100 por vídeo lido | idioma-alvo + EN + ES (+ outros se o tema tiver comunidade forte neles) |
  A distinção-chave: **ler transcrição é barato** (texto puro, sem baixar vídeo);
  `/watch` completo (frames + transcript) é caro — reserve para vídeos onde a TELA
  ensina (técnica manual, UI de ferramenta, demonstração). Um curso não se
  constrói com 3 vídeos: constrói-se lendo dezenas de transcrições e assistindo
  de verdade só os que a triagem apontar como densos.
- **Marca/visual** — nome/título, **cor de acento** (default roxo `#6366f1`;
  ofereça a paleta pronta da Fase 4 ou aceite um hex), **tema** (escuro padrão ou
  claro "editorial creme"), **par tipográfico** (neutro Inter, ou editorial
  Fraunces+Manrope+DM Mono), regras de estilo (ex.: sem emojis em texto corrido).
  Se o usuário citar um site de referência, extraia a paleta/fontes dele (firecrawl
  `scrape --format rawHtml` → grep de `--var`/hex/`font-family`).
- **Foto de abertura (hero)** — o curso vai ter uma imagem grande de abertura?
  (recomendado; é a tese visual). Se sim, o estilo dela DERIVA do tema e pergunte
  **qual gerador de imagem usar** — API OpenAI, API Google Gemini, API
  OpenRouter, API Higgsfield, MCP Higgsfield, MCP de geração de imagem já
  conectado (ex.: Magnific/Freepik), ou "decida você" (use o que estiver
  disponível no ambiente). Ver Fase 4b — esta skill é pública, não assuma que
  todo mundo tem o mesmo provedor configurado.
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
- **Vídeos:** se o usuário indicou vídeos específicos, use a skill **`/watch`**
  (passe a URL) para "assistir" — extrai frames + transcript e permite destilar
  fala + tela. Para DESCOBRIR vídeos que o usuário não indicou, rode a Fase 2b.
- **Verifique afirmações** antes de escrever: preço, recurso, estatística, status
  (vivo/morto). Prefira múltiplas fontes. Para review comprovadamente cético de
  achados importantes, um segundo agente pode tentar refutar.
- **Salve os achados brutos** em `research-log.md` conforme chegam (por rodada),
  com as URLs. É a bibliografia e a trilha de retomada.
- **Destile o não-óbvio** para o `PRD.md` §6 (Aprendizados-chave): o que um leigo
  não acharia sozinho. Esse é o valor do curso.

### Fase 2b — Curadoria de vídeo no YouTube (automatizada)

**Complementa a Fase 2, não a substitui** — a pesquisa web (fóruns, Reddit,
blogs, docs oficiais, papers) continua sendo o motor; rode as duas. O YouTube
entra como fonte adicional porque concentra o conhecimento de praticantes —
aulas, técnicas, métodos que não estão em texto. Buscar isso na mão não escala
e deixa passar os melhores.
Pipeline (escala conforme o nível de profundidade escolhido na Fase 1):

1. **Gerar queries** — 5-10 buscas a partir do tema e das lacunas do
   `research-log.md`, nos idiomas do nível escolhido (sempre idioma-alvo + EN;
   ES e outros no nível Profundo). Misture query genérica ("curso X completo"),
   de técnica ("como fazer Y sem Z") e de problema ("X não funciona / erro").
2. **Varrer metadados sem baixar nada:**
   `yt-dlp "ytsearchN:<query>" --flat-playlist -J` → título, canal, duração,
   views, data. Junte tudo num JSON de candidatos (dedupe por ID).
3. **Triagem 1 (metadados):** descarte óbvio — Shorts/<4 min, título clickbait
   sem substância, vídeo velho quando o tema muda rápido. Rankeie por sinal:
   views × recência × autoridade aparente do canal × aderência ao tema.
4. **Triagem 2 (transcrição, a etapa que importa):** para os ~top-N do ranking,
   baixe SÓ as legendas (barato, segundos por vídeo):
   `yt-dlp --skip-download --write-auto-subs --sub-langs "pt*,en*,es*" --sub-format vtt <URL>`
   Agentes paralelos leem as transcrições e pontuam cada vídeo (0-10) em:
   **método concreto** (passo a passo replicável vs conversa), **densidade**
   (dicas/minuto), **novidade** (o que o curso ainda não tem), **autoridade**
   (praticante demonstrando vs entusiasta resumindo). Registre a nota + 3 linhas
   de justificativa no `research-log.md`.
5. **Comentários — minere-os, valem ouro:** os melhores comentários de um vídeo
   bom carregam a experiência de OUTROS praticantes — correções ao vídeo,
   variações testadas, armadilhas ("fiz assim e deu errado porque..."). 99% é
   ruído; o filtro é o like count da comunidade. Para cada vídeo que passou na
   triagem 2:
   `yt-dlp --skip-download --write-comments --extractor-args "youtube:comment_sort=top;max_comments=100,all,0" <URL>`
   → o `.info.json` traz os comentários com `like_count`/`author`/`text`.
   Agente filtra: like_count alto + conteúdo técnico (ignora "obrigado!",
   elogios, pedidos). Achados de comentário entram no `research-log.md` COM
   marcação de origem ("comentário, não verificado") — são relatos anedóticos:
   use para gerar hipóteses e callouts de "praticantes relatam...", nunca como
   fato cravado sem segunda fonte.
6. **`/watch` completo só nos vencedores** — os vídeos com maior nota onde a
   TELA ensina algo que a transcrição não captura. Quantidade conforme o nível
   (1-2 / 3-5 / 8-15).
7. **Shortlist para o usuário:** apresente a tabela final (vídeo, canal, nota,
   por quê) antes de gastar os `/watch` — ele pode conhecer os canais e vetar/
   promover candidatos.

Tudo desta fase entra como rodada no `research-log.md`: queries usadas, nº de
candidatos varridos, notas da triagem, comentários aproveitados (com link do
vídeo). Se `yt-dlp` não estiver instalado, avise (`brew install yt-dlp`) — não
tente scrape manual do YouTube.

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
- **Referência cruzada = LINK DE ÂNCORA, nunca só número.** Escreva
  `<a href="#stacks">Seção de stacks</a>` (ou `... (<a href="#voz">Seção 05</a>)`),
  não "veja a seção 10" em texto solto. Número hardcoded quebra silenciosamente a
  cada renumeração (e o remap por regex perde variações como "seção" minúsculo —
  aconteceu). Âncora não muda quando a numeração muda; o `--check` valida que o
  alvo existe.
- **Placeholders em prompts-modelo.** Prompt de exemplo que o aluno vai copiar
  NUNCA carrega dado pessoal do usuário da conversa (nome da voz treinada, conta,
  e-mail, domínio). Use `[nome-da-sua-voz]`, `[seu-projeto]`. O curso é
  compartilhado; dado pessoal hardcoded é vazamento (ver Fase 4c).
- Para arquivos grandes, edições estruturais (inserir/mover/renumerar seções,
  reconstruir TOC/nav, corrigir acentos em massa) devem usar o helper Python
  `assets/build_helpers.py` — nunca corrigir acento com regex que toque em nomes
  de classe/atributo (só texto entre tags).

### Fase 4b — Ilustrações (opcional, mas o hero vale muito)

**Gerador de imagem é escolha do usuário (Fase 1) — esta skill não assume um só
provedor.** Cada ambiente tem chaves/MCPs diferentes; descubra o que está
disponível (`ToolSearch`/MCPs conectados) e confirme com o usuário antes de
gastar créditos. Opções comuns e como acioná-las:

| Provedor | Como chamar |
|---|---|
| **API OpenAI** | `images.generate` (modelo `gpt-image-1`), prompt + `size`; resposta em base64 ou URL. |
| **API Google Gemini** | `generateContent` com modelo de imagem (ex.: `gemini-2.5-flash-image` "nano banana" ou Imagen); prompt em texto. |
| **API OpenRouter** | proxy de chat completions apontando pra um modelo de imagem (ex.: `google/gemini-2.5-flash-image`); mesma chamada de texto, resposta traz a imagem. |
| **API Higgsfield** | endpoint de geração da Higgsfield (Soul e afins); consulte a doc da conta do usuário para modelo/parâmetros exatos. |
| **MCP Higgsfield** | tools do MCP da Higgsfield, se conectado — geração + polling conforme o server expuser. |
| **MCP de terceiros já conectado** (ex.: Magnific/Freepik) | fluxo típico `images_generate` → `creations_wait` (polling até ficar pronto) → baixar a `url`. |

Se nenhum provedor estiver disponível, **não trave**: avise o usuário e siga sem
hero/ilustrações (hero de texto — remova `.hero-bg`/`.hero-scrim` no template).

Independente do provedor: sempre **16:9** para figuras, **sem texto renderizado**
(modelos erram letras — legenda vai no `<figcaption>`).

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

**Fluxo:** gerar em paralelo (uma mensagem, várias chamadas ao provedor
escolhido) → esperar/baixar (poll se o provedor for assíncrono) → **otimizar**
(`sips -Z 1600 -s formatOptions 82`, ou ~2200px p/ o hero) → conferir
**< ~300 KB** por imagem → salvar em `assets/img/` → embutir em `<figure>` (ou
nas vars do hero). Rode `build_helpers.py --assets`.

### Fase 4c — Passada de consistência (crítica, não pule)

Roda na criação E periodicamente: **a cada ~3 rodadas de expansão, uma rodada de
consolidação** dedicada só a isto (a degradação não aparece na criação — acumula
nas costuras das expansões). Releia o curso inteiro caçando o que destrói confiança:
- **Conteúdo que contradiz a TESE do curso** (Princípio 9) — receita/método/
  recomendação que rompe a linha declarada no PRD sem callout de desvio. Inclui
  a versão numérica: dois "mínimos", dois "sempre", duas recomendações-padrão
  incompatíveis entre hero, seção-mapa e seções internas.
- **Referências-fantasma** — texto que aponta para conteúdo que não existe no
  curso ("a mesma receita já usada" que nunca foi apresentada). Típico de
  conteúdo destilado de vídeo: o autor do vídeo referenciava OUTRO vídeo dele.
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
- nenhuma referência cruzada "Seção NN" quebrada após renumeração (o check é
  case-insensitive — "seção 10" minúsculo também conta).
- acentos corretos (sem ASCII no lugar de acentuado).
- `--outline` bate com `course-structure.md` (ver checklist de fechamento).

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

## Modelos e economia de tokens

A skill não exige um modelo único — o custo/qualidade otimiza escolhendo o
cérebro por etapa. Princípio: **trabalho de VOLUME → modelo rápido/barato;
trabalho de JULGAMENTO → o melhor modelo disponível.** O julgamento é pouco
token e define o curso inteiro; o volume é muito token e é mecânico.

| Etapa | Natureza | Modelo Claude sugerido |
|---|---|---|
| Fase 1 — Entrevista/escopo | conversa curta | qualquer um (Sonnet basta) |
| Fase 2 — agentes de pesquisa web | volume (busca+extração) | Sonnet nos subagentes |
| Fase 2b — varredura/triagem de transcrições e comentários | volume mecânico, muito token | **Haiku ou Sonnet** nos subagentes |
| Destilar o não-óbvio, fechar ESTRUTURA, decisões editoriais, tese | julgamento de alto impacto, pouco token | **Opus/Fable** |
| Fase 4 — escrever o HTML (why-boxes, didática) | volume + qualidade de escrita | Sonnet escreve bem; Opus/Fable se a voz didática for o diferencial |
| Fase 4c — passada cética / consistência | julgamento (achar contradição exige raciocínio) | **Opus/Fable**, em sessão/subagente separado |
| Renumeração, checks, correções mecânicas | script (`build_helpers.py`) | nenhum — não gaste modelo com o que o script faz |

No Claude Code: rode o loop principal no melhor modelo do plano e passe
`model`/subagente mais barato nos fan-outs de volume (o parâmetro de modelo do
Agent/Workflow). Sonnet dá conta da skill inteira num plano menor; o upgrade
para Opus/Fable rende mais nas 3 linhas de julgamento da tabela — se for
escolher UM momento para o modelo forte, escolha a estrutura + a passada cética.

**Portabilidade (a metodologia é agnóstica):** esta skill roda no Claude Code,
mas o MÉTODO (entrevista → pesquisa → PRDs → artefato → vida) funciona em
qualquer assistente atual. Equivalências: fan-out de pesquisa ≈ Deep Research
(ChatGPT/Gemini/Perplexity); PRD persistente ≈ Projects (ChatGPT/Claude) ou
Gems (Gemini); subagentes baratos ≈ rodar as triagens num modelo mini/flash.
O que não é portátil são os helpers (`build_helpers.py`) e o fluxo de arquivos —
num chat puro, o artefato vira um documento Markdown/HTML que o usuário guarda
e recola a cada rodada.

## Expansão contínua (chamadas seguintes)

Quando o curso já existe, TODA mudança passa por aqui — expansão grande, seção
nova, correção de conteúdo ou "só troca esse parágrafo". É AQUI que os cursos
degradam — o HTML evolui e os PRDs ficam para trás, a próxima expansão lê o mapa
errado, e conteúdo novo entra sem reconciliar com a tese. O fluxo:

1. **Leia os PRDs primeiro** (evita duplicar) — e rode
   `build_helpers.py --outline curso.html` para conferir que `course-structure.md`
   ainda bate com o HTML real. Se não bate, RECONCILIE ANTES de expandir
   (alguém editou fora do processo; não construa sobre mapa errado).
2. **Abra rodada nova** no `research-log.md`, pesquise só o delta (Fase 2/2b).
3. **Proposta de colocação ANTES de escrever:** registre na rodada onde o
   conteúdo novo vai entrar (subseção da NN? seção nova na Parte P?) e o
   impacto (renumeração? nova Parte?). Se durante a integração a decisão mudar
   (virou seção autônoma, criou Parte nova), ATUALIZE o registro — decisão de
   estrutura sem trilha é como os cursos apodrecem.
4. **Cheque contra a tese** (Princípio 9): conteúdo novo contradiz a linha do
   curso? → callout de desvio explícito ou rótulo de bônus. Nunca em silêncio.
5. Insira/renumere via helper; refs cruzadas por âncora (não por número).
6. **Feche a rodada com o checklist abaixo.** A cada ~3 expansões, rode uma
   rodada de consolidação (Fase 4c completa, com subagente cético).

**Proporcionalidade (para o fluxo não virar burocracia):**
- **Micro-edição** (typo, acento, frase reescrita sem mudar conteúdo factual):
  edite direto + rode `--check`. Sem rodada nova — mas se tocar em NÚMERO, preço
  ou regra, deixa de ser micro.
- **Mudança de conteúdo** (número, regra, recomendação, callout novo, parágrafo
  com fato novo): rodada LEVE — 3 linhas no research-log (o que mudou, por quê,
  fonte) + checagem contra a tese + `--check`. Não precisa re-pesquisar nada.
- **Expansão** (seção nova, vídeo incorporado, reorganização): fluxo completo
  1-6 acima + checklist de fechamento.
Na dúvida, sobe um nível. O barato é registrar; o caro é reconstruir a trilha
seis meses depois.

### Checklist de fechamento de rodada (criação OU expansão)

Uma rodada só está fechada quando TUDO abaixo é verdade:

- [ ] `build_helpers.py --check curso.html` passa (âncoras, contagens, imagens).
- [ ] `build_helpers.py --outline curso.html` == `course-structure.md` (Partes,
      seções, ordem, âncoras). Divergiu → atualizar o structure doc AGORA.
- [ ] `PRD.md` reflete o estado atual: nº de seções/Partes, numeração citada em
      qualquer §, e nenhum dado que uma rodada posterior já desmentiu.
- [ ] Mapa de renumeração do `course-structure.md` registra o remap da rodada
      (ou declara explicitamente "sem reorganização nesta rodada").
- [ ] Rodada no `research-log.md` fechada com: o que entrou, ONDE entrou (decisão
      de colocação final), fontes, e pendências.
- [ ] Conteúdo novo checado contra a tese (desvios têm callout).
- [ ] Nenhum número novo sem fonte no log; nenhum dado pessoal em prompt-modelo.

O curso avança em versões — anote a versão/data no PRD a cada rodada fechada.

## Dependências (o que precisa estar instalado)

Esta skill orquestra outras skills e ferramentas. Verifique ANTES de começar
(e avise o usuário do que falta em vez de travar no meio):

### Skills

| Skill | Para quê | Obrigatória? | Onde encontrar / instalar |
|---|---|---|---|
| **`/watch`** | "Assistir" vídeos (frames + transcript) na Fase 2/2b | Sim, se o curso usa vídeos | github.com/bradautomates/claude-video (MIT) — `git clone` para `~/.claude/skills/watch` |
| **firecrawl** (`firecrawl-search`/`-scrape`) | Busca web com extração de página completa e scrape de fontes oficiais | Não — o WebSearch nativo cobre o essencial | CLI: `brew install firecrawl` (ou npm) + `FIRECRAWL_API_KEY` de firecrawl.dev; skills no marketplace/repo da Firecrawl |

### Ferramentas de linha de comando

| Ferramenta | Para quê | Obrigatória? | Instalar (macOS) |
|---|---|---|---|
| **yt-dlp** | Fase 2b inteira (varredura, legendas, comentários) e o download do `/watch` | Sim, para YouTube | `brew install yt-dlp` |
| **ffmpeg** | Extração de frames do `/watch` | Junto com o /watch | `brew install ffmpeg` |
| **python3** | `build_helpers.py` (checks, outline, renumeração) | Sim | já vem no macOS |
| **playwright** (Python) | Screenshots reais da Fase 5 (desktop/mobile) | Recomendada | `pip3 install playwright && playwright install chromium` — fallback: `chrome --headless=new` |
| **wrangler** | Fase 6 (publicar no Cloudflare Pages) | Só se publicar | `npm i -g wrangler` + `wrangler login` |
| **sips** | Otimizar imagens (Fase 4b) | Só com ilustrações | nativo no macOS (Linux: ImageMagick `convert`) |

### Nativos do Claude Code (nenhuma instalação)

`WebSearch`, `AskUserQuestion`, subagentes (`Agent`/`Task`) — o fan-out de
pesquisa da Fase 2 usa só isso se o firecrawl não estiver disponível.

### Degradação graciosa (sem dependência ≠ travar)

- Sem `yt-dlp` → pule a Fase 2b, avise (`brew install yt-dlp`) e siga com a Fase 2.
- Sem `/watch` → use só legendas/transcrições via yt-dlp (perde a análise de tela).
- Sem firecrawl → WebSearch nativo.
- Sem provedor de imagem → hero de texto (Fase 4b).
- Sem playwright/Chrome → entregue com os checks do helper e avise que o render não foi verificado.
- Sem wrangler → entregue local e documente a Fase 6 como pendência.

## Arquivos desta skill
- `SKILL.md` — este guia.
- `assets/course-theme.css` — o tema completo (cole no `<style>` do HTML).
- `assets/html-template.html` — esqueleto + todos os componentes documentados.
- `assets/build_helpers.py` — renumeração, correção de acentos segura, sanity
  checks, `--outline` (mapa real do HTML p/ diff contra `course-structure.md`).
- `templates/PRD.md`, `course-structure.md`, `reference-matrix.md`, `research-log.md`.
