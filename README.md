# C Unit Testing with Ceedling# Testing C Code



This repository demonstrates automatic unit test generation and execution for C code using Ceedling, Unity, and CMock.This repository is set up to test C code with automatic test generation, execution, and coverage reporting.



## Project Structure## Project

- `src/`: Source C files (e.g., `main.c`)

- `test/`: Test files (e.g., `test_main.c`)- `main.c`: Sample C code with an `add` function.

- `include/`: Header files (e.g., `main.h`)- `test_main.c`: Unit tests using Unity framework.

- `mocks/`: Auto-generated mock files- `unity/`: Unity testing framework for C unit testing.

- `project.yml`: Ceedling configuration- `generate_tests.py`: Script to automatically generate test cases for changed functions.

- `.github/workflows/ci.yml`: GitHub Actions for CI

## Workflow

## Features

- **Automatic Test Execution**: On push/PR, Ceedling compiles, runs tests, and generates coverage.The workflow in `.github/workflows/test-gocodeo.yml`:

- **Mocking**: CMock generates mocks for dependencies (e.g., external functions).1. Detects changed C files on push.

- **Coverage**: gcov/lcov for detailed reports.2. Generates test cases for new/modified functions.

- **Embedded C Ready**: Supports mocking hardware interfaces.3. Compiles and runs all tests.

4. Generates and uploads coverage reports.

## Setup Locally

1. Install Ruby and GCC: `sudo apt update && sudo apt install -y ruby gcc lcov`## Test Generation

2. Install Ceedling: `gem install ceedling`

3. Run tests: `ceedling test:all`- Automatic: `generate_tests.py` parses changed C files, identifies functions, and generates Unity test stubs.

4. Generate coverage: `lcov --capture --directory build/test/out/ --output-file coverage.info && genhtml coverage.info --output-directory coverage`- Manual: Additional tests can be added in `test_*.c` files.



## WorkflowFor Embedded C, adapt the code and scripts accordingly (e.g., add hardware mocks).This repository is set up to test C code with automatic test generation, execution, and coverage reporting.

1. Push C code changes.

2. Ceedling detects changes, generates mocks if needed, compiles with coverage.## Project

3. Runs tests and uploads coverage to Codecov.

- `main.c`: Sample C code with an `add` function.

## Adding Tests- `test_main.c`: Unit tests using Unity framework.

- Write tests in `test/` using Unity macros (e.g., `TEST_ASSERT_EQUAL`).- `unity/`: Unity testing framework.

- Ceedling handles the rest.

## Workflow

For inter-file dependencies, CMock auto-mocks them for isolated testing.
The workflow in `.github/workflows/test-gocodeo.yml` compiles the code with coverage, runs tests, and reports coverage.

## Test Generation

- Manual unit tests with Unity.
- For automatic generation: Can add fuzzing with AFL or property-based approaches.
