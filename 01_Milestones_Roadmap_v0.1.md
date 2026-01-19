# Milestones_Roadmap_v0.1

**Project:** UE5 Build & Release Platform (DevOps Portfolio)  
**Goal:** working end-to-end pipeline + documentation (portfolio-ready)

---

## MVP Definition of Done
- [ ] UE5 project builds locally
- [ ] CI builds UE5 project automatically
- [ ] Build artifact is packaged (zip) and downloadable
- [ ] Python tool (`buildctl`) controls build/package/publish flow
- [ ] Minimal infra runs via Docker Compose
- [ ] Infra provisioning/automation uses **Ansible**
- [ ] Monitoring works (Prometheus + Grafana)
- [ ] Demo guide exists (5 min verification)

---

## Bootstrap + UE5 Baseline
**Outcome:** local UE5 build works + repo skeleton + first docs.

- [ ] Create repo layout: `docs/ infra/ tools/ ue/ ansible/`
- [ ] Add minimal UE5 project into `ue/`
- [ ] Local build instructions + prerequisites
- [ ] Decide build target (MVP: Win64)

**Deliverables**
- [ ] [`docs/00_Doc.md`](docs/00_Doc.md)
- [ ] `docs/02_Local_Build_UE5.md`
- [ ] UE5 project builds locally (repeatable)

---

## CI/CD Build + Artifact
**Outcome:** `git push` → CI build → artifact available.

- [ ] Create CI pipeline workflow
- [ ] Build UE5 project on CI runner
- [ ] Package build output into versioned zip
- [ ] Publish artifact (CI artifacts is enough for MVP)

**Deliverables**
- [ ] `docs/03_CICD.md`
- [ ] First CI artifact published and downloadable

---

## Python Tooling (`buildctl`)
**Outcome:** CI uses reusable Python commands instead of ad-hoc scripts.

- [ ] Create Python CLI skeleton in `tools/buildctl/`
- [ ] Implement:
  - [ ] `buildctl build`
  - [ ] `buildctl package`
  - [ ] `buildctl publish`
  - [ ] `buildctl metadata`
- [ ] Generate `build.json` and include it in the artifact
- [ ] Update CI to use `buildctl`

**Deliverables**
- [ ] `docs/04_Python_Tooling.md`
- [ ] `tools/buildctl/` committed and used in CI

---

## Infra + Ansible + Monitoring + Demo
**Outcome:** platform services run + monitored.

- [ ] Create `infra/docker-compose.yml` with:
  - [ ] Prometheus
  - [ ] Grafana
  - [ ] (optional) simple artifact storage service
- [ ] Add minimal Grafana dashboard (basic metrics)
- [ ] Create Ansible playbook to provision/start infra
- [ ] Write runbook + troubleshooting
- [ ] Final demo guide

**Deliverables**
- [ ] `docs/05_Ansible.md`
- [ ] `docs/06_Observability.md`
- [ ] `docs/07_Runbooks.md`
- [ ] `docs/Demo.md`

---
