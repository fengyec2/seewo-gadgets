@echo off
:: ================================================
:: WPS/Office 进程清理工具
:: By Luminary v2.1
:: ================================================
setlocal enabledelayedexpansion
cls

:: 管理员权限检查 ==================================
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo;
    echo  [权限提升] 正在请求管理员权限...
    echo  ----------------------------------------
    echo  此操作需要管理员权限来终止系统进程
    timeout /t 1 >nul
    powershell -Command "Start-Process cmd -ArgumentList '/c %~dpnx0' -Verb RunAs"
    exit /b
)

:: 界面初始化 =====================================
echo;
echo  ========================================
echo  WPS/Office 进程清理工具
echo  ========================================
echo;
echo  [执行操作] 正在终止以下应用程序进程...
echo;

:: 进程定义 ======================================
set "processes=wps.exe wpp.exe et.exe wpscloudsvr.exe wpspdf.exe POWERPNT.EXE wpscenter.exe wpsupdatesvr.exe"
set /a total=0, killed=0, failed=0

:: 进程终止循环 ==================================
for %%p in (%processes%) do (
    set /a total+=1
    set "status="
    set "msg="

    :: 尝试终止进程
    taskkill /f /im %%p >nul 2>&1
    if !errorlevel! equ 0 (
        set "status=[成功]"
        set "msg=已结束进程"
        set /a killed+=1
    ) else (
        :: 检查进程是否实际存在
        tasklist | find /i "%%p" >nul 2>&1
        if !errorlevel! equ 0 (
            set "status=[失败]"
            set "msg=无法终止(可能权限不足)"
            set /a failed+=1
        ) else (
            set "status=[忽略]"
            set "msg=进程未运行"
        )
    )
    
    :: 统一输出格式
    call :AlignOutput "%%p" "!status!" "!msg!"
)

:: 结果统计 ======================================
echo;
echo  ----------------------------------------
call :AlignOutput "统计结果" "已处理:!total!" "成功:!killed!" "失败:!failed!"
echo;

:: 根据结果输出建议
if %failed% gtr 0 (
    echo  [操作建议]
    echo  1. 请尝试手动关闭相关程序
    echo  2. 或以管理员身份再次运行本工具
    echo  3. 检查是否有杀毒软件拦截
) else (
    echo  [状态] 所有目标进程已清理完成
)

:: 延迟退出
echo;
timeout /t 1 >nul
exit /b

:: 格式化输出函数 ================================
:AlignOutput
set "proc=%~1"
set "col1=%~2"
set "col2=%~3"
set "col3=%~4"

:: 固定列宽对齐
set "proc=!proc:~0,15!"
set "col1=!col1:~0,8!"
set "col2=!col2:~0,20!"

echo  !col1!  !proc!  !col2!  !col3!
goto :eof