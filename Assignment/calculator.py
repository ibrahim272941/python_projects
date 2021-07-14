main_display = '\tBasic Calculator\n\n\t(1)Toplama\n\n\t(2)Cikarma\n\n\t(3)Carpma\n\n\t(4)Bölme'

print(main_display)

while True :

       soru = (input('Giris yapmak icin bir numara tuslayin Cikmak icin "q" ya basin\t:'))
       if soru =='q':
              print('\t\t#####Exiting The Calculator#####')
              break
       elif soru == '1':

              sayi = int(input('Toplama yapmak icin ilk sayiyi girin\t:'))
              sayi_1 = int(input('Toplama yapmak icin ilk sayiyi girin\t:'))
              print(sayi + sayi_1)

       elif soru=='2':
              sayi = int(input('Cikarma yapmak icin ilk sayiyi girin\t:'))
              sayi_1 = int(input('Cikarma yapmak icin ilk sayiyi girin\t:'))  

              print(sayi - sayi_1)

       elif soru=='3':
              sayi = int(input('Carpma yapmak icin ilk sayiyi girin\t:'))
              sayi_1 = int(input('Carpma yapmak icin ilk sayiyi girin\t:'))  

              print(sayi * sayi_1)    

       elif soru=='4':
              sayi = int(input('Bölme yapmak icin ilk sayiyi girin\t:'))
              sayi_1 = int(input('Bölme yapmak icin ilk sayiyi girin\t:'))  

              print(sayi / sayi_1)           
    
       else :
              print('Lütfen bir daha deneyin')