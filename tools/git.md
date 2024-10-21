# Git Tips

## Add a Remote Repository to Push To as Origin

Sometimes I create a repo locally before creating it elsewhere. In order to push everything up, there are two quick steps.
```
git remote add origin <url>
git push --set-upstream origin main
```
## Save Changes to Use Later or on Another Machine as a Patch

When using open source software, I find myself making small changes that are very specific to what I am doing but it's not enough to make a fork of the repository and track in a separate branch. There are so few changes that it's easier to just make a document outlining them and where to apply them. An easier way to do this is with a patch. A patch file is the textual output from a `git diff` that Git can understand when you want to apply it to the code. This is handy when the same codebase is used in multiple locations and can be used for automated setup, or for quicker manual setup.

`git diff` works by relaying any changes that are tracked, such as this file:
```
$ git diff
diff --git a/tools/git.md b/tools/git.md
index 149d1e2..7c2118a 100644
--- a/tools/git.md
+++ b/tools/git.md
@@ -8,3 +8,6 @@ git remote add origin <url>
 git push --set-upstream origin main
 
+## Save Changes to Use Later or on Another Machine as a Patch
+
+When using open source software, I find myself making small changes that are very specific to what I am doing but it's not enough to make a fork of the repository and track in a separate branch. There are so few changes that it's easier to just make a document outlining them and where to apply them. An easier way to do this is with a patch. A patch file is the textual output from a `git diff` that Git can understand when you want to apply it to the code. This is handy when the same codebase is used in multiple locations and can be used for automated setup, or for quicker manual setup.
```

To save these staged changes into a patch file, redirect the standard output into `my_patch.patch`.  
```
git diff --cached --no-color > gnb.patch > my_patch.patch
```

Then the changes can be applied to a repository without the changes.
```
git apply my_patch.patch
```
## Stash Changes for Later Use

When working in a shared codebase with updates here and there, you may have changes that you need to save but they are not able to be committed. In other cases, you made some modifications but need to merge a branch into your code to finish the work. When you are unable to commit the changes, you can stash them instead. Stashing will affect all of your tracked changes that could/would be overwritten by pulling updates or merging. Then once the updates are added to your repository, the changes can be popped back in. A workflow would look like this:
```
git stash
git pull
git stash pop
```
- First the tracked changes were stashed.
- Next the repository pulled the latest updates.
- Then the stash was popped back into the codebase.

## Undo The Last Local Commit

To undo the most recent local commit:
```
git reset HEAD~
```
- This will leave the files unchanged but all of the modifications will need added and committed again.
- This is useful when you've made local changes and a commit that you want to push but the main branch is already ahead of you.
