# Session 5 Activity — Follow a User Journey

Use the local order example first. Then continue with the **same public GitHub project selected in Session 2**. The exact assessment and submission instructions remain in **itslearning**.

## Part A — Local order practice

1. Read the [buyer story and criteria](scenario-and-criteria.md). Write the expected total for 1,250 cents at 10% from the pricing rule, before running the application.
2. Open the [practice instructions](practice/README.md). Predict which line of the prepared browser test will fail and why.
3. Run the starter test. Keep the actual command and result. Its `pytest.fail("TODO: ...")` is an intentional missing assertion.
4. Replace that stop with assertions for the saved-order heading, identifier and **exact retrieved total**. Rerun the test and keep the actual result. Do not infer success from the source code alone.
5. Use the [exploratory activity](exploratory-charter.md) to investigate a different risk, such as an invalid discount followed by correction. Record the action and data, exact visible result, expected rule or question, and next probe. Treat an unexpected result as a question until reproduced and compared with a requirement.
6. State what the scripted browser test established, what your exploration observed and what remains untested. Record the browser, app revision and fresh starting state.

## Part B — Your existing GitHub project

1. Link to the same project and one genuine user goal. Find its actual public workflow and relevant source or documentation. A browser is optional: a command-line or service workflow can be end-to-end when it crosses the meaningful boundaries of that project.
2. Write **2–4 observable acceptance criteria**. Identify the source of each expected result; do not copy expected values from the output you are testing.
3. Map the starting conditions, user actions, boundaries, visible outcome and read-back or state check where relevant. Choose a useful risk to investigate.
4. Identify one existing native test or propose a focused test with a meaningful assertion. Run it only in a local or authorized environment. Record the command and observed outcome, or clearly label the test **proposed, not run** and explain the blocker.
5. Make a short exploratory plan for a different risk. If you can investigate safely in an authorized environment, record factual observations. Otherwise label the plan **not executed**.
6. Ask AI for at most three missing high-risk journey or exploration ideas, grounded in your project criteria. **Accept, modify or reject** at least one suggestion and explain your decision using source or observed evidence. Do not present an AI suggestion as an executed result.
7. Finish with a short **SII reflection**: Strength, Improvement and Insight.

## Evidence to keep

A concise table or short report is enough: project/source links, user goal and criteria, journey map, test and outcome status, exploratory notes or clearly labelled plan, evidence limits, one AI decision and SII. Separate **observed**, **proposed** and **unconfirmed** claims. Do not test third-party services without authorization.

Follow **itslearning** for assessment, deadlines and submission.
