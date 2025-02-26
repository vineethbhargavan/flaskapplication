# flaskapplication --service principal

vineeth [ ~ ]$ az ad sp create-for-rbac --name "deployapptoappservice" --role contributor --scopes /subscriptions/xxx-4c5a-47f4-8c4d-e0bc70bc1841/resourceGroups/az400preparation --sdk-auth
Option '--sdk-auth' has been deprecated and will be removed in a future release.
Creating 'contributor' role assignment under scope '/subscriptions/03343086-4c5a-47f4-8c4d-e0bc70bc1841/resourceGroups/az400preparation'
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "clientId": "xxx-420c-4bf6-85f4-97bb339d3c6b",
  "clientSecret": "_YT8Q~xxx",
  "subscriptionId": "xxx-4c5a-47f4-8c4d-e0bc70bc1841",
  "tenantId": "xxx-8037-4ff7-b20d-a3a10890ebb5",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
vineeth [ ~ ]$ 