
def  main():

    import streamlit as st
    from PIL import Image
    import sys
    import os
    from streamlit import cli as stcli
    st.title("TOP RESTAURANTS IN SYDNEY")
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



    names=["1. Quay",  "2.\xa0La Salut", "3.\xa0Lankan Filling Station" ,"4.\xa0Café Paci", "5.\xa0Lola's Level 1", "6.\xa0Saint Peter","7.\xa0Ursula's Paddington", "8.\xa0Sixpenny","9.\xa0Ester",
           "10.\xa0Sean's","11.\xa0LuMi","12.\xa0Odd Culture Newtown", "13.\xa0Bentley Restaurant and Bar","14.\xa0Hubert", "15.\xa0Margaret","16.\xa0Firedoor",
           "17.\xa0Chaco Bar","18.\xa0Automata", "19.\xa010 William Street","20.\xa0Sáng by Mabasa"]


    
    website=['If you fancy a fine dining experience with panoramic views of Sydney harbour and Sydney’s pristine waters, this is a great option for you. They offer an extensive menu by Australian chef Peter Gilmore.\n', 'This spot is inspired by Barcelona, Spain. It offers a menu by chef Scott McComas-Williams bringing a taste of Spain to Redfern, Sydney. It showcases the peak of Australian produce.\xa0\n', 'This is a casual eatery, where our food is inspired by traditional Sri Lankan flavours seen through the eyes of Australia. It features a Modern restaurant serving Sri Lankan pancakes, curries & drinks in an easygoing ambience by chef and owner O Tama Carey.\n', 'This hip industrial-chic restaurant offers a gourmet menu of Modern Australian dishes with a twist by finnish-bornn chef Pasi Petanen. The menu explores his Finnish roots with influence drawing from Mexican and Vietnamese cuisine.\n', 'The South European-inspired menu features generously portioned dishes with a clever mix of sharing. The adage to food is to be free spirited, so think of the flavours of Italy, Spain, Greece and the Mediterranean Coast.\n', 'A highly rated seafood restaurant with a fresh and unique menu by Chef Josh Niland. Dry-aged fish is worth a try and is what Niland is renowned for, this restaurant gives quite the experience with the Chef cooking in front of you.\n', 'At his first solo restaurant, acclaimed chef Phil Wood explores and expands Australian cuisine with a produce-driven menu combining classic European cooking. Private dining and group bookings are also available.\n', 'Chefs Daniel Puskas and Anthony Schifilliti lead the kitchen in utilising homegrown local suppliers, growers and producers to focus on creating a narrative around all things that make-up Australia. The restaurant is a cosy space which serves modern Australian food. Reservations are required and events can be held here.\n', 'Trendy restaurant executing eclectic dishes in a concrete-walled space with a wood-fired oven. Australian cuisine\n', 'Small, market-driven restaurant with tasting menus and set meals, plus outdoor seats and surf views. Affectionately known as ‘Sean’s’ since opening in 1993, our little ‘salty jewel’ of a restaurant serves comforting home–style food balanced with modern tastes. A small but affordable spot.']
    address=[' Upper Level Overseas Passenger Terminal, The Rocks\n', ' 305 Cleveland St, Redfern\xa0\n', ' Ground Floor, 58 Riley St, Darlinghurst\xa0\n', ' 131 King street, Newtown\n', ' Level 1/180/186 Campbell Parade, Bondi Beach\n', ' 362 Oxford St, Paddington\n', ' 92 Hargrave St, Paddington\xa0\n', ' 83 Percival Rd, Stanmore\n', ' 46_52 meagher st, chippendale\xa0\n', ' 270 Campbell Parade, North Bondi\xa0\n']
    rating=['4.5 stars\n', '4.7 stars\n', '4.2 stars\n', '4.7 stars\n', '3.6 stars\n', '4.6 stars\n', '4.5 stars\n', '4.8 stars\n', '4.5 stars\n', '4.1 stars\n']

    path = str(os.path.dirname(__file__))
    #st.write(path)
    #arr = os.listdir()
    #st.write(arr)
    
    with Quay:
        st.header(names[0])
        st.markdown("##### Address :   "+ address[0])
        st.markdown("##### Star-Rating :  "+ rating[0])
        col1,col2,col3,col4, col5=st.columns(5)
        img=Image.open("/app/web/1. Quay1.jpg")
        col1.image(img, use_column_width=True)
        img=Image.open("/app/web/1. Quay2.jpg")
        col2.image(img, use_column_width=True)
        img=Image.open("/app/web/1. Quay3.jpg")
        col3.image(img, use_column_width=True)
        img=Image.open("/app/web/1. Quay4.jpg")
        col4.image(img, use_column_width=True)
        img=Image.open("/app/web/1. Quay5.jpg")
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[0][3:]):
            st.write(website[0])
            
            
            

    with La_Salut:
        st.header(names[1])
        st.markdown("##### Address :   "+ address[1])
        st.markdown("##### Star-Rating :  "+ rating[1])
        col1,col2,col3=st.columns(3)
        img=Image.open("/app/web/2. La Salut1.jpg")
        col1.image(img, use_column_width=True)
        img=Image.open("/app/web/2. La Salut2.jpg")
        col2.image(img, use_column_width=True)
        img=Image.open("/app/web/2. La Salut3.jpg")
        col3.image(img,use_column_width=True)
        if st.button("Read More About "+ names[1][3:]):
            st.write(website[1])

    with Lankan_Filling_Station:
        st.header(names[2])
        st.markdown("##### Address :   "+ address[2])
        st.markdown("##### Star-Rating :  "+ rating[2])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open("/app/web/3. Lankan Filling Station1.jpg")
        col1.image(img, use_column_width=True)
        img=Image.open("/app/web/3. Lankan Filling Station2.jpg")
        col2.image(img, use_column_width=True)
        img=Image.open("/app/web/3. Lankan Filling Station3.jpg")
        col3.image(img, use_column_width=True)
        img=Image.open("/app/web/3. Lankan Filling Station4.jpg")
        col4.image(img, use_column_width=True)
        img=Image.open("/app/web/3. Lankan Filling Station5.jpg")
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[2][3:]):
            st.write(website[2])

    with Café_Paci:
        st.header(names[3])
        st.markdown("##### Address :   "+ address[3])
        st.markdown("##### Star-Rating :  "+ rating[3])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open("/app/web/4. Café Paci1.jpg")
        col1.image(img, use_column_width=True)
        img=Image.open("/app/web/4. Café Paci2.jpg")
        col2.image(img, use_column_width=True)
        img=Image.open("/app/web/4. Café Paci3.jpg")
        col3.image(img, use_column_width=True)
        img=Image.open("/app/web/4. Café Paci4.jpg")
        col4.image(img, use_column_width=True)
        img=Image.open("/app/web/4. Café Paci5.jpg")
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[3][3:]):
            st.write(website[3])

    with Lolas_Level_1:
        name= names[4]
        st.header(names[4])
        st.markdown("##### Address :   "+ address[4])
        st.markdown("##### Star-Rating :  "+ rating[4])
        col1,col2,col3, col4, col5=st.columns(5)
        img=Image.open("/app/web/5. Lola's Level 11.jpg")
        col1.image(img, use_column_width=True)
        img=Image.open("/app/web/5. Lola's Level 12.jpg")
        col2.image(img, use_column_width=True)
        img=Image.open("/app/web/5. Lola's Level 13.jpg")
        col3.image(img, use_column_width=True)
        img=Image.open("/app/web/5. Lola's Level 14.jpg")
        col4.image(img, use_column_width=True)
        img=Image.open("/app/web/5. Lola's Level 15.jpg")
        col5.image(img, use_column_width=True)
        if st.button("Read More About "+ names[4][3:]):
            st.write(website[4])



import streamlit 
import sys
from streamlit import cli as stcli
if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())


















    
    
    
    
    

