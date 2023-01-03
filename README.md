## Python
## Python  Exercises from 2-5
## Assignment Scope
This assignment was to copy the Python exercise folders from week 2-5 to a GitHub repository (repo). A GitHub public repo was setup to include a readme file to explain about the repo. This was setup using best practise from the lecture’s notes. A branch was setup using *Git branch* in Git called *Python-Dev*. The repo was cloned to the local desktop using the GitHub URL and git clone on the local machine. This was created in a local folder called Python.      
## The aims of this assignment 
1. Create a repo in GitHub called python.
2. Include a Readme file explaining about the repo.
3. Add gitignore for python to exclude unwanted bit code and not to include SSH keys.
4. Select a creative license, to copy right the work.  
5. Create a branch in this repo for Dev work called *Python-Dev*.
6. Make some changes in your local repo which would push to *Python-Dev branch*. The readme file would be edited to perform this task. 
6. Using best practise enable Protect matching branches. 
7. Make some changes in your local repo and commit these to *Python-Dev branch* and then to *Python main*. These changes would be pushed to GitHub.
## Method  #
For this part of the assignment a backup was taken of the Python exercise folder. In GitHub a repo called Python is created.  Git ignore was selected to ignore Python files and ignore SSH as in the instructors’ notes. A license was selected with the setting *Creative Commons Zero v1.0 Universal*. A readme file is selected to be created in the repo to be used later. On the local machine a folder called python is created on the desktop. From the repo in GitHub the URL is copied from the code menu and on the local machine from PowerShell *git clone https://github.com/L00170166/Python.git* is run from the python folder. *Xcopy* is used to copy the python files into the local repo. In PowerShell *git status* command is run on the python folder. Now the newly copied python files are present and need to be committed. From PowerShell *git commit* is executed. Using Visual Studio Code (VSC) the readme file is opened from the repo and edited. Using PowerShell *git branch* is executed to create a folder called *Python-Dev*. Using PowerShell *git logs* shows the newly creative Python-dev is now the *head*. Changes were made to the Readme file using VCS. Using PowerShell *git status* we can see changes are waiting to be committed. Running *git log* we now can see *Python-Dev* is now the head. These are committed to *Python-Dev branch* running *git commit*. Once these changes are validated, they are committed to *Python main*. A *git push* is preform from git to GitHub. The changes could be seen in repo *branch* and not in repo *main*. Commit to main preformed in GitHub. 
In this assignment, *Git and GitHub* were used to perform the main tasks. PowerShell was also used to run Git commands to confirm the status and analyse logs. GitHub desktop was also downloaded to see it uses. It is a GUI interface, which creates and executes the commands for Git\GitHub.    

