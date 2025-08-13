import copy

# Prototype Interface
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete Prototype
class GameCharacter(Prototype):
    def __init__(self, name, model, weapon, skills):
        self.name = name
        self.model = model
        self.weapon = weapon
        self.skills = skills

    def __str__(self):
        return (f"Name: {self.name}, "
                f"Model: {self.model}, "
                f"Weapon: {self.weapon}, "
                f"Skills: {', '.join(self.skills)}")

# Uso del patrón Prototype
if __name__ == "__main__":
    # Personaje base
    base_warrior = GameCharacter(
        name="Warrior",
        model="warrior_model.obj",
        weapon="Sword",
        skills=["Attack", "Block", "Charge"]
    )

    # Clonando y modificando
    elite_warrior = base_warrior.clone()
    elite_warrior.name = "Elite Warrior"
    elite_warrior.weapon = "Magic Sword"
    elite_warrior.skills.append("Heal")

    # Resultados
    print(base_warrior)
    print(elite_warrior)
