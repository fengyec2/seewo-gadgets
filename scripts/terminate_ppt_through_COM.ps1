$ppt = [Runtime.InteropServices.Marshal]::GetActiveObject("PowerPoint.Application")
if ($ppt.SlideShowWindows.Count -gt 0) {
    $ppt.SlideShowWindows[1].View.Exit()
}