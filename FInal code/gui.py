import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from main import *
import tkinter.font as tkfont

class ModernButton(ttk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs, style='Modern.TButton')

class MathFunctionsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Functions Calculator")
        self.root.configure(bg='#2c3e50')
        
        # Configure styles
        self.setup_styles()
        
        # Create main frame
        main_frame = ttk.Frame(root, style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        title = ttk.Label(main_frame, text="Mathematical Functions", 
                         font=title_font, style='Title.TLabel')
        title.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame, style='Modern.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_gcd_tab()
        self.create_prime_tab()
        self.create_evenodd_tab()
        self.create_matrix_tab()
        self.create_factorial_tab()   # ✅ NEW TAB for factorial
    
    def setup_styles(self):
        # Configure styles for modern look
        style = ttk.Style()
        
        # Configure theme
        style.configure('TFrame', background='#2c3e50')
        style.configure('Main.TFrame', background='#2c3e50')
        
        # Notebook style
        style.configure('Modern.TNotebook', background='#2c3e50')
        style.configure('Modern.TNotebook.Tab', 
                       padding=[12, 8],
                       font=('Helvetica', 10, 'bold'),
                       background='#2c3e50',
                       foreground='#2c3e50')
        
        # Label style
        style.configure('Title.TLabel', 
                       background='#2c3e50',
                       foreground='#FFD700',  # Golden yellow
                       font=('Helvetica', 16, 'bold'))
        
        style.configure('Modern.TLabel',
                       background='#2c3e50',
                       foreground='#FFEB3B',  # Light yellow
                       font=('Helvetica', 10))
        
        # Entry style
        style.configure('TEntry', 
                       fieldbackground='#ecf0f1',
                       foreground='#2c3e50',
                       padding=10)
        
        # Button style
        style.map('Modern.TButton',
                 background=[('active', '#3498db'), ('!active', '#2980b9')],
                 foreground=[('active', '#2c3e50'), ('!active', '#2c3e50')])  # Same as background
        style.configure('Modern.TButton',
                       padding=[15, 10],
                       font=('Helvetica', 10, 'bold'))
        
        # Result style
        style.configure('Result.TLabel',
                       background='#2c3e50',
                       foreground='#FFD700',  # Golden yellow
                       font=('Helvetica', 12, 'bold'))
    
    def create_input_field(self, parent, label_text):
        frame = ttk.Frame(parent, style='Main.TFrame')
        frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text=label_text, 
                 style='Modern.TLabel').pack(side=tk.LEFT, padx=5)
        
        entry = ttk.Entry(frame, style='Modern.TEntry', width=20)
        entry.pack(side=tk.RIGHT, padx=5)
        return entry
    
    def create_gcd_tab(self):
        gcd_frame = ttk.Frame(self.notebook, style='Main.TFrame')
        self.notebook.add(gcd_frame, text='GCD Calculator')
        
        # Content wrapper for centering
        content = ttk.Frame(gcd_frame, style='Main.TFrame')
        content.pack(expand=True, pady=20)
        
        # GCD Input fields with better layout
        self.gcd_num1 = self.create_input_field(content, "First Number:")
        self.gcd_num2 = self.create_input_field(content, "Second Number:")
        
        # Button with modern style
        ModernButton(content, text="Calculate GCD", 
                    command=self.calculate_gcd).pack(pady=20)
        
        self.gcd_result = ttk.Label(content, text="", style='Result.TLabel')
        self.gcd_result.pack(pady=10)
        
    def create_prime_tab(self):
        prime_frame = ttk.Frame(self.notebook, style='Main.TFrame')
        self.notebook.add(prime_frame, text='Prime Checker')
        
        # Content wrapper for centering
        content = ttk.Frame(prime_frame, style='Main.TFrame')
        content.pack(expand=True, pady=20)
        
        self.prime_num = self.create_input_field(content, "Enter Number:")
        
        ModernButton(content, text="Check Prime", 
                    command=self.check_prime).pack(pady=20)
        
        self.prime_result = ttk.Label(content, text="", style='Result.TLabel')
        self.prime_result.pack(pady=10)
    
    def calculate_gcd(self):
        try:
            num1 = int(self.gcd_num1.get())
            num2 = int(self.gcd_num2.get())
            result = gcd(num1, num2)
            self.gcd_result.config(text=f"GCD: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def check_prime(self):
        try:
            num = int(self.prime_num.get())
            result = is_prime(num)
            self.prime_result.config(
                text=f"{num} is {'prime' if result else 'not prime'}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_evenodd_tab(self):
        evenodd_frame = ttk.Frame(self.notebook, style='Main.TFrame')
        self.notebook.add(evenodd_frame, text='Even/Odd Checker')
        
        # Content wrapper for centering
        content = ttk.Frame(evenodd_frame, style='Main.TFrame')
        content.pack(expand=True, pady=20)
        
        self.evenodd_num = self.create_input_field(content, "Enter Number:")
        
        ModernButton(content, text="Check Even/Odd", 
                    command=self.check_evenodd).pack(pady=20)
        
        self.evenodd_result = ttk.Label(content, text="", style='Result.TLabel')
        self.evenodd_result.pack(pady=10)

    def check_evenodd(self):
        try:
            num = int(self.evenodd_num.get())
            result = "even" if num % 2 == 0 else "odd"
            self.evenodd_result.config(text=f"{num} is {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    #Matrix Operations Tab (22BCS080)
    def create_matrix_tab(self):
        matrix_frame = ttk.Frame(self.notebook, style='Main.TFrame')
        self.notebook.add(matrix_frame, text='Matrix Operations')

        content = ttk.Frame(matrix_frame, style='Main.TFrame')
        content.pack(expand=True, pady=20)

        # Matrix A input
        ttk.Label(content, text="Matrix A (rows and columns)", style='Modern.TLabel').pack()
        self.mat_a_rows = self.create_input_field(content, "Rows:")
        self.mat_a_cols = self.create_input_field(content, "Cols:")

        self.mat_a_entries = []

        def generate_matrix_a_fields():
            for e in self.mat_a_entries:
                e.destroy()
            self.mat_a_entries.clear()
            try:
                rows = int(self.mat_a_rows.get())
                cols = int(self.mat_a_cols.get())
                for i in range(rows):
                    row_entry = self.create_input_field(content, f"Row {i+1} (space separated):")
                    self.mat_a_entries.append(row_entry)
            except:
                messagebox.showerror("Error", "Enter valid rows and columns")

        ModernButton(content, text="Generate Matrix A Fields", command=generate_matrix_a_fields).pack(pady=5)

        # Operation selection
        ttk.Label(content, text="Select Operation", style='Modern.TLabel').pack(pady=5)
        self.matrix_op = ttk.Combobox(content, values=["Transpose", "Add another matrix", "Multiply by another matrix", "Determinant", "Power"])
        self.matrix_op.pack(pady=5)

        # Matrix B input (only shown when needed)
        self.mat_b_frame = ttk.Frame(content, style='Main.TFrame')
        self.mat_b_frame.pack(expand=True, pady=10)
        self.mat_b_rows = None
        self.mat_b_cols = None
        self.mat_b_entries = []

        def generate_matrix_b_fields():
            for e in self.mat_b_entries:
                e.destroy()
            self.mat_b_entries.clear()
            try:
                rows = int(self.mat_b_rows.get())
                cols = int(self.mat_b_cols.get())
                for i in range(rows):
                    row_entry = self.create_input_field(self.mat_b_frame, f"Row {i+1} (space separated):")
                    self.mat_b_entries.append(row_entry)
            except:
                messagebox.showerror("Error", "Enter valid rows and columns")

        def show_matrix_b_fields(*args):
            for widget in self.mat_b_frame.winfo_children():
                widget.destroy()
            self.mat_b_entries.clear()
            if self.matrix_op.get() in ["Add another matrix", "Multiply by another matrix"]:
                ttk.Label(self.mat_b_frame, text="Matrix B (rows and columns)", style='Modern.TLabel').pack()
                self.mat_b_rows = self.create_input_field(self.mat_b_frame, "Rows:")
                self.mat_b_cols = self.create_input_field(self.mat_b_frame, "Cols:")
                ModernButton(self.mat_b_frame, text="Generate Matrix B Fields", command=generate_matrix_b_fields).pack(pady=5)

        self.matrix_op.bind("<<ComboboxSelected>>", show_matrix_b_fields)

        self.matrix_result = ttk.Label(content, text="", style='Result.TLabel')
        self.matrix_result.pack(pady=10)

        ModernButton(content, text="Run Operation", command=self.run_matrix_op).pack(pady=10)


    def run_matrix_op(self):
        try:
            # Read Matrix A
            A_data = [list(map(int, e.get().split())) for e in self.mat_a_entries]
            A = Matrix(A_data)
            op = self.matrix_op.get()

            # For Add/Multiply, read Matrix B
            B = None
            if op in ["Add another matrix", "Multiply by another matrix"]:
                if not self.mat_b_entries:
                    messagebox.showerror("Error", "Matrix B fields not filled")
                    return
                B_data = [list(map(int, e.get().split())) for e in self.mat_b_entries]
                B = Matrix(B_data)

            # Perform selected operation
            if op == "Transpose":
                result = A.transpose()
            elif op == "Determinant":
                result = A.determinant()
            elif op == "Power":
                k = simpledialog.askinteger("Power", "Enter k:")
                if k is None:
                    return
                result = A.power(k)
            elif op == "Add another matrix" and B:
                result = A.add(B)
            elif op == "Multiply by another matrix" and B:
                result = A.multiply(B)
            else:
                messagebox.showerror("Error", "Invalid operation or missing Matrix B")
                return

            self.matrix_result.config(text=str(result))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Factorial Tab (22BCS071)
    def create_factorial_tab(self):
        factorial_frame = ttk.Frame(self.notebook, style='Main.TFrame')
        self.notebook.add(factorial_frame, text='Factorial Calculator')

        content = ttk.Frame(factorial_frame, style='Main.TFrame')
        content.pack(expand=True, pady=20)

        self.factorial_num = self.create_input_field(content, "Enter Number:")

        ModernButton(content, text="Calculate Factorial", 
                    command=self.calculate_factorial).pack(pady=20)

        self.factorial_result = ttk.Label(content, text="", style='Result.TLabel')
        self.factorial_result.pack(pady=10)

    def calculate_factorial(self):
        try:
            num = int(self.factorial_num.get())
            if num < 0:
                messagebox.showerror("Error", "Please enter a non-negative integer")
                return
            result = factorial(num)
            self.factorial_result.config(text=f"Factorial: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MathFunctionsGUI(root)
    root.geometry("400x500")
    root.minsize(400, 500)
    root.configure(bg='#2c3e50')
    root.mainloop()
