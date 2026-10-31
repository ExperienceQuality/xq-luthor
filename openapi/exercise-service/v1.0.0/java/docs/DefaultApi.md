# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExerciseLog**](DefaultApi.md#createExerciseLog) | **POST** /api/v1/exercise-logs | Create an exercise log |
| [**getExerciseLog**](DefaultApi.md#getExerciseLog) | **GET** /api/v1/exercise-logs/{exerciseLogId} | Get one exercise log |
| [**listDistinctExercises**](DefaultApi.md#listDistinctExercises) | **GET** /api/v1/exercise-logs/exercises | List distinct exercises |
| [**listExerciseLogs**](DefaultApi.md#listExerciseLogs) | **GET** /api/v1/exercise-logs | List exercise logs |


<a id="createExerciseLog"></a>
# **createExerciseLog**
> ExerciseLog createExerciseLog(createExerciseLogRequest)

Create an exercise log

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Exercise log created |  * Location -  <br>  |
| **400** | Invalid request |  -  |
| **409** | Request conflicts with persisted data |  -  |

<a id="getExerciseLog"></a>
# **getExerciseLog**
> ExerciseLog getExerciseLog(exerciseLogId)

Get one exercise log

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exercise log |  -  |
| **400** | Invalid request |  -  |
| **404** | Exercise log not found |  -  |

<a id="listDistinctExercises"></a>
# **listDistinctExercises**
> List&lt;ExerciseSummary&gt; listDistinctExercises()

List distinct exercises

Returns unique exercise names with log counts and latest log timestamps.

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Distinct exercises |  -  |

<a id="listExerciseLogs"></a>
# **listExerciseLogs**
> List&lt;ExerciseLog&gt; listExerciseLogs(exerciseName, sort, limit)

List exercise logs

### Example
```java
// Import classes:
import com.experiencequality.exerciseservice.invoker.ApiClient;
import com.experiencequality.exerciseservice.invoker.ApiException;
import com.experiencequality.exerciseservice.invoker.Configuration;
import com.experiencequality.exerciseservice.invoker.models.*;
import com.experiencequality.exerciseservice.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exerciseName = "exerciseName_example"; // String | Case-insensitive exercise-name filter.
    String sort = "loggedAt"; // String | 
    Integer limit = 20; // Integer | 
    try {
      List<ExerciseLog> result = apiInstance.listExerciseLogs(exerciseName, sort, limit);
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
| **exerciseName** | **String**| Case-insensitive exercise-name filter. | [optional] |
| **sort** | **String**|  | [optional] [default to loggedAt] [enum: loggedAt, highestSetVolume] |
| **limit** | **Integer**|  | [optional] [default to 20] |

### Return type

[**List&lt;ExerciseLog&gt;**](ExerciseLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exercise logs |  -  |
| **400** | Invalid request |  -  |

