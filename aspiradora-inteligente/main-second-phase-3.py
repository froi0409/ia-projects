from entities.VacummDoublePerception import VacummDoublePerception
vacumm_cleaner = VacummDoublePerception()

print("Are you in A? is the quadrant dirty?")

while True:
    # if vacumm_cleaner.state != "served-c1":
    print("Ingresar percepción: ")
    perception_1 = input()
    perception_2 = input()

    print(vacumm_cleaner.state, vacumm_cleaner.action, perception_1, perception_2)
    vacumm_cleaner.state = vacumm_cleaner.update_state(vacumm_cleaner.state, vacumm_cleaner.action, perception_1, perception_2)
    rule = vacumm_cleaner.rules[vacumm_cleaner.state]
    vacumm_cleaner.action = rule
    actionText = vacumm_cleaner.actions[vacumm_cleaner.action]


    print(actionText)
