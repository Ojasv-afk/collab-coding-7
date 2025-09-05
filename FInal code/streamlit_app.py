import streamlit as st
from main import *

# Configure Streamlit page
st.set_page_config(
    page_title="Math Functions Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply vibrant theme styling
st.markdown("""
<style>
    /* Main background and gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* Remove top padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
    }

    /* Remove top margin from main container */
    .main .block-container {
        margin-top: 0rem !important;
    }
    
    /* Headers with gradient text */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        background: linear-gradient(90deg, #4CAF50, #00BCD4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }
    
    /* Tabs styling with neon effect */
    .st-emotion-cache-1y4p8pa {
        background-color: rgba(45, 45, 45, 0.3) !important;
        backdrop-filter: blur(10px);
        border-radius: 10px;
    }
    .st-emotion-cache-1y4p8pa button {
        color: #00fff2 !important;
        text-shadow: 0 0 10px rgba(0, 255, 242, 0.5);
        transition: all 0.3s ease;
    }
    .st-emotion-cache-1y4p8pa button[data-baseweb="tab"][aria-selected="true"] {
        color: #ff00ff !important;
        border-bottom-color: #ff00ff !important;
        text-shadow: 0 0 10px rgba(255, 0, 255, 0.5);
        transform: scale(1.05);
    }
    .st-emotion-cache-1y4p8pa button:hover {
        transform: scale(1.1);
    }
    
    /* Input fields with glow effect */
    .stNumberInput div input {
        color: #ffffff !important;
        background-color: rgba(45, 45, 45, 0.3) !important;
        border: 2px solid #00fff2 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease;
    }
    .stNumberInput div input:focus {
        box-shadow: 0 0 15px rgba(0, 255, 242, 0.5);
        border-color: #ff00ff !important;
    }
    .stNumberInput div span {
        color: #00fff2 !important;
    }
    
    /* Labels with gradient */
    .stNumberInput label {
        background: linear-gradient(90deg, #00fff2, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }
    
    /* Animated Buttons */
    .stButton button {
        width: 100%;
        background: linear-gradient(45deg, #00fff2, #ff00ff) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 0.7rem !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 255, 242, 0.4);
    }
    .stButton button:active {
        transform: translateY(0);
    }
    
    /* Success/Warning/Error messages with animations */
    .stSuccess {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(0, 255, 242, 0.1)) !important;
        color: #00ff88 !important;
        border-left: 4px solid #00ff88 !important;
        animation: slideIn 0.3s ease;
    }
    .stWarning {
        background: linear-gradient(135deg, rgba(255, 182, 0, 0.1), rgba(255, 0, 255, 0.1)) !important;
        color: #ffb600 !important;
        border-left: 4px solid #ffb600 !important;
        animation: slideIn 0.3s ease;
    }
    .stError {
        background: linear-gradient(135deg, rgba(255, 76, 76, 0.1), rgba(255, 0, 255, 0.1)) !important;
        color: #ff4c4c !important;
        border-left: 4px solid #ff4c4c !important;
        animation: slideIn 0.3s ease;
    }
    
    /* Animation keyframes */
    @keyframes slideIn {
        from {
            transform: translateX(-10px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    /* Container styling */
    .element-container, .stMarkdown, div[data-testid="stVerticalBlock"] > div {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    
    /* Card-like containers */
    .element-container > div {
        background: rgba(45, 45, 45, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(0, 255, 242, 0.1);
        transition: all 0.3s ease;
        overflow: hidden;
    }
    .element-container > div:hover {
        border-color: rgba(255, 0, 255, 0.3);
        box-shadow: 0 0 20px rgba(0, 255, 242, 0.1);
    }
    
    /* Fix header alignments */
    .stHeader {
        padding: 0 !important;
        margin-bottom: 1rem !important;
    }
    
    /* Fix button container width */
    .stButton {
        width: 100% !important;
        max-width: none !important;
    }
    
    /* Fix number input width */
    .stNumberInput {
        width: 100% !important;
    }
    
    /* Better tab spacing */
    div[data-baseweb="tab-list"] {
        gap: 10px;
        padding: 10px !important;
    }
    
    /* Better message spacing */
    .stSuccess, .stWarning, .stError {
        margin: 1rem 0 !important;
        padding: 0.75rem 1rem !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Title with emoji and animation
    st.markdown("""
        <div style='background: rgba(45, 45, 45, 0.2); padding: 1rem; border-radius: 10px; margin: 0; backdrop-filter: blur(10px);'>
            <h1 style='text-align: center; animation: fadeIn 1s ease-in; margin: 0; background: linear-gradient(90deg, #00fff2, #ff00ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                🧮 Mathematical Functions Calculator
            </h1>
        </div>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    """, unsafe_allow_html=True)
    
    
    # Create tabs with icons
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔢 GCD Calculator",
        "🎯 Prime Checker",
        "⚖️ Even/Odd Checker",
        "🧮 Matrix Operations"
    ])
    
    # GCD Calculator Tab
    with tab1:
        st.header("GCD Calculator")
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("First Number", min_value=0, step=1, key="gcd_num1")
        with col2:
            num2 = st.number_input("Second Number", min_value=0, step=1, key="gcd_num2")
        
        if st.button("Calculate GCD", key="gcd_button"):
            if num1 == 0 and num2 == 0:
                st.error("Both numbers cannot be zero")
            else:
                try:
                    result = gcd(int(num1), int(num2))
                    st.success(f"GCD of {int(num1)} and {int(num2)} is: {result}")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Prime Checker Tab
    with tab2:
        st.header("Prime Number Checker")
        num = st.number_input("Enter a number", min_value=0, step=1, key="prime_num")
        
        if st.button("Check Prime", key="prime_button"):
            if num < 0:
                st.error("Please enter a positive number")
            elif num == 0 or num == 1:
                st.warning(f"{int(num)} is neither prime nor composite")
            else:
                try:
                    result = is_prime(int(num))
                    if result:
                        st.success(f"{int(num)} is a prime number!")
                    else:
                        st.warning(f"{int(num)} is not a prime number")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Even/Odd Checker Tab
    with tab3:
        st.header("Even/Odd Checker")
        num = st.number_input("Enter a number", step=1, key="evenodd_num")
        
        if st.button("Check Even/Odd", key="evenodd_button"):
            try:
                result = "even" if int(num) % 2 == 0 else "odd"
                st.success(f"{int(num)} is {result}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # Matrix Operations Tab (22BCS080)
    with tab4:
        st.header("Matrix Operations")

        # ---------------- Matrix A Input ----------------
        st.subheader("Matrix A")
        rows_a = st.number_input("Number of rows for Matrix A", min_value=1, step=1, key="a_rows")
        cols_a = st.number_input("Number of columns for Matrix A", min_value=1, step=1, key="a_cols")

        matrix_a_data = []
        for i in range(rows_a):
            row = st.text_input(f"Enter row {i+1} of Matrix A (space separated)", key=f"a_row_{i}")
            if row:
                try:
                    matrix_a_data.append(list(map(int, row.strip().split())))
                except ValueError:
                    st.error(f"Invalid input in row {i+1}. Please enter integers only.")

        if len(matrix_a_data) == rows_a and all(len(r) == cols_a for r in matrix_a_data):
            A = Matrix(matrix_a_data)

            # ---------------- Select Operation ----------------
            op = st.selectbox("Select operation", [
                "Transpose",
                "Add another matrix",
                "Multiply by another matrix",
                "Determinant",
                "Power"
            ])

            # ---------------- Matrix B Input (if required) ----------------
            B = None
            if op in ["Add another matrix", "Multiply by another matrix"]:
                st.subheader("Matrix B")
                rows_b = st.number_input("Number of rows for Matrix B", min_value=1, step=1, key="b_rows")
                cols_b = st.number_input("Number of columns for Matrix B", min_value=1, step=1, key="b_cols")

                matrix_b_data = []
                for i in range(rows_b):
                    row = st.text_input(f"Enter row {i+1} of Matrix B (space separated)", key=f"b_row_{i}")
                    if row:
                        try:
                            matrix_b_data.append(list(map(int, row.strip().split())))
                        except ValueError:
                            st.error(f"Invalid input in B row {i+1}. Please enter integers only.")

                if len(matrix_b_data) == rows_b and all(len(r) == cols_b for r in matrix_b_data):
                    B = Matrix(matrix_b_data)

            # ---------------- Power Input (if required) ----------------
            k = None
            if op == "Power":
                k = st.number_input("Enter power k", min_value=1, step=1, key="matrix_power")

            # ---------------- Run Operation Button ----------------
            if st.button("Run Operation"):
                try:
                    if op == "Transpose":
                        st.write("Result:")
                        st.write(A.transpose())
                    elif op == "Add another matrix" and B:
                        st.write("Result:")
                        st.write(A.add(B))
                    elif op == "Multiply by another matrix" and B:
                        st.write("Result:")
                        st.write(A.multiply(B))
                    elif op == "Determinant":
                        st.write("Result:")
                        st.write(A.determinant())
                    elif op == "Power" and k is not None:
                        st.write("Result:")
                        st.write(A.power(k))
                    else:
                        st.warning("Invalid operation or incomplete inputs")
                except Exception as e:
                    st.error(str(e))
        else:
            st.info("Please complete all rows of Matrix A to perform operations.")


if __name__ == "__main__":
    main()
