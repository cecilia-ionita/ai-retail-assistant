# PROJECT LOG

## Sprint 0 – Project Setup

### Objectives

- Create the project structure
- Configure the Python environment
- Initialize the documentation
- Prepare the project configuration


### Completed Tasks

- Created the project folder structure.
- Configured the Python virtual environment.
- Created the initial README.md.
- Configured pyproject.toml.
- Configured .gitignore.
- Initialized the local Git repository.
- Renamed the default Git branch from master to main.
- Added the initial project files to Git staging.
- Created the first Git commit: "Initial project setup".
- Verified the repository status and commit history.

### Lessons Learned

- Importance of project structure.
- Purpose of README.md.
- Role of pyproject.toml.
- Why Git ignores specific files.
- Git tracks the history of changes in a software project.
- git status shows the current state of the repository.
- git add prepares changes for the next commit.
- A commit represents a saved version of the project.
- The main branch is the primary development branch.
- HEAD points to the current commit of the active branch.
- A clean working tree means that all current changes are committed.

### Next Sprint

Sprint 1 – Application foundation and first Python modules.

### Personal Notes

Today I understood why a good software project starts with documentation before writing code.

I learned that pyproject.toml is the identity card of a Python project.

I learned how to create and configure README.md, .gitignore and PROJECT_LOG.md.


## Sprint 1 - Application Foundation

### Objectives

- Create the first Python business logic module.
- Implement basic retail sales calculations.
- Introduce automated testing with pytest.
- Practice the development workflow: code, test, verify and commit.

### Completed Tasks

- Created the `methods` Python package.
- Created the `shared` Python package.
- Created the `tests` Python package.
- Created `methods/sales.py`.
- Implemented `calculate_sale_value()`.
- Implemented `calculate_profit()`.
- Implemented `calculate_profit_margin()`.
- Created `tests/test_sales.py`.
- Installed and configured pytest.
- Created unit tests for the three sales calculation functions.
- Successfully executed the test suite: 3 tests passed.
- Committed the sales calculations and unit tests to Git.


### Lessons Learned

- A unit test verifies whether a function returns the expected result.
- `assert` compares the actual result with the expected result.
- If the actual and expected results are different, the test fails.
- Automated tests help detect errors when the application code is changed.
- Sale value is calculated as quantity multiplied by unit price.
- Profit is calculated as sales value minus cost.
- Profit margin is calculated as profit divided by sales value.
- A profit margin of 0.25 represents 25%.
- pytest can automatically discover and execute tests from the `tests` package.