
from FlightRadar24.api import FlightRadar24API

def main():

    fr_api = FlightRadar24API()
    
    while True:
        choice = input('\nInput a question number: ')
        if choice == '1':
            print(question1(fr_api))

def question1(fr_api):
    airlines = fr_api.get_airlines()

    company_code = []
    for x in airlines:
        company_code.append(x['ICAO'])
    company_code

    most_flight_company = {'ICAO':'','active_flights':0}
    for x in company_code:
        active_flights = len(fr_api.get_flights(airline = x))
        if most_flight_company['active_flights'] < active_flights:
            most_flight_company = {'ICAO':x,'active_flights':active_flights}

    for x in airlines:
        if x['ICAO'] == most_flight_company['ICAO']:
            company = x['Name']
            break

    return f'The company with the most active flights in the world is {company}'
    
    
if __name__ == '__main__':
    main()