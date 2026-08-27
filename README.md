# ShellRPG-cdn · v0.8.0

Deutsch | [English](README.en.md)

## Rolle

`ShellRPG-cdn` ist ausschließlich der öffentliche **Bild-Endpunkt von ShellRPG-www**.
Er enthält keine autoritative Spielmechanik, keine Wiki-Inhalte, keine Client-
Distribution und keine allgemeinen Download-/Anwendungsdateien.

Aktiver Payload-Scope:

```text
assets/www/public/media/**
```

Zulässig sind nur Bildformate, die der WWW-Pipeline ausdrücklich akzeptiert
(PNG, JPEG, GIF, WebP, SVG und ICO).

## Pflegehinweis

- Bei relevanten Content-, Contract-, Feature- oder Redaktionsänderungen an
  diesem Endpunkt `README.md`, `README.en.md` und `VERSION` gemeinsam
  berücksichtigen.

## Aktiver Lieferweg

- GitHub-backed Primärpfad für WWW-Bilder:
  `https://cdn.jsdelivr.net/gh/RPG-Wulf/ShellRPG-cdn@main/assets/www`
- `scripts/sync_workspace_assets.py` liest ausschließlich
  `ShellRPG-www/public/media` und kopiert ausschließlich Bilddateien nach
  `assets/www/public/media`.
- Öffentliche Schreibzugriffe sind nicht vorgesehen. Befüllung erfolgt nur
  über die kontrollierte WWW-/Deployment-Pipeline.
- Ein dynv6-Fallback kann lokal bzw. im Deployment konfiguriert werden, muss
  aber vor Cutover über DNS und HTTPS nachweislich erreichbar sein.

## Explizit nicht erlaubt

- Wiki-Inhalte oder Wiki-eigene Assets auf diesem CDN
- `ShellRPG-client` als CDN-Quelle oder CDN-Verbraucher
- JavaScript, CSS, JSON-Manifeste, Binärdownloads oder Anwendungen als
  allgemeiner CDN-Payload
- öffentliche Upload- oder Schreibschnittstellen

## Legacy-Migrationszustand

Die historischen Pfade `assets/client` und `manifests/www` können im Repository
noch vorhanden sein. Sie werden vom Sync-Skript nicht mehr befüllt und gehören
nicht mehr zum aktiven CDN-Vertrag. Ihre Entfernung ist bewusst ein
**Post-Validation-Schritt**: erst wenn WWW-Bildlieferung, Redirects, HTTPS und
Cache-Verhalten in Staging/Produktion erfolgreich geprüft wurden.

## Sicherheit

- Zugangsdaten für dynv6 liegen nicht in versionierten Dateien.
- Reale Tokens gehören ausschließlich in lokal ignorierte `secrets/`- oder
  `var/`-Dateien.
- CDN-Inhalte sind öffentlich lesbar, aber nicht öffentlich schreibbar.
- Das CDN besitzt keine API-, Session- oder Authentifizierungsverantwortung.

## Praktische Kommandos

```bash
python scripts/sync_workspace_assets.py
python scripts/update_dynv6.py
./shell.sh
```

`./shell.sh` bleibt ein schlanker Wrapper für den lokalen dynv6-Update-Job.
