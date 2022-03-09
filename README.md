# __delver-rpg__
- TODO: CONVERT TO [PYCORD](https://github.com/Pycord-Development/pycord)
- [discord.py docs](https://discordpy.readthedocs.io/en/stable/api.html)
- [tutorial](https://tutorial.vcokltfre.dev)
- [emoji unicode](https://www.fileformat.info/info/unicode/char/search.htm)
- [unicode search](https://unicode-table.com)

`A semi-idle RPG bot for discord`
- Send you character on timed dungeons
- get loot
- buy/trade armor, weapons, potions

## __Dungeons__
- __character can die__
- have availability timer
- random affixes
- solo dungeons always available
- chance to have 2-4 player dungeons
- some need a specific class
- can save 1 dungeon for later (upgrade)
- will reward a chest (armor/wep/consumable)
- deplete stamina
- regen stamina (x/hour) after dungeon 

## __Classes__
### Warrior
-  more health/armor
- PartyBuff: dmg reduction

### Mage
- better healing and use of potions
- PartyBuff: amplify potions

### Rogue
- more damage
- PartyBuff: increase party dmg

### Ranger
- Utility
- PartyBuff: reduce stamina consumption

## __Items__
### Potions (primary/secondary)
- health
- stamina

### Gear
- armor
- weapon
- ring

## __Commands__
```.status```
- check status of dungeon
- can interact for better results

```.store```
- buy/sell basic gear/potions
- chance for limited items

```.inventory```
- view/equip items

```.rest```
- sleep for 8 hours to regain hp/stam

```.inspect <characterName>```
- view summary for all characters
- view full details of a specific character

```.item <item>```
- view details of item

```.char [-full] [-url <urlString>]```
- view short summary of stats and equiped items
- -full, view full summary of character
- -url <urlString>, set pfp 

```.helpMe```
- sends a direct message to user with **.help** summary