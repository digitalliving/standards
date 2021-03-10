Standards for
[Data Products](https://github.com/digitalliving/standards/tree/master/draft/DataProducts)
must conform to the following set of rules:

## Standard specification format

Each standard must be described in corresponding JSON file, which is an OpenAPI 3.0
spec. Name of this file must be in UpperCamelCase.

## OpenAPI scheme

_Rules below are applied for each standard._

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

### Spec file must not define any severs

> ❌ Wrong: Server URLs provided

```json
{
  "servers": [{ "url": "https://example.com" }]
}
```

### Spec file must not define security section for API endpoint

> ❌ Wrong: Security section is defined for path

```json
{
  "paths": {
    "/AirQuality/Current": {
      "post": {
        "security": {
          "ApiKeyAuth": []
        }
      }
    }
  }
}
```
