Standards for
[Data Products](https://github.com/digitalliving/standards/tree/master/draft/DataProducts)
must conform to the following set of rules:

_Note: the rules below assume that each standard is defined as an OpenAPI 3.0 spec file
in the corresponding path._

### Spec file must define only one POST endpoint

> ❌ Wrong: Two endpoints defined

```json
{
  "paths": {
    "/AirQuality/Current": { "post": {} },
    "/Company/BasicInfo": {}
  }
}
```

> ❌ Wrong: Endpoint has POST and GET method

```json
{
  "paths": {
    "/AirQuality/Current": { "post": {}, "get": {} }
  }
}
```

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": { "post": {} }
  }
}
```

### Spec file must include request body schema

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CurrentAirQualityRequest"
              }
            }
          },
          "required": true
        },
        "components": {
          "schemas": {
            "CurrentAirQualityRequest": {}
          }
        }
      }
    }
  }
}
```

### Spec file must include schema for successful (200 OK) response

> ❌ Wrong: Responses section is empty

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "responses": {}
      }
    }
  }
}
```

> ❌ Wrong: CurrentAirQualityResponse reference is missing

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CurrentAirQualityResponse"
                }
              }
            }
          }
        }
      },
      "components": {
        "schemas": {
          "CompanyBasicInfoRequest": {}
        }
      }
    }
  }
}
```

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CurrentAirQualityResponse"
                }
              }
            }
          }
        }
      },
      "components": {
        "schemas": {
          "CurrentAirQualityResponse": {}
        }
      }
    }
  }
}
```

### Schemas for request body and responses must be of `application/json` content type

> ❌ Wrong: Schema is by mistake defined for `multipart/form-data` content type

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/CurrentAirQualityRequest"
              }
            }
          },
          "required": true
        }
      }
    }
  }
}
```

> ✅ Correct

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CurrentAirQualityRequest"
              }
            }
          },
          "required": true
        }
      }
    }
  }
}
```
