# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 05:58:01 2019

@author: HARSHITHA 
"""

import pandas as pd
import numpy as np
from tkinter import Label

from tkinter import *
from tkinter import ttk
#from tkinter.filedialog import askopenfilename
from tkinter import messagebox



root = Tk() 
root.title('Data Mining Based Risk Estimation of Road Accidents')
root.geometry('850x650')
root.configure(background="#C8F9C4")
root.attributes('-fullscreen', True)


var = StringVar()
label = Label( root, textvariable = var,font=('arial',20,'bold'),bd=20,background="#C8F9C4")
var.set("Data Mining Based Risk Estimation of Road Accidents")
label.grid(row=0,columnspan=6)
#removeB = Tk.Button(self.itemFrame, text="Remove", width=10, command=self.removeIsosurface)

def remove1():
    
    root.destroy()
    
def clear():
    
    root.destroy()
    import os
   
    os.system('python risk.py')

def Rule_display():
    root1=Tk()
    root1.title("Rules")
    root1.geometry('800x800')
    root1.configure(background="turquoise3")
    root1.attributes('-fullscreen', True)
    

    root1.grid_columnconfigure(0, minsize=300) 
    
    label_6 = ttk.Label(root1, text = 'support',font=("Helvetica", 16),background="turquoise3")
    label_6.grid(row=1,column=2)
    
    Entry_6 = Entry(root1)
    Entry_6.grid(row=1,column=3)
    
    
    
    label_7 = ttk.Label(root1, text = 'confidence',font=("Helvetica", 16),background="turquoise3")
    label_7.grid(row=2,column=2)
    
    Entry_7 = Entry(root1)
    Entry_7.grid(row=2,column=3)
    
    def ruleplot():
        if not Entry_6.get():
            messagebox.showwarning("missing value","please range the support value")
        elif not Entry_7.get():
             messagebox.showwarning("missing value","please range the confidence value")
        elif(not Entry_6.get() or not Entry_7.get()):
            messagebox.showwarning("missing value","please range the support or confidence value")       
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
        from apyori import apriori  
        import pandas as pd
        import numpy as np
        df=pd.read_csv('3g.csv')
        df.shape
        df.columns
        del df['SrNo'] 
        del df['Fatal']
        del df['Grevious']
        del df['Minor']
        del df['Injured']
        del df['Date']
        del df['a']
        
        records = []  
        for i in range(0, 807):  
            records.append([str(df.values[i,j]) for j in range(0, 10)])
        association_rules = apriori(records, min_support=float(Entry_6.get()), min_confidence=float(Entry_7.get()), min_lift=1.0)
        association_results = list(association_rules)
        for item in association_results:
        
            # first index of the inner list
            # Contains base item and add item
            pair = item[0] 
            items = [x for x in pair]
        import random
        import matplotlib.pyplot as plt
         
        support=[]
        confidence=[]
        lift=[]
        color=[]
        for a in association_results:
            support.append(a[1])
            confidence.append(a[2][0][2])
            lift.append(a[2][0][3])
            color.append(a[2][0][3]*20.0)
            
        print(len(support))
        rules = []
        for item in association_results:
            # first index of the inner list
            # Contains base item and add item
            pair = item[0] 
            items = [x for x in pair]
            rules.append("Rule: " + str(items)+"->"+ items[0]+"\n")
            #print("Rule: " + str(items)+"->"+ items[0])
            print(rules)
        rules = "".join(x for x in rules)
        Text_rule.delete('1.0',END)
        Text_rule.insert(INSERT,rules)
        
    Text_rule = Text(root1)
    #Text_rule.tag_config("here", background="black", foreground="green")
    Text_rule.configure({"background": "bisque"})
    Text_rule.configure({"foreground": "black"})

    Text_rule.grid(row=3,column=2)
    
   # B3 = Button(root1, text = "",width=10,bg="turquoise3")
   # B3.grid(row=4,column=2)
   # estyle = ttk.Style()
   # Entry_extra = Entry(root1)
   # Entry_extra.grid(row=1,column=1)
   # estyle.configure("EntryStyle.TEntry",background="green",) 
    root1.grid_rowconfigure(4, minsize=40) 
    
    B3 = Button(root1, text = "mine",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="DarkOrange2",command=ruleplot)
    B3.grid(row=5,column=2)
    
    def removeIsosurface():
        root1.destroy()

    B12 = Button(root1, text = "Quit",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="DarkOrange2",command=removeIsosurface)
    B12.grid(row=6,column=2)

    
    root1.mainloop()


data_new = []
def new_data():
    root10 = Tk()
    root10.title('Report Anonymous Accidents')
    root10.geometry('400x300+750+100')
    root10.configure(background="VioletRed1")
    
    """var = StringVar()
    label = Label( root, textvariable = var,font=('arial',20,'bold'),bd=20,background="Powderblue")
    var.set("")
    label.grid(row=0,columnspan=6)
    """
    label_1 = ttk.Label(root10, text ='Date',font=("Helvetica", 16),background="VioletRed1")
    label_1.grid(row=0,column=0)
    
    Entry_1 = Entry(root10)
    Entry_1.grid(row=0,column=1)
    
    label_2 = ttk.Label(root10, text = 'Time',font=("Helvetica", 16),background="VioletRed1")
    label_2.grid(row=1,column=0)
    
    Entry_2 = Entry(root10)
    Entry_2.grid(row=1,column=1)
    
    label_3 = ttk.Label(root10, text = 'Location',font=("Helvetica", 16,),background="VioletRed1")
    label_3.grid(row=2,column=0)
    
    Entry_3 = Entry(root10)
    Entry_3.grid(row=2,column=1)
    
    label_4 = ttk.Label(root10, text = 'Type of vehicle' ,font=("Helvetica", 16),background="VioletRed1")
    label_4.grid(row=3,column=0)
    
    Entry_4 = Entry(root10)
    Entry_4.grid(row=3,column=1)
    
    label_5 = ttk.Label(root10, text = 'Type of accident',font=("Helvetica", 16),background="VioletRed1")
    label_5.grid(row=4,column=0)
    
    Entry_5 = Entry(root10)
    Entry_5.grid(row=4,column=1)
    
    label_6 = ttk.Label(root10, text = 'No of Casualities',font=("Helvetica", 16),background="VioletRed1")
    label_6.grid(row=5,column=0)
    
    Entry_6 = Entry(root10)
    Entry_6.grid(row=5,column=1)
    
    label_7 = ttk.Label(root10, text = 'Vehicle Number',font=("Helvetica", 16),background="VioletRed1")
    label_7.grid(row=6,column=0)
    
    Entry_7 = Entry(root10)
    Entry_7.grid(row=6,column=1)
    
    global model,labelText
    
    def writetocsv():
        global model,labelText
        if (not Entry_1.get() or not Entry_2.get() or not Entry_3.get() or not Entry_4.get() or not Entry_5.get() or not Entry_6.get() or not Entry_7.get()) :
            messagebox.showinfo("missing value","enter data")
        else:    
            data_new.append(Entry_1.get()+","+Entry_2.get()+","+Entry_3.get()+","+Entry_4.get()+","+Entry_5.get()+","+Entry_6.get()+","+Entry_7.get()+"\n")
        
            file = open('data.csv','w')
            file.writelines(data_new)
            file.close()
        
    label_7 = Button(root10, text = 'submit',font=("Helvetica", 16),background="green yellow",command = writetocsv)
    label_7.grid(row=7,column=0)
    
    def remove():
        root10.destroy()

    Bq = Button(root10, text = "Quit",height=1,padx=3,pady=3,bd=3,font=("Helvetica", 16),width=5,bg="green yellow",command=remove)
    Bq.grid(row=7,column=1)


def risk_predict():
    root11 = Tk()
    root11.title('RISK PREDICTION')
    #root11.geometry('500x500')
    #root11.configure(background="white")
    root11.geometry("500x500+780+00")
    root11.configure(background="SeaGreen1")
    
    var = StringVar()
    label = Label( root11, textvariable = var,font=('arial',20,'bold'),bd=20,background="white")
    var.set("RISK PREDICTION")
    label.grid(row=0,columnspan=6)
    
    label_1 = ttk.Label(root11, text ='Area',font=("Helvetica", 16),background="white")
    label_1.grid(row=1,column=0)
    label_21 = ttk.Label(root11, text ='Time',font=("Helvetica", 16),background="white")
    label_21.grid(row=1,column=2)
    tkvar = StringVar(root11)
    tkvar21 = StringVar(root11)
    choices = ['A Narayanapura','Agaram','Banasavadi','Basavanapura','Bellanduru','Benniganahalli','Bharathi Nagar','BTM Layout','C V Raman Nagar','Chickpete','Devasandra','Dharmaraya Swamy Temple','Dodda Nekkundi','Domlur','Garudachar Playa','Gurappanapalya','Hagadur','HAL Airport','Halsoor','Hemmigepura','Horamavu','Hoysala Nagar','HSR Layout','Hudi','J P Nagar','Jaraganahalli','Jayanagar East','Jeevanbhima Nagar','Jogupalya','K R Puram','Kacharkanahalli','Kadugodi','Kammanahalli','Konena Agrahara','Madivala','Marathahalli','New Tippasandara','Other','other','Ramamurthy Nagar','Sampangiram Nagar','Sarakki','Shantala Nagar','Singasandra','Sudham Nagara','Varthuru','Vasanthpura','Vijnana Nagar','Vijnanapura','Yelchenahalli']
    choices21=['Early','PeakM','RegularM'] 
    popupMenu = OptionMenu(root11, tkvar, choices[1], *choices)
    popupMenu1 = OptionMenu(root11, tkvar21, choices21[1], *choices21)
    #popupMenu = OptionMenu(root11, tkvar, choices[1], *choices)
    #Label(root, text="select area",background="purple2").grid(row=0,column=0)
    popupMenu.grid(row=1,column=1)
    popupMenu1.grid(row=1,column=3)
    tkvar.set('Select area')
    tkvar21.set('Select Time')
  
    def train():
        from PIL import ImageTk,Image  
        import pandas as pd
        import numpy as np
        global kmf2label
        #kmf2label = {'Area' : ""}
        #kmf2label['Area'] = {'Kadugodi': 1, 'Garudachar Playa': 1, 'Hudi': 1, 'Other': 1, 'Devasandra': 1,'Hagadur': 1, 'Bellanduru': 0, 'Marathahalli': 0, 'Dodda Nekkundi': 0, 'Varthuru': 0,'HAL Airport': 0, 'Vijnana Nagar': 0, 'Konena Agrahara': 1, 'A Narayanapura': 0,'C V Raman Nagar': 0, 'Jeevanbhima Nagar': 0, 'HSR Layout': 1, 'Domlur': 1, 'Jogupalya': 1,'Hoysala Nagar': 0, 'New Tippasandara': 0, 'Benniganahalli': 1, 'Singasandra': 0,'Basavanapura': 0, 'Halsoor': 1, 'Agaram': 1, 'Shantala Nagar': 1, 'Sampangiram Nagar': 0,'Sudham Nagara': 1, 'Dharmaraya Swamy Temple': 0, 'Chickpete': 1, 'Banasavadi': 0,'Horamavu': 1, 'Kacharkanahalli': 1, 'Kammanahalli': 1, 'Vijnanapura': 1, 'Ramamurthy Nagar': 1,'K R Puram': 1, 'BTM Layout': 1, 'Madivala': 1, 'Gurappanapalya': 0, 'J P Nagar': 0, 'Sarakki': 1,'Jaraganahalli': 1, 'Vasanthpura': 1, 'Hemmigepura': 1, 'Yelchenahalli': 1,'Jayanagar East': 1, 'Bharathi Nagar': 0,}
        
        bdf = pd.read_excel('bangalore-cas-alerts.xlsx')
        bdf.info()
        bdf = bdf.rename(columns = {'deviceCode_time_recordedTime_$date':'timestamp'})
        bdf['timestamp'] = pd.to_datetime(bdf['timestamp'])
        bdf['eventDate'] = pd.to_datetime(bdf['timestamp'])
        bdf['eventDate'] = bdf['eventDate'].dt.strftime('%Y%m%d')
        bdf['e_hour'] = pd.to_datetime(bdf['timestamp'], format = '%H:%M:%S').dt.hour
        bdf['ehourCat'] = 0
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 0) & (bdf['e_hour'] < 6), 1, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 6) & (bdf['e_hour'] < 10), 2, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 10) & (bdf['e_hour'] < 16), 3, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 16) & (bdf['e_hour'] < 21), 4, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 21) & (bdf['e_hour'] < 24), 5, bdf['ehourCat'])
        
        bwdf = pd.read_excel('bangalore-weather.xlsx')
        bwdf['w_hour'] = pd.to_datetime(bwdf['time'], format= '%H:%M').dt.hour
        bwdf['hourCat'] = 0
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 0) & (bwdf['w_hour'] < 6), 1, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 6) & (bwdf['w_hour'] < 10), 2, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 10) & (bwdf['w_hour'] < 16), 3, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 16) & (bwdf['w_hour'] < 21), 4, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 21) & (bwdf['w_hour'] < 24), 5, bwdf['hourCat'])
        bwdf = bwdf.drop_duplicates(subset = ['weatherDate', 'hourCat'], keep = 'first')
        bwdf['ehourCat'] = bwdf['hourCat']
        bwdf['weatherDate'] = bwdf['weatherDate'].astype(str)
        bdf['weatherDate'] = bdf['eventDate']
        bdf['weatherDate'] = bdf['weatherDate'].astype(str)
        b1 = pd.merge(bdf, bwdf, on = ['weatherDate', 'ehourCat'], how = 'left')
        b1 = b1.rename(columns = {'deviceCode_location_wardName':'Area'})
        badf = pd.read_excel('bangalore-accident-zones.xlsx')
        b = pd.merge(b1, badf, on = ['Area'], how = 'left')
        b = b.rename(columns = {'deviceCode_pyld_alarmType':'Alarm_Type'})
        b = b.rename(columns = {'deviceCode_pyld_speed':'Plying_Speed'})
        b['hasOversped'] = np.where(b.Plying_Speed > 60, 1, 0)
        b['hasOversped'] = np.where(b.Alarm_Type == 'Overspeed', 1, b['hasOversped'])
        for column in ['temperature', 'visibility', 'condition']:
            b[column].fillna(b[column].mode()[0], inplace=True)
        b['visibility'] = np.where(b['visibility'] < 10, 0, 1)
        df = b.copy()
        df['hasOversped'] = np.where(b.hasOversped == 1, 'Yes', 'No')
        df['visibility'] = np.where(b.visibility == 0, 'Low', 'High')
        df['ehourCat'] = b['ehourCat'].map({1: 'Early', 2: 'PeakM', 3: 'RegularM'})
        b['Accident_Severity'] = b['Accident_Severity'].map({'High': 3, 'Medium': 2, 'Low': 1})
        b['Pothole_Severity'] = b['Pothole_Severity'].map({'High': 3, 'Medium': 2, 'Low': 1})
        b['Alarm_Type'] = b['Alarm_Type'].map({'PCW': 1, 'FCW': 2, 'Overspeed': 3, 'HMW': 4, 'UFCW': 5, 'LDWL': 6, 'LDWR': 7})
        b['condition'] = b['condition'].map({'Clear': 1, 'Sunny': 2, 'Passing clouds': 3,
               'Broken clouds': 4, 'Scattered clouds': 5, 'Fog': 6, 'Haze': 7, 'Partly cloudy': 8,
               'Mild': 9, 'Drizzle. Broken clouds': 10})
        b['Area'] = b['Area'].map({'Kadugodi': 1, 'Garudachar Playa': 2, 'Hudi': 3, 'Other': 4, 'Devasandra': 5,
               'Hagadur': 6, 'Bellanduru': 7, 'Marathahalli': 8, 'Dodda Nekkundi': 9, 'Varthuru': 10,
               'HAL Airport': 11, 'Vijnana Nagar': 12, 'Konena Agrahara': 13, 'A Narayanapura': 14,
               'C V Raman Nagar': 15, 'Jeevanbhima Nagar': 16, 'HSR Layout': 17, 'Domlur': 18, 'Jogupalya': 19,
               'Hoysala Nagar': 20, 'New Tippasandara': 21, 'Benniganahalli': 22, 'Singasandra': 23,
               'Basavanapura': 24, 'Halsoor': 25, 'Agaram': 26, 'Shantala Nagar': 27, 'Sampangiram Nagar': 28,
               'Sudham Nagara': 29, 'Dharmaraya Swamy Temple': 30, 'Chickpete': 31, 'Banasavadi': 32,
               'Horamavu': 33, 'Kacharkanahalli': 34, 'Kammanahalli': 35, 'Vijnanapura': 36, 'Ramamurthy Nagar': 37,
               'K R Puram': 38, 'BTM Layout': 39, 'Madivala': 40, 'Gurappanapalya': 41, 'J P Nagar': 42, 'Sarakki': 43,
               'Jaraganahalli': 44, 'Vasanthpura': 45, 'Hemmigepura': 46, 'Yelchenahalli': 47,
               'Jayanagar East': 48, 'Bharathi Nagar': 49, 'other': 4})
        
        writer = pd.ExcelWriter('bangalore-consolidated-data.xlsx')
        b.to_excel(writer, index = False, sheet_name = 'Sheet1')
        df.to_excel(writer, index = False, sheet_name = 'Sheet2')
        writer.save()
        
        del b['deviceCode_deviceCode'], b['deviceCode_location_latitude'], b['deviceCode_location_longitude']
        del b['w_hour'], b['Mapped_Location'], b['timestamp'], b['e_hour'], b['weatherDate']
        del b['hourCat'], b['time'], b['temperature'], b['eventDate'], b['Plying_Speed']
        
        del df['deviceCode_deviceCode'], df['deviceCode_location_latitude'], df['deviceCode_location_longitude']
        del df['w_hour'], df['Mapped_Location'], df['timestamp'], df['e_hour'], df['weatherDate']
        del df['hourCat'], df['time'], df['temperature'], df['eventDate'], df['Plying_Speed']
               
        from sklearn.cluster import KMeans
        #b=pd.read_excel('bangalore-consolidated-data.xlsx')
        X = b.values.astype(np.float)
        kmeans = KMeans(n_clusters = 2, max_iter = 2000, algorithm = 'full').fit(X)
        kmf2labels = kmeans.labels_
        kmf2labels = kmf2labels.tolist()
        print('Finished clustering using K-Means')
        
        b['labels'] = kmf2labels
        df['labels'] = kmf2labels
        df['labels'] = df['labels'].map({0: 'High', 1: 'Low'})
        
        from sklearn.metrics import confusion_matrix
        mat = confusion_matrix(b['Pothole Severity'], label)
        sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=digits.b['Pothole Severity'],yticklabels=b['Accident Severity'])
        plt.xlabel('true label')
        plt.ylabel('predicted label');
        
        import os
        from PIL import ImageTk,Image
        def main_risk_predict():
            area = df[df['Area']==tkvar.get()]
            time = area[area['ehourCat']==tkvar21.get()]
            #global kmf2label
            res=time['labels'].mode()
            #progress=ttk.Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')
            #def bar():
             #   import time
              #  progress['value']=20
              #  root.update_idletasks()
               # time.sleep(1)
                
            Entry_12.delete(0,END)
            
            Entry_12.insert(0,res[0])
           
            if res[0]=='Low':
                image = Image.open("low.png")
                image = image.resize((550, 250), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image)  
                panel1 = Label(root, image=img)
                panel1.image = img
                panel1.grid(row=3,column=0)
            elif res[0]=='High':
                image = Image.open("high.png")
                image = image.resize((550, 250), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image)  
                panel1 = Label(root, image=img)
                panel1.image = img
                panel1.grid(row=3,column=0)
            else :
                image = Image.open("medium.png")
                image = image.resize((550, 250), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image)  
                panel1 = Label(root, image=img)
                panel1.image = img
                panel1.grid(row=3,column=0)
                
        label_7 = Button(root11, text = 'submit',font=("Helvetica", 16),background="white",command = main_risk_predict)
        label_7.grid(row=2,column=1)
        
        Entry_11.delete(0,END)
        Entry_11.insert(0,'Finished clustering using K-Means')
            
    Entry_12 = Entry(root11)
    Entry_12.grid(row=3,column=2)

    Entry_11 = Entry(root11)
    Entry_11.grid(row=0,column=1)    

    label_8 = Button(root11, text = 'train',font=("Helvetica", 16),background="white",command = train)
    label_8.grid(row=0,column=0) 
    
    
def plot_graph():
    root10 = Tk()
    
    
    
    root10.title('GRAPHS')
   # root10.geometry('500x500')
    root10.geometry("500x500+780+00")
    
    root10.configure(background="deepPink3")
    #root0.configure(background="SeaGreen1")
   # global panel11
    def remove2():
        root10.destroy()
        
        
        
        #panel1(self,visible='no')
        #root.destroy()
        #root.mainloop()
        #root.update()
   # global panel11
    from PIL import ImageTk,Image
    
    import numpy as np # linear algebra
    import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
    import os
        
    import matplotlib.pyplot as plt
    import seaborn as sns
    def graph1():
        df=pd.read_csv('3g.csv')
        ncount=df['Nature of Accident'].value_counts()
        ncount=ncount[:10,]
        plt.figure(figsize=(10,5))
        
        sns.barplot(ncount.index,ncount.values,alpha=0.8)
        plt.title('Cause of accident')
        plt.xlabel('causes')
        plt.ylabel('occurance')
        plt.savefig('graph1.png',dpi=199)
        
        
        image = Image.open("graph1.png")
        image = image.resize((550, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)
        Text_aa.place(x=50,y=620,height=200,width=600)
        Text_aa.delete('1.0',END)
        for i,j in zip(ncount.index,ncount.values):
            
            analysis=" > the cause of accident is \t "+ str(i) +"with \t" +str(j)+" occurances and "+str(j/806)+" probability \n"
            Text_aa.insert(INSERT,analysis)
        
        
    
    def graph2():
        df=pd.read_csv('3g.csv')
        ncount=df['Weather Condition'].value_counts()
        ncount=ncount[:10,]
        plt.figure(figsize=(10,5))
        
        sns.barplot(ncount.index,ncount.values,alpha=0.8)
        plt.title('weather condition')
        plt.xlabel('weather type')
        plt.ylabel('occurances')
        plt.savefig('graph2.png',dpi=199)
        
        image = Image.open("graph2.png")
        image = image.resize((550, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)
        #self.panel1.grid_remove()
        Text_aa.delete('1.0',END)
        Text_aa.place(x=50,y=620,height=200,width=600)
        for i,j in zip(ncount.index,ncount.values):
            analysis=" > the weather condition of accident is \t "+ str(i) +" \t with \t" +str(j)+" occurances and "+str(j/806)+" probability \n"
            Text_aa.insert(INSERT,analysis)
    
    def graph3():
        df=pd.read_csv('new 4g.csv')
        ncount=df['Hospital'].value_counts()
        ncount=ncount[:10,]
        plt.figure(figsize=(10,5))
        
        sns.barplot(ncount.index,ncount.values,alpha=0.8)
        plt.title('hospitals admitted')
        plt.xlabel('hospital')
        plt.ylabel('occurances')
        plt.savefig('graph3.png',dpi=199)
        image = Image.open("graph3.png")
        image = image.resize((550, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)
        Text_aa.place(x=50,y=620,height=200,width=600)
        Text_aa.delete('1.0',END)
        for i,j in zip(ncount.index,ncount.values):
            
            analysis=" > the hospital for response is \t "+ str(i) +" \t with \t" +str(j)+" occurances and "+str(j/806)+" probability \n"
            Text_aa.insert(INSERT,analysis)
    def graph5():
        df=pd.read_csv('new 4g.csv')
        ncount=df['Encoded_VehicleResponsible'].value_counts()
        ncount=ncount[:10,]
        plt.figure(figsize=(10,5))
        
        sns.barplot(ncount.index,ncount.values,alpha=0.8)
        plt.title('type of vehicle')
        plt.xlabel('vehicle type')
        plt.ylabel('occurances')
        plt.savefig('graph5.png',dpi=199)
        image = Image.open("graph5.png")
        image = image.resize((550, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)
        Text_aa.place(x=50,y=620,height=200,width=600)
        Text_aa.delete('1.0',END)
        for i,j in zip(ncount.index,ncount.values):
            
            analysis=" > the vehicle responsible for accident is \t "+ str(i) +"with \t" +str(j)+" occurances and "+str(j/806)+" probability \n"
            Text_aa.insert(INSERT,analysis)
   
    def graph6():
        df=pd.read_csv('new 4g.csv')
        ncount=df['Road Condition'].value_counts()
        ncount=ncount[:10,]
        plt.figure(figsize=(10,5))
        
        sns.barplot(ncount.index,ncount.values,alpha=0.8)
        plt.title('type of road')
        plt.xlabel('condition type')
        plt.ylabel('occurances')
        plt.savefig('graph6.png',dpi=199)
        image = Image.open("graph6.png")
        image = image.resize((550, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)     
        Text_aa.place(x=50,y=620,height=200,width=600)
        Text_aa.delete('1.0',END)
        
        for i,j in zip(ncount.index,ncount.values):
            
            analysis=" > the road condition of accident is \t "+ str(i) +"with \t" +str(j)+" occurances and "+str(j/806)+" probability \n"
            Text_aa.insert(INSERT,analysis)
        
    def graph4():
        import numpy as np # linear algebra
        import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
        import os
        
        import matplotlib.pyplot as plt
        import seaborn as sns
        # Input data files are available in the "../input/
        #" directory.
        # For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
        from pandas import DataFrame , read_csv
        df=pd.read_csv('Details_of_road_accident_deaths_by_situation_state.csv')
        ncount=df['STATE/UT'].value_counts()
        #ap=df[df['STATE/UT']=='ANDHRA PRADESH']
        #ap1=ap[ap['Year']==2001]
        #a=ap1.head(14)
        #ap=df[df['STATE/UT']=='KARNATAKA']
        #ap1=ap[ap['Year']==2001]
        #a=ap1.head(14)
        t=df[df['CAUSE']=='Total Truck/Lorry']
        #t.head()
        r=t[t['STATE/UT']== tkvar.get()]
        fig = plt.figure(figsize=(20,10))
        ax = plt.axes()
        
        x = np.linspace(0, 10, 1000)
        ax.plot(r['Year'],r['Total'])
        ymax=max(r['Total'])
        xpos=r['Total'].idxmax()
        xmax=r['Year'][xpos]
        
        ax.annotate('highest',xy=(xmax,ymax),xytext=(xmax,ymax+5),arrowprops=dict(facecolor='black',shrink=0.05),)
        #ax.set_ylim(0.20)
        #ax.plot(r['Year'],r['Male'],label='male')
        #ax.plot(r['Year'],r['Female'],label='female')
        plt.title('NO OF ACCIDENTS DUE TO TRUCK AND LORRY')
        plt.xlabel('year')
        plt.ylabel('no of accidents')
        plt.savefig('graph4.png',dpi=199)
        
        image = Image.open("graph4.png")
        image = image.resize((750, 350), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)
        
        Text_aa.delete('1.0',END)
        
        Text_aa.place(x=100,y=680,height=100,width=600)
        
        analysis=" > the trends say: The accidents were highest in the year \t "+str(xmax)+" with \t"+ str(r['Total'].max())+" \t accidents \n"
        Text_aa.insert(INSERT,analysis)
        
        

    label_1 = ttk.Label(root10,background="white")
    label_1.grid(row=1,column=0)    
    
    var = StringVar()
    label = Label( root10, textvariable = var,font=('arial',20,'bold'),bd=20,background="white")
    var.set("RISK PREDICTION")
    label.grid(row=0,columnspan=6)
    
    label_1 = ttk.Label(root10, text ='Area',font=("Helvetica", 16),background="deepPink3")
    label_1.grid(row=1,column=0)
    tkvar = StringVar(root10)
    choices = ['ANDHRA PRADESH','ASSAM','BIHAR','CHHATTISGARH','GOA','GUJARAT','HARYANA','HIMACHAL PRADESH','JAMMU & KASHMIR','JHARKHAND','KARNATAKA','KERALA','KERALA','MADHYA PRADESH','MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','ODISHA','PUNJAB','RAJASTHAN','SIKKIM','TAMIL NADU','TRIPURA','UTTAR PRADESH','UTTARAKHAND','WEST BENGAL','TOTAL (STATES)','A & N ISLANDS','CHANDIGARH','D & N HAVELI','DAMAN & DIU','DELHI (UT)','LAKSHADWEEP','PUDUCHERRY','TOTAL (UTs)','TOTAL (ALL INDIA)',]
     
    popupMenu = OptionMenu(root10, tkvar, choices[1], *choices)
    #Label(root, text="select area",background="purple2").grid(row=0,column=0)
    popupMenu.grid(row=1,column=1)
    tkvar.set('Select area')
  
    
    B_rule = Button(root10, text = "Causes",height=1,padx=8,pady=8,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph1)
    B_rule.grid(row=2,column=0) 
    
    
    
    B = Button(root10, text = "condition",height=1,padx=8,pady=8,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph2)
    B.grid(row=3,column=0)
    
    B1 = Button(root10, text = "Hospitals",height=1,padx=8,pady=8,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph3)
    B1.grid(row=2,column=4)
    
    B3 = Button(root10, text = "Trends",height=1,padx=8,pady=8,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph4)
    B3.grid(row=3,column=4)

    B4 = Button(root10, text = "Type of vehicle",height=1,padx=8,pady=8,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph5)
    B4.grid(row=4,column=0)
    
    B5 = Button(root10, text = "Road cond",height=1,padx=8,pady=8,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph6)
    B5.grid(row=4,column=4)
    
    Bqx = Button(root10, text = "Back",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="red",command=remove2)
    Bqx.grid(row=5,column=0)
    
    Text_aa = Text(root)
    #Text_rule.tag_config("here", background="black", foreground="green")
    Text_aa.configure({"background": "bisque"})
    Text_aa.configure({"foreground": "black"})

    Text_aa.grid(row=4,column=0)
    scrollb=Scrollbar(Text_aa)
    
    Text_aa['yscrollcommand']=scrollb.set
    
    

#label_0 = ttk.Label(root,background="white")
#label_0.grid(row=1,column=0)

root.grid_columnconfigure(0, minsize=250) 
#root.grid_rowconfigure(0, minsize=250) 
    
B_rule = Button(root, text = "Rules",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="#EC6E6E",command=Rule_display)
B_rule.grid(row=1,column=1) 

B = Button(root, text = "Risk prediction",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="#ECE86E",command=risk_predict)
B.grid(row=2,column=1)

label_00 = ttk.Label(root,background="white")
label_00.grid(row=1,column=3)

B1 = Button(root, text = "Analytics",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="#6EEC77",command=plot_graph)
B1.grid(row=1,column=3)

B3 = Button(root, text = "Report accident",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=new_data)
B3.grid(row=2,column=3)

Bexit = Button(root, text = "Exit",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="coral2",command=remove1)
Bexit.grid(row=2,column=4)

Bclear = Button(root, text = "clear",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="coral2",command=clear)
Bclear.grid(row=1,column=4)


  

root.mainloop()