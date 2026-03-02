# Diagrams (Playbooks Repo)

This repo supports **diagram-as-code** for decision trees, quick reference flows, and architectural overviews.

## Preferred formats

- **Mermaid** (`.mmd`) — flowcharts/sequence/state diagrams
- **Graphviz** (`.dot`) — graphs, dependency maps, and alternate flow representations

When adding a diagram, commit both:
1) the **source file** (`.mmd` or `.dot`), and
2) an exported **PNG** (and/or SVG) for easy viewing on GitHub.

## Local tooling (macOS)

Installed:
- Mermaid CLI: `mmdc`
- Graphviz: `dot`

### Mermaid → PNG

```bash
mmdc -i docs/images/diagram.mmd -o docs/images/diagram.png --backgroundColor white --scale 2
```

### Graphviz → PNG

```bash
dot -Tpng docs/images/diagram.dot -o docs/images/diagram.png
```

## Repo convention

Store diagrams in:
- `docs/images/`

Name:
- `kebab-case` and descriptive (e.g., `containment-decision-tree.png`)
