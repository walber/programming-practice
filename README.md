# leetcode-py
A Python package to generate professional LeetCode practice environments.

## Install leetcode-py-sdk
```bash
pip install leetcode-py-sdk
```

## Install UV
An extremely fast Python package and project manager, written in Rust.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Or
```bash
pip install uv
```

## Simple setup
```bash
uv venv leetcode-folder
cd leetcode-folder
lcpy gen -n 1
```

## Testing
```bash
cd leetcode-folder
uv run python -m pytest two_sum/test_solution.py
```

## List all problems
```bash
lcpy list
```

## Filter results
```bash
lcpy list <neetcode, neetcode-250, grind, grind-75, algo-master-75>
```

## Generate a problem by its number
```bash
lcpy gen -n <#number>
```
