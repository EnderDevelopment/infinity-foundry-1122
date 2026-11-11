# Minecraft 1.12.2 Forge Modpack

Infinity Foundry 1.12.2 is a Minecraft modpack project and Forge modpack metadata package for Minecraft 1.12.2 using Forge 14.23.5.2860. It organizes a large technology, automation, storage, building, farming, exploration, utility, and integration mod inventory while providing pack metadata and a small marker mod for the project.

## Install

1. Install 64-bit Java 8.
2. Install Minecraft Forge 14.23.5.2860 for Minecraft 1.12.2.
3. Download compatible Minecraft 1.12.2 Forge versions of the mods listed in `modlist.txt` from their official project pages.
4. Place the downloaded mod files in the `mods` folder of the Forge 1.12.2 instance.
5. Launch Minecraft with the Forge 1.12.2 profile.
6. If a mod requires an additional dependency or configuration file, install it according to that mod's official instructions.

The repository includes `manifest.json`, `pack.toml`, `pack.mcmeta`, and `modlist.txt` for pack identification and organization. The current manifest does not contain remote mod file IDs, so third-party mod files must be installed manually.

## Use

1. Open the Minecraft launcher and select the Forge 1.12.2 profile.
2. Start the game with the installed mod files.
3. Use the included mod inventory to assemble and maintain the Infinity Foundry 1.12.2 instance.
4. Use `modlist.txt` as the reference for the project’s recorded mod names.
5. To build the included marker mod, run `./gradlew build` from the project directory when a compatible Gradle wrapper is available. The generated marker jar is placed in `build/libs`; external mod jars remain separate and belong in the instance `mods` folder.

The included marker mod only identifies the pack and logs that it has loaded. It does not add custom recipes, blocks, items, world generation, or gameplay systems.

---

More Minecraft mod projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/33d02cba-29d2-4516-9b46-858a5a73e42f?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=33d02cba-29d2-4516-9b46-858a5a73e42f
