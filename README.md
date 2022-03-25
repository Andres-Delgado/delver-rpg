# delver-rpg
__CONVERT TO [PYCORD](https://github.com/Pycord-Development/pycord)__
- [discord.py docs](https://discordpy.readthedocs.io/en/stable/api.html)
- [psycopg2 docs](https://www.psycopg.org/docs/)
- [DB Design](https://stackoverflow.com/questions/1292577/designing-tables-for-storing-various-requirements-and-stats-for-multiplayer-game)
- [unicode search](https://unicode-table.com)
- [emoji unicode](https://www.fileformat.info/info/unicode/char/search.htm)

`A semi-idle RPG discord bot for my friends`
- Send your character on timed dungeons
- get loot
- buy items at [town store](#town-store)

## Dungeons
- __character can die if not prepared__
- have availability timer
- solo dungeons always available
- chance to have 2-4 player dungeons
- some need a specific class
- can save 1 dungeon for later (upgrade at store)
- deplete stamina
- regen stamina (x/hour) after dungeon
- rewards a loot chest (armor/wep/consumable)

### Affixes
- Many Monsters - better chance for gold and consumables
- Big Boys (Bosses) - better chance for rare items
- RP Quest - better experience
- Class Quest
  - unlocks class abilities at shop
  - if unlocked, reduces cost?
- Story Quest
  - unlocked at various milestones (e.g lv 5/10/15)
  - __difficult__

### Requirments
- level
- group
  - random class
  - random stat check

### Combat (idk about this yet tbh)
- player can choose to participate in dungeon
  - x times per dungeon
  - example: in a 4hour dungeon
    - once before 2hr mark
    - again after 2hr mark
- embed will have reactions to
  - dodge left/right
  - attack/use special ability
  - block
  - use consumable
  - run
- enemy/player actions will happen simultaneously
- enemy attack patterns can be learned
- will give better rewards then if dungeon was left idle

## Town Store
- items refresh every x hours
- always available
  - health/stam potions
  - random green items
  - dungeon refresh consumable
- chance
  - ?? buff potions (+x max health/stam)
  - blue items
- purchase upgrades
  - store upgrades
  - class special abilties
    - for when interacting with dungeon
  - weapons/armor
  - passives
    - save +1 additional dungeon for later
    - recover +1 hp/stam per hour

## Trading
- can trade items and gold

## Classes
### Warrior
- better armor
- PartyBuff: dmg reduction
- prioritize dungeons with small monsters bc of armor

### Mage (rename to Alchemist?)
- better healing and use of potions
- PartyBuff: amplify potions
- flexible on dungeon length/type
- dungeon preference depends on consumables equiped

### Rogue
- better damage
- PartyBuff: increase party dmg
- prioritize short dungeons bc low hp/armor

### Ranger
- better health, utility
- PartyBuff: reduce stamina consumption
- prioritize longer dungeons bc better stam

## Leveling
- players choose what stats to increase

### Stats
- health
- stam - limits dungeons
- armor
  - determined by equiped
  - damage mitigation
- dmg - determined by weapon

## Commands

```.menu```
- core ui for interaction

```.create <character_name>```
- character creation

```.status```
- check status of dungeon
- can interact for better results

```.store```
- buy/sell basic gear/potions
- chance for limited items

```.inventory```
- view/equip items

```.rest x```
- sleep for x hours to regain hp/stam
- oversleeping will give rested xp

```.inspect <character_name>```
- view summary for all characters
- view full details of a specific character

```.item <item>```
- view details of item

```.char [-full] [-url <urlString>]```
- view short summary of stats and equiped items
- -full, view full summary of character
- -url <urlString>, set pfp

```.helpMe```
- sends a direct message to user with `.help` summary


## Future updates
- crafting
  - dungeon rewards have chance to drop gathering dungeon map
  - new dungeon with gathering affix - more mats
- auction house
- achievements
- metadata stats
  - dungeons completed
  - total gold spent