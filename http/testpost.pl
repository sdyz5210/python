use LWP::UserAgent;;
use HTTP::Request;
use HTTP::Response;
use HTTP::Request::Common;

$agent=new LWP::UserAgent;
$request=POST('http://192.168.22.115:8080/Tools/Procedure!updateState',[userId=>2,appId=>5,projectId=>6]);
$request->header('User-Agent'=>'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1');
$request->header('Accept-Encoding'=>'gzip, deflate');

$response=$agent->request($request);
print $response->status_line,"\n";
print $response->content;