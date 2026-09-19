---
title: Withdrawals
status: in-progress
phase: 1
owner: andy
last_updated: 2026-09-19
related: []
---

# S11 — Withdrawals

## Descripción

Retiro de ganancias.

## Estado

- Fase: 1
- Estado: En progreso (parcial)
  - ledger local A7 en app (tabla `ledger_entries` append-only, migración
    v1→v2 con semilla, solicitud con mínimo $5, lista con estados;
    commit `bc21089`)
  - sync Supabase en curso: outbox local (DB v3, backoff) + worker push
    a `earnings`/`withdrawals` con mapeo de enums verificado; payouts
    reales pendientes
- Dependencias: S10
- Bloqueadores: ledger A7

## Función

Procesar retiros de ganancias a los usuarios.

## Contratos de datos

(si aplica)

## Notas de implementación

(si aplica)
