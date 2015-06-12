use LWP::Simple;

$content = get("http://192.168.22.115:8080/Tools/Procedure!updateState?userId=2&appId=5&projectId=6"); 
print $content