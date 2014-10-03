class Player(object):
    _registry = []

    def __init__(self, user_id = 0, user_name = "Brak", user_points = 0, user_round = 1,
    user_rank = 0, free_point = None):
        self._registry.append(self)
        self.user_id = user_id
        self.user_name = user_name
        self.user_points = user_points
        self.user_round = user_round
        self.user_rank = user_rank
        self.user_color = [0,0]
        self.free_point = free_point
        self.oponents =  []
    def __repr__(self):
        return repr((self.user_id, self.user_name, self.user_points, self.user_round,
        self.user_rank, self.user_color, self.free_point, self.oponents ))