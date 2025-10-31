class Building:
    def __init__(self, id_building: str, list_infras: list, building_age: int):
        """
        Initialise un bâtiment avec son identifiant, sa liste d'infrastructures, et son âge.
        """
        self.id_building = id_building
        self.list_infras = list_infras  # Liste d’objets Infra
        self.building_age = building_age  # Âge du bâtiment, impacte la difficulté

    def get_building_difficulty(self) -> float:
        """Calcule la somme des difficultés des infrastructures à réparer, avec un ajustement pour l'âge du bâtiment."""
        base_difficulty = sum(
            infra.get_infra_difficulty()
            for infra in self.list_infras
            if infra.infra_type == "a_remplacer"
        )
        age_factor = 1 + (self.building_age / 100)  # Augmente la difficulté selon l'âge du bâtiment
        return base_difficulty * age_factor

    def repair(self):
        """Répare toutes les infrastructures associées à ce bâtiment."""
        for infra in self.list_infras:
            infra.repair_infra()

    def check_building_condition(self) -> str:
        """Retourne l'état global du bâtiment en fonction de l'état de ses infrastructures."""
        if all(infra.infra_type == "infra_intacte" for infra in self.list_infras):
            return "Bâtiment en bon état"
        else:
            return "Bâtiment endommagé"

    def __lt__(self, other):
        """Permet de trier les bâtiments selon leur difficulté."""
        return self.get_building_difficulty() < other.get_building_difficulty()

    def __repr__(self):
        return f"Building({self.id_building}, {len(self.list_infras)} infras, âge={self.building_age} ans, difficulté={self.get_building_difficulty():.2f})"

