# SessionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSession**](SessionsApi.md#addSession) | **POST** /api/v1/routines/{routineId}/sessions |  |
| [**deleteSession**](SessionsApi.md#deleteSession) | **DELETE** /api/v1/routines/{routineId}/sessions/{sessionId} |  |
| [**getSession**](SessionsApi.md#getSession) | **GET** /api/v1/routines/{routineId}/sessions/{sessionId} |  |
| [**replaceSession**](SessionsApi.md#replaceSession) | **PUT** /api/v1/routines/{routineId}/sessions/{sessionId} |  |


<a id="addSession"></a>
# **addSession**
> Session addSession(ifMatch, routineId, sessionWrite)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    SessionWrite sessionWrite = new SessionWrite(); // SessionWrite | 
    try {
      Session result = apiInstance.addSession(ifMatch, routineId, sessionWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#addSession");
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
| **400** | Request validation failed. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **409** | Domain conflict, such as an archived routine. |  -  |
| **412** | If-Match does not match the current routine version. |  -  |
| **428** | Required If-Match header is missing. |  -  |

<a id="deleteSession"></a>
# **deleteSession**
> deleteSession(ifMatch, routineId, sessionId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteSession(ifMatch, routineId, sessionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#deleteSession");
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
| **204** | Session deleted and remaining positions compacted. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **412** | If-Match does not match the current routine version. |  -  |
| **428** | Required If-Match header is missing. |  -  |

<a id="getSession"></a>
# **getSession**
> Session getSession(routineId, sessionId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    try {
      Session result = apiInstance.getSession(routineId, sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#getSession");
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
| **200** | Session details. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |

<a id="replaceSession"></a>
# **replaceSession**
> Session replaceSession(ifMatch, routineId, sessionId, sessionWrite)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID sessionId = UUID.randomUUID(); // UUID | 
    SessionWrite sessionWrite = new SessionWrite(); // SessionWrite | 
    try {
      Session result = apiInstance.replaceSession(ifMatch, routineId, sessionId, sessionWrite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#replaceSession");
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
| **400** | Request validation failed. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **409** | Domain conflict, such as an archived routine. |  -  |
| **412** | If-Match does not match the current routine version. |  -  |
| **428** | Required If-Match header is missing. |  -  |

