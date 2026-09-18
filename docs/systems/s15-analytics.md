---
title: Analytics
status: in-progress
phase: 2
owner: andy
last_updated: 2026-09-17
related: []
---

# S15 — Analytics

## Descripción

Analítica del sistema: métricas de dispositivo en app + backend pendiente.

## Estado

- Fase: 2 (alcance local adelantado en app Fase 1, sin backend)
- Estado: En progreso — snapshot local + score + UI en app (@27ce64a); backend/analytics externo pendiente
- Dependencias: (ninguna)
- Bloqueadores: (ninguno)

## Función

Recopilar y visualizar métricas de uso y rendimiento: RAM app/sistema, almacenamiento, sensores disponibles, red (tipo/velocidad/validación), CPU (cores/ABI), batería + score Óptimo/Atención/Crítico. Sin backend ni permisos nuevos (APIs públicas Android).

## Contratos de datos

Snapshot por canal nativo `resourcedigital/device_health` → `getSnapshot()`: `ramAppKb`, `ramSystemTotalKb/FreeKb`, `storageFreeBytes/TotalBytes`, `sensors[]`, `networkType`, `linkSpeedMbps`, `networkValidated`, `cpuCores`, `cpuAbis[]`, `batteryLevel`, `batteryCharging`. UI: chips en Home + sección Dispositivo en Perfil.

## Notas de implementación

Alcance local privacy-first (§5: sin PII, formas agregadas). Histórico 7 días, gráficos y backend (Firebase/Supabase) quedan para Fase 2.
