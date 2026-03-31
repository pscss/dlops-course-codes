# DLOps Course Codes

DLOps course codes and notebooks — IIT Jodhpur M.Tech AI (M22AIE215)

## Tech Stack

- **Python** 3.12
- **Package Manager:** uv
- **Deep Learning:** PyTorch 2.11.0 (CUDA 13.0, cuDNN 9.19)
- **Task Runner:** poethepoet
- **Linting & Formatting:** ruff
- **Type Checking:** mypy
- **Testing:** pytest + coverage
- **Pre-commit Hooks:** trailing whitespace, end-of-file fixer, yaml check, large file check, merge conflict check, ruff

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed globally
- NVIDIA GPU with CUDA support (for PyTorch GPU acceleration)

### Installation

```bash
# Clone the repository
git clone https://github.com/pscss/dlops-course-codes.git
cd dlops-course-codes

# Install all dependencies (creates .venv automatically)
uv sync

# Install pre-commit hooks
uv run poe develop
```

### Environment Variables

Project environment variables are stored in `.env` (not committed to git). Create your own:

```bash
cat > .env << 'EOF'
PROJECT_NAME=dlops-course-codes
CUDA_VISIBLE_DEVICES=0
PYTHONPATH=.
TORCH_HOME=.cache/torch
EOF
```

These are automatically loaded by `uv run` and `poe` tasks.

## Daily Workflow

### Running Code

```bash
# Run any Python script
uv run python <script.py>

# Run Jupyter notebook server
uv run jupyter notebook
```

### Task Runner Commands

All tasks are defined in `pyproject.toml` under `[tool.poe.tasks]` and run via `uv run poe <task>`.

| Command | What it does |
|---|---|
| `uv run poe develop` | Install pre-commit hooks |
| `uv run poe test` | Run tests with coverage tracking |
| `uv run poe coverage` | Show coverage report in terminal |
| `uv run poe coverage-html` | Generate HTML coverage report in `coverage/` |
| `uv run poe lint` | Check code for lint errors |
| `uv run poe format` | Auto-format all Python files |
| `uv run poe fix` | Auto-fix lint errors where possible |
| `uv run poe sort` | Sort import statements |
| `uv run poe type-check` | Run static type checking with mypy |
| `uv run poe check` | Run lint + type-check + test (all checks) |
| `uv run poe pre-commit-check` | Run all pre-commit hooks on all files |

### Managing Dependencies

```bash
# Add a production dependency
uv add <package>

# Add a dev-only dependency
uv add --dev <package>

# Remove a dependency
uv remove <package>

# Sync environment from lockfile (after pulling changes)
uv sync
```

### Pre-commit Hooks

Hooks run automatically on every `git commit`. They check:

- Trailing whitespace in `.py` files
- Missing newline at end of `.py` files
- Valid YAML syntax
- No accidentally committed large files (>500KB, excludes notebooks)
- No leftover merge conflict markers
- Ruff linting and formatting

To run hooks manually on all files:

```bash
uv run poe pre-commit-check
```

## Project Structure

```
dlops-course-codes/
├── .env                        # Environment variables (not committed)
├── .gitignore
├── .pre-commit-config.yaml     # Pre-commit hook configuration
├── .python-version             # Python version pin (3.12)
├── .vscode/
│   └── settings.json           # VS Code workspace settings
├── notebooks/                  # Course notebooks with outputs
├── tests/
│   ├── __init__.py
│   └── test_setup.py           # Setup verification tests
├── pyproject.toml              # Project config, dependencies, tool settings
├── uv.lock                     # Locked dependency versions
└── README.md
```

## GPU Verification

```bash
uv run python -c "
import torch
print('PyTorch:', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
print('CUDA version:', torch.version.cuda)
print('cuDNN version:', torch.backends.cudnn.version())
print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A')
"
```

## CI/CD

> **TODO:** GitHub Actions pipeline for automated testing, linting, and type checking on push/PR.
