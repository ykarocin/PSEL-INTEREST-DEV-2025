# MembersApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**membersAddMember**](#membersaddmember) | **POST** /api/v1/members/ | Add Member|
|[**membersRemoveMember**](#membersremovemember) | **DELETE** /api/v1/members/{team_id}/{user_id} | Remove Member|

# **membersAddMember**
> MemberRead membersAddMember(memberCreate)


### Example

```typescript
import {
    MembersApi,
    Configuration,
    MemberCreate
} from './api';

const configuration = new Configuration();
const apiInstance = new MembersApi(configuration);

let memberCreate: MemberCreate; //

const { status, data } = await apiInstance.membersAddMember(
    memberCreate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **memberCreate** | **MemberCreate**|  | |


### Return type

**MemberRead**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membersRemoveMember**
> any membersRemoveMember()


### Example

```typescript
import {
    MembersApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new MembersApi(configuration);

let teamId: number; // (default to undefined)
let userId: number; // (default to undefined)

const { status, data } = await apiInstance.membersRemoveMember(
    teamId,
    userId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **teamId** | [**number**] |  | defaults to undefined|
| **userId** | [**number**] |  | defaults to undefined|


### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

