---
title: Auth and Registry
status: done
phase: 1
owner: andy
last_updated: 2026-09-19
related: []
---

# S10 — Auth and Registry

## Descripción

Autenticación y registro de usuarios.

## Estado

- Fase: 1
- Estado: Completado
  - auth local Keystore (login/registro/consentimiento/splash+gate).
    Logout frena sharing (detiene servicio + revoca banda, P0-4)
  - Fase 2 en curso en app: Supabase Auth anónimo por dispositivo +
    vínculo Google (`linkIdentityWithIdToken`, sin duplicar nodo)
    verificados contra nube; sesión en Keystore, claves por
    `--dart-define`
- Dependencias: (ninguna)
- Bloqueadores: (ninguno)

## Función

Gestionar registro, login y autenticación de usuarios.

## Contratos de datos

(si aplica)

## Notas de implementación

(si aplica)
