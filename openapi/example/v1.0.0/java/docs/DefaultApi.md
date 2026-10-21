# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHealth**](DefaultApi.md#getHealth) | **GET** /health | Service health check |


<a id="getHealth"></a>
# **getHealth**
> HealthStatus getHealth()

Service health check

### Example
```java
// Import classes:
import com.experiencequality.example.invoker.ApiClient;
import com.experiencequality.example.invoker.ApiException;
import com.experiencequality.example.invoker.Configuration;
import com.experiencequality.example.invoker.models.*;
import com.experiencequality.example.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      HealthStatus result = apiInstance.getHealth();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getHealth");
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

[**HealthStatus**](HealthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service is healthy. |  -  |

