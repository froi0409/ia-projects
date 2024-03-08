import time

from entities.EfficientVacummCleanerABM import EfficientVacummCleanerABM
vacumm_cleaner = EfficientVacummCleanerABM()

print("¿El cuadrante A está sucio?")

while True:
    # if vacumm_cleaner.state != "served-c1":
    print("Ingresar percepción: ")
    perception = input()

    vacumm_cleaner.state = vacumm_cleaner.update_state(vacumm_cleaner.state, vacumm_cleaner.action, perception)
    rule = vacumm_cleaner.rules[vacumm_cleaner.state]
    vacumm_cleaner.action = rule
    actionText = vacumm_cleaner.actions[vacumm_cleaner.action]

    print(actionText)
