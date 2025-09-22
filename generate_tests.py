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
        functions.append((func_name, param_list, dependencies, body))
    return functions

def simulate_function(func_name, body, params):
    # Simple simulation: assume params are 10,20,... and mocks return fixed values
    # This is a basic implementation - in practice, you'd need proper AST parsing
    
    # Mock return values
    mock_returns = {
        'add': 30,      # add(10,20) -> 30
        'compute': 40,  # compute(30) -> 40  
        'multiply': None  # depends on args
    }
    
    # Parse simple assignments and return
    lines = [line.strip() for line in body.split(';') if line.strip()]
    variables = {}
    
    # Set input params
    if len(params) >= 1:
        variables[params[0]] = 10
    if len(params) >= 2:
        variables[params[1]] = 20
    
    for line in lines:
        if '=' in line and not line.startswith('return'):
            # Assignment like: int result = add(x, y)
            var, expr = line.split('=', 1)
            var = var.strip().split()[-1]  # remove type
            expr = expr.strip()
            
            # Evaluate simple function calls
            if 'add(' in expr:
                variables[var] = mock_returns['add']
            elif 'compute(' in expr:
                arg = expr.split('(')[1].split(')')[0].strip()
                if arg in variables:
                    variables[var] = mock_returns['compute']
                else:
                    variables[var] = mock_returns['compute']
            elif 'multiply(' in expr:
                args = expr.split('(')[1].split(')')[0]
                arg1, arg2 = [a.strip() for a in args.split(',')]
                if arg1 in variables:
                    val1 = variables[arg1]
                else:
                    val1 = int(arg1) if arg1.isdigit() else 10
                val2 = int(arg2) if arg2.isdigit() else 2
                variables[var] = val1 * val2  # Simple multiply simulation
        elif line.startswith('return'):
            # Return statement
            expr = line[6:].strip()  # remove 'return'
            if expr in variables:
                return variables[expr]
            elif expr.isdigit():
                return int(expr)
            elif 'multiply(' in expr:
                args = expr.split('(')[1].split(')')[0]
                arg1, arg2 = [a.strip() for a in args.split(',')]
                val1 = variables.get(arg1, 10)
                val2 = int(arg2) if arg2.isdigit() else 2
                return val1 * val2
            else:
                return 42  # fallback
    
    return 42  # fallback

def generate_test_stub(func_name, params, dependencies, body):
    # Generate test call
    if len(params) == 0:
        call = f"{func_name}()"
    elif len(params) == 1:
        call = f"{func_name}(10)"
    elif len(params) == 2:
        call = f"{func_name}(10, 20)"
    else:
        call = f"{func_name}({', '.join(['10'] * len(params))})"
    
    # Generate mocks
    mocks = []
    if 'add' in dependencies:
        mocks.append("add_ExpectAndReturn(10, 20, 30);")
    if 'compute' in dependencies:
        mocks.append("compute_ExpectAndReturn(30, 40);")
    if 'multiply' in dependencies:
        # Determine multiply args based on function
        if 'compute' in dependencies:
            mocks.append("multiply_ExpectAndReturn(40, 2, 80);")
        else:
            mocks.append("multiply_ExpectAndReturn(30, 3, 90);")
    
    mock_setup = "\n    ".join(mocks) if mocks else "    // No mocks needed"
    
    # Simulate expected result
    expected = simulate_function(func_name, body, params)
    
    return f"""
void test_{func_name}(void) {{
    // Mock setup
    {mock_setup}
    TEST_ASSERT_EQUAL({expected}, {call});
}}
"""

if __name__ == "__main__":
    changed_files = os.getenv('CHANGED_FILES', '').split()
    
    # If no changed files or script/workflow changed, check all src files
    if not changed_files or any('generate_tests.py' in f or 'ci.yml' in f for f in changed_files):
        import glob
        changed_files = glob.glob('src/*.c')
    
    tests = []
    includes = ["#include \"unity.h\""]
    existing_tests = set()
    
    for file in changed_files:
        if file.startswith('src/') and file.endswith('.c') and os.path.exists(file):
            base = os.path.basename(file).replace('.c', '')
            includes.append(f"#include \"{base}.h\"")
            functions = parse_functions(file)
            for func_name, params, deps, body in functions:
                test_func_name = f"test_{func_name}"
                existing_tests.add(test_func_name)
                tests.append((test_func_name, generate_test_stub(func_name, params, deps, body)))
                
                # Add mock includes based on dependencies
                if any(d in ['add', 'multiply'] for d in deps):
                    includes.append("#include \"mock_main.h\"")
                if 'compute' in deps:
                    includes.append("#include \"mock_utils.h\"")
    
    if tests:
        # Remove duplicates from includes
        includes = list(dict.fromkeys(includes))
        include_str = "\n".join(includes)
        
        # Assume one file, generate test_<basename>.c
        base = os.path.basename(changed_files[0]).replace('.c', '')
        test_file = f'test/test_{base}.c'
        
        # Read existing file if it exists
        existing_content = ""
        if os.path.exists(test_file):
            with open(test_file, 'r') as f:
                existing_content = f.read()
        
        # Parse existing test functions
        existing_test_funcs = set()
        for line in existing_content.split('\n'):
            if line.strip().startswith('void test_') and '(' in line:
                func_name = line.split('(')[0].replace('void ', '').strip()
                existing_test_funcs.add(func_name)
        
        # Append only new tests
        new_tests = []
        for test_func_name, test_content in tests:
            if test_func_name not in existing_test_funcs:
                new_tests.append(test_content)
        
        if new_tests:
            with open(test_file, 'a') as f:  # Append mode
                if not existing_content:  # If file was empty, add includes
                    f.write(f"{include_str}\n")
                f.write("\n".join(new_tests))
            print(f"Appended {len(new_tests)} new test(s) to {test_file}")
        else:
            print("No new functions to test")
    else:
        print("No new functions to test")