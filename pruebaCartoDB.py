from cartodb import CartoDBAPIKey, CartoDBException
API_KEY ='9b9553511ddb8fa0690e9c25b2e03a734f682fdf'
cartodb_domain = 'rpellontid'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
    print cl.sql('select * from hinchas')
except CartoDBException as e:
    print ("some error ocurred", e)
