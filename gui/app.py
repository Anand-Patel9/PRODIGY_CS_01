import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from caesar_cipher.cipher import CaesarCipher
from caesar_cipher.file_utils import FileCipher
from caesar_cipher.brute_force import BruteForce

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher Tool")
        self.root.geometry("600x400")
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Shift value
        ttk.Label(main_frame, text="Shift Value (1-25):").grid(row=0, column=0, sticky=tk.W)
        self.shift_var = tk.IntVar(value=3)
        self.shift_spin = ttk.Spinbox(main_frame, from_=1, to=25, textvariable=self.shift_var, width=5)
        self.shift_spin.grid(row=0, column=1, sticky=tk.W)
        
        # Text input
        ttk.Label(main_frame, text="Text:").grid(row=1, column=0, sticky=tk.NW)
        self.text_input = tk.Text(main_frame, height=5, width=50)
        self.text_input.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        ttk.Button(btn_frame, text="Encrypt", command=self.encrypt_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Decrypt", command=self.decrypt_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Brute Force", command=self.brute_force).pack(side=tk.LEFT, padx=5)
        
        # File operations
        file_frame = ttk.LabelFrame(main_frame, text="File Operations", padding=10)
        file_frame.grid(row=4, column=0, columnspan=3, pady=10, sticky=tk.EW)
        
        ttk.Button(file_frame, text="Encrypt File", command=self.encrypt_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Decrypt File", command=self.decrypt_file).pack(side=tk.LEFT, padx=5)
        
        # Results
        ttk.Label(main_frame, text="Results:").grid(row=5, column=0, sticky=tk.NW)
        self.result_text = tk.Text(main_frame, height=5, width=50, state=tk.DISABLED)
        self.result_text.grid(row=6, column=0, columnspan=3, pady=5)
    
    def encrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to encrypt")
            return
        
        cipher = CaesarCipher(self.shift_var.get())
        encrypted = cipher.encrypt(text)
        self.show_result(encrypted)
    
    def decrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to decrypt")
            return
        
        cipher = CaesarCipher(self.shift_var.get())
        decrypted = cipher.decrypt(text)
        self.show_result(decrypted)
    
    def brute_force(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to brute force")
            return
        
        results = BruteForce.brute_force_decrypt(text)
        result_str = "\n".join([f"Shift {shift}: {text}" for shift, text in results])
        self.show_result(result_str)
    
    def encrypt_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
    
        output_path = filedialog.asksaveasfilename(defaultextension=".enc")
        if not output_path:
            return
    
        try:
            FileCipher.encrypt_file(filepath, output_path, self.shift_var.get())
            messagebox.showinfo("Success", "File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt file:\n{str(e)}")
    
    def decrypt_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        
        output_path = filedialog.asksaveasfilename(defaultextension=".dec")
        if not output_path:
            return
        
        try:
            FileCipher.decrypt_file(filepath, output_path, self.shift_var.get())
            messagebox.showinfo("Success", "File decrypted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt file: {str(e)}")
    
    def show_result(self, text):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", text)
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()