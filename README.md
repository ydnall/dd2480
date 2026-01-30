# DD2480: Assignment 1 - Launch Interceptor Program

This repository contains the implementation of the DECIDE program and its tests.

This “Launch Interceptor Program” determines whether an interceptor should be launched based upon input radar tracking information.
The main backbone of this program is the DECIDE()-function, which will output a boolean launch decision, "YES" or "NO", based on our input data. Given a set of data points and a set of parameters, the program evaluates 15 Launch Interceptor Conditions (LIC0–LIC14), combines LCM and CMV in the Preliminary Unlocking Matrix (PUM),  to produce the final LAUNCH decision.

## Requirements

- Python 3.10+
- Docker 20.10.0+ (Industry standard minimum recommendation)

### Hardware requirements

The program is written in pure Python, without dependencies that require certain architectures or operating systems. Therefore, as long as Python can be run on a machine, it can run this program. Some valid examples are:

- Operating systems: Linux, Windows, MacOS.
- Architectures: x86/x64, ARM64.

## Run program

There are two supported ways to run the code.
First, you can use Docker from the repository root to build and run a containerized version of the project.

### 1. Quick start (Docker)

```
docker build -t dd2480 .
docker run --rm dd2480
```

Second, you can run locally using a Python virtual environment. From inside assignment1/, create and activate a venv, install dependencies, and run the tests:

### 2. Local setup (venv)

```
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest
```

## Run tests (venv)

```
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest
```

## CI

GitHub Actions runs tests and linting on pushes and pull requests to `main` using Python 3.10.

## Statement of contributions

- Sumeya Yasir Isse (sumeyayasir): Made the solutions and ran tests for LIC 3, 4, 5; implemented FUV.

- Yiqin Lin (Potoqin): Made the solutions and ran tests for LIC 9, 10, 11; wrote README/documentation.

- Emma Lindblom (emmalindblm): Made the solutions and ran tests for LIC 6, 7, 8; organized group and kept track of grading criteria.

- Andy Li (ydnall): Made the solutions and ran tests for LIC 12, 13, 14; implemented CMV, **init**.py, and the top-level decide integration.

- Martin Zivojinovic (ZivoMartin): Made the solutions and ran tests for LIC 0, 1, 2; implemented PUM.

## Way of working (Essence self-assessment)

- We structured the work using GitHub Issues and feature branches. Each Launch Interceptor Condition (LIC) was tracked as its own issue, and each member implemented their assigned LICs on a separate branch linked to that issue. Changes were integrated through pull requests, which required other group members to review before merging into the main branch.
  This helped keep the main branch clean and ensured that each merge represented a small, traceable change (an atomic commit). With the discussions and review history preserved in its corresponding PR.

Right now, we consider our way of working to be “Foundation Established”. This is because we delegate clear tasks from the start, and we integrate regularly through reviewed PRs. However, since the project has only been running for a short time, it is not realistic to claim that the workflow is at higher states of way-of-working. To move towards higher states, our next step is to apply this workflow consistently for every change ie always work via their respective issues and branches, always open a PR with review, and treat test cases as part of “done” before merging.

## License

See [LICENSE](../LICENSE).
