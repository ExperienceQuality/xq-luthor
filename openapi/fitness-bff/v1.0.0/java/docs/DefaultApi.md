# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSession**](DefaultApi.md#addSession) | **POST** /api/v1/routines/{routineId}/sessions |  |
| [**archiveRoutine**](DefaultApi.md#archiveRoutine) | **DELETE** /api/v1/routines/{routineId} |  |
| [**captureSnapshot**](DefaultApi.md#captureSnapshot) | **POST** /api/v1/routines/{routineId}/snapshots |  |
| [**createExerciseLog**](DefaultApi.md#createExerciseLog) | **POST** /api/v1/exercise-logs |  |
| [**createRoutine**](DefaultApi.md#createRoutine) | **POST** /api/v1/routines |  |
| [**deleteSession**](DefaultApi.md#deleteSession) | **DELETE** /api/v1/routines/{routineId}/sessions/{sessionId} |  |
| [**getCurrentUser**](DefaultApi.md#getCurrentUser) | **GET** /api/v1/me | Return minimal authenticated principal information. |
| [**getRoutine**](DefaultApi.md#getRoutine) | **GET** /api/v1/routines/{routineId} |  |
| [**getSession**](DefaultApi.md#getSession) | **GET** /api/v1/routines/{routineId}/sessions/{sessionId} |  |
| [**getSessionView**](DefaultApi.md#getSessionView) | **GET** /api/v1/routines/{routineId}/sessions/{sessionId}/view | Compose a session prescription and recent exercise history. |
| [**listExerciseLogs**](DefaultApi.md#listExerciseLogs) | **GET** /api/v1/exercise-logs |  |
| [**listExercises**](DefaultApi.md#listExercises) | **GET** /api/v1/exercises | List distinct exercise names from the user&#39;s log history. |
| [**listRoutines**](DefaultApi.md#listRoutines) | **GET** /api/v1/routines |  |
| [**listSnapshots**](DefaultApi.md#listSnapshots) | **GET** /api/v1/routines/{routineId}/snapshots |  |
| [**replaceSession**](DefaultApi.md#replaceSession) | **PUT** /api/v1/routines/{routineId}/sessions/{sessionId} |  |
| [**updateRoutine**](DefaultApi.md#updateRoutine) | **PATCH** /api/v1/routines/{routineId} |  |


<a id="addSession"></a>
# **addSession**
> Session addSession(ifMatch, routineId, sessionWrite)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    SessionWrite sessionWrite = new SessionWrite(); // SessionWrite | 
    try {
      Session result = apiInstance.addSession(ifMatch, routineId, sessionWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addSession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | |
| **routineId** | **UUID**|  | |
| **sessionWrite** | [**SessionWrite**](SessionWrite.md)|  | |

### Return type

[**Session**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Session created. |  * ETag -  <br>  * Location -  <br>  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **409** | Domain conflict. |  -  |
| **412** | ETag precondition failed. |  -  |
| **428** | If-Match is required. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="archiveRoutine"></a>
# **archiveRoutine**
> archiveRoutine(ifMatch, routineId)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.archiveRoutine(ifMatch, routineId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#archiveRoutine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | |
| **routineId** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Routine archived. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **412** | ETag precondition failed. |  -  |
| **428** | If-Match is required. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="captureSnapshot"></a>
# **captureSnapshot**
> Snapshot captureSnapshot(ifMatch, idempotencyKey, routineId)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      Snapshot result = apiInstance.captureSnapshot(ifMatch, idempotencyKey, routineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#captureSnapshot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | |
| **idempotencyKey** | **String**|  | |
| **routineId** | **UUID**|  | |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Snapshot captured. |  * ETag -  <br>  * Location -  <br>  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **412** | ETag precondition failed. |  -  |
| **428** | If-Match is required. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="createExerciseLog"></a>
# **createExerciseLog**
> ExerciseLog createExerciseLog(createExerciseLogRequest)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateExerciseLogRequest createExerciseLogRequest = new CreateExerciseLogRequest(); // CreateExerciseLogRequest | 
    try {
      ExerciseLog result = apiInstance.createExerciseLog(createExerciseLogRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createExerciseLog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createExerciseLogRequest** | [**CreateExerciseLogRequest**](CreateExerciseLogRequest.md)|  | |

### Return type

[**ExerciseLog**](ExerciseLog.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Exercise log created. |  * Location -  <br>  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="createRoutine"></a>
# **createRoutine**
> Routine createRoutine(routineCreate)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RoutineCreate routineCreate = new RoutineCreate(); // RoutineCreate | 
    try {
      Routine result = apiInstance.createRoutine(routineCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRoutine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **routineCreate** | [**RoutineCreate**](RoutineCreate.md)|  | |

### Return type

[**Routine**](Routine.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Routine created by Routine Service. |  * Location -  <br>  * ETag -  <br>  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="deleteSession"></a>
# **deleteSession**
> deleteSession(ifMatch, routineId, sessionId)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteSession(ifMatch, routineId, sessionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | |
| **routineId** | **UUID**|  | |
| **sessionId** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Session deleted. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **412** | ETag precondition failed. |  -  |
| **428** | If-Match is required. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="getCurrentUser"></a>
# **getCurrentUser**
> GetCurrentUser200Response getCurrentUser()

Return minimal authenticated principal information.

### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      GetCurrentUser200Response result = apiInstance.getCurrentUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCurrentUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCurrentUser200Response**](GetCurrentUser200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authenticated identity claims safe for client display. |  -  |

<a id="getRoutine"></a>
# **getRoutine**
> Routine getRoutine(routineId)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      Routine result = apiInstance.getRoutine(routineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRoutine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **routineId** | **UUID**|  | |

### Return type

[**Routine**](Routine.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routine from Routine Service. |  * ETag -  <br>  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="getSession"></a>
# **getSession**
> Session getSession(routineId, sessionId)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    try {
      Session result = apiInstance.getSession(routineId, sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **routineId** | **UUID**|  | |
| **sessionId** | **UUID**|  | |

### Return type

[**Session**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session prescription. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="getSessionView"></a>
# **getSessionView**
> SessionView getSessionView(routineId, sessionId, historyLimit)

Compose a session prescription and recent exercise history.

### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    Integer historyLimit = 5; // Integer | 
    try {
      SessionView result = apiInstance.getSessionView(routineId, sessionId, historyLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSessionView");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **routineId** | **UUID**|  | |
| **sessionId** | **UUID**|  | |
| **historyLimit** | **Integer**|  | [optional] [default to 5] |

### Return type

[**SessionView**](SessionView.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session view composed from Routine Service exercise-records. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="listExerciseLogs"></a>
# **listExerciseLogs**
> ExerciseLogPage listExerciseLogs(exerciseName, sort, limit, cursor)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exerciseName = "exerciseName_example"; // String | 
    String sort = "loggedAt"; // String | 
    Integer limit = 20; // Integer | 
    String cursor = "cursor_example"; // String | 
    try {
      ExerciseLogPage result = apiInstance.listExerciseLogs(exerciseName, sort, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExerciseLogs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **exerciseName** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] [default to loggedAt] [enum: loggedAt, highestSetVolume] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |

### Return type

[**ExerciseLogPage**](ExerciseLogPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exercise log page. |  -  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="listExercises"></a>
# **listExercises**
> List&lt;ExerciseSummary&gt; listExercises()

List distinct exercise names from the user&#39;s log history.

### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<ExerciseSummary> result = apiInstance.listExercises();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExercises");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ExerciseSummary&gt;**](ExerciseSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Distinct exercises. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="listRoutines"></a>
# **listRoutines**
> RoutinePage listRoutines(limit, cursor, includeArchived)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 20; // Integer | 
    String cursor = "cursor_example"; // String | 
    Boolean includeArchived = false; // Boolean | 
    try {
      RoutinePage result = apiInstance.listRoutines(limit, cursor, includeArchived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRoutines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |
| **includeArchived** | **Boolean**|  | [optional] [default to false] |

### Return type

[**RoutinePage**](RoutinePage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routine page from Routine Service. |  -  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="listSnapshots"></a>
# **listSnapshots**
> List&lt;Snapshot&gt; listSnapshots(routineId)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      List<Snapshot> result = apiInstance.listSnapshots(routineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSnapshots");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **routineId** | **UUID**|  | |

### Return type

[**List&lt;Snapshot&gt;**](Snapshot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Up to two routine snapshots. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="replaceSession"></a>
# **replaceSession**
> Session replaceSession(ifMatch, routineId, sessionId, sessionWrite)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    SessionWrite sessionWrite = new SessionWrite(); // SessionWrite | 
    try {
      Session result = apiInstance.replaceSession(ifMatch, routineId, sessionId, sessionWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replaceSession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | |
| **routineId** | **UUID**|  | |
| **sessionId** | **UUID**|  | |
| **sessionWrite** | [**SessionWrite**](SessionWrite.md)|  | |

### Return type

[**Session**](Session.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session replaced. |  * ETag -  <br>  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **412** | ETag precondition failed. |  -  |
| **428** | If-Match is required. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

<a id="updateRoutine"></a>
# **updateRoutine**
> Routine updateRoutine(ifMatch, routineId, routinePatch)



### Example
```java
// Import classes:
import com.experiencequality.fitnessbff.invoker.ApiClient;
import com.experiencequality.fitnessbff.invoker.ApiException;
import com.experiencequality.fitnessbff.invoker.Configuration;
import com.experiencequality.fitnessbff.invoker.auth.*;
import com.experiencequality.fitnessbff.invoker.models.*;
import com.experiencequality.fitnessbff.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    RoutinePatch routinePatch = new RoutinePatch(); // RoutinePatch | 
    try {
      Routine result = apiInstance.updateRoutine(ifMatch, routineId, routinePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRoutine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | |
| **routineId** | **UUID**|  | |
| **routinePatch** | [**RoutinePatch**](RoutinePatch.md)|  | |

### Return type

[**Routine**](Routine.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated routine. |  * ETag -  <br>  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource not found or inaccessible. |  -  |
| **412** | ETag precondition failed. |  -  |
| **428** | If-Match is required. |  -  |
| **502** | Downstream response invalid or contract-incompatible. |  -  |
| **503** | Required downstream service unavailable. |  -  |

