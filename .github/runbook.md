# Runbook

Operational procedures for the `ring-seq-py` package.

## First-time setup

These steps are performed once, before the first release.

### 1. Create a PyPI account

1. Go to [pypi.org](https://pypi.org) and register (or log in).
2. Enable 2FA on the account — PyPI requires it for any project with an
   uploaded release.

### 2. Configure Trusted Publishing on PyPI

PyPI's **Trusted Publishing** lets GitHub Actions authenticate via OIDC —
no API tokens to store, no secrets to rotate.

1. On PyPI, open the project (or its **"pending publishers"** page if the
   project does not yet exist): **Publishing** > **Add a new pending
   publisher** (or **Add** on an existing project).
2. Fill in:
   - **PyPI Project Name**: `ring-seq-py`
   - **Owner**: `scala-tessella`
   - **Repository name**: `ring-seq-py`
   - **Workflow name**: `publish.yml`
   - **Environment name**: `pypi`
3. Save.

### 3. Create the `pypi` environment on GitHub

1. Go to the repository > **Settings** > **Environments** > **New
   environment**.
2. Name it `pypi` (must match the workflow's `environment:` key and the
   PyPI trusted-publisher configuration).
3. Optionally add protection rules (required reviewers, or restrict
   deployments to tag refs matching `v*`).

## Publishing a release

### What happens

```
v2.1.0 tag pushed
  |
  +---> publish.yml: verify tag v2.1.0 == pyproject.toml version 2.1.0
  |       |
  |       v matches
  |
  +---> Run tests (pytest)
  |       |
  |       v pass
  |
  +---> Build sdist + wheel (python -m build)
  |       |
  |       v success
  |
  +---> Upload via OIDC trusted publishing --> package live on PyPI
  |
  +---> site.yml (in parallel): mkdocs gh-deploy --> docs site updated
```

### Steps

1. **Bump the version** in `pyproject.toml`:

   ```toml
   version = "2.1.0"
   ```

2. **Update `CHANGELOG.md`** — add a new dated section describing the
   release.

3. **Commit and push** to `master`:

   ```bash
   git add pyproject.toml CHANGELOG.md
   git commit -m "Bump version to 2.1.0"
   git push origin master
   ```

4. **Tag and push** the tag:

   ```bash
   git tag v2.1.0
   git push origin v2.1.0
   ```

The release workflow (`.github/workflows/publish.yml`) takes care of the
rest, and `.github/workflows/site.yml` deploys the docs in parallel.

### Safeguards

- `publish.yml` re-runs the full test suite on Python 3.12 before building,
  independent of the `python-package` CI that runs on pushes and PRs.
- The workflow verifies that the Git tag matches the version in
  `pyproject.toml`. A mismatch fails the pipeline before anything is
  uploaded.
- Publishing uses OIDC Trusted Publishing — no long-lived API tokens are
  stored in GitHub secrets.
- The `pypi` environment can be configured with required reviewers to make
  every release a manual approval step.

## CI overview

The CI workflow (`.github/workflows/python-package.yml`) runs on every push
to `master` and on every pull request.

| Job | What it checks | Runs on |
|---|---|---|
| **Ruff lint** | `ruff check .` | Ubuntu, Python 3.12 |
| **Ruff format** | `ruff format --check .` | Ubuntu, Python 3.12 |
| **Tests** | `pytest tests/AllTest.py` | Ubuntu × Python 3.10 – 3.14 |

In addition:

- `.github/workflows/site.yml` deploys the mkdocs site on any `v*` tag push.
- `.github/workflows/publish.yml` publishes to PyPI on any `v*` tag push.

## Routine maintenance

### Updating the minimum Python version

1. Change `requires-python` in `pyproject.toml`.
2. Change `target-version` under `[tool.ruff]` in `pyproject.toml`
   (e.g. `py310` → `py311`).
3. Drop the EOL version from the matrix in
   `.github/workflows/python-package.yml`.
4. Update the "Working for Python `3.X` and above" line in `README.md`.

### Running the full CI checks locally

```bash
ruff check .
ruff format --check .
pytest tests/AllTest.py
```

On Debian/Ubuntu, install `ruff` once via `pipx install ruff` to avoid the
PEP 668 "externally managed environment" error.

### Building and previewing docs locally

```bash
pip install mkdocs-material "mkdocstrings[python]"
mkdocs serve
```

Open <http://127.0.0.1:8000/> in a browser to preview.

### Keeping GitHub Actions fresh

Watch for Node.js deprecation warnings in CI runs and bump action versions
(`actions/checkout`, `actions/setup-python`, `actions/cache`,
`pypa/gh-action-pypi-publish`) when new majors land. Dependabot or Renovate
can automate this.
