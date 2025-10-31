class Infrastructure:
    def __init__(self, infra_id: str, length: float, infra_type: str, nb_houses: int, location: str):
        """
        Initialise une infrastructure avec son identifiant, sa longueur, son type, le nombre de maisons et sa localisation.
        """
        self.infra_id = infra_id
        self.length = float(length)
        self.infra_type = infra_type
        self.nb_houses = int(nb_houses)
        self.location = location  # Ajout de la localisation

    def repair_infra(self):
        """Marque cette infrastructure comme réparée."""
        self.infra_type = "infra_intacte"

    def check_condition(self) -> str:
        """Retourne l'état de l'infrastructure en fonction de son type et sa localisation."""
        if self.infra_type == "infra_intacte":
            return "Infrastructure en bon état"
        else:
            return "Infrastructure endommagée"

    def get_infra_difficulty(self) -> float:
        """Retourne la difficulté de cette infrastructure en fonction de sa longueur et de la zone géographique."""
        if self.nb_houses == 0:
            return float('inf')  # Retourne une valeur infinie si aucune maison n'est présente
        geo_factor = 1.0
        if self.location == "montagne":
            geo_factor = 1.5  # Facteur géographique qui augmente la difficulté en montagne
        elif self.location == "plaine":
            geo_factor = 0.8  # Facteur géographique qui réduit la difficulté en plaine
        return (self.length / self.nb_houses) * geo_factor

    def __radd__(self, other):
        """Permet de sommer les difficultés."""
        if isinstance(other, (int, float)):
            return other + self.get_infra_difficulty()
        return NotImplemented

    def __repr__(self):
        return f"Infrastructure({self.infra_id}, {self.length:.2f}m, {self.infra_type}, {self.nb_houses} maisons, {self.location})"


