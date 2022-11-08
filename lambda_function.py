import json
import requests
import pymysql

def lambda_handler(event, context):

    #Database Connection:
    # connection = pymysql.connect(host='lin-11314-6893-mysql-primary.servers.linodedb.net', user='user_8', password='0wPz3hkQrX_sfLnhi_sD5',db='db8',ssl={"fake_flag_to_enable_tls":True})
    # cur = connection.cursor()
    # cur.connection.commit()

    postcode = ''.join(event['rawQueryString'].split('=')[1])
    
    #Our initial API is used to gather the constituency that will be attached to the searched postcode
    #Using the parsed json information we can also store the longitude and latitude as the inputs for the three following API's

    constituency_url = "https://api.postcodes.io/postcodes/{}/".format(postcode)
    res = requests.get(constituency_url)

    cons_data = json.loads(res.content)
    constituency = cons_data['result']['parliamentary_constituency']
    
    long = cons_data['result']['longitude']
    lat = cons_data['result']['latitude']

    # As aforementioned the longitude and latitude are utilised in the following API to identify the nearest postcodes

    nearest_pc_url = "https://api.postcodes.io/postcodes?lon={}&lat={}/".format(long, lat)
    res1 = requests.get(nearest_pc_url)

    npc_data = json.loads(res1.content)
    
    #From the parsed data we can identify the nearby postcodes as demonstrated in the for loop.
    #Due to the size of the data file it was easier to append the postcodes into a list titled nearby_pc

    nearby_pc = [] 

    for r in npc_data['result']:
        nearby_pc.append(r['postcode'])

    # for item in nearby_pc:
    #     cur.execute("INSERT IGNORE INTO nearest_postcode (nearest_postcode, pid) VALUES (%s, %s)", (nearby_pc[0], nearby_pc[1]))
            #The function above only executes one postcode to be inserted into the database
            #By changing the secondary nearby_pc we are able to inserted the other nearby postcodes into the database as demonstrated below:
            #("INSERT IGNORE INTO nearest_postcode (nearest_postcode, pid) VALUES (%s, %s)", (nearby_pc[0], nearby_pc[2-7]))

    
    #The longitude and latitude were again utilised to determine the crime data associated to a particular postcode

    crimes_url = "https://data.police.uk/api/crimes-street/all-crime?lat={}&lng={}&limit=10".format(lat,long)
    res2 = requests.get(crimes_url)

    crim_data = json.loads(res2.content)
    
    #Following the same trend as before, the data parsed was stored within a list
    #However, on this occassion we only required the latest 10 and so we iterate through the list using enumarate and set out results to only equal 10 searches
    
    crimes_list = []

    if crim_data:
        for index, item in enumerate(crim_data):
            if index < 10:
                category = item['category']
                area = item['location']['street']['name']
                outcome = None 
                if item['outcome_status']:
                    outcome = item['outcome_status']['category']
                
                crimes_list.append((category,area,outcome))

    #for item in nearby_pc:
        #cur.execute("INSERT IGNORE INTO nearest_postcode (crime_stats, category, area, outcome, pid) VALUES (%s, %s)", (crimes_list[0], crimes_list[1]))
        #The function above only executes one postcode to be inserted into the database
            #By changing the secondary nearby_pc we are able to inserted the other nearby postcodes into the database as demonstrated below:
            #("INSERT IGNORE INTO nearest_postcode (nearest_postcode, pid) VALUES (%s, %s)", (crimes_list[0], crimes_list[2-9]))

    #The longitude and latitiude were again utilised to access any planning permissions within a 5 mile radius
    #Due to the extensive information the parsed data presented, a for loop was utilised to extract the relevant data from the ['records']

    #This API was inserted in between a try & except function due to the limitiations of the URL... when working it will display all the necessary planning information
    #It is a failsafe that is neccessary should the URL not pass and thus the failsafe doesnt break the entire code

    try:
        plan_permissions_url = "https://www.planit.org.uk/api/applics/json?lat={}&lng={}&krad=5.0&recent=30&pg_sz=5&sort=-start_date&compress=on".format(lat,long)
        res3 = requests.get(plan_permissions_url)
    
        pp_data = json.loads(res3.content)
        print(pp_data)
        pp_list = []
    
        for x in pp_data['records']:
            pp_list.append(x['uid'])
            pp_list.append(x['description'])
            pp_list.append(x['app_size'])
            pp_list.append(x['app_state'])
            pp_list.append(x['app_type'])
            
    except KeyError as e:
        print('Error: {}'.format(e))

    #for item in nearby_pc:
        #cur.execute("INSERT IGNORE INTO nearest_postcode (planning_permissions, category, area, outcome, pid) VALUES (%s, %s)", (pp_list[0], pp_list[1]))
        #The function above only executes one postcode to be inserted into the database
            #By changing the secondary nearby_pc we are able to inserted the other nearby postcodes into the database as demonstrated below:
            #("INSERT IGNORE INTO nearest_postcode (planning_permissions, uniqueID, description, app_size, app_state, app_type, pid) VALUES (%s, %s)", (pp_list[0], pp_list[2-4]))
    
    #Body is used to store the results gathered from the individual API calls as demonstrated below:
    
    body = {
        "parliamentary_constituency": constituency,
        "nearby_postcodes": nearby_pc,
        "criminal_activity": crimes_list,
        "planning_permissions": pp_list
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
