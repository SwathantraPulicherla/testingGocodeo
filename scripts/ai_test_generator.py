#!/usr/bin/env python3
import google.generativeai as genai
import os
import glob
import argparse
from pathlib import Path
import re

def read_source_files(source_dir="."):
    """Read all C source files from the source directory"""
    source_code = ""
    
    # Look for C files in the repository root
    c_files = glob.glob("*.c")
    h_files = glob.glob("*.h")
    
    print(f"Found {len(c_files)} C files and {len(h_files)} header files")
    
    # Read header files first
    for file_path in h_files:
        try:
            with open(file_path, 'r') as f:
                source_code += f"// Header: {file_path}\n{f.read()}\n\n"
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    # Read C source files
    for file_path in c_files:
        try:
            with open(file_path, 'r') as f:
                source_code += f"// Source: {file_path}\n{f.read()}\n\n"
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return source_code

def extract_functions(source_code):
    """Extract function signatures from C code"""
    function_pattern = r'\w+\s+\w+\([^)]*\)\s*\{'
    functions = re.findall(function_pattern, source_code)
    return functions

def generate_test_prompt(source_code, issue_title, issue_body):
    """Create a detailed prompt for Gemini"""
    functions = extract_functions(source_code)
    
    prompt = f"""
TASK: Generate comprehensive unit tests for C code using the Unity testing framework.

SOURCE CODE:
{source_code}

FUNCTIONS DETECTED:
{chr(10).join(functions) if functions else 'No functions detected'}

ISSUE TITLE: {issue_title}
ISSUE DESCRIPTION: {issue_body}

REQUIREMENTS:
1. Generate complete Unity test cases for all detectable functions
2. Include both normal operation and edge cases
3. Test error conditions and boundary values
4. Include proper setup/teardown functions
5. Use descriptive test function names
6. Include necessary headers and mocks

OUTPUT FORMAT:
- Complete C file with Unity tests
- Include #include directives for necessary headers
- Use TEST_ASSERT_* macros appropriately
- Group related tests in test suites

Generate the complete test file:
```c
"""
    return prompt

def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set")
        exit(1)
    
    issue_title = os.environ.get('ISSUE_TITLE', 'Generate unit tests')
    issue_body = os.environ.get('ISSUE_BODY', '')
    
    # Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-1.5-flash')    # Read source code
    source_code = read_source_files()
    if not source_code:
        print("No source code found to analyze")
        exit(1)
    
    # Generate prompt
    prompt = generate_test_prompt(source_code, issue_title, issue_body)
    
    print("Generating tests with Gemini AI...")
    
    try:
        response = model.generate_content(prompt)
        test_code = response.text
        
        # Clean up the response (remove markdown code blocks if present)
        if '```c' in test_code:
            test_code = test_code.split('```c')[1].split('```')[0]
        elif '```' in test_code:
            test_code = test_code.split('```')[1].split('```')[0]
        
        # Ensure tests directory exists
        os.makedirs('tests/generated', exist_ok=True)
        
        # Write generated tests
        output_file = 'tests/generated/generated_tests.c'
        with open(output_file, 'w') as f:
            f.write(test_code)
        
        print(f"Tests generated successfully: {output_file}")
        print(f"Generated {len(test_code)} characters of test code")
        
    except Exception as e:
        print(f"Error generating tests: {e}")
        exit(1)

if __name__ == "__main__":
    main()