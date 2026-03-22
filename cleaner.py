import re

def clean_code(code):
    # remove single-line comments
    code = re.sub(r'//.*', '', code)

    # remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

    return code


def optimize_context(code, max_chars=4000):
    return code[:max_chars]