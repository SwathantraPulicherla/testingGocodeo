# Developer Repository with Universal C Test Generator

This repository demonstrates how a C developer can use the **Universal C Test Generator** to automatically generate comprehensive unit tests using AI.

## 🎯 What is the Universal C Test Generator?

The Universal C Test Generator is an AI-powered system that:
- Analyzes your C source code
- Automatically generates comprehensive unit tests
- Provides build systems and testing frameworks
- Integrates seamlessly with GitHub Actions

**Repository**: [Gemini-Agent-and-api](https://github.com/SwathantraPulicherla/Gemini-Agent-and-api)

## � Repository Structure (Developer View)

```
your-c-project/
├── src/                    # Your C source code goes here
│   ├── your_module.c
│   ├── your_module.h
│   └── main.c
├── scripts/               # AI test generation scripts
│   └── ai_test_generator.py
├── .github/
│   └── workflows/         # CI/CD automation
│       └── ai-test-generation.yml
└── README.md
```

## 🚀 Workflow

### 1. Write Your Code
Add your C source files to the `src/` directory:

```c
// src/temperature_sensor.c
#include <stdio.h>

float get_temperature(void) {
    // Your temperature sensor logic
    return 25.5f;
}
```

### 2. Trigger AI Test Generation
- **Create an issue** with title containing "generate test" and label `ai-test-generation`
- **Or run workflow manually** from GitHub Actions tab

### 3. What Happens Automatically
The Universal C Test Generator will:
- ✅ Clone the test generator repository
- ✅ Copy build systems (CMake/Makefile) and testing framework (Unity)
- ✅ Analyze your source code in `src/`
- ✅ Generate comprehensive unit tests using Gemini AI
- ✅ Create `tests/generated/generated_tests.c`
- ✅ Build and run the tests
- ✅ Commit everything back to your repository

### 4. Review Results
After the workflow completes, you'll have:
- Complete test suite in `tests/generated/`
- Build system (Makefile/CMakeLists.txt)
- Unity testing framework
- All tests passing ✅

## 🔧 Requirements

- **GitHub Repository** with Actions enabled
- **Gemini API Key** set as repository secret `GEMINI_API_KEY`
- **C Source Code** in `src/` directory

## 🎯 Benefits

- **Zero Test Writing**: AI generates all tests automatically
- **Comprehensive Coverage**: Tests all functions, edge cases, and error conditions
- **CI/CD Ready**: Automated testing in your pipeline
- **Framework Agnostic**: Works with any C codebase
- **Time Saving**: Focus on code, let AI handle testing

## 📋 Example Generated Tests

The AI will create tests like:

```c
void test_get_temperature_range(void) {
    float temp = get_temperature();
    TEST_ASSERT_TRUE(temp >= -40.0f && temp <= 125.0f);
}

void test_edge_cases(void) {
    // AI finds and tests boundary conditions
    TEST_ASSERT_TRUE(validate_range(-40.0f));  // Min valid
    TEST_ASSERT_FALSE(validate_range(-41.0f)); // Below min
}
```

## � Getting Started

1. **Clone this template** or create your repository structure
2. **Add your C code** to `src/`
3. **Set up Gemini API key** in repository secrets
4. **Create an issue** or run workflow to generate tests
5. **Review and iterate** on the AI-generated tests

The Universal C Test Generator transforms C development by making testing automatic, allowing developers to focus on writing quality code while ensuring robust test coverage.
