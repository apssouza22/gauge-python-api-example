from step_impl.utils.ServiceClient import ServiceClient


class ProviderServiceClient(ServiceClient):

    def search(self, access_token:str, query: dict):
        self.access_token = access_token
        headers = {'Authorization': "Bearer " + self.access_token}
        response = self._apiRequest(method='GET', endpoint='/api/v1/providers', json=query, headers=headers)
        json = response.json()
        return json
