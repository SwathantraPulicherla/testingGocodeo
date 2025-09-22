#!/usr/bin/env python3
import os
import re

def parse_functions(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    functions = re.findall(r'\w+\s+(\w+)\([^)]*\)\s*{', code)
    return functions

def generate_test_stub(func_name):
    return f"""
void test_{func_name}(void) {{
    // Mock setup
    add_ExpectAndReturn(10, 20, 30);  // Mock add(10,20) to return 30
    TEST_ASSERT_EQUAL(40, {func_name}(10));  // 10 + 20 = 30, but wait, compute returns add(x,10), so add(10,10)=20, but mocked to 30, so 30
}}
"""

if __name__ == "__main__":
    changed_files = os.getenv('CHANGED_FILES', '').split()
    tests = []
    for file in changed_files:
        if file.startswith('src/') and file.endswith('.c'):
            functions = parse_functions(file)
            for func in functions:
                tests.append(generate_test_stub(func))
    
    if tests:
        # Assume one file, generate test_<basename>.c
        base = os.path.basename(changed_files[0]).replace('.c', '')
        test_file = f'test/test_{base}.c'
        with open(test_file, 'w') as f:
            f.write(f"#include \"unity.h\"\n#include \"{base}.h\"\n#include \"mock_main.h\"\n" + "\n".join(tests))
        print(f"Generated {test_file}")
    else:
        print("No new functions to test")