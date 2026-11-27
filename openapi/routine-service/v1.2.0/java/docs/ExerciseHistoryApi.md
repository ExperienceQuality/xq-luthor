# ExerciseHistoryApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSessionExerciseRecords**](ExerciseHistoryApi.md#listSessionExerciseRecords) | **GET** /api/v1/routines/{routineId}/exercise-records |  |


<a id="listSessionExerciseRecords"></a>
# **listSessionExerciseRecords**
> ExerciseRecordPage listSessionExerciseRecords(sessionId, routineId, limit, cursor)



Reads the session definition and composes matching exercise logs from Exercise Service. The caller&#39;s delegated identity must be propagated to Exercise Service. 

### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.auth.*;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.ExerciseHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ExerciseHistoryApi apiInstance = new ExerciseHistoryApi(defaultClient);
    UUID sessionId = UUID.randomUUID(); // UUID | 
    UUID routineId = UUID.randomUUID(); // UUID | 
    Integer limit = 20; // Integer | 
    String cursor = "cursor_example"; // String | 
    try {
      ExerciseRecordPage result = apiInstance.listSessionExerciseRecords(sessionId, routineId, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExerciseHistoryApi#listSessionExerciseRecords");
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

[**ExerciseRecordPage**](ExerciseRecordPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exercise records matching the session&#39;s exercise references. |  -  |
| **400** | Request validation failed. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Resource does not exist or is not owned by the authenticated principal. |  -  |
| **502** | Downstream response was invalid. |  -  |
| **503** | Exercise Service unavailable; Retry-After may be present. |  * Retry-After -  <br>  |

