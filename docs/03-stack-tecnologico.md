---
title: Stack Tecnologico
status: active
phase: null
owner: andy
last_updated: 2026-09-17
related: []
---


## Frontend & Mobile

- **Framework:** Flutter 3.47.4 / Dart 3.13.3
- **IDE:** Android Studio / VS Code
- **JDK:** OpenJDK 26.0.2.1
- **Android SDK:** API **37** / Build-tools 37.0.0
- **Estado:** Riverpod 3.4.3 / go_router 18.0.1
- **Router app:** `lib/core/router/app_router.dart` (46 tests en verde)
- **Android nativo:** `constraintlayout 2.2.1`, `compileSdk 37`

## Backend & Infraestructura

- **Backend:** Supabase (PostgreSQL 15+) — DECIDIDO NO por ahora;
  solo futuro sync outbox mínimo, sin migrar auth (decisión 2026-09-16)
- **Auth:** local Keystore en Fase 1; Supabase Auth (JWT) diferido a futuro *si se pide*
- **Edge Functions:** Deno
- **Monitoreo:** Sentry + UptimeRobot - *Fase 2*
- **Analytics:** PostHog + Metabase - *Fase 2*

## Capa DePIN & Blockchain

- **L1 Blockchain:** peaq - *Fase 2*
- **Identidad:** peaq ID (DID) - *Fase 2*
- **Pagos:** peaq pay + PayOS - *Fase 2*
- **Almacenamiento:** DeNet (Watcher Node) - *Fase 3*
- **Cómputo:** Acurast (Processor Lite) - *Fase 3*

## SDKs & Librerías Clave

- **Banda:** BrightSDK integrado real y aprobado (AAR en `android/app/libs/`);
  Honeygain y Pawns.app sin contrato. Ganancias solo en dashboard Bright
  (+24h); el SDK no expone API de revenue

- **Servicio:** `flutter_background_service` (foreground + heartbeat 15 min tipo dataSync)
- **Overlay:** burbuja flotante del nodo implementada (arrastrable con snap
  a bordes, doble-tap abre inicio, idle 5 s, toggle en Perfil). Fork
  vendorizado `flutter_overlay_window` 0.5.0 en `plugins/` con `PARCHE.md`
  (app @146ca82)
- **Seguridad:** `flutter_rasp` + `flutter_secure_storage` (Keystore) +
  `sqflite_sqlcipher 3.4.1` (buffer cifrado con migración .bak)
- **Sensores:** `sensors_plus` (streams como funciones; 4 sensores cada 5 s,
  timeout 4 s, anti-solape)
- **Firma release:** pendiente (sigue clave debug, sin R8)
