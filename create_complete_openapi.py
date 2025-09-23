#!/usr/bin/env python3
"""
Script to create the complete OpenAPI specification from the user's provided collection
"""
import json
import sys

# The complete OpenAPI specification provided by the user
COMPLETE_OPENAPI_SPEC = """{
  "openapi": "3.0.3",
  "info": {
    "title": "Weir AI APIs v1.0.0",
    "version": "1.0.0",
    "description": "Comprehensive API for Name, Image, and Likeness (NIL) detection and management platform",
    "contact": {
      "name": "Weir AI Support",
      "email": "support@weir.ai"
    }
  },
  "servers": [
    {
      "url": "https://{baseUrl}",
      "description": "Console/Base server",
      "variables": {
        "baseUrl": {
          "default": "api.example.com"
        }
      }
    },
    {
      "url": "https://{apiBaseUrl}",
      "description": "External API server",
      "variables": {
        "apiBaseUrl": {
          "default": "external.example.com"
        }
      }
    }
  ],
  "paths": {
    "/auth/token": {
      "post": {
        "summary": "Generate Access Token",
        "description": "Generate an access token for external API authentication using Basic Authentication",
        "operationId": "external_generate_access_token_post",
        "tags": [
          "External"
        ],
        "security": [
          {
            "basicAuth": []
          }
        ],
        "responses": {
          "200": {
            "description": "Access token generated successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "data": {
                      "type": "object",
                      "properties": {
                        "access_token": {
                          "type": "string"
                        },
                        "token_type": {
                          "type": "string",
                          "default": "Bearer"
                        },
                        "expires_in": {
                          "type": "integer",
                          "description": "Token expiration in seconds"
                        }
                      }
                    },
                    "message": {
                      "type": "string"
                    },
                    "timestamp": {
                      "type": "string",
                      "format": "date-time"
                    }
                  }
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized - Invalid credentials"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "JWT Bearer token authentication"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Basic authentication with username and password"
      }
    },
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "default": false
          },
          "error": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string"
              },
              "message": {
                "type": "string"
              },
              "details": {
                "type": "object"
              }
            }
          },
          "timestamp": {
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "SuccessResponse": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "default": true
          },
          "data": {
            "type": "object"
          },
          "message": {
            "type": "string"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time"
          }
        }
      }
    }
  },
  "tags": [
    {
      "name": "External",
      "description": "External APIs for third-party integrations"
    },
    {
      "name": "Console",
      "description": "Console APIs for organization and platform management"
    },
    {
      "name": "Admin",
      "description": "Admin APIs for system administration and monitoring"
    }
  ]
}"""

def main():
    """Create the complete OpenAPI specification file"""
    try:
        # Parse the JSON
        openapi_spec = json.loads(COMPLETE_OPENAPI_SPEC)
        
        # Write to file
        with open('v1.0.0/reference/openapi.json', 'w', encoding='utf-8') as f:
            json.dump(openapi_spec, f, indent=2)
        
        print("✅ OpenAPI specification created successfully!")
        print(f"📊 Total paths: {len(openapi_spec.get('paths', {}))}")
        print(f"📊 Total tags: {len(openapi_spec.get('tags', []))}")
        
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error creating OpenAPI file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
