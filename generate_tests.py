#!/usr/bin/env python3
import os
import re

def parse_functions(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    # Match function definitions: return_type func_name(param1_type param1, param2_type param2) {
    pattern = r'\w+\s+(\w+)\(([^)]*)\)\s*{'
    matches = re.findall(pattern, code)
    functions = []
    for match in matches:
        func_name = match[0]
        params = match[1].strip()
        if params:
            param_list = [p.strip().split()[-1] for p in params.split(',')]
        else:
            param_list = []
        functions.append((func_name, param_list))
    return functions

def generate_test_stub(func_name, params):
    # Generate test call with sample values
    if len(params) == 0:
        call = f"{func_name}()"
        args = ""
    elif len(params) == 1:
        call = f"{func_name}(10)"
        args = "10"
    elif len(params) == 2:
        call = f"{func_name}(10, 20)"
        args = "10, 20"
    else:
        call = f"{func_name}({', '.join(['10'] * len(params))})"
        args = ', '.join(['10'] * len(params))
    
    # Basic mocks - this is simplistic, in reality would need to analyze function body
    mocks = """
    // Mock setup - adjust based on function dependencies
    add_ExpectAndReturn(10, 20, 30);
    compute_ExpectAndReturn(30, 40);
    multiply_ExpectAndReturn(40, 2, 80);"""
    
    return f"""
void test_{func_name}(void) {{
    {mocks}
    TEST_ASSERT_EQUAL(80, {call});  // Expected result - adjust manually
}}
"""

if __name__ == "__main__":
    changed_files = os.getenv('CHANGED_FILES', '').split()
    tests = []
    for file in changed_files:
        if file.startswith('src/') and file.endswith('.c'):
            functions = parse_functions(file)
            for func_name, params in functions:
                tests.append(generate_test_stub(func_name, params))
    
    if tests:
        # Assume one file, generate test_<basename>.c
        base = os.path.basename(changed_files[0]).replace('.c', '')
        test_file = f'test/test_{base}.c'
        with open(test_file, 'w') as f:
            f.write(f"#include \"unity.h\"\n#include \"{base}.h\"\n#include \"mock_main.h\"\n#include \"mock_utils.h\"\n" + "\n".join(tests))
        print(f"Generated {test_file}")
    else:
        print("No new functions to test")