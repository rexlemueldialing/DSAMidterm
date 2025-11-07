# ***Visual Studio Code and Github: Installation, Set-Up, and Basic Operations***

## Visual Studio Code

### A. Installation of VSCode

**Step 1.** Download from microsoft website (options for windows and mac).

**Step 2.** Install the .exe file and simply click "next" for the following tabs.

**Step 3.** To verify if it is installed, just search in windows search bar.

<hr style="border: none; border-bottom: 0.5px solid #d0d7de; margin: 16px 0;">

### B. Basic Operation: _Opening VSCode through CMD_

**Step 1.** Create a folder.

**Step 2.** Create a dummy file (e.g. “dummyFile.txt”).

**Step 3.** In the folder directory, type “cmd” and press enter.

**Step 4.** Once redirected to the Command Prompt, make sure that the directory is correct. Then type “code .” to open VSCode.

---
## Git Hub

### A. Installation of Git

**Step 1.** To Download Git, go to Git’s official website. For Windows, under “Standalone Installer”, choose x64 or ARM64 depending on your desktop’s architecture.

**Step 2.** After downloading, install Git.

**Step 3.** During the installation set-up of Git, simply click “next” for every step.

**Step 4.** To verify if Git is installed, select a folder > hit right click > show more options. You should now see the option “Open Git Bash Here”.

---

### B1. Set-Up _GitHub in VSCode_

**Step 1.** First select View > Terminal > at the top right of terminal, click the dropdown > set to command prompt (still should be in the directory of desired folder).

**Step 2.** Next go to File > select "Auto Save”.

**Step 3.** Once finished, we can now download the necessary extensions. To download extensions, go to Extensions > search for  “Conventional Commits and Source Control” > Install both.

**Step 4.** To link VSCode to GitHub > go to Accounts > click “Backup and Sync Settings” > Sign in > select Sign in with GitHub > log in GitHub (make sure to use one email for easy linking).

**Step 5.** To verify if VSCode is linked to your GitHub, go to Accounts. Your GitHub account should be displayed at the very top.

**Step 6.** Lastly, To create a basic HTML code, hit right click > New file > enter file name (e.g. “helloWorld.html”) > write anything. To check if it worked, go to your file folder. The HTML file you just created should be saved there and runs once clicked.

---

### B2. Set-Up _Repository_

**Step 1.** First, create a repository, go to Home > Create New Repository. In the New Repository Page, enter Repository Name (e.g. “DSAMidterm”) > set to Public > Create repository.

**Step 2.** Once a repository is created, go to codemy.com/git/ for setting up your source control (This is the standard way. Allows users to view who and what is edited or changes made in a file).

**Step 3.** Set up Source Control:

&nbsp;&nbsp;**Step 3.1** Go to VSCode and create a new file. Name it as “README.md

&nbsp;&nbsp;**Step 3.2** Go to Terminal > dropdown button > select Git Bash (Git bash should be colorful)

&nbsp;&nbsp;**Step 3.3** From codemy.com/git/, copy each line one by one, then paste it in the VSCode terminal. (Keep in mind that the dollar sign ($) should not be doubled)

&nbsp;&nbsp;&nbsp;&nbsp;**Step 3.3.1** Start with “git init” — to initialize the process.

&nbsp;&nbsp;&nbsp;&nbsp;**Step 3.3.2** Go from top to bottom and input the requirements needed for each line.

&nbsp;&nbsp;&nbsp;&nbsp; ![git command for source control](images/Screenshot%202025-10-31%20105456.png)


**Step 4.** To link VSCode to GitHub > go to Accounts > click “Backup and Sync Settings” > Sign in > select Sign in with GitHub > log in GitHub (make sure to use one email for easy linking).

**Step 5.** To verify if VSCode is linked to your GitHub, go to Accounts. Your GitHub account should be displayed at the very top.

**Step 6.** Lastly, To create a basic HTML code, hit right click > New file > enter file name (e.g. “helloWorld.html”) > write anything. To check if it worked, go to your file folder. The HTML file you just created should be saved there and runs once clicked.

---

### C1. Basic Operation: _Push new or edited file to GitHub_

**Step 1.** Go to Source Control > locate Changes > stage changes.

**Step 2.** To upload changes to your GitHub Repository, click “Conventional Commits” (circle symbol) > select Features > select “No Scope” > choose Emoji (represent messages) > then add description (for record and to easily track changes made) > click “Sync Changes”.

**Step 3.** To check, reload your git hub.

---

### C2. Basic Operation: _Transfering Code File to Another Desktop_

**Step 1.** Dropdown code > copy url.

**Step 2.** TIn a different desktop, create a New folder (e.g. “PC No.3”) > Go to the folder created.

**Step 3.** Inside the folder, select “Open Git Bash Here” > git clone > right click > paste.

**Step 4.** Now your files are copied to another device. Also it is formatted the same way it is before.
