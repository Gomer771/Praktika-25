from statistics import Players

def main():
    file = 'playstation_players.csv'  
    stats = Players(file) 
    stats.load_data() 
    stats.data_check() 

if __name__ == '__main__':
    main()
