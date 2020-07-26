import pandas as pd

def preProcessResponsibleVehiclesData(data):

    #Encode Vehicles Involved with a custom logic
    data.loc [data['VehicleResponsible'].str.contains('lorry',case=False), 'Encoded_VehicleResponsible']='lorry'
    data.loc [data['VehicleResponsible'].str.contains('truck',case=False), 'Encoded_VehicleResponsible']='truck'
    data.loc [data['VehicleResponsible'].str.contains('car',case=False), 'Encoded_VehicleResponsible']='car'
    data.loc [data['VehicleResponsible'].str.contains('bus',case=False), 'Encoded_VehicleResponsible']='bus'
    data.loc [data['VehicleResponsible'].str.contains('motor cycle',case=False), 'Encoded_VehicleResponsible']='twowheeler'
    data.loc [data['VehicleResponsible'].str.contains('two wheeler',case=False), 'Encoded_VehicleResponsible']='twowheeler'
    data.loc [data['VehicleResponsible'].str.contains('bike',case=False), 'Encoded_VehicleResponsible']='twowheeler'
    data.loc [data['VehicleResponsible'].str.contains('unknown',case=False), 'Encoded_VehicleResponsible']='unknown'
    data.loc [data['VehicleResponsible'].str.contains('lcv',case=False), 'Encoded_VehicleResponsible']='car'
    data.loc [data['VehicleResponsible'].str.contains('tipper',case=False), 'Encoded_VehicleResponsible']='car'
    data.loc [data['VehicleResponsible'].str.contains('matador',case=False), 'Encoded_VehicleResponsible']='car'
    data.loc [data['VehicleResponsible'] =='', 'Encoded_VehicleResponsible']='nan'

    #encodedVehiclesResponsible=pd.get_dummies(data['Encoded_VehicleResponsible'],prefix='VehicleResponsible')
    #data['VehicleResponsible_0']=encodedVehiclesResponsible['VehicleResponsible_0']
    #data['VehicleResponsible_1']=encodedVehiclesResponsible['VehicleResponsible_1']
    #data['VehicleResponsible_2']=encodedVehiclesResponsible['VehicleResponsible_2']
    #data['VehicleResponsible_3']=encodedVehiclesResponsible['VehicleResponsible_3']

    #data=data.drop(['VehicleResponsible'],axis=1)
    #data=data.drop(['Encoded_VehicleResponsible'],axis=1)

    return data




