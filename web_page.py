import streamlit as st
from PIL import Image
from streamlit import cli as stcli

st.title("TOP 20 RESTAURANTS IN SYDNEY")
st.write('''Have you ever wanted to grab great food and tried to search for the best local restaurants and food
         spots but you spend way more time reading reviews than actually getting a feed? Well,
         we have created a list of the best local Sydney food spots to save your time.''')

Quay=st.container()
La_Salut=st.container()
Lankan_Filling_Station =st.container()
Café_Paci =st.container()
Lolas_Level_1 =st.container()
Saint_Peter =st.container()
Ursulas_Paddington =st.container()
Sixpenny =st.container()
Ester =st.container()
Sean=st.container()
LuMi =st.container()
Odd_Culture_Newtown =st.container()
Bentley_Restaurant_and_Bar =st.container()
Hubert =st.container()
Margaret =st.container()
Firedoor =st.container()
Chaco_Bar =st.container()
Automata =st.container()
William_Street=st.container()
Sáng_by_Mabasa =st.container()


fob=open('Ratings.txt', 'r')
names=[]
ratings=[]
for line in fob.readlines():
    try:
        name=line.split(' -- ')[0]
        rating=line.split(' -- ')[1]
        rating= rating[0] + '/5'
        names.append(name)
        ratings.append(rating)
    except:
        rating= " "
        names.append(name)
        ratings.append(rating)
names=names[1:]
ratings=ratings[1:]

fob_website=open("website.txt", 'r')
lines=fob_website.readlines()
line=2
line_address=0
line_rating=1
website=[]
address=[]
rating=[]
while line < 30:
    website.append(lines[line])
    address.append(lines[line_address].split('-')[1])
    rating.append(lines[line_rating])
    
    line=line+3
    line_address=line_address+3
    line_rating=line_rating+3


with Quay:
    st.header(names[0])
    st.markdown("##### Address :   "+ address[0])
    st.markdown("##### Star-Rating :  "+ rating[0])
    col1,col2,col3,col4, col5=st.columns(5)
    img=Image.open('1. Quay1.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open('1. Quay2.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open('1. Quay3.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open('1. Quay4.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open('1. Quay5.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[0][3:]):
        st.write(website[0])
        
        
        

with La_Salut:
    st.header(names[1])
    st.markdown("##### Address :   "+ address[1])
    st.markdown("##### Star-Rating :  "+ rating[1])
    col1,col2,col3=st.columns(3)
    img=Image.open('2. La Salut1.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open('2. La Salut2.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open('2. La Salut3.JPG')
    col3.image(img,use_column_width=True)
    if st.button("Read More About "+ names[1][3:]):
        st.write(website[1])

with Lankan_Filling_Station:
    st.header(names[2])
    st.markdown("##### Address :   "+ address[2])
    st.markdown("##### Star-Rating :  "+ rating[2])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(names[2]+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(names[2]+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(names[2]+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(names[2]+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(names[2]+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[2][3:]):
        st.write(website[2])

with Café_Paci:
    st.header(names[3])
    st.markdown("##### Address :   "+ address[3])
    st.markdown("##### Star-Rating :  "+ rating[3])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(names[3]+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(names[3]+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(names[3]+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(names[3]+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(names[3]+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[3][3:]):
        st.write(website[3])

with Lolas_Level_1:
    name= names[4]
    st.header(names[4])
    st.markdown("##### Address :   "+ address[4])
    st.markdown("##### Star-Rating :  "+ rating[4])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[4][3:]):
        st.write(website[4])

    
with Saint_Peter:
    name= names[5]
    st.header(names[5])
    st.markdown("##### Address :   "+ address[5])
    st.markdown("##### Star-Rating :  "+ rating[5])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[5][3:]):
        st.write(website[5])

with Ursulas_Paddington:
    name= names[6]
    st.header(names[6])
    st.markdown("##### Address :   "+ address[6])
    st.markdown("##### Star-Rating :  "+ rating[6])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    if st.button("Read More About "+ names[6][3:]):
        st.write(website[6])
    

with Sixpenny:
    name= names[7]
    st.header(names[7])
    st.markdown("##### Address :   "+ address[7])
    st.markdown("##### Star-Rating :  "+ rating[7])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[7][3:]):
        st.write(website[7])

with Ester:
    name= names[8]
    st.header(names[8])
    st.markdown("##### Address :   "+ address[8])
    st.markdown("##### Star-Rating :  "+ rating[8])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[8][3:]):
        st.write(website[8])

with Sean:
    name= names[9]
    st.header(names[9])
    st.markdown("##### Address :   "+ address[9])
    st.markdown("##### Star-Rating :  "+ rating[9])
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    if st.button("Read More About "+ names[9][3:]):
        st.write(website[9])
    

with LuMi:
    name= names[10]
    st.header(names[10])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Odd_Culture_Newtown:
    name= names[11]
    st.header(names[11])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Bentley_Restaurant_and_Bar:
    name= names[12]
    st.header(names[12])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Hubert:
    name= names[13]
    st.header(names[13])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)

with Margaret:
    name= names[14]
    st.header(names[14])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Firedoor:
    name= names[15]
    st.header(names[15])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Chaco_Bar:
    name= names[16]
    st.header(names[16])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Automata:
    name= names[17]
    st.header(names[17])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with William_Street:
    name= names[18]
    st.header(names[18])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
    
with Sáng_by_Mabasa:
    name= names[19]
    st.header(names[19])
    
    col1,col2,col3, col4, col5=st.columns(5)
    img=Image.open(name+ str(1)+ '.JPG')
    col1.image(img, use_column_width=True)
    img=Image.open(name+ str(2)+ '.JPG')
    col2.image(img, use_column_width=True)
    img=Image.open(name+ str(3)+ '.JPG')
    col3.image(img, use_column_width=True)
    img=Image.open(name+ str(4)+ '.JPG')
    col4.image(img, use_column_width=True)
    img=Image.open(name+ str(5)+ '.JPG')
    col5.image(img, use_column_width=True)
         
if __name__ == '__main__':
    stcli.main()


















    
    
    
    
    

