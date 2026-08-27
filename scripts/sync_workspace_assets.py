from __future__ import annotations

import shutil
from pathlib import Path


IMAGE_SUFFIXES = {
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def workspace_root() -> Path:
    return repo_root().parent


def copy_images(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    for candidate in source.rglob("*"):
        if not candidate.is_file() or candidate.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        relative = candidate.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(candidate, target)


def sync_workspace_assets(root: Path, workspace: Path) -> None:
    copy_images(
        workspace / "ShellRPG-www" / "public" / "media",
        root / "assets" / "www" / "public" / "media",
    )


def main() -> int:
    sync_workspace_assets(repo_root(), workspace_root())
    print("ShellRPG-cdn WWW images synchronized from ShellRPG-www.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
