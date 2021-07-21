import requests
from requests.structures import CaseInsensitiveDict
import json

def main():
    
    def get_ngrok_url():
        url = "http://localhost:4041/api/tunnels/" #please check the correct port that your ngrok instance use
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == 'command_line':
                return i['public_url']              
                break


    ngrok_url = get_ngrok_url()
    print(ngrok_url)

    url = "https://kutt.it/api/v2/links/<YourLinkId>"

    headers = CaseInsensitiveDict()
    headers["X-API-KEY"] = "<YOUR-API-KEY-HERE>"
    headers["Content-Type"] = "application/json"

    data = f"""
{{
	"target"  :  "{ngrok_url}",
  	"address" : "<YOUR-SHORTENED-URL-AFTER-KUTT.IT/>"
}}
"""
    print(data)


    resp = requests.patch(url, headers=headers, data=data)

    print(resp.status_code)


if __name__ =="__main__":
    main()