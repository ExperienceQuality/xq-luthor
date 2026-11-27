# RoutinesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**archiveRoutine**](RoutinesApi.md#archiveRoutine) | **DELETE** /api/v1/routines/{routineId} |  |
| [**createRoutine**](RoutinesApi.md#createRoutine) | **POST** /api/v1/routines |  |
| [**getRoutine**](RoutinesApi.md#getRoutine) | **GET** /api/v1/routines/{routineId} |  |
| [**listRoutines**](RoutinesApi.md#listRoutines) | **GET** /api/v1/routines |  |
| [**updateRoutine**](RoutinesApi.md#updateRoutine) | **PATCH** /api/v1/routines/{routineId} |  |


<a id="archiveRoutine"></a>
# **archiveRoutine**
> archiveRoutine(ifMatch, routineId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.RoutinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RoutinesApi apiInstance = new RoutinesApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.archiveRoutine(ifMatch, routineId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutinesApi#archiveRoutine");
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
| **204** | Routine archived; children are retained. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **412** | If-Match does not match the current routine version. |  -  |
| **428** | Required If-Match header is missing. |  -  |

<a id="createRoutine"></a>
# **createRoutine**
> Routine createRoutine(routineCreate)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.RoutinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RoutinesApi apiInstance = new RoutinesApi(defaultClient);
    RoutineCreate routineCreate = new RoutineCreate(); // RoutineCreate | 
    try {
      Routine result = apiInstance.createRoutine(routineCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutinesApi#createRoutine");
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
| **201** | Routine created. |  * Location -  <br>  * ETag -  <br>  |
| **400** | Request validation failed. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |

<a id="getRoutine"></a>
# **getRoutine**
> Routine getRoutine(routineId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.RoutinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RoutinesApi apiInstance = new RoutinesApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      Routine result = apiInstance.getRoutine(routineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutinesApi#getRoutine");
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
| **200** | Routine details. |  * ETag -  <br>  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |

<a id="listRoutines"></a>
# **listRoutines**
> RoutinePage listRoutines(limit, cursor, includeArchived)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.RoutinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RoutinesApi apiInstance = new RoutinesApi(defaultClient);
    Integer limit = 20; // Integer | 
    String cursor = "cursor_example"; // String | 
    Boolean includeArchived = false; // Boolean | 
    try {
      RoutinePage result = apiInstance.listRoutines(limit, cursor, includeArchived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutinesApi#listRoutines");
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
| **200** | Page of routines owned by the authenticated principal. |  -  |
| **400** | Request validation failed. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |

<a id="updateRoutine"></a>
# **updateRoutine**
> Routine updateRoutine(ifMatch, routineId, routinePatch)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.RoutinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RoutinesApi apiInstance = new RoutinesApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    RoutinePatch routinePatch = new RoutinePatch(); // RoutinePatch | 
    try {
      Routine result = apiInstance.updateRoutine(ifMatch, routineId, routinePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutinesApi#updateRoutine");
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
| **200** | Routine updated. |  * ETag -  <br>  |
| **400** | Request validation failed. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **412** | If-Match does not match the current routine version. |  -  |
| **428** | Required If-Match header is missing. |  -  |

