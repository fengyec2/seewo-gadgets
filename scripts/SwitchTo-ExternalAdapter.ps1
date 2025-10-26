#Requires -Version 5.1
<#
.SYNOPSIS
Windows网络管理自动化脚本 v2.4 (移除适配器状态检查)

功能清单：
1. 自动提权运行
2. 强制禁用/启用指定适配器
3. 启用系统级移动热点
4. 状态验证与错误处理
#>

#region 配置区
$Config = @{
    KillProcess    = "360ap"                     # 需要终止的进程名
    DisableAdapter = "WLAN"                      # 需要禁用的适配器
    EnableAdapter  = "WLAN 2"                    # 需要启用的适配器
    WaitSeconds    = 0                          # 执行完成等待时间
}
#endregion

#region 自动提权
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}
#endregion

#region 增强错误处理
trap {
    Write-Host "[致命错误] $_`n错误位置: $($_.InvocationInfo.ScriptLineNumber)" -ForegroundColor Red
    Write-Host "详细堆栈: $($_.Exception.StackTrace)" -ForegroundColor DarkYellow
    Write-Host "`n按任意键退出..." -ForegroundColor Magenta
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    exit 1
}
#endregion

#region 功能函数
function Manage-Process {
    param($ProcessName)
    try {
        if ($proc = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue) {
            Stop-Process -Id $proc.Id -Force -ErrorAction Stop
            Write-Host "[√] 进程已终止: $ProcessName" -ForegroundColor Green
        }
    } catch {
        Write-Host "[!] 进程终止失败: $_" -ForegroundColor Yellow
    }
}

function Force-ManageAdapter {
    param(
        [Parameter(Mandatory)]
        [string]$Name,
        [ValidateSet("Enable","Disable")]
        [string]$Action
    )
    try {
        $adapter = Get-NetAdapter -Name $Name -ErrorAction Stop
        
        # 直接执行操作不检查当前状态
        if ($Action -eq "Disable") {
            Disable-NetAdapter -Name $Name -Confirm:$false -ErrorAction Stop
            Write-Host "[√] 已强制禁用适配器: $Name" -ForegroundColor Green
        } else {
            Enable-NetAdapter -Name $Name -Confirm:$false -ErrorAction Stop
            Write-Host "[√] 已强制启用适配器: $Name" -ForegroundColor Green
        }
        
        # 操作后状态显示
        $newStatus = (Get-NetAdapter -Name $Name).Status
        Write-Host "当前状态 → $newStatus" -ForegroundColor Gray
    } catch {
        Write-Host "[!] 适配器 '$Name' 操作失败: $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
}
#endregion

#region 主流程
Clear-Host
Write-Host "`n=== 开始执行网络管理脚本 ===`n" -ForegroundColor Magenta

# 步骤1：终止指定进程
Manage-Process -ProcessName $Config.KillProcess

# 步骤2：强制操作适配器
Force-ManageAdapter -Name $Config.DisableAdapter -Action Disable
Force-ManageAdapter -Name $Config.EnableAdapter -Action Enable

# 步骤4：状态验证
Write-Host "`n=== 最终状态验证 ===" -ForegroundColor Cyan
Get-NetAdapter -Name $Config.EnableAdapter | Select-Object Name, Status, LinkSpeed | Format-List
netsh wlan show interfaces

# 步骤5：启动进程
Start-Process -FilePath "C:\Program Files (x86)\360AP\360AP.exe" -ArgumentList "/autorunfree"

# 等待指定秒数内按键，超时自动退出
Write-Host "`n脚本执行完毕，按任意键退出（等待时间：$($Config.WaitSeconds) 秒）..." -ForegroundColor Cyan

$timer = [System.Diagnostics.Stopwatch]::StartNew()
while (-not $Host.UI.RawUI.KeyAvailable -and $timer.Elapsed.TotalSeconds -lt $Config.WaitSeconds) {
    Start-Sleep -Milliseconds 100
}
if ($Host.UI.RawUI.KeyAvailable) {
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
}
#endregion