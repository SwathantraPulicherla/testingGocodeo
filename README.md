# Testing C Code

This repository is set up to test C code with automatic test generation, execution, and coverage reporting.

## Project

- `main.c`: Sample C code with an `add` function.
- `test_main.c`: Unit tests using Unity framework.
- `unity/`: Unity testing framework for C unit testing.
- `generate_tests.py`: Script to automatically generate test cases for changed functions.

## Workflow

The workflow in `.github/workflows/test-gocodeo.yml`:
1. Detects changed C files on push.
2. Generates test cases for new/modified functions.
3. Compiles and runs all tests.
4. Generates and uploads coverage reports.

## Test Generation

- Automatic: `generate_tests.py` parses changed C files, identifies functions, and generates Unity test stubs.
- Manual: Additional tests can be added in `test_*.c` files.

For Embedded C, adapt the code and scripts accordingly (e.g., add hardware mocks).This repository is set up to test C code with automatic test generation, execution, and coverage reporting.

## Project

- `main.c`: Sample C code with an `add` function.
- `test_main.c`: Unit tests using Unity framework.
- `unity/`: Unity testing framework.

## Workflow

The workflow in `.github/workflows/test-gocodeo.yml` compiles the code with coverage, runs tests, and reports coverage.

## Test Generation

- Manual unit tests with Unity.
- For automatic generation: Can add fuzzing with AFL or property-based approaches.
