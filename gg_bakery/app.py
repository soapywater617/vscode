import streamlit as st
import os
from urllib.parse import unquote
from PIL import Image, ImageOps, ImageDraw

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
    .nav a {
        color: #7F6252;
        text-decoration: none;
        font-weight: bold;
        padding: 0 8px;
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


# Navigation bar with links that set the ?page= parameter (no new tab)
st.markdown(
    '''<div class="nav">
    <a href="/?page=Landing%20Page">Home</a>
    <a href="/?page=G%26G%20In%20Numbers">G&G In Numbers</a>
    <a href="/?page=Delivery%20%26%20Pickup">Delivery & Pickup</a>
    <a href="/?page=Events%20%26%20Sales">Events & Sales</a>
    <a href="/?page=About%20Us">About Us</a>
    <a href="#footer-contact">Contact Us</a>
    <a href="/?page=Shop"><button class="shop-btn">Shop</button></a>
    </div>''',
    unsafe_allow_html=True
)

# All pages
all_pages = [
    "Landing Page",
    "Shop",
    "G&G In Numbers",
    "Delivery & Pickup",
    "Events & Sales",
    "About Us",
    "Contact Us"
]

# Get and set page from query params using st.query_params
query_params = st.query_params
page = query_params.get("page", "Landing Page")

# Sidebar navigation (optional, keeps in sync with top nav)
st.sidebar.title("Navigation")
selected = st.sidebar.radio("Go to", all_pages, index=all_pages.index(page))
st.query_params["page"] = selected
page = selected

if page == "Landing Page":
    st.markdown('<div class="custom-title">G&G Bakery</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheading">Subheading that sets up context, shares more info about the website, or generally gets people psyched to keep scrolling.</div>', unsafe_allow_html=True)
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
        st.image("gg_bakery/assets/matcha_puff.png", use_container_width=True) #matchapuff
        st.markdown('<div class="dessert-title">Cream Puffs</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">description description description many flavors</div>', unsafe_allow_html=True)
    with col3:
        st.image("gg_bakery/assets/pink_cupcake.png", use_container_width=True) #strawcupcakes
        st.markdown('<div class="dessert-title">Cupcakes</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Vanilla and strawberry icing on red velvet and vanilla-bean infused cupcakes</div>', unsafe_allow_html=True)

    # Our Mission
    st.markdown('<div class="section-title">Our Mission:</div>', unsafe_allow_html=True)
    col4, col5 = st.columns([2, 3])
    with col4:
        st.write('<div class="blackbody">G&G Bakery’s mission is blah blah bring a smile to every bake proper name place name story time stuff</div>', unsafe_allow_html=True)
    with col5:
        if (os.path.exists("gg_bakery/assets/gglogo.png")):
            st.image("gg_bakery/assets/gglogo.png", use_container_width=True)
        
        else:
            st.image("https://placehold.co/160x160?text=gglogo", use_container_width=True) #gglogo
        
    # Our Reviews
    st.markdown('<div class="section-title">Our Reviews</div>', unsafe_allow_html=True)
    col6, col7, col8 = st.columns(3)
    with col6:
        st.markdown('<div class="ltbrwn-title">“A terrific piece of praise”</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Name<br>Description</div>', unsafe_allow_html=True)
    with col7:
        st.markdown('<div class="ltbrwn-title">“A fantastic bit of feedback”</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Name<br>Description</div>', unsafe_allow_html=True)
    with col8:
        st.markdown('<div class="ltbrwn-title">“A genuinely glowing review”</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Name<br>Description</div>', unsafe_allow_html=True)
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
        st.caption('<div class="greybody">A subheading for this section, as long or as short as you like</div>', unsafe_allow_html=True)
        st.markdown('<button style="background: #7F6252; color: #fff; border: none; border-radius: 6px; padding: 6px 18px; font-family: Gaegu, cursive; font-size: 16px; margin-right: 8px;">Pricing</button>'
                    '<button style="background: #eee; color: #7F6252; border: none; border-radius: 6px; padding: 6px 18px; font-family: Gaegu, cursive; font-size: 16px;">More Info</button>', unsafe_allow_html=True)
    with col2:
        st.image("gg_bakery/assets/plainbagels.png", use_container_width=True) #plainbagels
    col3, col4 = st.columns([2, 3])
    with col3:
        st.image("gg_bakery/assets/straw_cake.png", use_container_width=True) 
    with col4:
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 32px; color: #7F6252; font-weight: bold;">Custom Cakes</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">A subheading for this section, as long or as short as you like</div>', unsafe_allow_html=True)
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
        st.caption('<div class="greybody">Description of lower product<br>$10.99</div>', unsafe_allow_html=True)
        st.image("gg_bakery/assets/bearbagels2.png", use_container_width=True) #bearbagels!
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #7F6252; font-weight: bold;">Bear Bagels ;)</div>', unsafe_allow_html=True)
        st.caption('<div class="greybody">Description of lower product<br>$10.99</div>', unsafe_allow_html=True)
    st.write("")
    # Section heading with 4 subheadings
    st.markdown('<div style="font-family: Gaegu, cursive; font-size: 36px; color: #7F6252; font-weight: bold; margin-top: 2em;">Section heading</div>', unsafe_allow_html=True)
    col7, col8, col9, col10 = st.columns(4)
    for col in [col7, col8, col9, col10]:
        with col:
            st.markdown('<div style="font-family: Gaegu, cursive; font-size: 18px; color: #7F6252; font-weight: bold;">Subheading</div>', unsafe_allow_html=True)
            st.caption('<div class="greybody">Body text for whatever you’d like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story.</div>', unsafe_allow_html=True)
    # Footer
    render_footer()


# New blank pages
elif page == "G&G In Numbers":
    st.markdown('<div style="font-family: Caveat Brush, cursive; font-size: 64px; color: #F64D4C; font-weight: bold; margin-top: 1em;">G&G in Numbers:</div>', unsafe_allow_html=True)
    #st.write("")
    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 28px; color: #F64D4C; font-weight: bold; margin-top: 2em;">Members Involved: ## </div>', unsafe_allow_html=True)
        st.markdown('<div class="blackbody">From volunteer bakers, story-reposters, delivery drivers, event-enterers, '
        'and our beloved customers, heheheheheheh but real number of members involved idk</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 28px; color: #F64D4C; font-weight: bold; margin-top: 8em;">Funds Raised: ## </div>', unsafe_allow_html=True)
        st.markdown('<div class="blackbody" style="margin-bottom: 2em;">Body text for your whole article or post. We’ll put in some lorem ipsum to show how a filled-out page might look:</div>', unsafe_allow_html=True)
    with col2:
        #st.markdown('<div class="section-title" style="font-size: 64px;">20</div>', unsafe_allow_html=True)
        # logo_path = "assets/gglogo.png"
        # if os.path.exists(logo_path):
        #     st.image(logo_path, use_container_width=False, width=160)
        # else:
        #     st.image("https://placehold.co/160x160?text=Logo", use_container_width=False, width=160)
        #st.write("")
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 28px; color: #F64D4C; font-weight: bold; margin-top: 8em;">Events Hosted: ##</div>', unsafe_allow_html=True)
        st.markdown('<div class="blackbody" style="margin-bottom: 0em;">From opening in 2024 till our summer break, we\'ve held 5 events: <br>look forward to even more for our next year!</div>', unsafe_allow_html=True)
        st.markdown("<div style='margin-top: 5em;'> </div>", unsafe_allow_html=True)
        logo_path = "gg_bakery/assets/landing_image.png"
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=False, width=160)
        else:
            st.image("https://placehold.co/160x160?text=Logo", use_container_width=False, width=160)
    render_footer()
