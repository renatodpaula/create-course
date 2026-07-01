<div align="center">

# create-course

**A Claude Code skill that turns a research topic into a finished course.**

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-6366f1)](https://github.com/renatodpaula/create-course)
[![Docs](https://img.shields.io/badge/docs-wiki-6366f1)](https://github.com/renatodpaula/create-course/wiki)
[![Author](https://img.shields.io/badge/author-Renato%20dPaula-6366f1)](https://renatodpaula.ai)

*[Ler em português](README.pt-BR.md)*

</div>

---

`create-course` interviews you about scope and audience, researches the topic
in depth with parallel agents, keeps everything in living PRD documents, and
delivers a single self-contained HTML course — the same process used to build
the "Clone Digital" course.

## How it works

| Step | What happens |
|---|---|
| **1. Interview** | `AskUserQuestion` nails down topic, audience, depth, language, brand, and image-generation provider. |
| **2. Research** | 4–8 parallel agents fan out across WebSearch/firecrawl (+ `/watch` for videos), cross-checking claims before they get written down. |
| **3. Living PRDs** | Findings land in four structured docs — vision, structure, reference matrix, research log — that stay up to date as the course grows. |
| **4. Build HTML** | A single `curso.html`: inline CSS, dark or light theme, `.why-box` signature component, hero photo. |
| **5. Consistency pass** | A full reread hunting contradictions, absolute claims the course later disproves, and padding. |
| **6. Verify** | Structural sanity checks + real browser renders at desktop and mobile viewports. |
| **7. Publish** *(optional)* | Deploy to Cloudflare Pages with a custom domain. |

## Principles

- **Explain the "why"** — every rule ships with the reasoning behind it.
- **Honesty over hype** — real costs, real limits, dated sources.
- **Paths, not tools** — organize around the decision the learner faces.
- **Living document** — the course is versioned, never "finished".
- **Lean** — no padding, no scarecrow numbers, no filler boxes.
- **Internally consistent** — no section contradicts another.

## Install

Symlink or copy it into wherever Claude Code reads skills from:

```bash
ln -s ~/Projetos/skills/create-course ~/.claude/skills/create-course
```

Then invoke with `/create-course`, or just ask to "create a course about X".

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | The full guide — interview → research → PRDs → HTML/illustrations/consistency → verify → publish. |
| `assets/course-theme.css` | Complete theme (paste into `<style>`); dark/light presets, fonts and hero as CSS variables. |
| `assets/html-template.html` | Skeleton with every component documented, including the full-bleed photo hero. |
| `assets/build_helpers.py` | Renumbering, safe accent fixes, and structural checks (`--check`, `--assets`, `--anchors`, `--renumber`). |
| `templates/*.md` | The four living PRDs. |

Full documentation, including HTML component reference and the publishing
guide: **[project wiki](https://github.com/renatodpaula/create-course/wiki)**.

## Author

**Renato dPaula** — [@renatodpaula.ai](https://renatodpaula.ai)
