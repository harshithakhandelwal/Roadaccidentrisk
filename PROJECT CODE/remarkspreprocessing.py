# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:59:02 2019

@author: Admin
"""

def preprocessRemarksData(data):

    #Encode Vehicles Involved with a custom logic
    data.loc [data['Remarks'].str.contains('MVJ',case=False,na=False), 'Hospital']='MVJH'
    data.loc [data['Remarks'].str.contains('Silicon city',case=False,na=False), 'Hospital']='siliconcityH'
    data.loc [data['Remarks'].str.contains('Silcon city',case=False,na=False), 'Hospital']='siliconcityH'
    data.loc [data['Remarks'].str.contains('Jalappa',case=False,na=False), 'Hospital']='JalappaH'
    data.loc [data['Remarks'].str.contains('Hoskote',case=False,na=False), 'Hospital']='hoskoteH'
    data.loc [data['Remarks'].str.contains('mulbagal ',case=False,na=False), 'Hospital']='mulbagalH'
    data.loc [data['Remarks'].str.contains('SNR',case=False,na=False), 'Hospital']='snrH'
    data.loc [data['Remarks'].str.contains('kr puram',case=False,na=False), 'Hospital']='kr puramH'
    data.loc [data['Remarks'].str.contains('avalahalli',case=False,na=False), 'Hospital']='avalahalliH'
    data.loc [data['Remarks'].str.contains('bhattarahalli',case=False,na=False), 'Hospital']='bhattarahalliH'
    #data.loc [data['Remarks'].str.contains('no',case=False), 'Hospital']='no'
    #data.loc [data['Remarks'].str.contains('clear',case=False), 'Hospital']='no'
    #data.loc [data['Remarks'].str.contains('self',case=False), 'Hospital']='no'
    #data.loc [data['Remarks'].str.contains('patrol',case=False), 'Hospital']='no'
    #data.loc [data['Remarks'].str.contains('car',case=False), 'Hospital']='no'
    #data.loc [data['Remarks'].str.contains('speed',case=False), 'Hospital']='no'
    #data.loc [data['Remarks'].str.contains('',case=False), 'Hospital']='bhattarahalliH'
    
   # data.loc [data['Remarks'].str.contains('',case=False), 'Hospital']=''
    #data.loc [data['Remarks'].str.contains('',case=False), 'Hospital']=''
    data.loc [data['Remarks'] =='', 'Hospital']='nan'

    #encodedVehiclesResponsible=pd.get_dummies(data['Encoded_VehicleResponsible'],prefix='VehicleResponsible')
    #data['VehicleResponsible_0']=encodedVehiclesResponsible['VehicleResponsible_0']
    #data['VehicleResponsible_1']=encodedVehiclesResponsible['VehicleResponsible_1']
    #data['VehicleResponsible_2']=encodedVehiclesResponsible['VehicleResponsible_2']
    #data['VehicleResponsible_3']=encodedVehiclesResponsible['VehicleResponsible_3']

    #data=data.drop(['VehicleResponsible'],axis=1)
    #data=data.drop(['Encoded_VehicleResponsible'],axis=1)

    return data