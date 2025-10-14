import streamlit as st
import streamlit.components.v1 as components #for dynamic calendar?
import calendar
from datetime import datetime #for calendar
import os
from urllib.parse import unquote
from PIL import Image, ImageOps, ImageDraw
# Put this after imports in app.py
hide_streamlit_style = """
    <style>
    /* Hide the left pages sidebar panel (Streamlit auto-pages) */
    [data-testid="stSidebar"] { display: none !important; }
    /* Hide the pages menu button (newer Streamlit uses a pages menu button) */
    button[aria-label="Open navigation menu"], button[title="Open navigation menu"] { display: none !important; }
    /* Hide the top-left hamburger (app menu) if needed */
    .css-1r6slb0.egzxvld0 { display: none !important; } /* fallback, may vary by version */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def render_footer():
    st.markdown(
        '''<div id="footer-contact" class="footer">
        <span style="display: flex; align-items: center; gap: 4px;">
            <a href="https://www.instagram.com/gg._.bakery_/" target="_blank" style="color: inherit; text-decoration: none;">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.5" y2="6.5"/></svg>
            </a>
            G&G Bakery
        </span>
        <span style="display: flex; align-items: center; gap: 4px;">
            <a href="mailto:gg.bakery.service@gmail.com" style="color: inherit; text-decoration: none;">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,6 12,13 2,6"/></svg>
            </a>
            <a href="mailto:gg.bakery.service@gmail.com" style="color: inherit; text-decoration: none;">gg.bakery.service@gmail.com</a>
        </span>
        </div>''',
        unsafe_allow_html=True
    )


# Inject Google Fonts and custom CSS for the landing page
st.markdown(
    '''
    <link href="https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Gaegu:wght@700&display=swap" rel="stylesheet">
    <style>
    body, .main, .block-container { background: #fff; }
    .nav {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 24px;
        font-family: 'Gaegu', cursive;
        font-size: 20px;
        margin-bottom: 2em;
        margin-top: -2em;
    }
    .ltbrwnbody a {
        color: #7F6252;
        text-decoration: none; 
    }
    .nav a {
        color: #7F6252;
        text-decoration: none;
        font-weight: bold;
        padding: 0 8px;
    }
    .section-title a {
        color: #F64D4C;
        text-decoration: none;
        font-weight: bold;
    }
    .shop-btn {
        background: #7F6252;
        color: #fff;
        border: none;
        border-radius: 4px;
        padding: 6px 16px;
        font-family: 'Gaegu', cursive;
        font-size: 16px;
        margin-left: 12px;
        cursor: pointer;
    }
    .custom-title {
        font-family: 'Caveat Brush', cursive;
        font-size: 64px;
        color: #F64D4C;
        margin-bottom: 0.2em;
        margin-top: 0.5em;
    }
    .subheading {
        font-family: 'Gaegu', cursive;
        font-size: 14px;
        color: #7F6252;
        margin-bottom: 1.5em;
    }
    .custom-btn {
        background: #B09382;
        color: #fff;
        border: none;
        border-radius: 6px;
        padding: 8px 24px;
        font-family: 'Gaegu', cursive;
        font-size: 16px;
        margin-bottom: 2em;
        cursor: pointer;
    }
    .section-title {
        font-family: 'Gaegu', cursive;
        font-size: 32px;
        color: #F64D4C;
        margin-top: .5em;
        margin-bottom: 0.5em;
        font-weight: bold;
    }
    .ltbrwn-title {
        font-family: 'Gaegu', cursive;
        font-size: 24px;
        color: #ba9e8d;
        margin-top: .5em;
        font-weight: bold;      

    }
    .dessert-title {
        font-family: 'Gaegu', cursive;
        font-size: 24px;
        color: #7F6252;
        font-weight: bold;
    }
    .footer {
        font-family: 'Gaegu', cursive;
        font-size: 12px;
        color: #000;
        margin-top: 3em;
        border-top: 1px solid #eee;
        padding-top: 1em;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 16px;
    }
    .greybody {
        font-family: 'Gaegu', cursive;
        font-size: 16px;
        color: #737373;
        font-weight: regular;
    }
    .ltbrwnbody {
        font-family: 'Gaegu', cursive;
        font-size: 16px;
        color: #ba9e8d;
        font-weight: regular;
    }
    .darkbrwnbody {
        font-family: 'Gaegu', cursive;
        font-size: 16px;
        color: #7F6252;
        font-weight: regular;
    }
    .blackbody {
        font-family: 'Gaegu', cursive;
        font-size: 16px;
        color: #000000;
        font-weight: 200;
   "}
    </style>
    ''',
    unsafe_allow_html=True
)


# Navigation bar with links that set the ?page= parameter does open a new tab...
st.markdown(
    '''<div class="nav">
    <a href="/?page=Landing%20Page" target="_self">Home</a>
    <!--<a href="/?page=G%26G%20In%20Numbers" target="_self">G&G In Numbers</a>-->
    <a href="/?page=Delivery%20%26%20Pickup" target="_self">Delivery & Pickup</a>
    <a href="/?page=Events%20%26%20Sales" target="_self">Events & Sales</a>
    <a href="/?page=About%20Us" target="_self">About Us</a>
    <a href="#footer-contact" target="_self">Contact Us</a>
    <a href="/?page=Shop" target="_self"><button class="shop-btn">Shop</button></a>
    </div>''',
    unsafe_allow_html=True
)

# All pages
all_pages = [
    "Landing Page",
    "Shop",
    #"G&G In Numbers",
    "Delivery & Pickup",
    "Events & Sales",
    "About Us",
    #"Contact Us"
]

# Get and set page from query params using st.query_params
query_params = st.query_params
page = query_params.get("page", "Landing Page")

# Sidebar navigation (optional, keeps in sync with top nav)
#st.sidebar.title("Navigation")
#selected = st.sidebar.radio("Go to", all_pages, index=all_pages.index(page))
#st.query_params["page"] = selected
#page = selected
def resize_image(path, target_size=(220,220)):
    from PIL import Image
    try:
        img = Image.open(path)
        return img.resize(target_size)
    except Exception as e:
        st.warning(f"Could not open image: {path} ({e})")
        return None
    
if page == "Landing Page":
    st.markdown('<div class="custom-title">G&G Bakery</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheading">Welcome valued customer!! Explore our past events, learn more about our team, or find the answer to your cravings in our shop! <br>Have fun ^-^</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://docs.google.com/forms/d/e/1FAIpQLSeN1ZFrdGuOProo8FecOigSmd70JB5NKeAt2uLTJOBRrqR-nQ/viewform"><button class="custom-btn">' \
    'Place a Custom Order</button></a>', unsafe_allow_html=True)
    st.write("")
    col1, col2, col3 = st.columns(3)
    # Logo
    logo_path = "gg_bakery/assets/landing_image.png"
    if os.path.exists(logo_path):
        with col2:
            st.image(logo_path, use_container_width=False, width=220)
    else:
        st.image("https://github.com/soapywater617/vscode/blob/b081cdd8a3218cbae5ac2838ca07b1a220201e05/gg_bakery/assets/landing_image.png", use_container_width=False, width=220)
    st.write("")


    # Recent Desserts
    st.markdown('<div class="section-title">Recent Desserts</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("gg_bakery/assets/tira.png", use_container_width=True) #tira
        st.markdown('<div class="dessert-title">Tiramisu</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Egg-less Tiramisu with smooth, cream cheese whipped cream.</div>', unsafe_allow_html=True)
    with col2:
        st.image(resize_image("gg_bakery/assets/cakepopbag.png",target_size=(220,220)), use_container_width=True) #matchapuff
        st.markdown('<div class="dessert-title">Cake Pops</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Soft, flavorful cake pops coated in premium matcha & chocolate</div>', unsafe_allow_html=True)
    with col3:
        st.image("gg_bakery/assets/pink_cupcake.png", use_container_width=True) #strawcupcakes
        st.markdown('<div class="dessert-title">Cupcakes</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Vanilla and strawberry icing on red velvet and vanilla-bean infused cupcakes</div>', unsafe_allow_html=True)

    #Our Calendary
    st.markdown('<div class="section-title">Calendar</div>', unsafe_allow_html=True)

    #creating calendar
    today = datetime.today()
    today_day = today.day
    today_month = today.month
    today_year = today.year

    #get month name and days in month
    month_name = calendar.month_name[today_month]
    daysInMonth = calendar.monthrange(today_year, today_month)[1]

    # for day in range(1, daysInMonth+1):
    #     if day == today_day and month == today_month and year == today_year:
    #         day_html = f'<li><span class="active">{day}</span></li>'
    #     else:
    #         day_html = f"<li>{day}</li>"
    #     calendar_html += day_html


    calendar_html = f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                    <link href="https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Gaegu:wght@700&display=swap" rel="stylesheet">
                    <style>
                    * {{box-sizing: border-box;}}
                    ul {{list-style-type: none;}}
                    body {{font-family: Verdana, sans-serif;}}

                    .month {{
                    font-family: Gaegu, cursive;
                    padding: 50px 10px;
                    width: 100%;
                    background: #ba9e8d;
                    text-align: center;
                    }}

                    .month ul {{
                    margin: 0;
                    padding: 0;
                    }}

                    .month ul li {{
                    color: white;
                    font-size: 28px;
                    text-transform: uppercase;
                    letter-spacing: 3px;
                    }}

                    .month .prev{{
                    float: left;
                    padding-top: 10px;
                    }}

                    .month .next {{
                    font-family: Gaegu, cursive;
                    float: right;
                    padding-top: 5px;
                    }}

                    .weekdays {{
                    font-family: Gaegu, cursive;
                    font-weight: bold;
                    font-size: 16px;
                    margin: 0;
                    padding: 10px 0;
                    background-color: #ddd;
                    }}

                    .weekdays li {{
                    font-family: Gaegu, cursive;
                    font-weight: bold;
                    font-size: 16px;
                    display: inline-block;
                    width: 11.6%;
                    color: #666;
                    text-align: center;
                    }}

                    .days {{
                    font-family: Gaegu, cursive;
                    padding: 10px ;
                    background: #eee;
                    margin: 0;
                    }}

                    .days li {{
                    list-style-type: none;
                    display: inline-block;
                    width: 5px;
                    height: 40px;
                    text-align: center;
                    border: 1px solid #ccc;
                    margin-bottom: 5px;
                    font-size:16px;
                    color: black;
                    }}

                    .days li .active {{
                    padding: 5px;
                    background: #ba9e8d;
                    color: white !important
                    }}

                    /* Add media queries for smaller screens */
                    @media screen and (max-width:720px) {{
                    .weekdays li, .days li {{width: 11.1%;}}
                    }}

                    @media screen and (max-width: 1000px) {{
                    .days li {{width: 13.5%;}}
                    .days li .active {{padding: 2px;}}
                    }}

                    @media screen and (max-width: 290px) {{
                    .weekdays li, .days li {{width: 8.2%;}}
                    }}
                    
                    </style>
                        <style>
                        .main .block-container {{
                        max-width: 100% !important;
                        padding-left: 0rem;
                        padding-right: 0rem;
                        }}   
                    </style>
                    </head>
                    <body>
                    <div style="width:100%; display:block;">
                    <div class="month">           
                    <ul>
                        <li>{month_name}</li>
                        <li style="font-size:18px">{today_year}</li>
                    </ul>
                    </div>

                    <ul class="weekdays">
                    <li>Mo</li>
                    <li>Tu</li>
                    <li>We</li>
                    <li>Th</li>
                    <li>Fr</li>
                    <li>Sa</li>
                    <li>Su</li>
                    </ul>

                    <ul class="days">
                    """

    # Fill in days of the month
    for day in range(1, daysInMonth + 1):
        if day == today_day:
            calendar_html += f"<li><span class='active'>{day}</span></li>"
        else:
            calendar_html += f"<li>{day}</li>"

    calendar_html += "</ul>"

    col1, col2 = st.columns([1,1])
    with col1:
        components.html(calendar_html, height=800, scrolling=True)
    with col2:
        st.markdown('<div class="ltbrwnbody" style=" font-size: 28px;">Available Today:</div>', unsafe_allow_html=True)
        st.caption('<div class="ltbrwnbody" style="margin-bottom: 1em;">Updated Daily! Click the dark brown words for more info</div>',unsafe_allow_html=True)
        #ongoing event
        st.markdown('<div class="ltbrwnbody" style="font-size: 20px;"><a href="/?page=Events%20%26%20Sales" target="_self">Bread shop:</a></div>',unsafe_allow_html=True)
        st.markdown('<div class="ltbrwnbody" style="font-size: 18px;">- Bagels<br>- Bread loaves</div>',unsafe_allow_html=True)
        #custom
        st.markdown('<div class="ltbrwnbody" style="font-size: 20px;"><a href="https://docs.google.com/forms/d/e/1FAIpQLSeN1ZFrdGuOProo8FecOigSmd70JB5NKeAt2uLTJOBRrqR-nQ/viewform">Custom Orders:</a></div>',unsafe_allow_html=True)
        st.markdown('<div class="ltbrwnbody" style="font-size: 18px; margin-bottom: 0.5em;">- Cakes</div>',unsafe_allow_html=True)
        st.image("gg_bakery/assets/customcake_ia.png", width=200) #custom cake pic
        st.caption('<div class="greybody" style="font-size: 14px; margin-top: -1em; margin-bottom: -2em;">One of our custom ordered cakes!</div>', unsafe_allow_html=True)
        st.markdown('<div class="ltbrwnbody" style="font-size: 20px; margin-top:-1em;"><br>- Cupcakes<br>- Cookies<br>- Pastries<br></div>',unsafe_allow_html=True)

    # Our Mission
    st.markdown('<div class="section-title">Our Mission:</div>', unsafe_allow_html=True)
    col4, col5 = st.columns([2, 3])
    with col4:
        st.write('<div class="blackbody">G&G Bakery strives not only to bring delicious treats ' \
        'to the local community, but also seeks to give back to the larger ' \
        'community by portioning 60 percent of our profits to fund movements that matter, ' \
        'from our community to a global scale</div>', unsafe_allow_html=True)
    with col5:
        if (os.path.exists("gg_bakery/assets/gglogo.png")):
            st.image("gg_bakery/assets/gglogo.png", use_container_width=True)
        
        else:
            st.image("https://placehold.co/160x160?text=gglogo", use_container_width=True) #gglogo
        
    # Our Reviews
    st.markdown('<div class="section-title" style="margin-top:200px;">Our Reviews</div>', unsafe_allow_html=True)
    col6, col7, col8 = st.columns(3)
    with col6:
        st.markdown('<div class="ltbrwn-title">“Not too sweet, very good”</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Fang<br>Sophie\'s mother</div>', unsafe_allow_html=True)
    with col7:
        st.markdown('<div class="ltbrwn-title">“it\'s so good”</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody"><br>Description</div>', unsafe_allow_html=True)
    with col8:
        st.markdown('<div class="ltbrwn-title">“I like the spotted vanilla parts”</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Winnie the pooh<br>Bought extra cupcakes</div>', unsafe_allow_html=True)
    # Footer
    render_footer()


