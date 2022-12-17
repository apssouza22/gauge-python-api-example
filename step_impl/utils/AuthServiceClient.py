from step_impl.utils.ServiceClient import ServiceClient


class AuthServiceClient(ServiceClient):

    def request_token(self, client_id, client_secret):
        json = {
            "grant_type": "client_credentials",
            "client_id": f"{client_id}",
            "client_secret": f"{client_secret}",
            "audience": "http://veda-test-api",
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self._apiRequest(method='POST', endpoint='/token', data=json, headers=headers)
        json = response.json()
        return json["access_token"]
