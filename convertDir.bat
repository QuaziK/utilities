@echo off

dir /b *.mp4 > fileList

for /f "tokens=*" %%A in (fileList) do (
	ffmpeg -i "%%A" "%%A.mp4"
	del "%%A"
	ren "%%A.mp4" "%%A"
)

dir /b *.webm *.avi *.m2v *.mkv *.ts *.mov > fileList

for /f "tokens=*" %%A in (fileList) do (
	ffmpeg -i "%%A" "%%~nA.mp4"
	del "%%A"
)

del fileList