elif page == "Shop":
    # Top hero section with background image and overlay text
    import base64
    from PIL import Image
    import io
    shoplogo_path = "gg_bakery/assets/shoplogo.png"
    if os.path.exists(shoplogo_path):
        with open(shoplogo_path, "rb") as img_file:
            b64_img = base64.b64encode(img_file.read()).decode()
        hero_bg = f"background-image: url('data:image/png;base64,{b64_img}'); background-size: cover; background-position: center; height: 320px; position: relative; display: flex; align-items: center; justify-content: center;"
    else:
        hero_bg = "background: #ccc; height: 320px; position: relative; display: flex; align-items: center; justify-content: center;"
    st.markdown(f'''
    <div style="{hero_bg}">
        <div style="position: absolute; width: 100%; height: 100%; background: rgba(0,0,0,0.3);"></div>
        <div style="position: relative; z-index: 2; width: 100%; text-align: center;">
            <h1 style="font-family: 'Gaegu', cursive; font-size: 64px; color: #fff; margin-bottom: 0.2em;">Our Shop</h1>
            <div style="font-family: 'Gaegu', cursive; font-size: 24px; color: #fff; margin-bottom: 1em;">Custom Orders Open Now!</div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSeN1ZFrdGuOProo8FecOigSmd70JB5NKeAt2uLTJOBRrqR-nQ/viewform">
            <button style="background: #7F625; color:  #7F6252; border: none; border-radius: 6px; padding: 10px 32px; font-family: 'Gaegu', cursive; font-size: 18px;">Order</button>
        </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    st.write("")
    # Currently selling and Custom Cakes section
    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 32px; color: #7F6252; font-weight: bold;">Bread Bags?</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Bread bags with </div>', unsafe_allow_html=True)
        st.markdown('<button style="background: #7F6252; color: #fff; border: none; border-radius: 6px; padding: 6px 18px; font-family: Gaegu, cursive; font-size: 16px; margin-right: 8px;">Pricing</button>'
                    '<button style="background: #eee; color: #7F6252; border: none; border-radius: 6px; padding: 6px 18px; font-family: Gaegu, cursive; font-size: 16px;">More Info</button>', unsafe_allow_html=True)
    with col2:
        st.image("gg_bakery/assets/plainbagels.png", use_container_width=True) #plainbagels
    col3, col4 = st.columns([2, 3])
    with col3:
        st.image("gg_bakery/assets/straw_cake.png", use_container_width=True) 
    with col4:
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 32px; color: #7F6252; font-weight: bold;">Custom Cakes</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Custom cake flavor and design to your liking!</div>', unsafe_allow_html=True)
        st.markdown('<button style="background:  #7F6252; color: #fff; border: none; border-radius: 6px; padding: 6px 18px; font-family: Gaegu, cursive; font-size: 16px; margin-right: 8px;">Pricing</button>'
                    '<button style="background: #eee; color: #7F6252; border: none; border-radius: 6px; padding: 6px 18px; font-family: Gaegu, cursive; font-size: 16px;">More Info</button>', unsafe_allow_html=True)
    st.write("")
    # Featured Product section
    st.markdown('<div style="font-family: Gaegu, cursive; font-size: 36px, color: #7F6252; font-weight: bold; margin-top: 2em;">Featured Product:</div>', unsafe_allow_html=True)
    col5, col6 = st.columns([2, 1])
    with col5:
        st.image("gg_bakery/assets/bearbuns.png", use_container_width=True)
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 18px; color: #7F6252; font-weight: bold;">Bear Buns!</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Sweet milk buns, shaped into cute bears :) (4in diameter)<br>Price of One: $6-7</div>', unsafe_allow_html=True)
    with col6:
        st.image("https://placehold.co/200x120?text=Photo", use_container_width=True)
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #7F6252; font-weight: bold;">Shokupan?</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Japanese Milk Bread<br>$10.99</div>', unsafe_allow_html=True)
        st.image("gg_bakery/assets/bearbagels2.png", use_container_width=True) #bearbagels!
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #7F6252; font-weight: bold;">Bear Bagels ;)</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Bagels of your choice with bear faces c._.o<br>$10.99</div>', unsafe_allow_html=True)
    st.write("")
    # Section heading with 4 subheadings
    st.markdown('<div style="font-family: Gaegu, cursive; font-size: 36px; color: #7F6252; font-weight: bold; margin-top: 2em;">Look Forward To:</div>', unsafe_allow_html=True)
    col7, col8, col9, col10 = st.columns(4)
    for col in [col7, col8, col9, col10]:
        with col:
            st.markdown('<div style="font-family: Gaegu, cursive; font-size: 18px; color: #7F6252; font-weight: bold;">Future Product</div>', unsafe_allow_html=True)
            st.caption('<div class="greybody">Something something description maybe + estimated date</div>', unsafe_allow_html=True)
    # Footer
    render_footer()


# New blank pages
# elif page == "G&G In Numbers":
#     st.markdown('<div style="font-family: Caveat Brush, cursive; font-size: 64px; color: #F64D4C; font-weight: bold; margin-top: 1em;">G&G in Numbers:</div>', unsafe_allow_html=True)
#     #st.write("")
#     col1, col2 = st.columns([2, 2])
#     with col1:
#         st.markdown('<div style="font-family: Gaegu, cursive; font-size: 28px; color: #F64D4C; font-weight: bold; margin-top: 2em;">Members Involved: ## </div>', unsafe_allow_html=True)
#         st.markdown('<div class="blackbody">From volunteer bakers, story-reposters, delivery drivers, event-enterers, '
#         'and our beloved customers, heheheheheheh but real number of members involved idk</div>', unsafe_allow_html=True)
#         st.markdown('<div style="font-family: Gaegu, cursive; font-size: 28px; color: #F64D4C; font-weight: bold; margin-top: 8em;">Funds Raised: ## </div>', unsafe_allow_html=True)
#         st.markdown('<div class="blackbody" style="margin-bottom: 2em;">Through all of our events, we\'ve collected ## for blank blank.</div>', unsafe_allow_html=True)
#     with col2:
#         #st.markdown('<div class="section-title" style="font-size: 64px;">20</div>', unsafe_allow_html=True)
#         # logo_path = "gg_bakery/assets/gglogo.png"
#         # if os.path.exists(logo_path):
#         #     st.image(logo_path, use_container_width=False, width=160)
#         # else:
#         #     st.image("https://placehold.co/160x160?text=Logo", use_container_width=False, width=160)
#         #st.write("")
#         st.markdown('<div style="font-family: Gaegu, cursive; font-size: 28px; color: #F64D4C; font-weight: bold; margin-top: 8em;">Events Hosted: ##</div>', unsafe_allow_html=True)
#         st.markdown('<div class="blackbody" style="margin-bottom: 0em;">From opening in 2024 till our summer break, we\'ve held 5 events: <br>look forward to even more for our next year!</div>', unsafe_allow_html=True)
#         st.markdown("<div style='margin-top: 5em;'> </div>", unsafe_allow_html=True)
#         logo_path = "gg_bakery/assets/landing_image.png"
#         if os.path.exists(logo_path):
#             st.image(logo_path, use_container_width=False, width=160)
#         else:
#             st.image("https://placehold.co/160x160?text=Logo", use_container_width=False, width=160)
#     render_footer()
elif page == "Delivery & Pickup":
    # Pickup Locations section
    st.markdown('<div style="font-family: Gaegu, cursive; font-size: 72px; color: #a82020; font-weight: bold; margin-top: 1em;">Delivery Locations:</div>', unsafe_allow_html=True)
    st.markdown('<div class="ltbrwnbody" style=" font-size: 18px; margin-bottom: 1em;">The star markers mark locations where we deliver to, including: UW, Interlake HS, Bellevue HS, Tyee MS, and Newport HS.</div>', unsafe_allow_html=True)
    st.image("gg_bakery/assets/map.png", use_container_width=True) #map T-T
    st.markdown('<a href="https://maps.app.goo.gl/uABmYt72znUA1Z8a7"><div class="ltbrwnbody" style=" font-size: 18px; margin-bottom: 2em;"><div style="color: #a82020">Click here to get Google Maps links to delivery meet-up locations</div></a>'
    '<br>For delivery, you will meet someone blah blah at the designated location blah blah as discussed with said blah blah'
    'at blah blah time.</div>', unsafe_allow_html=True)
    # Delivery Options section
    st.markdown('<div class="section-title" style="font-size: 40px; color: #a82020; margin-top: 2em;">Pickup (or other) Options:</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("gg_bakery/assets/cafe_sitting.png", use_container_width=True) #cafe_sitting.png
    with col2:
        st.image("gg_bakery/assets/gglogo.png", use_container_width=True) #gglogo? or other pic
    st.markdown('<div class="ltbrwnbody" style="color: #a82020">General pickups will be throughout the school day @ Newport HS<br>' \
    'Special deliveries can be made to your house. For more info,</div>', unsafe_allow_html=True)
    render_footer()

elif page == "Events & Sales":
    st.markdown('<div class="custom-title">Events & Sales:</div>', unsafe_allow_html=True)
    # Main event section
    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown('<div class="section-title" style="font-size: 20px;"><br> </div>', unsafe_allow_html=True)
        st.image("gg_bakery/assets/bearbagels2.png", use_container_width=True) #bearbagels2?
    with col2:
        st.markdown('<div class="section-title"style="margin-bottom: 0em; margin-top: 1em; font-size: 40px;"><a href="https://forms.gle/zsrcaV9UQntN98LV8">Bread Shop Now Open!</a></div>', unsafe_allow_html=True)
        #st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #222; margin-bottom: 0.5em;">Most recent</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 18px; color: #7F6252; font-weight: bold;">Bear Bagels:</div>', unsafe_allow_html=True)
        st.markdown('<div class="blackbody" style="font-size: 20px; color: #7F6252;">Something something special about our bread shop sales.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ltbrwnbody">Additional maybe nutrition details</div>', unsafe_allow_html=True)
    st.write("")
    #more pics of current event?
    st.write('<div class="section-title" style="font-size: 24px; margin-bottom: 1em;">More pics from our bread shop (<span style="color: #ffd626">•</span>U<span style="color: #ffd626">•</span>)</div>', unsafe_allow_html=True)
    more_imgs = [
        "gg_bakery/assets/plainbagels2.png",
        "gg_bakery/assets/bearbuns.png",
        "gg_bakery/assets/shokupan.png"
    ]
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            if os.path.exists(more_imgs[i]):
                st.image(more_imgs[i], use_container_width=True)
            else:
                st.image("https://placehold.co/200x120?text=Photo", use_container_width=True)


    # Past Events section
    st.markdown('<div class="section-title" style="margin-top: 2em;">Past Events</div>', unsafe_allow_html=True)
    #resizing images to have same height and width with PIL helper
    # def resize_image(path, target_size=(220,220)):
    #     from PIL import Image
    #     try:
    #         img = Image.open(path)
    #         return img.resize(target_size)
    #     except Exception as e:
    #         st.warning(f"Could not open image: {path} ({e})")
    #         return None

    # 2 rows of 3 images each
    past_event_imgs = [
        "gg_bakery/assets/customcookieorder.jpg",
        "gg_bakery/assets/puffpuff.png",
        "gg_bakery/assets/hcbopen.png",
        "gg_bakery/assets/matcha_puff.png",
        "gg_bakery/assets/tirastack.png",
        "gg_bakery/assets/hcb_ricekrispies.png"
    ]
    texts = [
    "Our 1st Custom Cookie Order 🍪",
    "Cream Puffs!",
    "Holiday Cookie Boxes",
    "Extra Combo Boxes",
    "Our favorite, Tiramisu!!",
    "Cupcakes...?"
    ]
    for i in range(0, 6, 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            with col:
                img = resize_image(past_event_imgs[i+j], target_size=(220,220))
                if img is not None:
                    st.image(img, use_container_width=True)
                #product_name = texts[i+j]
                st.markdown(f'<div class="blackbody" style="margin-bottom: 1em; font-size: 24px;">{texts[i+j]}</div>', unsafe_allow_html=True)
                #st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #222; font-weight: bold;">Product</div>', unsafe_allow_html=True)
                #st.markdown('<div class="greybody">Description of first product</div>', unsafe_allow_html=True)
                #st.markdown('<div class="greybody" style="margin-bottom: 1.5em">$10.99</div>', unsafe_allow_html=True)

    st.write('<div class="section-title" style="margin-top: 2em;">Upcoming Events</div>', unsafe_allow_html=True)
    st.markdown('<div class="ltbrwnbody" style="font-size: 24px;">Look forward to our Special Brookie sale! (unique flavors!!)</div>', unsafe_allow_html=True)
    render_footer()
elif page == "About Us":
    st.markdown('<div style="font-family: Caveat Brush, cursive; font-size: 64px; color: #F64D4C; font-weight: bold; margin-top: 1em;">Meet the Team:</div>', unsafe_allow_html=True)
    st.write("")
    # First member: left-aligned
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("gg_bakery/assets/giapic.png", width=220)
    with col2:
        st.markdown('<div class="ltbrwnbody" style="font-size: 22px; margin-top: 1em;">Gia is one of our two co-founders.' \
        'With a super tuff background in baking, she\'s brought her hobby of baking for friends to a community and regional-wide scale!<br>Favorite sweet treat:'
        '<span style="color: #ba9e8d;"> <span style="color: #7F6252;">Choco</span>late <span style="color: #7F6252;">Chip</span> Cook<span style="color: #7F6252;">ies XD</span></span></div>', unsafe_allow_html=True)
    # Second member: right-aligned
    col3, col4 = st.columns([2, 1])
    with col4:
        st.image("gg_bakery/assets/gracepic.png", width=220)    
    with col3:
        st.markdown('<div class="ltbrwnbody" style="font-size: 22px;margin-top: 2em; text-align: right;;">Grace, our other co-founder, bakes the best bread and bagels,'
        ' so please try them out yes thank you :)<br>' 
        'Favorite sweet treat: <span style="color: #221414;">Oreo <span style="color: #77cdff">Mc</span>Flurry <span style="color: #77cdff">:P</span></span></div>', unsafe_allow_html=True)
    # Third member: left-aligned
    col5, col6 = st.columns([1, 2])
    with col5:
        st.image("gg_bakery/assets/mepic2.png", width=220)
    with col6:
        st.markdown('<div class="ltbrwnbody" style="font-size: 22px; ; margin-top: 1em;">Sophie, a definitely super awesome coder, '
        'and very helpful person of course, is the tech and finance manager, making ordering and getting our desserts even easier~<br>Favorite sweet treat:'
        ' <span style="color: #ffc8d3;">Crumbl <span style="color: #e5b982;">Can</span>noli <span style="color: #e5b982;">Cookie...</span></span></span></div>', unsafe_allow_html=True)
    render_footer()
elif page == "Contact Us":
    st.title("Contact Us")
    st.write("")
