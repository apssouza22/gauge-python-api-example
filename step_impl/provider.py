from getgauge.python import Messages, data_store
from getgauge.python import step

from step_impl.utils.AuthServiceClient import AuthServiceClient
from step_impl.utils.ProviderServiceClient import ProviderServiceClient


@step("Search for providers with name <name> and surname <surname>")
def search_by_name(name, surname):
    print("Search for providers with name {} and surname {}".format(name, surname))
    result = data_store.suite["provider_client"].search(data_store.suite["access_token"], {"first_name": name, "last_name": surname})
    data_store.scenario["result"] = result
    pass


@step("Ensure all the results have the name <name>")
def validate_providers_name(name):
    print("Ensure all the results have the name {}".format(name))
    Messages.write_message('Total records: {}'.format(len(data_store.scenario["result"])))
    assert len(data_store.scenario["result"]) > 0

    Messages.write_message('Names:')
    for provider in data_store.scenario["result"]:
        assert provider["first_name"] + " " + provider["last_name"] == name
        Messages.write_message('{}'.format(provider["first_name"] + " " + provider["last_name"]))
    pass

# if __name__ == '__main__':
#     auth_client = AuthServiceClient("https://chtl7rcn4c.execute-api.us-east-1.amazonaws.com/staging")
#     access_token = auth_client.request_token(
#         "r1HB7VWwr9ka3u9NuBGoLrZ7EMNu0mgq",
#         "M2xv0Kmw65g9_acQbV9j260N8HTbJ4-1h1E0mVUfGQDtBDEi8fAEmAafn3ewEghR"
#     )
#     # provider = ProviderServiceClient("https://nztzddvej6.execute-api.us-east-1.amazonaws.com")
#     # result = provider.search(access_token, {})
#     print(access_token)
