# Git Notes
You can run all the commands in any terminal
as long as you are in the project directory.
If you have the project open in vs code,
you can use the integrated terminal (ctrl+`)
___

## General Dev Workflow
the typical workflow is to
- "branch" off of main
- work on changes in your local branch
- commit your changes on your branch
- push that branch to github
- submit a Pull Request (PR) in github
  - this is a request to merge your branch into the main branch
  - allows for others to review and accept your changes
- merge your branch into main (from the PR)
- (optional) delete that branch from github
  - only if you're finished working on that branch

~~~
  |
  |\ <-- pull request and merge
  | \
  |  |
  |  |
  |  | store-commands-branch
  | /
  |/
  |
main
~~~
Generally, you want to have small commits and PRs
so that it's easier to review and manage

Try not to submit a PR with full implementation
of a feature that has lots of changes and affected files.
You would instead want to make smaller PRs for each step of implementation.
### Example: working on .store command
- PR for setting up `.store` command and maybe initial embed
- PR with some functionality for initial embed
- PR for purchasing an item and going to a new embed
- PR for selling and item and going to new embed
- etc
___

## Setup
This allows us to update a local repo (your project on your pc)
with any changes made in "upstream" (the github hosted repo)

_might not be needed but whatever_
### add and set an upstream
```
git remote add upstream GITHUB_REPO_URL
```
___

## Branch Commands
when working on something,
we want to create a new branch and work on that branch.
this helps us avoid interfering with each other's changes

### display all branches
```
git branch
```

### create and switch to new branch
```
git checkout -b store-commands-buy
```

### switch branches
```
git checkout branch-name-here
```

### change current branch name
```
git branch -m store-commands-buy-ui
```

### delete a local branch
```
git branch -d branch-name-here
```
- must be on a different branch to delete

if there are merging/out of sync issues
then the delete branch command might fail,
you can instead use `-D` instead of `-d`
to force delete the branch.
**only do this if you are sure you don't need that branch anymore**
___

## Pull Commands
Sync local repo with changes made in the upstream repo

### pull from origin branch
```
git pull
```

### pull specific branch
```
git pull upstream main
```

if you try `git pull` in a local branch without adding `upstream main`,
it will look for your local branch name in the github repo and try to pull from it.
if it only exists locally and not in github, it will fail.
so we need to specify to pull from the `upstream main` branch
___

## Add, Commit, and Push Commands
once you finish working on some changes,
you'll want to stage, commit, then "push" your changes to github

_vs code has a simple ui in the source control tab
that you can use instead of manually running these commands.
but this is good to know anyway_

### add (stage) all files to index
```
git add .
```

### stage a specific file
```
git add path/to/file
```

### unstage files
```
git restore --staged .
```

```
git restore --staged path/to/file
```

### commit your files with a helpful summary message
```
git commit -m "setup for store ui"
```

### push your commit and branch to github
```
git push -u origin branch-name-here
```

### if you already pushed your branch to github
```
git push
```
___

## Stashing
use when you need to temporarily "hide" changes

## stash you changes
```
git stash
```

### "pop" stashed changes
this reapplies the stashed changes
```
git stash pop
```
___

## status
print the status of your branch
```
git status
```

this will show you
- current branch
- if you are up to date with origin branch
- list of modified files
- list of staged/unstaged files
___

## Merging
merge changes from branch-1 to branch-2,
assuming you are currently in branch-2
```
git merge branch-1
```
___

# Common Scenarios
## Pulling when you have a "dirty" branch
_"dirty" just means you have files with uncommited changes_
### Example
you are working in branch `store-commands`
and want to pull recent changes from the `main` branch in github

### Process
stash changes on your branch
```
git stash
```
pull from the main branch
```
git pull
```
reapply stashed changes
```
git stash pop
```
fix merge conflicts, if any
- **probably have to show you this step in person**
___

## Pushing local branch to github
### Example
you are working in branch `store-commands` and are ready to push
that branch to github

### Process
make sure you are
[up to date](#pulling-when-you-have-a-"dirty"-branch)
with upstream `main`

stage files you want to commit
- to stage all files
  ```
  git add .
  ```
- stage a single file
  ```
  git add commands/storecommands.py
  ```

commit the changes with a message
```
git commit -m "added more options to store"
```

push branch to github
```
git push -u origin store-commands
```
___

## Adding commits to a branch and/or Pull Request
### Example
you [pushed your branch to github](#pushing-changes-to-github) and submitted a PR,
but someone said your code was shit
and you need to change some of your implementation

### Process
implement suggested changes

stage files to index
```
git add .
```
```
git add path/to/file.py
```

commit your changes with a helpful message
```
git commit -m "fixing bug"
```

push to github
```
git push
```
this push will automatically update your PR with the new commit(s)
___

## Deleting local branch after it's merged in github
### Example
you finished working on branch `store-commands-hotfix`,
[pushed it to github](#pushing-changes-to-github),
submitted a PR, merged the PR,
and no longer need the branch in your local repo.

### Process
switch back to your local main branch
```
git checkout main
```

delete the old branch
```
git branch -d store-commands-hotfix
```

pull to sync latest changes
```
git pull upstream main
```
___

## Switching branches when you have a "dirty" branch
### Example
you are working in branch `store-commands`
and need to switch to branch `database-changes`
but the command
```
git checkout database-changes
```
threw this error:
```
error: Your local changes to the following files would be overwritten by checkout:
```

### Process
stash changes
```
git stash
```

switch branches
```
git checkout database-changes
```

do whatever you need to do on that branch

switch back to original branch
```
git checkout store-commands
```

pop stashed changes
```
git stash pop
  ```
___

## Merging one branch into another
### Example
you are currently working on branch `store-commands-sell`
and want to add in changes from another branch
`store-commands-buy`.

### Process
make sure you are in `store-commands-sell`
- with
  ```
  git branch
  ```
- or
  ```
  git status
  ```

stash changes on your branch (if you have any)
```
git stash
```

merge `store-commands-buy` into `store-commands-sell`
```
git merge store-commands-buy
```

pop stashed changes (if you stashed)
```
git stash pop
```

fix merge conflics. if any
- **will show in person**
