![snapedit_1696958911490](https://github.com/Belyashik2K/TruckersMP/assets/126521808/49b0190c-c741-4f36-bcc7-aed9d2e1d187)
# TruckersMP
> Fully async python wrapper for [TruckersMP API](https://truckersmp.com/developers/api)

## Installing

    pip install TruckersMP

## Features
* Fully async methods
* All methods return Pydantic model as result for easier interaction with data
* Full exception handling

## Usage
```python
from TruckersMP import TruckersMPClient

async def main():

    client = TruckersMPClient()

    # Get info about player
    player = await client.get_player(1)
    print("Player info")
    print("Player name >>>", player.name)
    print("Player ID >>>", player.id)
    print("Player join date >>>", player.joinDate)
    print('Is player in staff >>>', player.permissions.isStaff)
    print('Is player banned >>>', player.banned)

    print("-----------------------------------")

    # Get info about VTC
    vtc = await client.get_vtc(1)
    print("VTC info")
    print("VTC name >>>", vtc.name)
    print("VTC ID >>>", vtc.id)
    print("VTC tag >>>", vtc.tag)
    print("VTC owner >>>", vtc.owner_username)
    print("VTC members >>>", vtc.members_count)

    # And more...

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```

## Docs
> Go to https://truckersmp.com/developers/api for more information about API