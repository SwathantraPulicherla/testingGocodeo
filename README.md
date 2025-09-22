# testingGocodeo# C Unit Testing with Ceedling, Unity & CMock



A new repository for testing Go code.This repository demonstrates **fully automated** unit test generation and execution for C code with inter-file dependency mocking.

## 🚀 Features

- **Automatic Test Generation**: Tests are auto-generated for new functions on push
- **Dependency Mocking**: CMock isolates unit tests from external dependencies
- **CI/CD Integration**: GitHub Actions runs tests and generates coverage reports
- **Incremental Testing**: New tests append to existing test files

## 📁 Project Structure

- `src/`: Source C files with functions to test
- `test/`: Auto-generated test files (created by CI)
- `include/`: Header files
- `project.yml`: Ceedling configuration with mocking enabled
- `generate_tests.py`: Script that parses C code and generates meaningful tests
- `.github/workflows/ci.yml`: GitHub Actions workflow

## 🔧 How It Works

1. **Add C Functions**: Write functions in `src/*.c` that may call other modules
2. **Push to GitHub**: CI detects new functions and auto-generates tests
3. **Mock Dependencies**: CMock creates stubs for inter-file calls
4. **Run Tests**: Ceedling executes isolated unit tests
5. **Coverage Reports**: lcov generates HTML coverage reports

## 📝 Example

Add a function like:
```c
// src/math_ops.c
int calculate(int a, int b) {
    return add(a, b) * 2;  // Calls add from main.c
}
```

CI auto-generates:
```c
// test/test_math_ops.c
void test_calculate(void) {
    add_ExpectAndReturn(10, 20, 30);  // Mock the dependency
    TEST_ASSERT_EQUAL(60, calculate(10, 20));  // 30 * 2 = 60
}
```

## 🏃‍♂️ Usage

1. Add your C functions to `src/`
2. Push to GitHub
3. Tests run automatically in CI
4. Check Actions tab for results and coverage

No manual test writing required!

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
