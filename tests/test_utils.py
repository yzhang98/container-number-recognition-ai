import ast
from pathlib import Path


def get_function(func_name: str):
    source = Path('main.py').read_text()
    module = ast.parse(source)
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            mod = ast.Module([node], [])
            namespace = {}
            exec(compile(mod, 'main.py', 'exec'), namespace)
            return namespace[func_name]
    raise ValueError(f"Function {func_name} not found")


def test_within_buffer_true():
    within_buffer = get_function('within_buffer')
    assert within_buffer(100, 120, 30) is True


def test_within_buffer_false():
    within_buffer = get_function('within_buffer')
    assert within_buffer(100, 200, 50) is False

