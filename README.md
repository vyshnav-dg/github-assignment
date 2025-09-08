# github-assignment

This is a simple Inventory Management System written in Python. It does the basic functions like add and remove items and also get the total value of the current items in the inventory. A github actions workflow is also implemented for this repository that is triggered whenever a push or pull request is done on the `main` branch.

## Actions used
The following actions were used from the Github actions marketplace
- `actions/checkout@v4`
- `actions/setup-python@v6`

## Actions Workflow
- Uses ubuntu for running the actions
- Sets up Python v3.13
- Updates `pip` and installs any dependencies specified in `requirements.txt`. These packages are also cached for future actons.
- The repository is first linted with flake8
- The code is then tested with `unittest`

## Notes
- The workflow current uses only one job `build` which includes all the steps from setting up the environment to testing the code
- The user who triggered the workflow will receive notification and an email (based on their github settings), if a workflow has failed
- The installed dependencies were cached as most of the workflow will require them, unless new dependencies are added.
- Some additional status checks were included to let the user know about the progress of each step
- Difficulties were faced while trying to setup cache for the python dependencies.
    - `actions/setup-python` requires the repository to have a `requirements.txt` file or something similar. So a `requirements.txt` file was added to fix this
    - Even after the above fix, there was still an error that states `cache service returned 400`. To fix this, the latest version of `actions/setup-python` was used (version 6)
