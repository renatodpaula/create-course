# PRD — Curso "{{COURSE_TITLE}}"

**Versão:** 1.0
**Data:** {{DATE}}
**Autor/Owner:** {{OWNER}}
**Status:** {{ex: em pesquisa / v1 entregue / documento vivo para expansão}}

> **Documento vivo — a cada nova fonte pesquisada ou rodada de expansão, atualize `research-log.md` e `reference-matrix.md`** (e `course-structure.md` quando uma seção mudar).

---

## 1. Visão geral

{{Parágrafo: o que o curso ensina, para quem, e qual transformação promete. Uma frase-promessa clara.}}

**Entregável:** `{{slug}}.html` — arquivo único, canônico nesta pasta.

### Público-alvo
{{Quem é o aluno: nível, contexto, idioma. Do iniciante ao avançado, se aplicável.}}

### Princípios de conteúdo (regras do projeto)
- **Explicar o "porquê" (princípio central):** todo passo/regra traz o objetivo E a explicação do motivo por trás (componente `.why-box`). O aluno entende, não decora.
- **Honestidade:** sempre incluir limitações reais, custos reais e avisos legais. Não vender hype.
- **Organizar por CAMINHOS/CONCEITOS, não por ferramentas:** a espinha do curso são as decisões e métodos; ferramentas entram a serviço deles.
- **Ortografia completa e correta** no idioma-alvo — todos os acentos. Nunca trocar acentuados por ASCII.
- **Tema visual:** dark, fonte Inter, grids de colunas fixas (nunca `auto-fill` que gere linhas órfãs). Sem emojis em texto corrido (apenas como ícones de card, se combinado).

---

## 2. Estrutura atual do curso ({{N}} seções, {{P}} Partes)

{{Tabela: Parte | # | Seção | Status. Detalhes completos em `course-structure.md`.}}

| Parte | # | Seção | Status |
|---|---|-------|--------|
| **1 {{título}}** | 01 | {{...}} | — |

---

## 3. Decisões editoriais-chave (e o porquê)

{{Lista numerada das decisões de conteúdo que definem o curso, cada uma com a justificativa. Ex.: por que tal tópico é seção separada; qual a recomendação principal e por quê; o que entra como "bônus" vs "núcleo".}}

---

## 4. Referências mapeadas (resumo executivo)

Matriz completa em `reference-matrix.md`. Resumo por categoria:

{{Blocos por categoria com os itens principais — nome, preço/tier, prós, contras, disponibilidade no idioma-alvo.}}

---

## 5. Fontes analisadas

{{Método de pesquisa e principais fontes. Vídeos analisados (via /watch) em tabela: ID | canal | tema | incorporado em. URLs completas em `research-log.md`.}}

---

## 6. Aprendizados-chave (conhecimento destilado)

{{O conhecimento não-óbvio extraído da pesquisa, agrupado por tema. É o diferencial do curso — o que um leigo não acharia sozinho.}}

---

## 7. Lições técnicas de produção do HTML (para quem continuar)

- **Grids:** colunas fixas (`repeat(N,1fr)`) que batam com a contagem de itens. `auto-fill + minmax` gera linhas órfãs.
- **Acentuação:** correções em massa via script Python que só altera texto entre tags (`re.split(r'(<[^>]+>)')`) — nunca tocar em nomes de classe/atributos.
- **Renumeração de seções:** ao inserir no meio, renumerar todos os `section-label` por ordem do DOM, reescrever TOC + nav, atualizar refs cruzadas "Seção N". Verificar: `<section>` abre==fecha, TOC==nº seções, âncoras únicas.

---

## 8. Roadmap futuro

{{Áreas candidatas a aprofundar; expansões planejadas; possível migração de formato.}}

---

## 9. Estado e próximos passos imediatos

- [ ] {{...}}

---

## Arquivos deste diretório
- `PRD.md` — este documento.
- `{{slug}}.html` — o curso completo (entregável canônico).
- `course-structure.md` — detalhamento seção a seção.
- `reference-matrix.md` — matriz de ferramentas/fontes (preços, prós, contras, disponibilidade).
- `research-log.md` — log de pesquisa: fontes, queries, achados brutos, rodadas.
