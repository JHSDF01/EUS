from train import depot
class DepotsClass():

    def __init__(self, depot_dict):
        #江ノ島留置線（2と3は廃止されたが過去用に残している）
        self.E01 = depot.DepotClass(depot_dict["E01"])
        self.E02 = depot.DepotClass(depot_dict["E02"])
        self.E03 = depot.DepotClass(depot_dict["E03"])
        self.E04A = depot.DepotClass(depot_dict["E04A"])
        self.E04B = depot.DepotClass(depot_dict["E04B"])
        #江ノ島駅本線
        self.T05A = depot.DepotClass(depot_dict["5A"])
        self.T05B = depot.DepotClass(depot_dict["5B"])
        self.T26A = depot.DepotClass(depot_dict["26A"])
        self.T26B = depot.DepotClass(depot_dict["26B"])
        #稲村ヶ崎駅本線（臨時）
        self.T10A = depot.DepotClass(depot_dict["10A"])
        self.T10B = depot.DepotClass(depot_dict["10B"])
        self.T21A = depot.DepotClass(depot_dict["21A"])
        self.T21B = depot.DepotClass(depot_dict["21B"])
        #鎌倉駅5番線
        self.T15A = depot.DepotClass(depot_dict["15A"])
        self.T15B = depot.DepotClass(depot_dict["15B"])
        #極楽寺検車区出区線
        self.Gtemp = depot.DepotClass(depot_dict["Gtemp"])
        #極楽寺検車区
        self.goku = depot.templeClass(depot_dict["goku"])

    def __del__(self):
        pass


            

        