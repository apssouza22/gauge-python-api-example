Authentication and authorizer spec
==============
Test the authorization and authentication


User should be able to authenticate with client credentials
----------
tags: all
* Authenticate with "r1HB7VWwr9ka3u9NuBGoLrZ7EMNu0mgq" and "M2xv0Kmw65g9_acQbV9j260N8HTbJ4-1h1E0mVUfGQDtBDEi8fAEmAafn3ewEghR"
* Validate returned access token


User should be able to access protected resources with access token
----------
tags: all
* Authenticate with "r1HB7VWwr9ka3u9NuBGoLrZ7EMNu0mgq" and "M2xv0Kmw65g9_acQbV9j260N8HTbJ4-1h1E0mVUfGQDtBDEi8fAEmAafn3ewEghR"
* Access protected resource with returned access token

User should be able to get access token with claims embedded
----------
tags: all
* Authenticate with "r1HB7VWwr9ka3u9NuBGoLrZ7EMNu0mgq" and "M2xv0Kmw65g9_acQbV9j260N8HTbJ4-1h1E0mVUfGQDtBDEi8fAEmAafn3ewEghR"
* Check that the access token contains the claims
