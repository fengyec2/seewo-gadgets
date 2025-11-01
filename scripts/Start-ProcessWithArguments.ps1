# start_hourglass.ps1
$exe = 'D:\PortableApp\Application\Hourglass\HourglassPortable.exe'
$args = @(
  '-t', '离考试结束还有'
  '-a', 'on'
  '-o', 'off'
  '-e', 'on'
  '-m', 'Lanyu'
  '-i', 'title'
  '-b', '860,120,400,200'
  '00:40:00'
)

Start-Process -FilePath $exe -ArgumentList $args -NoNewWindow -PassThru
# 如果想等待程序退出，改为：
# Start-Process -FilePath $exe -ArgumentList $args -NoNewWindow -Wait
