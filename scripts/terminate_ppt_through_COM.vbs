On Error Resume Next
Set ppt = GetObject(, "PowerPoint.Application")
If ppt.SlideShowWindows.Count > 0 Then
    ppt.SlideShowWindows(1).View.Exit
End If