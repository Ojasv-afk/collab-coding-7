import tkinter as tk
from tkinter import ttk, messagebox
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

if __name__ == "__main__":
    root = tk.Tk()
    app = MathFunctionsGUI(root)
    root.geometry("400x500")
    root.minsize(400, 500)
    root.configure(bg='#2c3e50')
    root.mainloop()