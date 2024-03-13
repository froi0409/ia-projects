class VacummDoublePerception:
    def __init__(self):
        self.states = {"scanning-a", "scanning-b", "in-a-clean", "in-a-dirty", "in-b-clean", "in-b-dirty"}

        self.rules = {
            "scanning-a": "ask-quadrant-a-and-is-dirty",
            "scanning-b": "ask-quadrant-b-and-is-dirty",
            "in-a-clean": "move-to-b",
            "in-b-clean": "move-to-a",
            "in-a-dirty": "clear-a",
            "in-b-dirty": "clear-b"
        }

        self.actions = {
            "ask-quadrant-a-and-is-dirty": "Are you in A? is the quadrant dirty?",
            "ask-quadrant-b-and-is-dirty": "Are you in B? is the quadrant dirty?",
            "move-to-a": "B is now cleaned, Do you want to move to quadrant A? move on",
            "move-to-b": "A is now cleaned, Do you want to move to quadrant B? move on",
            "clear-a": "Are you in quadrant A? Clear it",
            "clear-b": "Are you in quadrant B? Clear it"
        }

        self.model = [
            ["scanning-a", "ask-quadrant-a-and-is-dirty",   "yes",  "yes",      "in-a-dirty"],
            ["scanning-a", "ask-quadrant-a-and-is-dirty",   "yes",  "no",       "in-a-clean"],
            ["scanning-b", "ask-quadrant-b-and-is-dirty",   "yes",  "yes",      "in-b-dirty"],
            ["scanning-b", "ask-quadrant-b-and-is-dirty",   "yes",  "no",       "in-b-clean"],
            ["in-a-dirty", "clear-a",                       "yes",  "clear",    "in-a-clean"],
            ["in-a-clean", "move-to-b",                     "yes",  "move-on",  "scanning-b"],
            ["in-b-dirty", "clear-b",                       "yes",  "clear",    "in-b-clean"],
            ["in-b-clean", "move-to-a",                     "yes",  "move-on",  "scanning-a"]
        ]

        self.state = "scanning-a"
        self.action = "ask-quadrant-a-and-is-dirty"

    def exist_in_model(self, state, action, perception_1, perception_2):
        for row in self.model:
            if row[0] == state and row[1] == action and row[2] == perception_1 and row[3] == perception_2:
                return row[4]
        return None

    def update_state(self, state, action, perception_1, perception_2):
        result = self.exist_in_model(state, action, perception_1, perception_2)
        if result is not None:
            return result
        else:
            return state