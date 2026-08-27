from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.sync_workspace_assets import sync_workspace_assets


def test_sync_copies_only_www_images(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    cdn = tmp_path / "cdn"

    www_media = workspace / "ShellRPG-www" / "public" / "media" / "png"
    www_media.mkdir(parents=True)
    (www_media / "www.png").write_bytes(b"www")
    (www_media / "notes.txt").write_text("not an image", encoding="utf-8")

    www_manifest = workspace / "ShellRPG-www" / "assets" / "manifest"
    www_manifest.mkdir(parents=True)
    (www_manifest / "map.json").write_text("{}", encoding="utf-8")

    client_media = workspace / "ShellRPG-client" / "media"
    client_media.mkdir(parents=True)
    (client_media / "client.png").write_bytes(b"client")

    sync_workspace_assets(cdn, workspace)

    assert (cdn / "assets" / "www" / "public" / "media" / "png" / "www.png").read_bytes() == b"www"
    assert not (cdn / "assets" / "www" / "public" / "media" / "png" / "notes.txt").exists()
    assert not (cdn / "manifests" / "www" / "map.json").exists()
    assert not (cdn / "assets" / "client" / "media" / "client.png").exists()


def test_sync_ignores_symlinked_images(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    cdn = tmp_path / "cdn"
    media = workspace / "ShellRPG-www" / "public" / "media"
    media.mkdir(parents=True)

    outside = tmp_path / "outside.png"
    outside.write_bytes(b"private")
    (media / "linked.png").symlink_to(outside)

    sync_workspace_assets(cdn, workspace)

    assert not (cdn / "assets" / "www" / "public" / "media" / "linked.png").exists()
