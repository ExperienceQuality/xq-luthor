# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRoutineSession**](DefaultApi.md#addRoutineSession) | **POST** /api/v1/routines/{routineId}/sessions | Add an ordered session |
| [**archiveRoutine**](DefaultApi.md#archiveRoutine) | **DELETE** /api/v1/routines/{routineId} | Archive a routine |
| [**createRoutine**](DefaultApi.md#createRoutine) | **POST** /api/v1/routines | Create a routine |
| [**deleteRoutineSession**](DefaultApi.md#deleteRoutineSession) | **DELETE** /api/v1/routines/{routineId}/sessions/{sessionId} | Delete a session |
| [**getRoutine**](DefaultApi.md#getRoutine) | **GET** /api/v1/routines/{routineId} | Get a routine |
| [**getRoutineSession**](DefaultApi.md#getRoutineSession) | **GET** /api/v1/routines/{routineId}/sessions/{sessionId} | Get a routine session |
| [**listExerciseRecords**](DefaultApi.md#listExerciseRecords) | **GET** /api/v1/routines/{routineId}/exercise-records | Compose exercise records for a session |
| [**listRoutines**](DefaultApi.md#listRoutines) | **GET** /api/v1/routines | List routines |
| [**liveness**](DefaultApi.md#liveness) | **GET** /livez | Check liveness |
| [**readiness**](DefaultApi.md#readiness) | **GET** /readyz | Check readiness |
| [**replaceRoutineSession**](DefaultApi.md#replaceRoutineSession) | **PUT** /api/v1/routines/{routineId}/sessions/{sessionId} | Replace a session |
| [**updateRoutine**](DefaultApi.md#updateRoutine) | **PATCH** /api/v1/routines/{routineId} | Update routine metadata |


<a id="addRoutineSession"></a>
# **addRoutineSession**
> Session addRoutineSession(ifMatch, routineId, sessionRequest)

Add an ordered session

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    SessionRequest sessionRequest = new SessionRequest(); // SessionRequest | 
    try {
      Session result = apiInstance.addRoutineSession(ifMatch, routineId, sessionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addRoutineSession");
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
| **sessionRequest** | [**SessionRequest**](SessionRequest.md)|  | |

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Session added. |  -  |
| **400** | Request validation failed. |  -  |
| **412** | ETag precondition failed. |  -  |

<a id="archiveRoutine"></a>
# **archiveRoutine**
> archiveRoutine(ifMatch, routineId)

Archive a routine

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Routine archived. |  -  |
| **404** | Resource not found. |  -  |
| **412** | ETag precondition failed. |  -  |

<a id="createRoutine"></a>
# **createRoutine**
> Routine createRoutine(routineRequest)

Create a routine

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RoutineRequest routineRequest = new RoutineRequest(); // RoutineRequest | 
    try {
      Routine result = apiInstance.createRoutine(routineRequest);
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
| **routineRequest** | [**RoutineRequest**](RoutineRequest.md)|  | |

### Return type

[**Routine**](Routine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Routine created. |  * Location -  <br>  * ETag -  <br>  |
| **400** | Request validation failed. |  -  |

<a id="deleteRoutineSession"></a>
# **deleteRoutineSession**
> deleteRoutineSession(ifMatch, routineId, sessionId)

Delete a session

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteRoutineSession(ifMatch, routineId, sessionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRoutineSession");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Session deleted. |  -  |
| **404** | Resource not found. |  -  |
| **412** | ETag precondition failed. |  -  |

<a id="getRoutine"></a>
# **getRoutine**
> Routine getRoutine(routineId)

Get a routine

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routine details. |  -  |
| **404** | Resource not found. |  -  |

<a id="getRoutineSession"></a>
# **getRoutineSession**
> Session getRoutineSession(routineId, sessionId)

Get a routine session

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    try {
      Session result = apiInstance.getRoutineSession(routineId, sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRoutineSession");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session details. |  -  |
| **404** | Resource not found. |  -  |

<a id="listExerciseRecords"></a>
# **listExerciseRecords**
> RecordPage listExerciseRecords(sessionId, routineId, limit, cursor)

Compose exercise records for a session

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID sessionId = UUID.randomUUID(); // UUID | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    Integer limit = 20; // Integer | 
    String cursor = "cursor_example"; // String | 
    try {
      RecordPage result = apiInstance.listExerciseRecords(sessionId, routineId, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExerciseRecords");
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
| **sessionId** | **UUID**|  | |
| **routineId** | **UUID**|  | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**|  | [optional] |

### Return type

[**RecordPage**](RecordPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Composed exercise records. |  -  |
| **400** | Request validation failed. |  -  |
| **404** | Resource not found. |  -  |
| **502** | Downstream response was invalid. |  -  |
| **503** | Downstream service unavailable. |  -  |

<a id="listRoutines"></a>
# **listRoutines**
> RoutinePage listRoutines(limit, includeArchived, cursor)

List routines

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 20; // Integer | 
    Boolean includeArchived = false; // Boolean | 
    String cursor = "cursor_example"; // String | 
    try {
      RoutinePage result = apiInstance.listRoutines(limit, includeArchived, cursor);
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
| **includeArchived** | **Boolean**|  | [optional] [default to false] |
| **cursor** | **String**|  | [optional] |

### Return type

[**RoutinePage**](RoutinePage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routine page. |  -  |
| **400** | Request validation failed. |  -  |

<a id="liveness"></a>
# **liveness**
> liveness()

Check liveness

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.liveness();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#liveness");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service is alive. |  -  |

<a id="readiness"></a>
# **readiness**
> readiness()

Check readiness

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.readiness();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#readiness");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service is ready. |  -  |

<a id="replaceRoutineSession"></a>
# **replaceRoutineSession**
> Session replaceRoutineSession(ifMatch, routineId, sessionId, sessionRequest)

Replace a session

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    SessionRequest sessionRequest = new SessionRequest(); // SessionRequest | 
    try {
      Session result = apiInstance.replaceRoutineSession(ifMatch, routineId, sessionId, sessionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replaceRoutineSession");
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
| **sessionRequest** | [**SessionRequest**](SessionRequest.md)|  | |

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session replaced. |  -  |
| **404** | Resource not found. |  -  |
| **412** | ETag precondition failed. |  -  |

<a id="updateRoutine"></a>
# **updateRoutine**
> Routine updateRoutine(ifMatch, routineId, routinePatch)

Update routine metadata

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routine updated. |  * ETag -  <br>  |
| **400** | Request validation failed. |  -  |
| **404** | Resource not found. |  -  |
| **412** | ETag precondition failed. |  -  |

