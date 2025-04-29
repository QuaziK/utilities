@echo off

dir /b *.jpg > fileList

for /f "tokens=*" %%A in (fileList) do (
	REM ffmpeg -i "%%A" "%%~nA.png"
	echo %%A
	ren "%%A" "%%~nA.png"
	REM del "%%A"
)

del fileList