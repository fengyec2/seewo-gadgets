@echo off
:: ================================================
:: 自动自习提醒工具
:: By Luminary v2.2
:: ================================================
setlocal enabledelayedexpansion
cls

:: 配置区 ==========================================
set "delay=5"                & rem 可修改倒计时秒数
set "FileName=all_auto.ppsx" & rem 可修改目标文件名
set "file=%~dp0%FileName%"

:: 网络梗合集（可自由添加修改）
set "meme[0]=欲穷千里目，更上一 Ciallo~(∠ - ω <)⌒☆"
set "meme[1]=玩瓦罗兰特玩的"
set "meme[2]=你说的对，但是 PPT 是自己启动的"
set "meme[3]=正在启动某教学软件"
set "meme[4]=Ciallo~(∠ - ω< )⌒☆ 难，Ciallo~(∠ - ω< )⌒☆ 难，多歧路，今安在？"

:: ================================================

:: 显示随机网络梗
call :ShowRandomMeme

:: 初始化界面
echo;
echo  ========================================
echo;
echo  触发自习提醒
echo;
echo  类型：普通自习
echo;
echo  ========================================
echo;

:: 动态倒计时提示
echo  [操作提示]
echo  将在 %delay% 秒后自动打开: %FileName%
echo  按任意键可取消操作...
echo;
echo  [倒计时开始]
echo;

:: 修复版倒计时检测
for /l %%i in (%delay%,-1,1) do (
    set /p "=  >> 剩余 %%i 秒... " < nul
    choice /c ABCDEFGHIJKLMNOPQRSTUVWXYZ /t 1 /d N > nul 2> nul
    if errorlevel 1 if errorlevel 26 (
        echo;
        echo;
        echo  [状态] 操作已取消！
        echo  [提示] 检测到按键中断
        timeout /t 1 > nul
        exit /b
    )
    echo;
)

:: 文件检查
if not exist "%file%" (
    echo;
    echo  [错误] 文件未找到！
    echo  -------------------------------
    echo  ■ 预期位置: %file%
    echo  ■ 可能原因:
    echo     1. 文件名不是 %FileName%
    echo     2. 文件未与脚本同目录
    echo     3. 文件已被移动或删除
    echo;
    echo  [解决方案] 请检查后重试
    timeout /t 7 > nul
    exit /b
)

:: 执行打开
echo;
echo  [状态] 正在启动演示文稿...
echo  [文件] %FileName%
start "" "%file%"

:: 完成提示
echo;
echo  [完成] 已成功发送打开指令
timeout /t 1 > nul
exit /b

:: 随机网络梗函数 ================================
:ShowRandomMeme
set /a "rand=%random% %% 5"
echo;
echo  ========================================
echo;
echo  !meme[%rand%]!
goto :eof