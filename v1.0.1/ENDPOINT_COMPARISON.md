# Endpoint Comparison: v1.0.1 Postman Collection vs Documentation

## Summary

**Postman Collection v1.0.1**: 61 unique Weir API endpoints (excluding Twitter/X test requests)
**Documented in v1.0.1**: 66 endpoint files (includes shared auth endpoints used by both Console and Admin)

## Endpoints in Postman Collection

### External APIs (1)
- ✅ POST /auth/token - Generate Access Token

### Console APIs (34)

**Team Management (6)**
- ✅ POST /org/create/team
- ✅ GET /org/teams
- ✅ DELETE /org/team/:teamId
- ✅ POST /org/invite/team/member/:teamId
- ✅ GET /org/team/members/:teamId
- ✅ PATCH /org/team/:teamId/member/:memberId

**Authentication (4)** 
- ✅ POST /auth/m/register - Mobile Register
- ✅ POST /auth/validate/registration
- ✅ POST /auth/register
- ✅ PUT /auth/resend/otp/:session

**Organization Management (8)**
- ✅ GET /org/information
- ✅ PATCH /org/information
- ✅ GET /org/bill/history
- ✅ POST /org/subscribe
- ✅ GET /org/subscriptions
- ✅ GET /org/cards
- ✅ POST /org/card
- ✅ DELETE /org/card/:cardId

**Platform Management (4)**
- ✅ POST /org/create/platform
- ✅ GET /org/platforms
- ✅ DELETE /org/platform/:platformId
- ✅ GET /org/verify/platform/:platformId

**Client Management (4)**
- ✅ POST /org/create/client
- ✅ GET /org/clients
- ✅ PATCH /org/refresh/client
- ✅ DELETE /org/client/:clientId

**Talent Management (7)**
- ✅ GET /org/talent/roster
- ✅ POST /org/invite/talent
- ✅ GET /org/talent/name/search
- ✅ GET /org/licenses
- ✅ POST /org/talent/license/:talentId
- ✅ PATCH /org/talent/license/:licenseId/image
- ✅ DELETE /org/talent/license/{licenseId}/image/{imageId}

**User Management (2)**
- ✅ PATCH /user/profile
- ✅ PATCH /user/change/password

**Note**: Console Auth endpoints (Login, Logout, Refresh Token) are documented but shared with Admin Auth or use noauth.

### Admin APIs (26)

**Authentication (4)**
- ✅ POST /auth/authenticateAdmin
- ✅ POST /auth/login (Admin)
- ✅ POST /auth/refresh/token (Admin)
- ✅ POST /auth/logout (Admin)

**User Management (3)**
- ✅ POST /auth/register (Create Admin)
- ✅ GET /admin/members
- ✅ POST /admin/member/invite

**System Management (3)**
- ✅ GET /admin/organizations
- ✅ GET /admin/platforms
- ✅ GET /admin/licenses

**Mail Management (4)**
- ✅ POST /mail/create/template
- ✅ GET /mail/templates
- ✅ PUT /mail/template/:id
- ✅ DELETE /mail/template/:id

**Pod Management (9)**
- ✅ POST /pax/pod
- ✅ GET /pax/pods
- ✅ GET /pax/pod/:podId
- ✅ POST /pax/start/pod/:podId
- ✅ POST /pax/pause/pod/:podId
- ✅ POST /pax/stop/pod/:podId
- ✅ POST /pax/start/pods
- ✅ POST /pax/pause/pods
- ✅ POST /pax/stop/pods

**Logging (3)**
- ✅ POST /logs/log
- ✅ GET /logs/search
- ✅ GET /logs/all

## Potentially Missing from v1.0.1 (But in v1.0.0)

Endpoints that exist in v1.0.0 documentation but not in v1.0.1 Postman collection:

1. ❓ GET /platforms/{platformId} - Get Platform Details
2. ❓ POST /mail/send - Send Email
3. ❓ GET /mail/status/:id - Get Email Status
4. ❓ GET /pax (or /pax/get) - Get PAX (different from pods?)
5. ❓ POST /pax - Create PAX (different from pods?)
6. ❓ GET /logs/:id - Get Log Details
7. ❓ POST /logs/export - Export Logs
8. ❓ POST /external/validate/key - Validate API Key
9. ❓ GET /talent - Get Talent (different from roster?)
10. ❓ GET /talent/:id - Get Talent Profile

## Questions to Clarify

1. **Are PAX and Pods the same thing?** v1.0.0 has PAX endpoints, v1.0.1 Postman has Pod endpoints
2. **Should v1.0.1 include mail sending endpoints?** Not in Postman collection but in v1.0.0
3. **Are there talent profile endpoints?** v1.0.0 has get talent/profile, not in v1.0.1 collection
4. **Should there be console logging endpoints?** v1.0.0 has console logs, v1.0.1 only has admin logs
5. **Missing GET /user/profile?** I documented it but it's not explicitly in the Postman collection

## Recommendations

Please clarify:
1. Should I port relevant endpoints from v1.0.0 to v1.0.1?
2. Are there additional endpoints beyond the Postman collection?
3. Is there another API specification document I should reference?
4. Should Console APIs have Login/Logout/Refresh documented separately from shared auth?

---

**Current Status**: All 61 endpoints from Postman collection are documented (66 total including shared/additional auth endpoints)
