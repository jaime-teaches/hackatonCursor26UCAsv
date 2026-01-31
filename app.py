import streamlit as st

# Page Config
st.set_page_config(
    page_title="Mercado Justo - Frutas y Verduras", 
    page_icon="🥬", 
    layout="wide"
)

# --- Product Data ---
PRODUCTS = [
    # Frutas
    {"id": 1, "name": "Manzana Roja", "category": "Frutas", "price": 2500, "unit": "kg", "emoji": "🍎"},
    {"id": 2, "name": "Banano", "category": "Frutas", "price": 1800, "unit": "kg", "emoji": "🍌"},
    {"id": 3, "name": "Naranja", "category": "Frutas", "price": 2000, "unit": "kg", "emoji": "🍊"},
    {"id": 4, "name": "Fresa", "category": "Frutas", "price": 4500, "unit": "lb", "emoji": "🍓"},
    {"id": 5, "name": "Uva", "category": "Frutas", "price": 5000, "unit": "kg", "emoji": "🍇"},
    {"id": 6, "name": "Mango", "category": "Frutas", "price": 3000, "unit": "kg", "emoji": "🥭"},
    {"id": 7, "name": "Piña", "category": "Frutas", "price": 3500, "unit": "unidad", "emoji": "🍍"},
    {"id": 8, "name": "Sandía", "category": "Frutas", "price": 4000, "unit": "unidad", "emoji": "🍉"},
    {"id": 9, "name": "Limón", "category": "Frutas", "price": 2200, "unit": "kg", "emoji": "🍋"},
    {"id": 10, "name": "Papaya", "category": "Frutas", "price": 2800, "unit": "kg", "emoji": "🥭"},
    # Verduras
    {"id": 11, "name": "Tomate", "category": "Verduras", "price": 2500, "unit": "kg", "emoji": "🍅"},
    {"id": 12, "name": "Cebolla", "category": "Verduras", "price": 1500, "unit": "kg", "emoji": "🧅"},
    {"id": 13, "name": "Zanahoria", "category": "Verduras", "price": 1800, "unit": "kg", "emoji": "🥕"},
    {"id": 14, "name": "Papa", "category": "Verduras", "price": 1600, "unit": "kg", "emoji": "🥔"},
    {"id": 15, "name": "Lechuga", "category": "Verduras", "price": 1200, "unit": "unidad", "emoji": "🥬"},
    {"id": 16, "name": "Pepino", "category": "Verduras", "price": 1400, "unit": "kg", "emoji": "🥒"},
    {"id": 17, "name": "Pimentón", "category": "Verduras", "price": 3000, "unit": "kg", "emoji": "🫑"},
    {"id": 18, "name": "Brócoli", "category": "Verduras", "price": 3500, "unit": "kg", "emoji": "🥦"},
    {"id": 19, "name": "Espinaca", "category": "Verduras", "price": 2000, "unit": "manojo", "emoji": "🥬"},
    {"id": 20, "name": "Ajo", "category": "Verduras", "price": 8000, "unit": "kg", "emoji": "🧄"},
]

# --- Session State Initialization ---
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "page" not in st.session_state:
    st.session_state.page = "landing"

# --- Helper Functions ---
def format_price(price):
    """Format price in Colombian pesos"""
    return f"${price:,}".replace(",", ".")

def get_cart_total():
    """Calculate total cart value"""
    total = 0
    for product_id, quantity in st.session_state.cart.items():
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if product:
            total += product["price"] * quantity
    return total

def get_cart_count():
    """Get total items in cart"""
    return sum(st.session_state.cart.values())

def add_to_cart(product_id):
    """Add product to cart"""
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id] += 1
    else:
        st.session_state.cart[product_id] = 1

def remove_from_cart(product_id):
    """Remove one unit from cart"""
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id] -= 1
        if st.session_state.cart[product_id] <= 0:
            del st.session_state.cart[product_id]

def clear_cart():
    """Clear all items from cart"""
    st.session_state.cart = {}

