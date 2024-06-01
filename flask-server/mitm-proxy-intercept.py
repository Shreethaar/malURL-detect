from mitmproxy import http
import requests

class Intercept:
    def request(self,flow:http.HTTPFlow) -> None:
        if "example.com" in flow.request.pretty_host:
            data={
                    'url':flow.request.url
                    }
            request.post('http://127.0.0.1:5000/capture_url', json=data)

addons=[
        Intercept()
]

