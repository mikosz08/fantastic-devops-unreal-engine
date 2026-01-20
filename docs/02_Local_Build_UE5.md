# 02_Local_Build_UE5

**Project path:** `ue/FantasticUE5/FantasticUE5.uproject`  
**Target (MVP):** Windows (Win64)  
**Goal:** repeatable local package build

---

## Prerequisites (Windows)
- Unreal Engine 5 installed
- Visual Studio 2022 (Desktop development with C++)

---

## Build steps (baseline)
1. Open:
   - `ue/FantasticUE5/FantasticUE5.uproject`
2. (Recommended) Project Settings → Maps & Modes:
   - Set default map to `MainMap`
3. Package:
   - **Platforms → Windows → Package Project**
4. Pick output directory:
   - example: `output/local-win64/`

---

## Clean rebuild check
To verify the build is repeatable:

1. Close Unreal Editor
2. Delete (generated folders):
   - `ue/FantasticUE5/Saved/`
   - `ue/FantasticUE5/Intermediate/`
3. Package again to a new folder:
   - `output/local-win64-run2/`

Expect: **Build successful** and output `.exe` runs.

---

## Notes
Ray tracing is disabled for MVP.
