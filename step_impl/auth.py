from getgauge.python import data_store
from getgauge.python import step

from step_impl.utils.AuthServiceClient import AuthServiceClient
from step_impl.utils.ProviderServiceClient import ProviderServiceClient


@step("Authenticate with <client_id> and <client_secret>")
def authenticate(client_id, client_secret):
    print("Authenticate with {} and {}".format(client_id, client_secret))
    auth_client = data_store.suite.get("auth_client")
    access_token = auth_client.request_token(client_id, client_secret)
    data_store.suite["access_token"] = access_token


@step("Access protected resource with returned access token")
def access_protected_resource():
    result = data_store.suite["provider_client"].search(data_store.suite["access_token"], {})
    assert result is not None


@step("Validate returned access token")
def validate_token():
    print("Validate returned access token")
    # TODO: Validate access token
    pass


@step("Check that the access token contains the claims")
def access_protected_resource():
    # TODO: Check that the access token contains the claims
    pass

# if __name__ == '__main__':
#     auth_client = AuthServiceClient("https://chtl7rcn4c.execute-api.us-east-1.amazonaws.com/staging")
#     access_token = auth_client.request_token(
#         "r1HB7VWwr9ka3u9NuBGoLrZ7EMNu0mgq",
#         "M2xv0Kmw65g9_acQbV9j260N8HTbJ4-1h1E0mVUfGQDtBDEi8fAEmAafn3ewEghR"
#     )
#     provider = ProviderServiceClient("https://nztzddvej6.execute-api.us-east-1.amazonaws.com")
#     result = provider.search(access_token, {})
#     print(result)
