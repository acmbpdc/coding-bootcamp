# Contributing guidelines

## Commits

Please adhere to the following details when making commits :

*   Ensure that commit messages are written in present tense.
    Start with a verb and do not use pronouns.
    This is done to describe the content that is being committed.
    
    Adhere to the following convention :

    ```bash
    git commit -m "Fix bug"
    ```

    Avoid the following messages :

    ```bash
    git commit -m "I fixed the bug"
    git commit -m "Fixed the bug"
    git commit -m "I have fixed the bug"
    git commit -m "This fixes the bug"
    ```

*   If documents regarding a specific session are being committed, use the following syntax :

    ```bash
    git commit -m "[session-<num>] message"
    ```

    Example :

    ```bash
    git commit -m "[session-00] Add README"
    ```
*   Always try to refer to GitHub issues, relating to the commit

    ```bash
    git commit -m "Fix bug from #issue_number"
    ```