# delver-rpg
- __TODO: CONVERT TO [PYCORD](https://github.com/Pycord-Development/pycord)__
- [DB Design](https://stackoverflow.com/questions/1292577/designing-tables-for-storing-various-requirements-and-stats-for-multiplayer-game)
- [discord.py docs](https://discordpy.readthedocs.io/en/stable/api.html)
- [unicode search](https://unicode-table.com)
- [emoji unicode](https://www.fileformat.info/info/unicode/char/search.htm)

`A semi-idle RPG bot for discord`
- Send your character on timed dungeons
- get loot
- but items at [town store](#town-store) 

## Dungeons
- __character can die if not prepared__
- have availability timer
- solo dungeons always available
- chance to have 2-4 player dungeons
- some need a specific class
- can save 1 dungeon for later (upgrade)
- will reward a chest (armor/wep/consumable)
- deplete stamina
- regen stamina (x/hour) after dungeon 

### Affixes
- Many Monsters - better chance for gold and consumables
- Big Boys (Bosses) - better chance for rare items
- RP Quest - better experience

### Requirments
- level
- group
  - random class
  - random stat check

## Town Store
- health/stam potions always available
- chance to have buff potions (+x max health/stam)
- always have random green items
- chance to have blue items
- buy upgrades - (weapons/armor/passives)

## Trading
- can trade items and gold

## Classes
### Warrior
- better armor
- PartyBuff: dmg reduction

### Mage
- better healing and use of potions
- PartyBuff: amplify potions

### Rogue
- more damage
- PartyBuff: increase party dmg

### Ranger
- better health, utility
- PartyBuff: reduce stamina consumption

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
- auction house