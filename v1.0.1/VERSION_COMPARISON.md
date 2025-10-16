# API Version Comparison: v1.0.0 vs v1.0.1

## Summary Statistics

| Metric | v1.0.0 | v1.0.1 | Change |
|--------|--------|--------|--------|
| **Total Documented Endpoints** | 75 files | 66 files | -9 |
| **Unique to v1.0.0** | ~20 | - | Removed/Deprecated |
| **Unique to v1.0.1** | - | ~11 | New Features |
| **Common** | ~55 | ~55 | Maintained |

## Detailed Comparison

### 🟢 Common Endpoints (Present in Both Versions)

| Category | Endpoint | Method | Path |
|----------|----------|--------|------|
| **External APIs** |
| External | Generate Access Token | POST | /auth/token |
| **Console APIs - Authentication** |
| Auth | Register | POST | /auth/register |
| Auth | Mobile Register | POST | /auth/m/register |
| Auth | Validate Registration | POST | /auth/validate/registration |
| Auth | Resend OTP | PUT | /auth/resend/otp/:session |
| Auth | Login | POST | /auth/login |
| **Console APIs - Teams** |
| Teams | Create Team | POST | /org/create/team |
| Teams | Get Teams | GET | /org/teams |
| Teams | Delete Team | DELETE | /org/team/:teamId |
| Teams | Invite Member | POST | /org/invite/team/member/:teamId |
| Teams | Get Members | GET | /org/team/members/:teamId |
| **Console APIs - Organization** |
| Organization | Get Info | GET | /org/information |
| Organization | Update Info | PATCH | /org/information |
| Organization | Get Cards | GET | /org/cards |
| Organization | Add Card | POST | /org/card |
| **Console APIs - Platforms** |
| Platforms | Create Platform | POST | /org/create/platform |
| Platforms | Get Platforms | GET | /org/platforms |
| Platforms | Delete Platform | DELETE | /org/platform/:platformId |
| Platforms | Verify Platform | GET | /org/verify/platform/:platformId |
| **Console APIs - Clients** |
| Clients | Create Client | POST | /org/create/client |
| Clients | Get Clients | GET | /org/clients |
| **Admin APIs - Authentication** |
| Admin Auth | Login | POST | /auth/login |
| Admin Auth | Logout | POST | /auth/logout |
| Admin Auth | Refresh Token | POST | /auth/refresh/token |
| **Admin APIs - User Management** |
| Admin Users | Get Members | GET | /admin/members |
| Admin Users | Invite Member | POST | /admin/member/invite |
| Admin Users | Create Admin | POST | /auth/register |
| **Admin APIs - System** |
| Admin System | Get Organizations | GET | /admin/organizations |
| Admin System | Get Platforms | GET | /admin/platforms |
| Admin System | Get Licenses | GET | /admin/licenses |
| **Admin APIs - Mail** |
| Admin Mail | Create Template | POST | /mail/create/template |
| Admin Mail | Get Templates | GET | /mail/templates |
| Admin Mail | Update Template | PUT | /mail/template/:id |
| Admin Mail | Delete Template | DELETE | /mail/template/:id |
| **Admin APIs - Pods** |
| Admin Pods | Create Pod | POST | /pax/pod |
| Admin Pods | Get Pods | GET | /pax/pods |
| Admin Pods | Get Pod | GET | /pax/pod/:podId |
| Admin Pods | Start Pod | POST | /pax/start/pod/:podId |
| Admin Pods | Pause Pod | POST | /pax/pause/pod/:podId |
| Admin Pods | Stop Pod | POST | /pax/stop/pod/:podId |
| Admin Pods | Start All Pods | POST | /pax/start/pods |
| Admin Pods | Pause All Pods | POST | /pax/pause/pods |
| Admin Pods | Stop All Pods | POST | /pax/stop/pods |

---

### 🔴 Only in v1.0.0 (Removed/Not in v1.0.1 Postman Collection)

| Category | Endpoint | Notes |
|----------|----------|-------|
| **External APIs** |
| External | Validate API Key | Possibly deprecated or merged into token endpoint |
| **Console APIs - Logging** |
| Console Logs | Get Logs | Moved to Admin APIs in v1.0.1 |
| Console Logs | Get Log Details | Moved to Admin APIs or removed |
| Console Logs | Export Logs | Not in v1.0.1 Postman collection |
| **Console APIs - Mail** |
| Console Mail | Send Email | Not in v1.0.1 Postman collection (may be in different API) |
| Console Mail | Get Email Status | Not in v1.0.1 Postman collection |
| **Console APIs - PAX** |
| Console PAX | Create PAX | Possibly renamed to Pods or moved to Admin |
| Console PAX | Get PAX | Possibly renamed to Pods or moved to Admin |
| **Console APIs - Talent** |
| Console Talent | Get Talent | Replaced with Get Talent Roster |
| Console Talent | Get Talent Profile | Not in v1.0.1 Postman collection |
| **Console APIs - Platforms** |
| Platforms | Get Platform Details | Not in v1.0.1 Postman collection (may be merged) |
| **Others** |
| Various | ~10 additional endpoints | Check if deprecated or moved |

---

### 🟢 Only in v1.0.1 (New Features)

