#NAME:AHEREZA SARAH
#REGISTRATION NO.:16/U/35
#STUDENT NUMBER:216001552
#COMPUTER ENGINEERING YEAR 1
print('This program prints the day of your birth')
import calendar
dy=int(input('Enter your day:'))
mth=int(input('Enter your month:'))
yr=int(input('Enter your year:'))
sar=calendar.weekday(yr,mth,dy)
aher={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
print('Your day of birth is'),aher[sar]

