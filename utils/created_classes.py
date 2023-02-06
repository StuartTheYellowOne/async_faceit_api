class Rank:
    """
    :param nickname: 
    :param skill_level: 
    :param subs_done: 
    :param team_id: 
    :param team_leader: 
    :param team_type: 
    :type nickname: str
    :type skill_level: int
    :type subs_done: int
    :type team_id: str
    :type team_leader: str
    :type team_type: str
    """
    def __init__(self,
                 nickname: str,
                 skill_level: int,
                 subs_done: int,
                 team_id: str,
                 team_leader: str,
                 team_type: str,
                 **kwargs):
        super().__init__(**kwargs)
        self.nickname = nickname
        self.skill_level = skill_level
        self.subs_done = subs_done
        self.team_id = team_id
        self.team_leader = team_leader
        self.team_type = team_type
