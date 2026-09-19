---
title: SQLite Buffer
status: done
phase: 1
owner: andy
last_updated: 2026-09-19
related: []
---

# S04 — SQLite Buffer

## Descripción

Buffer local con SQLite.

## Estado

- Fase: 1
- Estado: Completado (adelantado Fase 2)
  - SQLite cifrado SQLCipher, clave en Keystore, migración automática
    con .bak (app commit 6c57ab0)
  - v3 suma tabla `outbox` genérica (idempotente, backoff 1m→1h) para
    el sync Supabase
- Dependencias: S10
- Bloqueadores: (ninguno)

## Función

Almacenar datos localmente en SQLite antes de enviarlos al backend.

## Contratos de datos

(si aplica)

## Notas de implementación

(si aplica)
