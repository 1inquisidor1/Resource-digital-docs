---
title: Foreground Service
status: done
phase: 1
owner: andy
last_updated: 2026-09-17
related: []
---

# S02 — Foreground Service

## Descripción

Servicio en primer plano para Android.

## Estado

- Fase: 1
- Estado: Completado
  - foreground persistente + heartbeat 15 min tipo dataSync (Android 14+)
  - overlay burbuja flotante (servicio specialUse, permiso
    SYSTEM_ALERT_WINDOW, fork vendorizado flutter_overlay_window 0.5.0
    con PARCHE.md, notificación silenciosa IMPORTANCE_LOW con botón
    Desactivar; app @146ca82)
- Dependencias: S10
- Bloqueadores: (ninguno)

## Función

Mantener el servicio activo en background con notificación persistente.

## Contratos de datos

(si aplica)

## Notas de implementación

(si aplica)
