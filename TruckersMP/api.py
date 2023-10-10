from typing import Optional, Union

from .requests import HTTPClient

from .models.player import Player
from .models.bans import Bans
from .models.servers import Server
from .models.events import EventTypes, Event
from .models.vtcs import VTCTypes, VTC
from .models.news import News
from .models.roles import Role
from .models.members import Member
from .models.versions import Versions
from .models.rules import Rules

class TruckersMPClient(HTTPClient):

    def __init__(self) -> None:
        """
        Initialize the TruckersMPClient.

        Docs: https://truckersmp.com/developers/api
        """
        super().__init__()
        self._URI = 'https://api.truckersmp.com/v2'

    async def get_player(self, player_id: int) -> Player:
        """
        Lookup player information

        Docs: https://truckersmp.com/developers/api#operation/get-player-id

        :param player_id: The ID of the player.
        """
        response = await self._request(f"{self._URI}/player/{player_id}")
        return Player(**response)
    
    async def get_bans(self, player_id: int) -> list[Bans]:
        """
        Latest 5 bans for a selected user if bans are not hidden or user has no bans. 
        Fetch the player information to check if user is currently banned.

        Docs: https://truckersmp.com/developers/api#operation/get-bans-id

        :param player_id: The ID of the player.
        """
        response = await self._request(f"{self._URI}/bans/{player_id}")
        bans = list()
        for ban in response:
            bans.append(Bans(**ban))
        return bans
    
    async def get_available_servers(self) -> list[Server]:
        """
        List of available TruckersMP servers and their status

        Docs: https://truckersmp.com/developers/api#operation/get-servers
        """
        response = await self._request(f"{self._URI}/servers")
        servers = list()
        for server in response:
            servers.append(Server(**server))
        return servers
    
    async def get_in_game_time(self) -> int:
        """
        The current in-game time. Game time is expressed in minutes, where 10 real seconds is 1 minute of in-game time. 
        It is number of minutes since 2015-25-10 15:48:32 CET.

        Note: Game time may not be exact as time will drift.

        Docs: https://truckersmp.com/developers/api#operation/get-game-time
        """
        request = await self._request(f"{self._URI}/game_time")

        # I spent a lot of attempts to convert the returned data to the date format, 
        # but I never got to the right solution. 
        # Write to me in private messages in Telegram (@belyashik2k) if you have found an algorithm for this.

        return request['game_time']
    
    async def get_events(self, event_id: Optional[int] = None) -> Union[Event, EventTypes]:
        """
        List all of the current, upcoming, and featured TruckersMP events.

        If event_id is not None, fetch a specific event.

        Docs: https://truckersmp.com/developers/api#operation/get-events

        :param event_id: The ID of the event.
        """
        if event_id is None:
            request = await self._request(f"{self._URI}/events")
            return EventTypes(**request)
        request = await self._request(f"{self._URI}/events/{event_id}")
        return Event(**request)
    
    async def get_user_events(self, user_id: int) -> list[Event]:
        """
        Get all the events from the specified user.

        Docs: https://truckersmp.com/developers/api#operation/get-user-id-events

        :param user_id: The ID of the user.
        """
        request = await self._request(f"{self._URI}/events/user/{user_id}")
        events = list()
        for event in request:
            events.append(Event(**event))
        return events
    
    async def get_featured_vtc(self) -> VTCTypes:
        """
        Get recent, featured, and featured cover VTCs.

        Docs: https://truckersmp.com/developers/api#operation/get-vtc
        """
        request = await self._request(f"{self._URI}/vtc")
        return VTCTypes(**request)
    
    async def get_vtc(self, vtc_id: int) -> VTC:
        """
        Get the specified VTC.

        :param vtc_id: The ID of the VTC.

        Docs: https://truckersmp.com/developers/api#operation/get-vtc-id
        """
        request = await self._request(f"{self._URI}/vtc/{vtc_id}")
        return VTC(**request)

    async def get_vtc_news(self, 
                           vtc_id: int, 
                           news_id: Optional[int] = None
                           ) -> Union[list[News], News]:
        """
        Get the news from the specified VTC.
        
        If news_id is not None, fetch a specific news article.
        
        :param vtc_id: The ID of the VTC.
        :param news_id: The ID of the news article.
        
        Docs: https://truckersmp.com/developers/api#operation/get-vtc-id-news"""

        if news_id is None:
            request = await self._request(f"{self._URI}/vtc/{vtc_id}/news")
            news_list = list()
            for news in request['news']:
                news_list.append(News(**news))
            return news_list
        request = await self._request(f"{self._URI}/vtc/{vtc_id}/news/{news_id}")
        print(request)
        return News(**request)
    
    async def get_vtc_roles(self, 
                            vtc_id: int, 
                            role_id: Optional[int] = None
                            ) -> Union[list[Role], Role]:
        """
        Get the roles from the specified VTC.

        If role_id is not None, fetch a specific role.

        :param vtc_id: The ID of the VTC.
        :param role_id: The ID of the role.

        Docs: https://truckersmp.com/developers/api#operation/get-vtc-id-roles
        """
        if role_id is None:
            request = await self._request(f"{self._URI}/vtc/{vtc_id}/roles")
            roles = list()
            for role in request['roles']:
                roles.append(Role(**role))
            return roles
        request = await self._request(f"{self._URI}/vtc/{vtc_id}/role/{role_id}")
        return Role(**request)
    
    async def get_vtc_members(self, 
                              vtc_id: int, 
                              member_id: Optional[int] = None
                              ) -> Union[list[Member], Member]:
        """
        Get the members from the specified VTC.
        
        If member_id is not None, fetch a specific member.
        
        :param vtc_id: The ID of the VTC.
        :param member_id: The ID of the member.
        
        Docs: https://truckersmp.com/developers/api#operation/get-vtc-id-members
        """
        if member_id is None:
            request = await self._request(f"{self._URI}/vtc/{vtc_id}/members")
            members = list()
            for member in request['members']:
                members.append(Member(**member))
            return members
        request =  await self._request(f"{self._URI}/vtc/{vtc_id}/member/{member_id}")
        return Member(**request)
    
    async def get_vtc_events(self, 
                             vtc_id: int, 
                             event_id: Optional[int] = None
                             ) -> Union[list[Event], Event]:
        """
        Get the events from the specified VTC.
        
        If event_id is not None, fetch a specific event.
        
        :param vtc_id: The ID of the VTC.
        :param event_id: The ID of the event.
        
        Docs: https://truckersmp.com/developers/api#operation/get-vtc-id-events
        """
        if event_id is None:
            request = await self._request(f"{self._URI}/vtc/{vtc_id}/events")
            events = list()
            for event in request:
                events.append(Event(**event))
            return events
        request = await self._request(f"{self._URI}/vtc/{vtc_id}/events/{event_id}")
        return Event(**request)
    
    async def get_current_version(self) -> Versions:
        """
        Get the current game versions on TruckersMP.

        Docs: https://truckersmp.com/developers/api#operation/get-version
        """
        request = await self._request(f"{self._URI}/version")
        return Versions(**request)

    async def get_in_game_rules(self) -> Rules:
        """
        Get the in-game rules.

        Docs: https://truckersmp.com/developers/api#operation/get-rules
        """
        request = await self._request(f"{self._URI}/rules")
        return Rules(**request)