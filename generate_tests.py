#!/usr/bin/env python3
import os
import re
import subprocess

def get_changed_files():
    try:
        result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1'], capture_output=True, text=True)
        return result.stdout.strip().split('\n')
    except:
        return []

def parse_functions(file_path):
    functions = []
    with open(file_path, 'r') as f:
        content = f.read()
    # Simple regex for function declarations (not perfect, but for demo)
    pattern = r'^\s*(\w+)\s+(\w+)\s*\(([^)]*)\)\s*{'
    for match in re.finditer(pattern, content, re.MULTILINE):
        return_type, func_name, params = match.groups()
        functions.append((return_type, func_name, params))
    return functions

def generate_test(functions, test_file):
    test_code = '''#include "unity/src/unity.h"
#include "main.c"

void setUp(void) {}
void tearDown(void) {}

'''
    for return_type, func_name, params in functions:
        test_code += f'void test_{func_name}(void) {{\n'
        if return_type == 'int':
            test_code += f'    TEST_ASSERT_EQUAL(0, {func_name}());\n'  # Placeholder
        test_code += '}\n\n'

    test_code += '''int main(void) {
    UNITY_BEGIN();
'''
    for _, func_name, _ in functions:
        test_code += f'    RUN_TEST(test_{func_name});\n'
    test_code += '''    return UNITY_END();
}
'''
    with open(test_file, 'w') as f:
        f.write(test_code)

def main():
    changed_files = get_changed_files()
    c_files = [f for f in changed_files if f.endswith('.c')]
    for c_file in c_files:
        if os.path.exists(c_file):
            functions = parse_functions(c_file)
            test_file = f'test_{os.path.basename(c_file)}'
            if functions and not os.path.exists(test_file):
                generate_test(functions, test_file)
                print(f'Generated {test_file}')

if __name__ == '__main__':
    main()