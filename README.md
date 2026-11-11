# Session 5 — System, End-to-End, Acceptance & Exploratory Testing

Session 4 checked the order API and stored state. This session follows a buyer through the local browser form, confirmation and saved-order view. You will also investigate a different risk through purposeful exploration, then transfer the method to the GitHub project you have used since Session 2.

## Learning goals

- Explain how system, end-to-end, acceptance and exploratory testing ask different, sometimes overlapping questions.
- Turn a buyer goal into observable criteria and an independent expected result (a test oracle).
- Complete and run a Playwright browser test that checks both confirmation and saved-order retrieval.
- Record factual exploratory observations, questions and evidence limits.
- Apply the same reasoning to an authentic browser, command-line or service journey in your selected project.

## Use these materials

- [Buyer story and acceptance criteria](scenario-and-criteria.md) — the agreed rules for the local example
- [Session 5 activity](activity.md) — local practice and transfer to your existing project
- [Browser practice](practice/README.md) — setup, starter test and commands
- [Exploratory activity](exploratory-charter.md) — mission and observation notes
- [Voluntary self-check](self-check.md) — optional, non-graded review

The practice application runs locally with an in-memory order store. The test deliberately stops at a missing saved-order assertion. That stop is an exercise prompt, not evidence of an application defect.

## References

- [ISTQB CTFL syllabus](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/) — test levels and exploratory testing
- [ISTQB test oracle glossary](https://glossary.istqb.org/en_US/term/test-oracle) — expected-result source
- [Playwright for Python](https://playwright.dev/python/docs/intro) — setup and browser testing
- [Playwright locators](https://playwright.dev/python/docs/locators) — finding controls by visible meaning

The lecture slides, official assignment instructions, deadlines and submission are in **itslearning**.
