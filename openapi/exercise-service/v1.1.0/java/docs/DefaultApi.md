# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExerciseLog**](DefaultApi.md#createExerciseLog) | **POST** /api/v1/exercise-logs | Create an exercise log for the authenticated user. |
| [**getExerciseLog**](DefaultApi.md#getExerciseLog) | **GET** /api/v1/exercise-logs/{exerciseLogId} | Get one exercise log owned by the authenticated user. |
| [**listDistinctExercises**](DefaultApi.md#listDistinctExercises) | **GET** /api/v1/exercise-logs/exercises | List distinct exercise names used by the authenticated user. |
| [**listExerciseLogs**](DefaultApi.md#listExerciseLogs) | **GET** /api/v1/exercise-logs | List the authenticated user&#39;s exercise logs. |


<a id="createExerciseLog"></a>
# **createExerciseLog**
> ExerciseLog createExerciseLog(createExerciseLogRequest)

Create an exercise log for the authenticated user.

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.auth.*;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

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

<a id="getExerciseLog"></a>
# **getExerciseLog**
> ExerciseLog getExerciseLog(exerciseLogId)

Get one exercise log owned by the authenticated user.

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.auth.*;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long exerciseLogId = 56L; // Long | 
    try {
      ExerciseLog result = apiInstance.getExerciseLog(exerciseLogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getExerciseLog");
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
| **exerciseLogId** | **Long**|  | |

### Return type

[**ExerciseLog**](ExerciseLog.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exercise log. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |
| **404** | Exercise log does not exist or is not owned by the authenticated principal. |  -  |

<a id="listDistinctExercises"></a>
# **listDistinctExercises**
> List&lt;ExerciseSummary&gt; listDistinctExercises()

List distinct exercise names used by the authenticated user.

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.auth.*;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<ExerciseSummary> result = apiInstance.listDistinctExercises();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDistinctExercises");
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
| **200** | Exercise usage summaries. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |

<a id="listExerciseLogs"></a>
# **listExerciseLogs**
> ExerciseLogPage listExerciseLogs(exerciseName, exerciseNames, sort, limit, cursor)

List the authenticated user&#39;s exercise logs.

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.auth.*;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exerciseName = "exerciseName_example"; // String | Case-insensitive exact exercise-name filter.
    List<String> exerciseNames = Arrays.asList(); // List<String> | Repeated query parameter; matches any supplied name case-insensitively.
    String sort = "loggedAt"; // String | 
    Integer limit = 20; // Integer | 
    String cursor = "cursor_example"; // String | 
    try {
      ExerciseLogPage result = apiInstance.listExerciseLogs(exerciseName, exerciseNames, sort, limit, cursor);
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
| **exerciseName** | **String**| Case-insensitive exact exercise-name filter. | [optional] |
| **exerciseNames** | [**List&lt;String&gt;**](String.md)| Repeated query parameter; matches any supplied name case-insensitively. | [optional] |
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
| **200** | Page of exercise logs. |  -  |
| **400** | Invalid request. |  -  |
| **401** | Missing, invalid, expired, or unacceptable access token. |  -  |

