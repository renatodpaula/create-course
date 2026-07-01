# create-course

*[Ler em português](README.pt-BR.md)*

A Claude Code skill that **builds a complete course from scratch** and delivers
a single, navigable HTML file — the same way the "Clone Digital" course was
produced.

**Flow:** interview (`AskUserQuestion`) → deep research with parallel agents
(WebSearch/firecrawl + the `/watch` skill for videos) → living PRDs (PRD,
structure, reference matrix, research log) → `curso.html` (inline CSS,
**dark or light** theme, **hero opening photo**, signature `.why-box`
component) → consistency pass → sanity checks + real render → optional
publishing (Cloudflare Pages).

**Principles:** explain the "why"; honesty (real costs/limits/legal notes);
organize by paths, not tools; living documents; source rigor; lean (no padding
or scarecrow numbers); internal consistency (no contradictions).

## Install
Symlink or copy it into wherever Claude Code reads skills from, e.g.:
```
ln -s ~/Projetos/skills/create-course ~/.claude/skills/create-course
```
Then invoke with `/create-course` or ask to "create a course about X".

## Files
- `SKILL.md` — the guide (interview → research → PRDs → HTML/illustrations/consistency → verify → publish).
- `assets/course-theme.css` — the full theme (paste into `<style>`); dark/light presets, fonts and hero as variables.
- `assets/html-template.html` — skeleton + documented components (full-bleed hero with photo).
- `assets/build_helpers.py` — renumbering, safe accent fixes, checks (`--check`, `--assets`, `--anchors`, `--renumber`).
- `templates/*.md` — the four PRDs.

Full documentation: [this repo's wiki](https://github.com/renatodpaula/create-course/wiki).

## Author
Renato dPaula — [@renatodpaula.ai](https://renatodpaula.ai)
