<h1> <img src="git-icon.png" width="30" height="30" style="float:left;"> Git Workshop

<p align="center"><img src="github-logo.png" height="200"></p>

# Motivation

**What is Version Control?**

Version control system (VCS) is a software tool that helps the developers keep track of every modification to the code. If a mistake is made and things break down, developers can go back and compare earlier versions to debug and help fix the problem.

**Why use Version Control?**

Version control allow ease of collaboration  with other developers with different teams working on different features. Besides that, developing software without using version control is risky, like not having backups.

**What is Git?**

Git is a version control system created by Linus Torvalds in 2005 for development of the Linux kernel. Git is distributed, every directory on every computer has a working copy of the code with a complete history of changes and full version tracking capabilities. 

**Why use Git?**

Git is the best choice for developers. Here are the main reasons why:

*	Git is **fast** in terms of performance using highly efficient algorithms to track all changes.
*	Git is **secure** with all files, directories, versions, commits and tags secured with a cryptographically secure hashing algorithm called SHA1.
*	Git is **flexible** with developers requiring no network access, when ready they can `push` their changes with one command.
*	Git is **free** and an open-source project with thousands of developers maintaining it.
*	Git is the factory **standard**, it is by far the most widely used version control system today.

---

## Installation

Follow the instructions on [this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) page to install `git`.

Try the following command:

```bash
git --version
```

If the installation is successful, you should see the version of the installed software.

```
git version 2.23.0
```

If something went wrong, you would see the following message instead:

```
command not found: git
```

---

## Configuration

#### `config`

To use `git` properly, you must set your name and email.

Use the `config` subcommand for this purpose.

```bash
git config --global user.name "Your Full Name"
git config --global user.email "youremailaddress@gmail.com"
```

>   #### Subcommand
>   
>   Some software are very complex and can have multiple use cases.
>   The use of subcommands allows developers to use these tools only for a particular task

---

## Local Workflow

Create a directory.

```bash
mkdir my-first-repo
cd my-first-repo
```

#### `init`

To initialize the repository, use the `init` subcommand.

```bash
git init
```

You have created a `git` repository on your local system.

>   #### Repository
>   
>   A repository is a directory that has elevated functionality.

With your preferred text editor, create a file called `README.md` with the following content:

```
# My First Repo

Hello, world!
```

A **README** file contains information about your repository, directories and files. It is a form of documentation which is a guide to developers giving a description about your project and instructions on how to run the code. The `.md` stands for **m**ark**d**own file. Markdown is a markup language which is easy to use for formatting text.

Use the `status` subcommand.

```bash
git status
```

You will be provided with the following information.

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

>   #### Branch
>   
>   Git can track file changes across multiple 'timelines' of a repository.
>   Each branch is its own universe. Git allows you to create branches from existing ones and move across them.

The default branch is called `master`

>   #### Commit
>   
>   A commit is nothing but a checkpoint. It is a milestone in that timeline.

In order to commit something, `git` needs to know exactly what to commit.

In our case we want `git` to save the new file that we created, i.e. `README.md`.

First let us add `README.md` to the staging area with the `add` subcommand.

```bash
git add README.md
```

Check the status of the repository

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   README.md

