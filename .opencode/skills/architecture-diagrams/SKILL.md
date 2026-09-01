---
name: architecture-diagrams
description: Create click-through, animated architecture diagrams as single self-contained HTML files.
---

# Architecture Diagrams

## When to Use This Skill
Use when you need to produce interactive architecture diagrams for workshops, design reviews, or onboarding materials. Ideal when static diagrams are insufficient and stakeholders need to watch data flow through a system rather than read static boxes.

## Workflow
1. Gather system context: list services, data stores, external integrations, and the data flows between them.
2. Decide on the narrative: what sequence of events the diagram should animate (e.g., "user signup flow").
3. Create a single self-contained HTML file with embedded SVG for shapes and CSS for styling.
4. Define CSS `@keyframes` animations for each flow segment, sequenced with `animation-delay`.
5. Add click handlers so users can trigger specific flow steps or reset the animation.
6. Label each component with its role and annotate key data transforms at each step.
7. Test the file in isolation (no server required) across Chrome, Firefox, and Safari.

## Rules
- The diagram must be a single HTML file with zero external dependencies.
- Use semantic colors: green for success paths, red for failures, yellow for warnings, blue for external services.
- Every animated flow segment must have a visible label describing the data being transferred.
- Keep the diagram readable at 1280px width minimum.
- Do not embed real credentials, secrets, or internal hostnames in the diagram.
- Provide a static fallback view (all components visible) alongside the animated version.
