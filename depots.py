import depot
class DepotsClass():

    def __init__(self, depot_dict):
        self.E01 = depot.DepotClass(depot_dict["E01"])
        self.E02 = depot.DepotClass(depot_dict["E02"])
        self.E03 = depot.DepotClass(depot_dict["E03"])
        self.E04A = depot.DepotClass(depot_dict["E04A"])
        self.E04B = depot.DepotClass(depot_dict["E04B"])
        self.T05A = depot.DepotClass(depot_dict["5A"])
        self.T05B = depot.DepotClass(depot_dict["5B"])
        self.T26A = depot.DepotClass(depot_dict["26A"])
        self.T26B = depot.DepotClass(depot_dict["26B"])
        self.T21A = depot.DepotClass(depot_dict["21A"])
        self.T21B = depot.DepotClass(depot_dict["21B"])
        self.Gtemp = depot.DepotClass(depot_dict["Gtemp"])
        self.goku = depot.templeClass(depot_dict["goku"])

    def __del__(self):
        pass


            

        