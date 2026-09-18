---
title: Hoja de Ruta
status: active
phase: null
owner: andy
last_updated: 2026-09-17
related: []
---


## Fase 1: Pre-Beta Infraestructura Core (v5.1 ALPHA)

**Objetivo:** Preparación e integración de MVP para validación en Ecuador.

- **Semana 1:** Configuración entorno + Aprobación SDKs de Banda (Honeygain/Pawns).
- **Semana 2:** UI + Integración SDK de Banda + Auth Local.
- **Semana 3:** Servicio Foreground + Overlay + Notificaciones locales.
- **Semana 4:** Validación Interna (5-10 usuarios beta en Ecuador).

**Estado real 2026-09-16:** S01/S02/S10/S12 done; S05 done mínimo real con BrightSDK aprobado (Honeygain/Pawns sin contrato); S11 parcial (solo mock, ledger A7 pendiente); S16 parcial (solo consentimiento+toggles); firma release pendiente (clave debug, sin R8).

**Actualización 2026-09-17:** overlay burbuja flotante implementado en app (@146ca82, fork vendorizado + PARCHE.md); identidad visual v1 cerrada (contrato app≡sitio en `08-identidad-visual.md`); logo malla hexagonal; S15 local (métricas dispositivo + score en Home/Perfil, app @27ce64a); reorganización UI por secciones con slots A7/S16; release arm64 35.4MB (arranque 1.1s vs 10.3s debug).

## Fase 2: Capa DePIN con peaq (Semanas 5-8)

**Objetivo:** Diferenciación tecnológica, backend y descentralización.

- **Semana 5:** peaq SDK (Identidad + peaq pay) + Supabase Auth.
- **Semana 6:** Sensores + Buffer Local + Analytics + Motor de Reparto Central.
- **Semana 7:** Retiros (Requiere configuración de cuentas PayPal/Banco).
- **Semana 8:** Panel Admin + Monitoreo.

**Estado real 2026-09-16:** S04 done (SQLite cifrado SQLCipher) y S03 done (4 sensores cada 5 s) adelantados de Fase 2; Supabase DECIDIDO NO por ahora (solo futuro sync outbox mínimo sin migrar auth); auditoría P0+P1 aplicada, quedan P2 y firma release.

## Fase 3: Ecosistema Completo (Semanas 9+)

**Objetivo:** Fuentes de ingreso de alto valor.

- **Semana 9:** Integración DeNet (Almacenamiento) + Acurast (Cómputo).
- **Semana 10:** PayOS + Feature Flags.
- **Semana 11:** Hardening de Seguridad (RASP, Pinning).
- **Semana 12:** Beta Ampliada (50 usuarios) y métricas finales.

**Pendiente app:** ledger A7, textos S16, firma release (keystore del owner), beta 5-10 usuarios, Honeygain/Pawns, Reporting API Bright (pedir a su manager).
