# Browser practice — Create, confirm and retrieve an order

This folder is self-contained. `app.py` supplies the local training application, `conftest.py` starts a fresh Flask server and store for the test, and `test_e2e.py` controls a Chromium browser with Playwright. No instructor solution files are needed.

## Set up

Use Python 3.10 or newer. From **this `practice/` folder**, run:

```bash
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python -m pytest -q
```

If your Python command is `python3`, use it consistently for all three commands. The browser installation needs a download; prepare it before the in-class practice when possible. If a browser or system dependency cannot be installed, record the exact blocker and follow the alternative in **itslearning** or the lecturer's instructions. Do not report an unrun test as passing.

## Complete the test

The first test run is **expected to fail** at an explicit `pytest.fail("TODO: ...")` after it opens the saved-order page. This is an exercise stop, not an observed product defect.

1. Read the [buyer story and criteria](../scenario-and-criteria.md).
2. Inspect `test_e2e.py`: the prepared steps already fill the form, submit the order, check the confirmation and follow **View saved order**.
3. Replace the `pytest.fail` line with assertions for the saved-order heading, identifier and exact total. Keep the expected amount based on the pricing rule.
4. Rerun `python -m pytest -q`. Record your actual command, result and environment. If an assertion fails, compare expected and observed values before deciding whether the problem is in the app, test or setup.
5. Continue with the [exploratory activity](../exploratory-charter.md) and the [Session 5 activity](../activity.md).

Each test invocation uses a local HTTP server, a fresh in-memory store and a Playwright browser context. A passing local test supports only the selected journey in that setup. It does not prove behavior in a deployed environment.
