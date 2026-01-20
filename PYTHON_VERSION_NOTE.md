# Python Version Note

This project requires Python 3.8+ as specified in the Pipfile.

If the default `pytest` command fails with import errors, please use:
```bash
python3 -m pytest server/testing/ -v
```

Or run the provided test runner:
```bash
python3 run_tests.py
```

All 11 tests should pass when run with Python 3.