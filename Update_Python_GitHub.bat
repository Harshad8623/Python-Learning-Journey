@echo off
setlocal EnableExtensions

rem =========================================================
rem  Python Learning Journey - One Click GitHub Update
rem  Save this file INSIDE your main "Python L" folder.
rem  Repository: Harshad8623/Python-Learning-Journey
rem =========================================================

title Python Learning Journey - GitHub Updater
color 0A

rem Always run from the folder containing this batch file.
pushd "%~dp0"
if errorlevel 1 goto folder_error

echo.
echo ======================================================
echo       PYTHON LEARNING JOURNEY - GITHUB UPDATER
echo ======================================================
echo.
echo Project folder: %CD%
echo.

where git >nul 2>&1
if errorlevel 1 goto missing_git

if not exist ".git" goto not_a_repo

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 goto not_a_repo

rem Do not push an unexpected branch by mistake.
set "BRANCH="
for /f "delims=" %%B in ('git branch --show-current 2^>nul') do set "BRANCH=%%B"
if /I not "%BRANCH%"=="main" goto wrong_branch

rem Use the existing origin. Add it only if no origin exists.
set "REMOTE="
for /f "delims=" %%R in ('git remote get-url origin 2^>nul') do set "REMOTE=%%R"
if not defined REMOTE (
    echo No origin remote was found. Configuring your repository...
    git remote add origin "https://github.com/Harshad8623/Python-Learning-Journey.git"
    if errorlevel 1 goto failed
    set "REMOTE=https://github.com/Harshad8623/Python-Learning-Journey.git"
)

rem Abort rather than accidentally uploading to another repository.
echo(%REMOTE%| findstr /I /C:"github.com/Harshad8623/Python-Learning-Journey" /C:"github.com:Harshad8623/Python-Learning-Journey" >nul
if errorlevel 1 goto wrong_remote

echo GitHub repository: %REMOTE%
echo Current branch: %BRANCH%
echo.

rem Create a basic Python .gitignore only if none exists.
rem If there is an existing .gitignore, it is preserved.
if not exist ".gitignore" (
    echo Creating a basic .gitignore for Python...
    > ".gitignore" echo # Python cache and build files
    >> ".gitignore" echo __pycache__/
    >> ".gitignore" echo *.py[cod]
    >> ".gitignore" echo .pytest_cache/
    >> ".gitignore" echo .mypy_cache/
    >> ".gitignore" echo .ruff_cache/
    >> ".gitignore" echo build/
    >> ".gitignore" echo dist/
    >> ".gitignore" echo # Virtual environments
    >> ".gitignore" echo .venv/
    >> ".gitignore" echo venv/
    >> ".gitignore" echo env/
    >> ".gitignore" echo # Local secrets
    >> ".gitignore" echo .env
    >> ".gitignore" echo .env.*
    >> ".gitignore" echo *.pem
    >> ".gitignore" echo *.key
    >> ".gitignore" echo # Editor and OS files
    >> ".gitignore" echo .idea/
    >> ".gitignore" echo Thumbs.db
    >> ".gitignore" echo .DS_Store
)

echo Checking for updated Python files...
git status --short
if errorlevel 1 goto failed

echo.
echo Staging changes from all project folders...
rem Exclude common local secrets and temporary folders even if
rem the existing .gitignore does not already ignore them.
git add -A -- . ":(exclude,glob)**/.env" ":(exclude,glob)**/.env.*" ":(exclude,glob)**/*.pem" ":(exclude,glob)**/*.key" ":(exclude,glob)**/venv/**" ":(exclude,glob)**/.venv/**" ":(exclude,glob)**/__pycache__/**"
if errorlevel 1 goto failed

rem Abort if sensitive files were already staged before this BAT ran.
git diff --cached --name-only -- ":(glob)**/.env" ":(glob)**/.env.*" ":(glob)**/*.pem" ":(glob)**/*.key" | findstr /R "." >nul
if not errorlevel 1 goto sensitive_staged

rem git diff --quiet: 0 = no changes, 1 = changes, 2+ = error.
git diff --cached --quiet
if errorlevel 2 goto failed
if errorlevel 1 goto make_commit

echo No new file changes. Checking for commits to push...
goto push_changes

:make_commit
echo.
echo Committing your updates...
git commit -m "Update Python learning programs and mini projects"
if errorlevel 1 goto failed

:push_changes
echo.
echo Pushing updates to GitHub main branch...
git push -u origin main
if errorlevel 1 goto push_failed

echo.
echo ======================================================
echo                 UPDATE SUCCESSFUL!
echo ======================================================
echo GitHub: https://github.com/Harshad8623/Python-Learning-Journey
echo Your repository has been updated successfully.
goto finish

:missing_git
echo ERROR: Git is not installed or not found in PATH.
echo Install Git for Windows and try again.
goto finish

:folder_error
echo ERROR: Could not open the folder containing this BAT file.
goto finish_without_popd

:not_a_repo
echo ERROR: The BAT file is not in your existing Git project root.
echo Put it beside the .git folder inside "Python L".
goto finish

:wrong_branch
echo ERROR: Current branch is "%BRANCH%", not "main".
echo Switch to main with: git switch main
echo No files were uploaded.
goto finish

:wrong_remote
echo ERROR: This folder points to a DIFFERENT GitHub repository:
echo %REMOTE%
echo No files were uploaded. Fix the origin remote first.
goto finish

:sensitive_staged
echo.
echo ERROR: A secret-like file is already staged for commit.
echo Review staged files and unstage the secret before trying again.
echo You can use: git restore --staged -- "path-to-secret"
echo No commit or push was performed.
goto finish

:push_failed
echo.
echo ERROR: GitHub push was rejected or could not connect.
echo Your local commit is saved. No force-push was attempted.
echo If GitHub has newer commits, reconcile them before retrying.
goto finish

:failed
echo.
echo ERROR: A Git command failed. Review the output above.
echo Your existing project files have not been deleted.
goto finish

:finish
popd
:finish_without_popd
echo.
echo Press any key to close this window...
pause >nul
endlocal
