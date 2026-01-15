# TeamsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**teamsCreateTeam**](#teamscreateteam) | **POST** /api/v1/teams/ | Create Team|
|[**teamsDeleteTeam**](#teamsdeleteteam) | **DELETE** /api/v1/teams/{team_id} | Delete Team|
|[**teamsGetTeam**](#teamsgetteam) | **GET** /api/v1/teams/{team_id} | Get Team|
|[**teamsListTeams**](#teamslistteams) | **GET** /api/v1/teams/ | List Teams|
|[**teamsUpdateTeam**](#teamsupdateteam) | **PUT** /api/v1/teams/{team_id} | Update Team|

# **teamsCreateTeam**
> TeamRead teamsCreateTeam(teamCreate)


### Example

```typescript
import {
    TeamsApi,
    Configuration,
    TeamCreate
} from './api';

const configuration = new Configuration();
const apiInstance = new TeamsApi(configuration);

let teamCreate: TeamCreate; //

const { status, data } = await apiInstance.teamsCreateTeam(
    teamCreate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **teamCreate** | **TeamCreate**|  | |


### Return type

**TeamRead**

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

# **teamsDeleteTeam**
> any teamsDeleteTeam()


### Example

```typescript
import {
    TeamsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TeamsApi(configuration);

let teamId: number; // (default to undefined)

const { status, data } = await apiInstance.teamsDeleteTeam(
    teamId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **teamId** | [**number**] |  | defaults to undefined|


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

# **teamsGetTeam**
> TeamRead teamsGetTeam()


### Example

```typescript
import {
    TeamsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TeamsApi(configuration);

let teamId: number; // (default to undefined)

const { status, data } = await apiInstance.teamsGetTeam(
    teamId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **teamId** | [**number**] |  | defaults to undefined|


### Return type

**TeamRead**

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

# **teamsListTeams**
> Array<TeamRead> teamsListTeams()


### Example

```typescript
import {
    TeamsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TeamsApi(configuration);

const { status, data } = await apiInstance.teamsListTeams();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<TeamRead>**

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

# **teamsUpdateTeam**
> TeamRead teamsUpdateTeam(teamUpdate)


### Example

```typescript
import {
    TeamsApi,
    Configuration,
    TeamUpdate
} from './api';

const configuration = new Configuration();
const apiInstance = new TeamsApi(configuration);

let teamId: number; // (default to undefined)
let teamUpdate: TeamUpdate; //

const { status, data } = await apiInstance.teamsUpdateTeam(
    teamId,
    teamUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **teamUpdate** | **TeamUpdate**|  | |
| **teamId** | [**number**] |  | defaults to undefined|


### Return type

**TeamRead**

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

