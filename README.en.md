# ShellRPG-cdn · v0.8.0

`ShellRPG-cdn` is exclusively the public **image endpoint for ShellRPG-www**.
It does not host authoritative game logic, Wiki content, client distribution,
or general application/download files.

Active payload scope:

```text
assets/www/public/media/**
```

Only WWW-approved image formats are accepted (PNG, JPEG, GIF, WebP, SVG, and
ICO).

## Maintenance Note

- For relevant content, contract, feature, or editorial changes touching this
  endpoint, keep `README.md`, `README.en.md`, and `VERSION` aligned.

## Active delivery path

- GitHub-backed primary base for WWW images:
  `https://cdn.jsdelivr.net/gh/RPG-Wulf/ShellRPG-cdn@main/assets/www`
- `scripts/sync_workspace_assets.py` reads only `ShellRPG-www/public/media`
  and copies only image files into `assets/www/public/media`.
- No public write interface is provided. Population is performed only by the
  controlled WWW/deployment pipeline.
- A dynv6 fallback may be configured locally or in deployment, but it must be
  proven reachable over DNS and HTTPS before cutover.

## Explicitly out of scope

- Wiki content or Wiki-owned assets on this CDN
- `ShellRPG-client` as a CDN source or consumer
- JavaScript, CSS, JSON manifests, binary downloads, or applications as
  general CDN payload
- public upload/write endpoints

## Legacy migration state

Historical `assets/client` and `manifests/www` paths may still exist in the
repository. The sync script no longer populates them and they are no longer
part of the active CDN contract. Their deletion is intentionally a
**post-validation step**, after WWW image delivery, redirects, HTTPS, and cache
behavior have passed staging/production verification.

## Security

- dynv6 credentials must not be committed.
- Real tokens belong only in ignored local `secrets/` or `var/` files.
- CDN content is publicly readable but not publicly writable.
- The CDN owns no API, session, or authentication responsibility.
