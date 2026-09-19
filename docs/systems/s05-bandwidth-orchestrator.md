---
title: Bandwidth Orchestrator
status: done
phase: 1
owner: andy
last_updated: 2026-09-16
related: []
---

# S05 — Bandwidth Orchestrator

## Descripción

Orquestador que decide qué SDK de banda ancha corre y cuándo, según consentimiento y red.

## Estado

- Fase: 1
- Estado: Completado (mínimo real)
  - BrightSDK integrado real y aprobado, AAR en android/app/libs/,
    diálogo verificado en físico (app commits 93b4f2f+6450122)
  - Solo Wi-Fi, opt-out en perfil. Ganancias solo en dashboard Bright
    (+24h); el SDK no expone API de revenue
- Dependencias: S02, S10
- Bloqueadores: Honeygain/Pawns sin contrato; Reporting API Bright
  pendiente de pedir a su manager para revenue real en app

## Función

Gestionar la compartición de ancho de banda usando Honeygain, Pawns y BrightSDK.
Solo comparte con Wi-Fi y consentimiento activo; nunca usa datos móviles sin permiso.

## Contratos de datos

- Entrada: consentimiento del usuario (S10), estado de red (Wi-Fi/móvil).
- Salida: GB compartidos y eventos de ingreso hacia `earnings` con `source: bandwidth`.

## Notas de implementación

- Un solo SDK activo a la vez; rotación configurable por S17.
- Pausa automática sin Wi-Fi o con batería baja (vía S02).
