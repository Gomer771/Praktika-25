
from exept import Exceptions

def execute_analysis():

    inspector = Exceptions('var5.csv')
    inspector.analyze_data()

if __name__ == "__main__":
    execute_analysis()