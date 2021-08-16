from src.main.Randomazer.Engine.DataLoader.DataLoader import DataLoader


class TestDataLoader(DataLoader):
    DataLoader._DATA_FILE_PATH = "..\\..\\..\\data\\RandomData.csv"

    def load_data(self):
        super().load_data()