# --- Page Functions ---
def show_landing_page():
    """Show the landing/intro page"""
    # Hero Section
    st.markdown("<h1 style='text-align: center;'>🥬 Mercado Justo</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Frutas y verduras frescas directo del campo a tu mesa</h3>", unsafe_allow_html=True)
    
    st.divider()
    
    # Main value proposition
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🌱 Frescura Garantizada")
        st.write("Productos recién cosechados de agricultores locales. Del campo a tu mesa en menos de 24 horas.")
    
    with col2:
        st.markdown("### 💰 Precios Justos")
        st.write("Sin intermediarios. Compramos directamente a los productores para ofrecerte los mejores precios.")
    
    with col3:
        st.markdown("### 🚚 Entrega a Domicilio")
        st.write("Recibe tus productos frescos en la puerta de tu casa. Envío gratis en compras mayores a $50.000.")
    
    st.divider()
    
    # How it works
    st.markdown("## 🛒 ¿Cómo funciona?")
    
    steps = st.columns(4)
    
    with steps[0]:
        st.markdown("### 1️⃣ Explora")
        st.write("Navega por nuestro catálogo de frutas y verduras frescas.")
    
    with steps[1]:
        st.markdown("### 2️⃣ Selecciona")
        st.write("Agrega los productos que necesitas a tu carrito.")
    
    with steps[2]:
        st.markdown("### 3️⃣ Confirma")
        st.write("Ingresa tus datos de entrega y método de pago.")
    
    with steps[3]:
        st.markdown("### 4️⃣ Recibe")
        st.write("Te llevamos tu pedido fresco hasta tu puerta.")
    
    st.divider()
    
    # Products preview
    st.markdown("## 🍎 Nuestros Productos")
    
    prod_cols = st.columns(5)
    sample_products = [
        ("🍎", "Manzana", "$2.500/kg"),
        ("🍌", "Banano", "$1.800/kg"),
        ("🍅", "Tomate", "$2.500/kg"),
        ("🥕", "Zanahoria", "$1.800/kg"),
        ("🥬", "Lechuga", "$1.200/und"),
    ]
    
    for i, (emoji, name, price) in enumerate(sample_products):
        with prod_cols[i]:
            with st.container(border=True):
                st.markdown(f"### {emoji}")
                st.markdown(f"**{name}**")
                st.caption(price)
    
    st.caption("...y muchos más productos frescos")
    
    st.divider()
    
    # Why choose us
    st.markdown("## ❤️ ¿Por qué elegirnos?")
    
    why_cols = st.columns(2)
    
    with why_cols[0]:
        st.markdown("""
        - **🌿 100% Natural**: Productos sin químicos ni conservantes artificiales
        - **👨‍🌾 Apoyo Local**: Compramos a pequeños agricultores de la región
        - **📦 Empaque Ecológico**: Usamos materiales biodegradables
        """)
    
    with why_cols[1]:
        st.markdown("""
        - **⚡ Entrega Rápida**: Pedidos antes de las 12 PM llegan el mismo día
        - **💳 Pago Fácil**: Efectivo, transferencia, Nequi o Daviplata
        - **🔄 Garantía de Frescura**: Si no estás satisfecho, te devolvemos tu dinero
        """)
    
    st.divider()
    
    # Testimonials
    st.markdown("## 💬 Lo que dicen nuestros clientes")
    
    test_cols = st.columns(3)
    
    with test_cols[0]:
        with st.container(border=True):
            st.write("*\"Las frutas siempre llegan frescas y los precios son excelentes. Ya no voy al supermercado.\"*")
            st.caption("— María G.")
    
    with test_cols[1]:
        with st.container(border=True):
            st.write("*\"Me encanta que apoyen a los agricultores locales. Se nota la diferencia en la calidad.\"*")
            st.caption("— Carlos R.")
    
    with test_cols[2]:
        with st.container(border=True):
            st.write("*\"Super rápido el envío y todo muy bien empacado. 100% recomendado.\"*")
            st.caption("— Ana M.")
    
    st.divider()
    
    # CTA
    st.markdown("## 🎉 ¡Comienza a comprar ahora!")
    
    cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])
    
    with cta_col2:
        st.info("🎁 **Primera compra**: Envío GRATIS sin mínimo de compra")
        
        if st.button("🛒 Ir a la Tienda", type="primary", use_container_width=True):
            st.session_state.page = "catalog"
            st.rerun()
        
        if st.button("📞 Contáctanos", use_container_width=True):
            st.session_state.page = "contact"
            st.rerun()
    
    st.divider()
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>📍 Calle Principal #123, Centro | 📱 +57 300 123 4567 | ✉️ mercadojusto@email.com</p>
        <p>Lunes a Sábado: 6:00 AM - 6:00 PM | Domingos: 6:00 AM - 2:00 PM</p>
    </div>
    """, unsafe_allow_html=True)

def show_header():
    """Show the header with navigation"""
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        st.title("🥬 Mercado Justo")
        st.caption("Frutas y verduras frescas a precio justo")
    
    with col2:
        if st.button("🏠 Inicio"):
            st.session_state.page = "landing"
            st.rerun()
    
    with col3:
        if st.button(f"🛒 Carrito ({get_cart_count()})", type="primary" if get_cart_count() > 0 else "secondary"):
            st.session_state.page = "cart"
            st.rerun()
    
    with col4:
        if st.button("📞 Contacto"):
            st.session_state.page = "contact"
            st.rerun()
    
    st.divider()

def show_catalog():
    """Show the product catalog"""
    show_header()
    
    # Filters
    col1, col2 = st.columns([1, 2])
    
    with col1:
        category = st.selectbox(
            "Categoría",
            ["Todas", "Frutas", "Verduras"]
        )
    
    with col2:
        search = st.text_input("🔍 Buscar producto", placeholder="Escribe el nombre del producto...")
    
    st.divider()
    
    # Filter products
    filtered_products = PRODUCTS.copy()
    
    if category != "Todas":
        filtered_products = [p for p in filtered_products if p["category"] == category]
    
    if search:
        filtered_products = [p for p in filtered_products if search.lower() in p["name"].lower()]
    
    # Display products in grid
    if not filtered_products:
        st.info("No se encontraron productos con esos criterios.")
    else:
        # Create rows of 4 products
        cols_per_row = 4
        for i in range(0, len(filtered_products), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                if i + j < len(filtered_products):
                    product = filtered_products[i + j]
                    with col:
                        with st.container(border=True):
                            st.markdown(f"### {product['emoji']} {product['name']}")
                            st.caption(f"Categoría: {product['category']}")
                            st.markdown(f"**{format_price(product['price'])}** / {product['unit']}")
                            
                            # Quantity in cart
                            qty = st.session_state.cart.get(product["id"], 0)
                            if qty > 0:
                                st.success(f"En carrito: {qty}")
                            
                            if st.button("Agregar 🛒", key=f"add_{product['id']}", use_container_width=True):
                                add_to_cart(product["id"])
                                st.rerun()

def show_cart():
    """Show the shopping cart"""
    show_header()
    
    st.subheader("🛒 Tu Carrito")
    
    if not st.session_state.cart:
        st.info("Tu carrito está vacío. ¡Agrega algunos productos!")
        if st.button("← Volver al catálogo"):
            st.session_state.page = "catalog"
            st.rerun()
        return
    
    # Cart items
    for product_id, quantity in list(st.session_state.cart.items()):
        product = next((p for p in PRODUCTS if p["id"] == product_id), None)
        if product:
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            
            with col1:
                st.markdown(f"**{product['emoji']} {product['name']}**")
                st.caption(f"{format_price(product['price'])} / {product['unit']}")
            
            with col2:
                if st.button("➖", key=f"minus_{product_id}"):
                    remove_from_cart(product_id)
                    st.rerun()
            
            with col3:
                st.markdown(f"**{quantity}**")
            
            with col4:
                if st.button("➕", key=f"plus_{product_id}"):
                    add_to_cart(product_id)
                    st.rerun()
            
            with col5:
                subtotal = product["price"] * quantity
                st.markdown(f"**{format_price(subtotal)}**")
            
            st.divider()
    
    # Total and actions
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"### Total: {format_price(get_cart_total())}")
    
    with col2:
        if st.button("🗑️ Vaciar carrito", type="secondary"):
            clear_cart()
            st.rerun()
    
    with col3:
        if st.button("✅ Finalizar compra", type="primary"):
            st.session_state.page = "checkout"
            st.rerun()
    
    st.divider()
    
    if st.button("← Seguir comprando"):
        st.session_state.page = "catalog"
        st.rerun()

def show_checkout():
    """Show the checkout form"""
    show_header()
    
    st.subheader("✅ Finalizar Compra")
    
    if not st.session_state.cart:
        st.warning("Tu carrito está vacío.")
        if st.button("← Volver al catálogo"):
            st.session_state.page = "catalog"
            st.rerun()
        return
    
    # Order summary
    with st.expander("📋 Resumen del pedido", expanded=True):
        for product_id, quantity in st.session_state.cart.items():
            product = next((p for p in PRODUCTS if p["id"] == product_id), None)
            if product:
                subtotal = product["price"] * quantity
                st.write(f"{product['emoji']} {product['name']} x{quantity} = {format_price(subtotal)}")
        st.divider()
        st.markdown(f"**Total: {format_price(get_cart_total())}**")
    
    st.divider()
    
    # Customer info form
    st.markdown("### 📝 Datos de entrega")
    
    with st.form("checkout_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Nombre completo *")
            phone = st.text_input("Teléfono *")
        
        with col2:
            email = st.text_input("Email")
            address = st.text_input("Dirección de entrega *")
        
        notes = st.text_area("Notas adicionales", placeholder="Instrucciones especiales, punto de referencia, etc.")
        
        payment = st.radio(
            "Método de pago",
            ["Efectivo contra entrega", "Transferencia bancaria", "Nequi/Daviplata"]
        )
        
        submitted = st.form_submit_button("🛒 Confirmar pedido", type="primary", use_container_width=True)
        
        if submitted:
            if not name or not phone or not address:
                st.error("Por favor completa los campos obligatorios (*)")
            else:
                st.balloons()
                st.success(f"""
                    ✅ **¡Pedido confirmado!**
                    
                    Gracias {name}, hemos recibido tu pedido por **{format_price(get_cart_total())}**.
                    
                    Te contactaremos al **{phone}** para coordinar la entrega a:
                    **{address}**
                    
                    Método de pago: **{payment}**
                """)
                clear_cart()
    
    if st.button("← Volver al carrito"):
        st.session_state.page = "cart"
        st.rerun()

def show_contact():
    """Show contact information"""
    show_header()
    
    st.subheader("📞 Contáctanos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🏪 Mercado Justo
        
        **Dirección:**  
        Calle Principal #123, Centro  
        Ciudad, País
        
        **Horario:**  
        Lunes a Sábado: 6:00 AM - 6:00 PM  
        Domingos: 6:00 AM - 2:00 PM
        
        **Teléfono:**  
        📱 +57 300 123 4567
        
        **WhatsApp:**  
        💬 +57 300 123 4567
        
        **Email:**  
        ✉️ mercadojusto@email.com
        """)
    
    with col2:
        st.markdown("""
        ### 🚚 Entregas a domicilio
        
        - Entrega gratuita en pedidos mayores a $50.000
        - Envíos el mismo día para pedidos antes de las 12:00 PM
        - Cubrimos toda la ciudad y alrededores
        
        ### 💬 ¿Tienes preguntas?
        
        Escríbenos por WhatsApp y te responderemos en minutos.
        
        ### 🌱 Nuestro compromiso
        
        Trabajamos directamente con agricultores locales para 
        ofrecerte productos frescos a precios justos, sin 
        intermediarios.
        """)
    
    st.divider()
    
    if st.button("← Volver al catálogo"):
        st.session_state.page = "catalog"
        st.rerun()

# --- Routing ---
if st.session_state.page == "landing":
    show_landing_page()
elif st.session_state.page == "catalog":
    show_catalog()
elif st.session_state.page == "cart":
    show_cart()
elif st.session_state.page == "checkout":
    show_checkout()
elif st.session_state.page == "contact":
    show_contact()
