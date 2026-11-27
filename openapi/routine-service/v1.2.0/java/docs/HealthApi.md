# HealthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**liveness**](HealthApi.md#liveness) | **GET** /livez |  |
| [**readiness**](HealthApi.md#readiness) | **GET** /readyz |  |


<a id="liveness"></a>
# **liveness**
> liveness()



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.liveness();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#liveness");
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



### Example
```java
// Import classes:
import com.experiencequality.routineservice.invoker.ApiClient;
import com.experiencequality.routineservice.invoker.ApiException;
import com.experiencequality.routineservice.invoker.Configuration;
import com.experiencequality.routineservice.invoker.models.*;
import com.experiencequality.routineservice.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.readiness();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#readiness");
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

