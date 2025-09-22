#!/usr/bin/env python3
import os
import re

def parse_functions(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    # Match function definitions: return_type func_name(param1_type param1, param2_type param2) { body }
    pattern = r'(\w+)\s+(\w+)\(([^)]*)\)\s*\{([^}]*)\}'
    matches = re.findall(pattern, code, re.DOTALL)
    functions = []
    for match in matches:
        return_type, func_name, params, body = match
        if params.strip():
            param_list = [p.strip().split()[-1] for p in params.split(',')]
        else:
            param_list = []
        # Find function calls in body
        calls = re.findall(r'\b(\w+)\s*\(', body)
        # Filter out known functions, assume others are from other files
        dependencies = [call for call in calls if call not in ['printf', 'malloc', 'free'] and call != func_name]
        functions.append((func_name, param_list, dependencies))
    return functions

def generate_test_stub(func_name, params, dependencies):
    # Generate test call with sample values
    if len(params) == 0:
        call = f"{func_name}()"
    elif len(params) == 1:
        call = f"{func_name}(10)"
    elif len(params) == 2:
        call = f"{func_name}(10, 20)"
    else:
        call = f"{func_name}({', '.join(['10'] * len(params))})"
    
    # Generate mocks based on dependencies
    mocks = []
    expected_result = 42  # Default
    
    if 'add' in dependencies:
        mocks.append("add_ExpectAndReturn(10, 20, 30);")
        expected_result = 30
    if 'compute' in dependencies:
        mocks.append("compute_ExpectAndReturn(30, 40);")
        expected_result = 40
    if 'multiply' in dependencies:
        if 'compute' in dependencies:
            mocks.append("multiply_ExpectAndReturn(40, 2, 80);")
            expected_result = 80
        else:
            mocks.append("multiply_ExpectAndReturn(30, 3, 90);")
            expected_result = 90
    
    mock_setup = "\n    ".join(mocks)
    
    return f"""
void test_{func_name}(void) {{
    // Mock setup
    {mock_setup}
    TEST_ASSERT_EQUAL({expected_result}, {call});
}}
"""

if __name__ == "__main__":
    changed_files = os.getenv('CHANGED_FILES', '').split()
    tests = []
    includes = ["#include \"unity.h\""]
    for file in changed_files:
        if file.startswith('src/') and file.endswith('.c'):
            base = os.path.basename(file).replace('.c', '')
            includes.append(f"#include \"{base}.h\"")
            functions = parse_functions(file)
            for func_name, params, deps in functions:
                tests.append(generate_test_stub(func_name, params, deps))
                # Add mock includes based on dependencies
                if any(d in ['add', 'multiply'] for d in deps):
                    includes.append("#include \"mock_main.h\"")
                if 'compute' in deps:
                    includes.append("#include \"mock_utils.h\"")
    
    if tests:
        # Remove duplicates from includes
        includes = list(dict.fromkeys(includes))
        include_str = "\n".join(includes)
        test_str = "\n".join(tests)
        # Assume one file, generate test_<basename>.c
        base = os.path.basename(changed_files[0]).replace('.c', '')
        test_file = f'test/test_{base}.c'
        with open(test_file, 'w') as f:
            f.write(f"{include_str}\n{test_str}")
        print(f"Generated {test_file}")
    else:
        print("No new functions to test")