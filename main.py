# -*- coding: utf-8 -*-

from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from math import sin, cos, sqrt, atan2,pi
import time


class Form(BoxLayout):
    def draw_marker(self): #lista miast wraz ze zdjęciami oraz współrzędnych
        self.list_of_points = [['toronto.jpg', 43, -79],['walencja.jpg', 39, 0],
                               ['ateny.jpg', 37, 23],['rio.jpg', -22, -43],['ny.jpg', 40, -74],
                               ['kilimandzaro.jpg', 37, -3],['krakow.jpg', 50, 19],['sydney.jpg', -33, 151], 
                               ['mekka.jpg', 21, 39],['giza.jpg', 30, 31],['londyn.jpg', 51, 0],['koniec.jpg', 54, 18]]
        
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text="{:10.5f}".format(self.latitude)
        self.search_long.text="{:10.5f}".format(self.longitude)
        
    
    def check_points(self):                             
        print(self.i)                                   
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        time.sleep(1)
        R = 6383.0
        lat1 = (self.latitude)*pi/180
        lon1 = (self.longitude)*pi/180
        lat2 = (self.list_of_points[self.i][1])*pi/180
        lon2 = (self.list_of_points[self.i][2])*pi/180

        dlon = lon1 - lon2    #
        dlat = lat1- lat2
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c   #obliczanie odległosci 
        self.dis.append(distance)
        print(distance)
          
        suma=sum(self.dis)
        
        if suma<1000:                   #punkty
            self.score=1000
        elif suma>1000 and suma<10000:
            self.score=500
        else:
            self.score=100
        self.i=self.i+1
        self.my_image.source =self.list_of_points[self.i][0]
        
        if self.i+1==(len(self.list_of_points)):
            self.koniec.text="Koniec gry"
        self.wynik2.text="{:10.0f}".format(self.score)    
        
    def falszywa(self): 
        self.wynik2.text='0' 
        self.i=0
        self.dis=[]
        self.my_image.source =self.list_of_points[0][0]
        self.koniec.text="START"
           

class MapViewApp(App):
    pass

MapViewApp().run()