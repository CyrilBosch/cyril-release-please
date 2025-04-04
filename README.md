# ✨ Cyril Release Please ✨

## 🌟 Overview
This repository provides a simple example to test and implement the [Release Please](https://github.com/googleapis/release-please-action) tool and API from Google.

The workflow is defined in `.github/workflows/release-please.yml`. 🚀 Any push to the `main` branch triggers a pull request to create a release. Once the pull request is merged, the release becomes visible on GitHub and is tagged appropriately.

## ⚙️ Installation
All dependencies are defined in the `pyproject.toml` file. Follow these steps to set up the environment:

1. 🛠️ Create a virtual environment:
    ```bash
    uv venv
    ```
    Alternatively, specify a Python version:
    ```bash
    uv venv --python python3.11
    ```

2. 🔑 Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

3. 📦 Synchronize dependencies:
    ```bash
    uv sync
    ```

## 🧹 Linters
Two linters are configured for this project: **Flake8** and **Ruff**.

### 🐍 Flake8
- GitHub Actions workflow: `.github/workflows/lint.yml`
- To fix issues automatically, use `autopep8`:
  ```bash
  uv pip install autopep8
  autopep8 your_file.py --in-place
  ```

### 🦊 Ruff
- GitHub Actions workflow: `.github/workflows/lint_ruff.yml`
- To check for issues:
  ```bash
  ruff check
  ```
- To fix issues:
  ```bash
  ruff check --fix
  ```
- To format code:
  ```bash
  ruff format
  ```