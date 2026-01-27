# 03_CICD

This project uses **GitHub Actions** for CI.

---

## Workflows
- **Sanity**: `.github/workflows/sanity_build.yml`
  - Trigger: `push` to `main`, PRs, `workflow_dispatch`
- **UE5 Build**: `.github/workflows/ue5_build.yml`
  - Trigger: `push` to `main`, `workflow_dispatch`

---

## Self-hosted runner (UE5 builds)
UE5 packaging runs on a **self-hosted Windows runner** because Unreal Engine is installed locally on that machine.

Runner name: `fantastic-runner`  
Windows service name:
`actions.runner.mikosz08-fantastic-devops-unreal-engine.fantastic-runner`

### Turn runner OFF / ON (PowerShell)
```powershell
# OFF: stop runner service
Stop-Service -Name "actions.runner.mikosz08-fantastic-devops-unreal-engine.fantastic-runner"

# ON: start runner service
Start-Service -Name "actions.runner.mikosz08-fantastic-devops-unreal-engine.fantastic-runner"

# STATUS: check if it's Running / Stopped
Get-Service -Name "actions.runner.mikosz08-fantastic-devops-unreal-engine.fantastic-runner"
