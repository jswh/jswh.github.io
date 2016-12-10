set CDIR=%~dp0
call %CDIR%\Scripts\activate.bat
git add .
git commit -a -m "write article"
git push origin pelican
cp %CDIR%\CNAME %CDIR%\output\CNAME
::git reve-parse
::for /f %%i in ('git rev-list --max-count=1 origin/master') do set GIT_HEADER=%%i
python %CDIR%\Scripts\ghp-import -m "Generate Pelican site" -b master %CDIR%\output
git push origin master
pause