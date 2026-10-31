# SnapshotsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**captureSnapshot**](SnapshotsApi.md#captureSnapshot) | **POST** /api/v1/routines/{routineId}/snapshots |  |
| [**getSnapshot**](SnapshotsApi.md#getSnapshot) | **GET** /api/v1/routines/{routineId}/snapshots/{snapshotId} |  |
| [**listSnapshots**](SnapshotsApi.md#listSnapshots) | **GET** /api/v1/routines/{routineId}/snapshots |  |


<a id="captureSnapshot"></a>
# **captureSnapshot**
> Snapshot captureSnapshot(ifMatch, idempotencyKey, routineId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      Snapshot result = apiInstance.captureSnapshot(ifMatch, idempotencyKey, routineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#captureSnapshot");
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
| **201** | Snapshot captured; older snapshots beyond retention are pruned atomically. |  * ETag -  <br>  * Location -  <br>  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **409** | Domain conflict, such as an archived routine. |  -  |
| **412** | If-Match does not match the current routine version. |  -  |
| **428** | Required If-Match header is missing. |  -  |

<a id="getSnapshot"></a>
# **getSnapshot**
> Snapshot getSnapshot(routineId, snapshotId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    UUID snapshotId = UUID.randomUUID(); // UUID | 
    try {
      Snapshot result = apiInstance.getSnapshot(routineId, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#getSnapshot");
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
| **snapshotId** | **UUID**|  | |

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
| **200** | Snapshot details. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |

<a id="listSnapshots"></a>
# **listSnapshots**
> List&lt;Snapshot&gt; listSnapshots(routineId)



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    UUID routineId = UUID.randomUUID(); // UUID | 
    try {
      List<Snapshot> result = apiInstance.listSnapshots(routineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#listSnapshots");
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
| **200** | Up to the two most recent snapshots, newest first. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |

