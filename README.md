# Solar Data Discovery – Week 1 Setup

## Project Overview
This repository contains the starter structure for the MoonLight Energy Solutions solar analytics challenge. The goal is to explore, clean, and compare solar farm datasets across Benin, Sierra Leone, and Togo. Subsequent tasks (EDA, cross-country comparison, dashboard) build on the environment prepared here.

## Environment Setup
Follow these steps to reproduce the development environment:

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/solar-challenge-week1.git
   cd solar-challenge-week1
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Verify CI locally (optional)**
   ```bash
   python --version
   ```

## Repository Structure
```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow (installs deps + checks Python version)
├── .vscode/
│   └── settings.json       # Workspace defaults (venv + pytest target)
├── Assignment.txt          # Challenge brief (not part of submission)
├── data/                   # Raw and cleaned datasets (ignored by git)
├── notebooks/
│   ├── __init__.py
│   └── README.md           # Guidance for notebooks you add per task
├── requirements.txt        # Base Python dependencies
├── scripts/
│   ├── __init__.py
│   └── README.md           # Placeholder docs for automation scripts
├── src/                    # Placeholder for project source code
├── tests/
│   └── __init__.py
└── venv/                   # Local virtual environment (ignored by git)
```

As you proceed with later tasks:
- Keep all CSVs inside `data/`.
- Use feature branches like `eda-benin`, `compare-countries`, and `dashboard-dev`.
- Add notebooks under `notebooks/` and production code under `src/` or `app/`.

## Git Workflow Checklist
- Create branch `setup-task` and make at least three commits (`init: add .gitignore`, `chore: venv setup`, `ci: add GitHub Actions workflow`, etc.).
- Open a pull request into `main`, ensure CI passes, then merge.
- Tag future work to its own branch and PR for clarity.

## Next Steps
- Task 2: Start the EDA notebooks on dedicated branches.
- Task 3: Produce cross-country comparison visuals and summaries.
- Optional bonus: Build the Streamlit dashboard under `app/`.

Good luck with the solar analytics challenge!

