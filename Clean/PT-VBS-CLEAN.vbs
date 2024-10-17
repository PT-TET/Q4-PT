Set objWMIService = GetObject( "winmgmts:\\.\root\cimv2" )
Set objList = objWMIService.ExecQuery( "Select * from Win32_ComputerSystem" )
	WScript.Echo "PT VBS TEST!"