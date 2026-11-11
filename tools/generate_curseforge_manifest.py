#!/usr/bin/env python3
"""Generate a CurseForge Minecraft 1.12.2 manifest from modlist.txt."""

import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = "https://api.curseforge.com/v1"
GAME_ID = 432
MINECRAFT_VERSION = "1.12.2"
FORGE_LOADER_TYPE = 1

ALIASES = {
    "Applied Energistics 2": "Applied Energistics 2",
    "BuildCraft Lib": "BuildCraft",
    "CLibrary": "CLib",
    "Forge Multipart CBE": "Forge Multipart",
    "Just Enough Reactors": "Just Enough Reactors",
    "Mekanism: Generators": "Mekanism Generators",
    "Mekanism: Tools": "Mekanism Tools",
    "PTRLib-1.0.": "PTRLib",
}


def request_json(path, params, api_key):
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"{API_URL}{path}?{query}",
        headers={"x-api-key": api_key, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["data"]


def choose_project(name, api_key):
    search_name = ALIASES.get(name, name)
    projects = request_json(
        "/mods/search",
        {
            "gameId": GAME_ID,
            "searchFilter": search_name,
            "classId": 6,
            "pageSize": 10,
        },
        api_key,
    )
    exact = [p for p in projects if p["name"].casefold() == search_name.casefold()]
    candidates = exact or projects
    if len(candidates) != 1:
        labels = ", ".join(f'{p["name"]} ({p["id"]})' for p in candidates[:5])
        raise RuntimeError(f"{name}: ambiguous project match: {labels or 'none'}")
    return candidates[0]


def choose_file(project_id, name, api_key):
    files = request_json(
        f"/mods/{project_id}/files",
        {"gameVersion": MINECRAFT_VERSION, "pageSize": 100},
        api_key,
    )
    compatible = [
        f for f in files
        if f.get("isAvailable", True)
        and FORGE_LOADER_TYPE in f.get("sortableGameVersions", [])
    ]
    if not compatible:
        compatible = [f for f in files if f.get("isAvailable", True)]
    if not compatible:
        raise RuntimeError(f"{name}: no available {MINECRAFT_VERSION} file")
    compatible.sort(key=lambda f: f["fileDate"], reverse=True)
    return compatible[0]


def main():
    api_key = os.environ.get("CURSEFORGE_API_KEY")
    if not api_key:
        raise RuntimeError("Set CURSEFORGE_API_KEY to a CurseForge API key")

    with open("modlist.txt", encoding="utf-8") as source:
        names = [line.strip() for line in source if line.strip()]

    files = []
    failures = []
    for name in names:
        try:
            project = choose_project(name, api_key)
            file_info = choose_file(project["id"], name, api_key)
            files.append({"projectID": project["id"], "fileID": file_info["id"], "required": True})
            print(f"{name}: project {project['id']}, file {file_info['id']} ({file_info['name']})")
        except (RuntimeError, urllib.error.HTTPError, urllib.error.URLError) as error:
            failures.append(str(error))
            print(f"ERROR: {error}", file=sys.stderr)

    if failures:
        raise RuntimeError(f"Could not resolve {len(failures)} mod(s); manifest was not written")

    manifest = {
        "manifestType": "minecraftModpack",
        "manifestVersion": 1,
        "name": "EnderDevelopment 1.12.2 Pack",
        "version": "1.0.0",
        "author": "EnderDevelopment",
        "files": files,
        "overrides": "overrides",
        "minecraft": {
            "version": MINECRAFT_VERSION,
            "modLoaders": [{"id": "forge-14.23.5.2860", "primary": True}],
        },
    }
    with open("manifest.json", "w", encoding="utf-8") as destination:
        json.dump(manifest, destination, indent=2)
        destination.write("\n")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
