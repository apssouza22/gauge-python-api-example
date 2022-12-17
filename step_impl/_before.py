import os

from getgauge.python import data_store
from getgauge.python import before_suite

from step_impl.utils.AuthServiceClient import AuthServiceClient
from step_impl.utils.ProviderServiceClient import ProviderServiceClient


@before_suite
def before_suite_hook():
    print("Before Suite")
    data_store.suite["auth_client"] = AuthServiceClient(os.getenv("AUTH_ENDPOINT"))
    data_store.suite["provider_client"] = ProviderServiceClient(os.getenv("PROVIDER_ENDPOINT"))
