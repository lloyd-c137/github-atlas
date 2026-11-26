#!/usr/bin/env python3
"""Build a reproducible, self-contained GitHub Collaborator skill ZIP."""
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "github-collaborator"
OUT = ROOT / "dist" / "github-collaborator-skill.zip"
version = (SKILL / "VERSION").read_text(encoding="utf-8").strip()
manifest = (SKILL / "SKILL.md").read_text(encoding="utf-8")
if f'version: "{version}"' not in manifest:
    raise SystemExit("Version mismatch between VERSION and SKILL.md")

OUT.parent.mkdir(exist_ok=True)
with ZipFile(OUT, "w") as archive:
    for path in sorted(SKILL.rglob("*")):
        if not path.is_file():
            continue
        name = path.relative_to(ROOT).as_posix()
        item = ZipInfo(name, (2020, 1, 1, 0, 0, 0))
        item.compress_type = ZIP_DEFLATED
        item.external_attr = 0o100644 << 16
        archive.writestr(item, path.read_bytes())

with ZipFile(OUT) as archive:
    if archive.testzip() is not None:
        raise SystemExit("Archive integrity check failed")
    names = set(archive.namelist())
    for path in SKILL.rglob("*"):
        if path.is_file() and path.relative_to(ROOT).as_posix() not in names:
            raise SystemExit(f"Missing from package: {path}")

digest = sha256(OUT.read_bytes()).hexdigest()
(ROOT / "dist" / "github-collaborator-skill.zip.sha256").write_text(
    f"{digest}  github-collaborator-skill.zip\n", encoding="ascii"
)
print(f"PASS: built github-collaborator {version}; sha256 {digest}")
