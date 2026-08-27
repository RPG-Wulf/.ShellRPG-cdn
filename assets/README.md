# ShellRPG-cdn Assets

Der aktive CDN-Bestand gehört ausschließlich `ShellRPG-www`.

## Aktiver Root

- `assets/www/public/media` enthält öffentliche WWW-Bilder.
- `scripts/sync_workspace_assets.py` liest ausschließlich
  `ShellRPG-www/public/media` und akzeptiert ausschließlich Bildformate.
- WWW kann diese Bilder direkt über den konfigurierten CDN-Basis-URL oder
  über seinen bildbeschränkten `/asset/*`-Fallback beziehen.

## Nicht aktiver Scope

- `assets/client` ist historischer Legacy-Bestand und kein aktiver CDN-Root.
- Wiki-Inhalte oder Wiki-eigene Assets dürfen nicht in diesen CDN-Bestand
  aufgenommen werden.
- Allgemeine CSS-/JS-/JSON-/Download-Dateien sind kein CDN-Payload.

Legacy-Bestände werden erst nach erfolgreicher Deployment-Validierung entfernt;
der Producer befüllt sie bereits jetzt nicht mehr.
