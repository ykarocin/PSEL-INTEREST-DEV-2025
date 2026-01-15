# UtilsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**utilsHealthCheck**](#utilshealthcheck) | **GET** /api/v1/utils/health-check/ | Health Check|

# **utilsHealthCheck**
> boolean utilsHealthCheck()


### Example

```typescript
import {
    UtilsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UtilsApi(configuration);

const { status, data } = await apiInstance.utilsHealthCheck();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

