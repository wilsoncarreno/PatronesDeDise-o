from abc import ABC, abstractmethod

# ---- Element hierarchy ----
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor"):
        pass

class City(Element):
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def accept(self, visitor: "Visitor"):
        visitor.visit_city(self)

class Industry(Element):
    def __init__(self, name, annual_revenue):
        self.name = name
        self.annual_revenue = annual_revenue
    def accept(self, visitor: "Visitor"):
        visitor.visit_industry(self)

class Sight(Element):
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    def accept(self, visitor: "Visitor"):
        visitor.visit_sight(self)

# ---- Visitor interface + concretes ----
class Visitor(ABC):
    @abstractmethod
    def visit_city(self, city: City): ...
    @abstractmethod
    def visit_industry(self, industry: Industry): ...
    @abstractmethod
    def visit_sight(self, sight: Sight): ...

class XmlExportVisitor(Visitor):
    def __init__(self):
        self._parts = []
    def visit_city(self, city: City):
        self._parts.append(f'<city name="{city.name}" population="{city.population}"/>')
    def visit_industry(self, industry: Industry):
        self._parts.append(f'<industry name="{industry.name}" revenue="{industry.annual_revenue}"/>')
    def visit_sight(self, sight: Sight):
        self._parts.append(f'<sight name="{sight.name}" rating="{sight.rating}"/>')
    def output(self):
        return "<graph>\n  " + "\n  ".join(self._parts) + "\n</graph>"

class StatsVisitor(Visitor):
    def __init__(self):
        self.city_count = 0
        self.total_population = 0
        self.industry_count = 0
        self.total_revenue = 0.0
        self.sight_count = 0
        self.avg_rating_sum = 0.0
    def visit_city(self, city: City):
        self.city_count += 1
        self.total_population += city.population
    def visit_industry(self, industry: Industry):
        self.industry_count += 1
        self.total_revenue += industry.annual_revenue
    def visit_sight(self, sight: Sight):
        self.sight_count += 1
        self.avg_rating_sum += sight.rating
    def report(self):
        avg_rating = (self.avg_rating_sum / self.sight_count) if self.sight_count else 0.0
        return {
            "cities": self.city_count,
            "total_population": self.total_population,
            "industries": self.industry_count,
            "total_revenue": self.total_revenue,
            "sights": self.sight_count,
            "avg_sight_rating": round(avg_rating, 2),
        }

# ---- Client code ----
elements: list[Element] = [
    City("Rome", 2873000),
    Industry("BankCorp", 1_200_000.0),
    Sight("Colosseum", 4.8),
    City("Milan", 1352000),
    Sight("Duomo", 4.7),
]

# Apply XML export visitor
xml_vis = XmlExportVisitor()
for el in elements:
    el.accept(xml_vis)
print(xml_vis.output())

# Apply stats visitor
stats_vis = StatsVisitor()
for el in elements:
    el.accept(stats_vis)
print(stats_vis.report())