| Category | Endpoint | Description |
|----------|----------|-------------|
| **Console APIs - Authentication** |
| Auth | Logout | POST /auth/logout | Explicitly added for Console |
| Auth | Refresh Token | POST /auth/refresh/token | Explicitly added for Console |
| **Console APIs - Teams** |
| Teams | Update Member Role | PATCH /org/team/:teamId/member/:memberId | New role management |
| **Console APIs - Organization** |
| Organization | Get Billing History | GET /org/bill/history | New billing features |
| Organization | Subscribe | POST /org/subscribe | New subscription management |
| Organization | Get Subscriptions | GET /org/subscriptions | New subscription plans |
| Organization | Delete Card | DELETE /org/card/:cardId | Enhanced card management |
| **Console APIs - Clients** |
| Clients | Refresh Client | PATCH /org/refresh/client | New credential rotation |
| Clients | Delete Client | DELETE /org/client/:clientId | Enhanced client management |
| **Console APIs - Talent** |
| Talent | Get Talent Roster | GET /org/talent/roster | Replaces Get Talent |
| Talent | Invite Talent | POST /org/invite/talent | New talent invitation |
| Talent | Search Talent | GET /org/talent/name/search | New search capability |
| Talent | Get Licenses | GET /org/licenses | New license management |
| Talent | Create License | POST /org/talent/license/:talentId | New NIL license creation |
| Talent | Add License Images | PATCH /org/talent/license/:licenseId/image | New image management |
| Talent | Remove License Image | DELETE /org/talent/license/{licenseId}/image/{imageId} | New image management |
| **Console APIs - Users** |
| Users | Get Profile | GET /user/profile | New user profile endpoint |
| Users | Update Profile | PATCH /user/profile | New profile management |
| Users | Change Password | PATCH /user/change/password | New password management |
| **Admin APIs - Authentication** |
| Admin Auth | Authenticate Admin | POST /auth/authenticateAdmin | New admin auth method |
| **Admin APIs - Logging** |
| Admin Logging | Create Log | POST /logs/log | New logging capability |
| Admin Logging | Search Logs | GET /logs/search | Enhanced log search |
| Admin Logging | Get All Logs | GET /logs/all | Comprehensive log retrieval |

---

## Key Changes in v1.0.1

### ✅ Enhancements

1. **Talent Management (Major Addition)**
   - Full NIL license management
   - Talent roster management
   - License image management
   - Talent invitation and search

2. **User Management (New)**
   - User profile endpoints
   - Password management
   - Profile updates

3. **Enhanced Subscription & Billing**
   - Billing history
   - Subscription management
   - Card management improvements

4. **Enhanced Team Management**
   - Member role updates
   - Better member management

5. **Comprehensive Logging**
   - Admin-focused logging
   - Search and filter capabilities
   - Log creation API

### ❌ Removals/Changes

1. **Console Logging Moved**
   - Logging moved from Console to Admin APIs
   - More appropriate for admin oversight

2. **Mail Sending Removed from Console**
   - Console mail endpoints removed
   - May be in a separate service or deprecated

3. **PAX Terminology**
   - PAX possibly renamed to Pods
   - Consolidated under Admin APIs

4. **External API Validation**
   - Validate API Key endpoint not in v1.0.1
   - May be handled differently

5. **Talent Endpoints Restructured**
   - Get Talent and Get Talent Profile replaced
   - New roster-based approach

---

## Migration Guide

### Endpoints to Update

| v1.0.0 Endpoint | v1.0.1 Equivalent | Action Required |
|-----------------|-------------------|-----------------|
| GET /talent | GET /org/talent/roster | Update path and handle response changes |
| GET /talent/:id | Search via /org/talent/name/search | Update logic to use search |
| Console /logs/\* | Admin /logs/\* | Switch to Admin APIs with admin auth |
| /pax/\* (Console) | /pax/\* (Admin) | Use Admin authentication |
| POST /mail/send (Console) | Not in v1.0.1 | Check alternative or use external service |
| GET /external/validate/key | Not in v1.0.1 | Use token generation flow |

### New Capabilities in v1.0.1

- ✅ NIL License Management (7 new endpoints)
- ✅ User Profile Management (3 new endpoints)
- ✅ Enhanced Billing & Subscriptions (3 new endpoints)
- ✅ Comprehensive Logging (3 new endpoints)
- ✅ Client Credential Rotation (1 new endpoint)
- ✅ Team Member Role Management (1 new endpoint)

---

## Recommendations

### For v1.0.0 Users Migrating to v1.0.1

1. **Review Talent Endpoints**: Major restructuring in talent management
2. **Update Logging**: Move from Console to Admin APIs
3. **Check Mail Functionality**: Console mail endpoints removed
4. **Verify PAX/Pods**: Confirm terminology and access patterns
5. **Add NIL License Support**: Leverage new license management features
6. **Implement User Profiles**: Use new user management endpoints

### Missing from Both Versions

Consider if these should be added:
- Forgot Password flow endpoints (if not using external service)
- Email verification resend (beyond OTP)
- Two-factor authentication
- API key management (beyond client credentials)
- Webhook management
- Rate limit status endpoints
- Health check / status endpoints

---

## Conclusion

**v1.0.1 represents a significant evolution** with:
- **Major additions**: Talent/NIL license management, user profiles, enhanced billing
- **Consolidation**: Logging and pod management moved to Admin APIs
- **Deprecations**: Some Console endpoints removed or restructured
- **Total**: 66 documented endpoints (vs 75 files in v1.0.0)

The v1.0.1 API is more focused and better organized, with clear separation between Console and Admin functionalities.

---

**Note**: Some v1.0.0 endpoints may have been placeholders or deprecated. The v1.0.1 Postman collection represents the current production API state.
