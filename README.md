### Backend API (Python / Flask)

A REST API built with Python and Flask that serves mock employee data, supports paginated employee listings and individual employee lookups, and exposes a health-check endpoint. Uses Gunicorn as the production WSGI server and runs inside a Docker container as a non-root user.

### CI/CD & Deployment

- **GitHub Actions:** Automates build, testing, security scanning, and container image publishing.
- **Containerization:** Builds Docker images and publishes them to Azure Container Registry (ACR).
- **Automated Testing:** Runs backend unit tests as part of the CI pipeline.
- **DevSecOps Integration:** Incorporates security checks into CI to identify issues before deployment.
- **Kubernetes / AKS:** Supports deployment as part of the full-stack employee application running on Azure Kubernetes Service (AKS).

### DevSecOps & Security

- **Gitleaks:** Scans for accidentally committed secrets and credentials.
- **Unit Tests:** Validates backend functionality, with 100% test coverage achieved.
- **Semgrep:** Performs static application security testing (SAST).
- **Dependabot:** Detects vulnerable and outdated dependencies and raises update pull requests.
- **Trivy:** Scans container images for known vulnerabilities.

**Security improvements:** Resolved 15 identified vulnerabilities involving mutable container image tags, dependencies with known CVEs, and running containers as root.

## Roadmap

* [x] GitHub OIDC / WIF
* [ ] Support for AWS deployment