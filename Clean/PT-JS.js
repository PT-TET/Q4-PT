var objWMIService = GetObject("winmgmts:\\\\.\\root\\cimv2");
var objList = objWMIService.ExecQuery("SELECT * FROM Win32_ComputerSystem");
    WScript.Echo("PT JSCRIPT TEST!");