```

Earlier, our file was untracked. After adding it to the staging area, `git` realizes that we are planning to commit this file.

>   #### Staging Area
>   
>   The staging area is where you prepare the set of changes you want to `add` to your repository. It is the set of files that git will keep ready for a commit.

Confirm the changes with `commit` and a message by using the `-m` flag

```bash
git commit -m "Intial Commit" # the -m flag is for a message. A message usually describes what the commit has done.
```

The `commit` command takes the staged changes and commits it to the project history.

When making commits use a clear and concise message describing the changes you have made.

## Remote Workflow

Our goal is to create a synced copy of our local repository on GitHub. This way, we can share our projects with the rest of the world.

Just like how Instagram is meant for photos, [GitHub](https://github.com/) is meant for `git` repositories.

Either login or create an account. Register with the email with which you set up your `config`. You can add your institute email address later to access the [GitHub Student Developer Pack](https://education.github.com/pack).

Once you have logged in, navigate to the top right corner and click the little **+** icon and click on **New repository**.

To setup your remote repository:

*   Give it a suitable name. In this case `my first repo` is apt.

    >   Git automatically converts the spaces to hyphens `-` in the name of your repository.

*   You can give it a description.
*   You can set it to private.
*   Since we have already created a `README.md` in our local repo, uncheck the `Initialize this repository with a README.md`

>   #### `.gitignore`
>   
>   It is a hidden file in your repository that tells git to ignore changes made to certain files.

>   #### License
>   
>   For repositories to be open source, a license is added to control the use, changes and distribution of the project.
>   For more information check out [this link](https://help.github.com/en/articles/licensing-a-repository)

We have created an empty repository on GitHub. Let us link this with our local repository.

Copy the link of the GitHub repository.

It would look like this:

```
https://github.com/acmbpdc/my-first-repo.git
```

Use the `remote` subcommand to add a remote.

```bash
git remote add origin <link-to-your-github-repo>
```

>   #### Remote
>   
>   A remote is essentially a duplicate of the repository. It could be anything. You can have a remote on GitHub, GitLab, Google Drive, Dropbox, and even your own server.

By convention, the name `origin` is given to the main remote.

Right now, the local and remote repositories are linked. However, they are not synced yet.

To sync the repositories, either:

*   the local repo pulls from the remote (local is behind)
*   the local repo pushes into the remote (local is ahead)

In our case, we need to perform a `push`

```bash
git push origin master # push the commits of the master branch to the remote named origin
```

If you refresh the page for your GitHub repository, you should see the changes in effect.

Go ahead and add the following line to the `README.md`

```
Follow [this link](./)
```

Create a commit. Push the commit to the GitHub repository.

On refreshing the page on GitHub, the new link you added should point to the page itself.

You can check the commit history with the `log` command

```bash
git log
```
>   #### HEAD
>
>   The `HEAD` is simply a special pointer that points to the local `branch` you are on.
>   In this case, we are on the default `branch` or the `master branch`.
>
>   `HEAD` generally refers to the most recent commit on the current `branch`.
>
>   When `HEAD` is not pointing to the most recent commit, it is called a `detached HEAD`.
>
>   The `origin/master` refers to the remote `master branch`.
>   You can see it on "Initial commit" since we haven't updated our changes onto the repository.

## Collaboration

You have seen the power of GitHub as a cloud storage platform for repositories. Now, let's build something together.

There are a few nuances associated with the process of collaborating on GitHub.

*   If the owner of a repository has added you as a collaborator, you can directly make changes to a repository.
*   If you are not a collaborator of the repository, you cannot make changes to it unless you create a fork of that repository and can later request the collaborators of the original repository to merge your changes.

>   #### Fork
>
>   A fork is a copy of a GitHub repository. A fork resides only within the context of GitHub.

>   #### Clone
>
>   A clone is a copy of a repository. Technically, any two repositories that are linked (via remote) are said to be clones. 

In our case, we created a clone of our local repository on the GitHub infrastructure.

Navigate to [acmbpdc/git-workshop](https://github.com/acmbpdc/git-workshop).

Create a fork of this repository. It will take a few seconds.

Clone this the newly forked repository from GitHub and onto your local system. Use the `clone` subcommand to do this.

```bash
git clone <url-of-your-fork-on-github>
```

Use the `remote` subcommand to view your remotes

```bash
git remote -v
```

You should see something like this:

```
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin  https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
```

Sometimes, while making changes of your own, the original GitHub repository gets updated.

To pull changes from the original repository, add another remote.

```bash
git remote add upstream <url-of-the-original-github-repo>
```

To sync changes made to the original use the `fetch` subcommand

```bash
git fetch upstream
```

You can add these changes to your local master branch

```bash
git merge upstream/master
```

If you want, you can put these new changes from the original GitHub repo onto the forked repo on GitHub

```bash
git push origin master
```

Now that you know how to deal with any changes on the original repository, you can start making your own changes.

Create a branch using the `branch` subcommand

```bash
git branch my-branch
```

Move into this new branch using the `checkout` subcommand

```bash
git checkout my-branch
```

Make any changes that you want and commit.

In order to submit a pull request, it is best to merge these changes from your branch into the `master` branch.

```bash
git checkout master
git merge my-branch
```

Push these changes to your forked repository on GitHub

```
git push origin master
```

Navigate to the page of your GitHub fork and create a pull request.

Essentially, you are requesting the original repository to pull your changes.


# Summary

We covered:

*	[Motivation](#motivation)
*	[Basics](#basics)
    *   [Create your first repository](#create-your-first-repository)
    *   [Clone your repository](#clone-your-repository)
    *   [Modify your repository](#modify-your-repository)