class EfficientVacummCleanerABM:
    def __init__(self):
        self.states = {"in-a", "in-b", "moving-to-a", "waiting-for-moving-to-a", "moving-to-b",
                       "waiting-for-moving-to-b", "cleaning-a", "cleaning-b"}

        self.rules = {
            "in-a": "ask-if-is-dirty-a",
            "in-b": "ask-if-is-dirty-b",
            "moving-to-a": "move-to-a",
            "moving-to-b": "move-to-b",
            "waiting-for-moving-to-a": "wait-for-move-to-a",
            "waiting-for-moving-to-b": "wait-for-move-to-b",
            "cleaning-a": "quadrant-a-cleaned",
            "cleaning-b": "quadrant-b-cleaned"
        }

        self.actions = {
            "ask-if-is-dirty-a": "¿El cuadrante A esta sucio?",
            "ask-if-is-dirty-b": "El cuadrante B esta sucio?",
            "move-to-b": "Mover aspiradora sl cuadrante B",
            "move-to-a": "Mover Aspiradora al cuadrante A",
            "wait-for-move-to-a": "Optimizando Recursos (esperando para mover al cuatrante A)",
            "wait-for-move-to-b": "Optimizando Recursos (esperando para mover al cuadrante B",
            "quadrant-a-cleaned": "Limpiar Cuadrante A",
            "quadrant-b-cleaned": "Limpiar Cuadrante B"
        }

        self.model = [
            ["in-a",                    "ask-if-is-dirty-a",    "a-is-dirty",       "cleaning-a"],
            ["in-a",                    "ask-if-is-dirty-a",    "a-is-clean",       "waiting-for-moving-to-b"],
            ["cleaning-a",              "quadrant-a-cleaned",   "clear-a",          "waiting-for-moving-to-b"],
            ["in-b",                    "ask-if-is-dirty-b",    "b-is-dirty",       "cleaning-b"],
            ["in-b",                    "ask-if-is-dirty-b",    "b-is-clean",       "waiting-for-moving-to-a"],
            ["cleaning-b",              "quadrant-b-cleaned",   "clear-b",          "waiting-for-moving-to-a"],
            ["moving-to-a",             "move-to-a",            "move-vacummer",    "in-a"],
            ["moving-to-b",             "move-to-b",            "move-vacummer",    "in-b"],
            ["waiting-for-moving-to-a", "wait-for-move-to-a",   "wait",             "moving-to-a"],
            ["waiting-for-moving-to-b", "wait-for-move-to-b",   "wait",             "moving-to-b"]
        ]

        self.state = "in-a"
        self.action = "ask-if-is-dirty-a"

    def exist_in_model(self, state, action, perception):
        for row in self.model:
            if row[0] == state and row[1] == action and row[2] == perception:
                return row[3]
        return None

    def update_state(self, state, action, perception):
        result = self.exist_in_model(state, action, perception)
        if result is not None:
            return result
        else:
            return state