elif page == "Delivery & Pickup":
    # Pickup Locations section
    st.markdown('<div style="font-family: Gaegu, cursive; font-size: 72px; color: #a82020; font-weight: bold; margin-top: 1em;">Delivery Locations:</div>', unsafe_allow_html=True)
    st.markdown('<div class="ltbrwnbody" style=" font-size: 18px; margin-bottom: 1em;">The star markers mark locations where we deliver to, including: UW, Interlake HS, Bellevue HS, Tyee MS, and Newport HS.</div>', unsafe_allow_html=True)
    st.image("gg_bakery/assets/map.png", use_container_width=True) #map T-T
    st.markdown('<a href=""><div class="ltbrwnbody" style=" font-size: 18px; margin-bottom: 2em;"><div style="color: #a82020">Click here to get google maps links to delivery meet up locations</div></a>'
    '<br>For delivery, you will meet someone blah blah at the designated location blah blah as discussed with said blah blah'
    'at blah blah time.</div>', unsafe_allow_html=True)
    # Delivery Options section
    st.markdown('<div class="section-title" style="font-size: 40px; color: #a82020; margin-top: 2em;">Pickup (or other) Options:</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("gg_bakery/assets/cafe_sitting.png", use_container_width=False, width=220) #cafe_sitting.png
    with col2:
        st.image("gg_bakery/assets/gglogo.png", use_container_width=True) #gglogo? or other pic
    st.markdown('<div class="ltbrwnbody" style="color: #a82020">General pickups will be throughout the school day @ Newport HS<br>' \
    'Special deliveries can be made to your house. For more info,</div>', unsafe_allow_html=True)
    render_footer()

elif page == "Events & Sales":
    # Main event section
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("gg_bakery/assets/bearbagels2.png", use_container_width=True) #bearbagels2?
    with col2:
        st.markdown('<div class="section-title"style="margin-bottom: 0em; margin-top: 0em; font-size: 40px;">Special Bread Shop Event?</div>', unsafe_allow_html=True)
        #st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #222; margin-bottom: 0.5em;">Most recent</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-family: Gaegu, cursive; font-size: 18px; color: #222; font-weight: bold;">$$$</div>', unsafe_allow_html=True)
        st.markdown('<div class="blackbody">Something something special about our bread shop sales.</div>', unsafe_allow_html=True)
        st.markdown('<div class="greybody">Additional maybe nutrition details</div>', unsafe_allow_html=True)
    st.write("")
    # Past Events section
    st.markdown('<div class="section-title">Past Events</div>', unsafe_allow_html=True)
    #resizing images to have same height and width with PIL helper
    def resize_image(path, target_size=(220,220)):
        from PIL import Image
        try:
            img = Image.open(path)
            return img.resize(target_size)
        except Exception as e:
            st.warning(f"Could not open image: {path} ({e})")
            return None

    # 2 rows of 3 images each
    past_event_imgs = [
        "gg_bakery/assets/customcookieorder.jpg",
        "gg_bakery/assets/puffpuff.png",
        "gg_bakery/assets/hcbopen.png",
        "gg_bakery/assets/matcha_puff.png",
        "gg_bakery/assets/tirastack.png",
        "gg_bakery/assets/hcb_ricekrispies.png"
    ]
    for i in range(0, 6, 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            with col:
                img = resize_image(past_event_imgs[i+j], target_size=(220,220))
                if img is not None:
                    st.image(img, use_container_width=True)
                st.markdown('<div style="font-family: Gaegu, cursive; font-size: 16px; color: #222; font-weight: bold;">Product</div>', unsafe_allow_html=True)
                st.markdown('<div class="greybody">Description of first product</div>', unsafe_allow_html=True)
                st.markdown('<div class="greybody" style="margin-bottom: 1.5em">$10.99</div>', unsafe_allow_html=True)
    render_footer()
elif page == "About Us":
    st.markdown('<div style="font-family: Caveat Brush, cursive; font-size: 64px; color: #F64D4C; font-weight: bold; margin-top: 1em;">Meet the Team:</div>', unsafe_allow_html=True)
    st.write("")
    # First member: left-aligned
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(gg_bakery/assets/giapic.png", width=220)
    with col2:
        st.markdown('<div class="ltbrwnbody">Gia something something lorem ipsum blah blah<br>Favorite sweet treat: Oreo McFlurry :P</div>', unsafe_allow_html=True)
    # Second member: right-aligned
    col3, col4 = st.columns([2, 1])
    with col4:
        st.image("gg_bakery/assets/gracepic.png", width=220)    
    with col3:
        st.markdown('<div class="ltbrwnbody" style="text-align: right;">Grace something something lorem ipsum blah blah blah blah blah<br>Favorite sweet treat: Chocolate Chip Cookies</div>', unsafe_allow_html=True)
    # Third member: left-aligned
    col5, col6 = st.columns([1, 2])
    with col5:
        st.image("gg_bakery/assets/mepic.png", width=220)
    with col6:
        st.markdown('<div class="ltbrwnbody">Sophie something something lorem ipsum blah blah<br>Favorite sweet treat: Crumbl Cannoli Cookie</div>', unsafe_allow_html=True)
    render_footer()
elif page == "Contact Us":
    st.title("Contact Us")
    st.write("")
