from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = "<your_storage_account_connection_string>"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = "mycontainer"

container_client = blob_service_client.get_container_client(container_name)
if not container_client.exists():
    container_client.create_container()

file_name = "full_file_name.txt"

blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

with open(file_name, "rb") as data:
    blob_client.upload_blob(data)