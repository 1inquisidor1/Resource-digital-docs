---
title: Identidad Visual
status: active
phase: null
owner: andy
last_updated: 2026-09-17
related: [03-stack-tecnologico.md]
---

# 08 — Identidad Visual

> Contrato app≡sitio v1. La app replica estos tokens del sitio
> (`assets/css/styles.css`) en `lib/core/theme/app_theme.dart`.
> No hay divergencia: si el sitio cambia un token, la app debe seguirlo.

## Tokens de color

| Token app | Valor | Token sitio |
|---|---|---|
| `accent` | `#00E5A0` | `--accent` |
| `accentDim` | `#00B884` | `--accent-dim` |
| `bg0` / `bg1` / `bg2` / `bg3` | `#070B14` / `#0D1321` / `#151D2E` / `#1A2540` | `--bg-0…3` |
| `border` / `borderHover` | `#1E2A3A` / `#2A3A52` | `--border…` |
| `text0…text3` | `#F8FAFC` / `#CBD5E1` / `#94A3B8` / `#64748B` | `--text-0…3` |
| `warning` / `danger` / `info` / `future` | `#FBBF24` / `#F87171` / `#60A5FA` / `#A78BFA` | ídem |
| `accentGlow` | `#00E5A0` al 12% | `--accent-glow` |
| `primaryGradient` | acento → info, diagonal | `--gradient-primary` |

## Tipografía y medidas

| Token app | Valor | Token sitio |
|---|---|---|
| `fontSans` / `fontMono` | Inter / JetBrains Mono (empaquetadas) | `--font-sans` / `--font-mono` |
| `toggleDuration` | 350ms | — (solo app) |
| radius / spaces | 16 · 4/6/8/12/16/24 | `--radius-lg` / `--space-*` |

Casos tipográficos cerrados en app: `balanceAmount` (mono 32 w800),
`balanceRate` (mono 12), `statValue` (mono bold), `sectionHeader`
(sans 16 w700). Regla del repo app: prohibido `TextStyle` con
literales fuera de `app_theme.dart`.

## Logo oficial

- Concepto: malla hexagonal (red descentralizada) en `#00E5A0` sobre
  abismo, núcleo hexagonal (continuidad con el logo anterior).
- Fuente: `assets/logo.svg` (+ `logo_fg.svg` sin fondo) en el repo app.
- Launchers Android generados con `flutter_launcher_icons` (no a mano).
- Pendiente: copiar `logo.svg` a los assets del sitio y usarlo como
  favicon/logo donde hoy hay placeholder (`assets/images/favicon.svg`).
- Hecho 2026-09-17: `logo.svg` y `logo-fg.svg` copiados a
  `assets/images/`; `favicon.svg` ahora es el logo oficial (todas las
  páginas lo referencian ya, sin cambios de rutas).
