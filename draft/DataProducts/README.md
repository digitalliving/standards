Standards for
[Data Products](https://github.com/digitalliving/standards/tree/master/draft/DataProducts)
must conform to the following set of rules:

## Required files per standard

Each standard must be described in 3 files:

- `<standard_name>.json` - OpenAPI spec defining POST route for the standard
- `<standard_name>.jsonld` - [JSON-LD](https://json-ld.org) definition of standard
  attributes
- `<standard_name>.html` - Human representation of OpenAPI spec. For example, web page
  using [Swagger UI](https://swagger.io/tools/swagger-ui/)

## OpenAPI scheme

_Note: the rules below apply for OpenAPI 3.0 spec files of each standard._

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
