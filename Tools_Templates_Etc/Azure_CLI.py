from azure.cli.core import get_default_cli
from azure.mgmt.resource import ResourceManagementClient
from azure.cli.core._profile import Profile


az_cli = get_default_cli()
az_cli.invoke([''])


profile = Profile()
subscription_id = profile.get_subscription()[0]
access_token = profile.get_raw_token()[0]['access_token']


resource_client = ResourceManagementClient(
    credentials=None,
    subscription_id=subscription_id
)

resource_client.config.credentials = ('BearerToken', {'access_token': access_token})


resource_groups = resource_client.resource_groups.list()
for group in resource_groups:
    print(group.name)