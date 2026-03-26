import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import re


# --- ZIMBAPPESI MOTORU ---
def execute_zimbappesi(code, console):
    scu_memory = {}
    console.insert(tk.END, "[Sistem] Güvenlik Kontrolü ve Derleme Başladı...\n", "system")

    if "Namespace = scu.Child;" not in code:
        console.insert(tk.END, "(!) HATA: Namespace eksik!\n", "error");
        return

    main_pattern = r'int\s+buffer\.main\s*\(\s*int\s+main\s*\*\s*\)\s*\{'
    if not re.search(main_pattern, code):
        console.insert(tk.END, "(!) HATA: Giriş noktası (main) hatalı!\n", "error");
        return

    if not code.strip().endswith("}"):
        console.insert(tk.END, "(!) HATA: Blok kapatılmamış '}'!\n", "error");
        return

    try:
        content = re.search(r'\{([\s\S]*)\}', code).group(1).strip()
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if not line or "return:" in line: continue
            if not line.endswith(";"):
                console.insert(tk.END, f"(!) HATA: ';' eksik -> {line}\n", "error");
                return

            if "print.console.write.String" in line:
                t = re.search(r'\{(.*?)\}', line).group(1).replace('"', '')
                console.insert(tk.END, f"{t}\n")
            elif "int.Value" in line:
                m = re.search(r'\{(.*?)=(.*?)\}', line)
                scu_memory[m.group(1).strip()] = int(m.group(2).replace(';', '').strip())
            elif "print.console.write.Var" in line:
                m = re.search(r'\{(.*?)\}', line)
                expr = m.group(1).replace(';', '').strip()
                res = eval(expr, {"__builtins__": None}, scu_memory)
                console.insert(tk.END, f"{res}\n")
    except Exception as e:
        console.insert(tk.END, f"(!) SİSTEM HATASI: {e}\n", "error")


# --- DOSYA İŞLEMLERİ ---
def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".zcsf", filetypes=[("Zimbappesi Code", "*.zcsf")])
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(code_editor.get("1.0", tk.END))
        messagebox.showinfo("Başarılı", f"Kod {path} olarak kaydedildi!")


def open_file():
    path = filedialog.askopenfilename(filetypes=[("Zimbappesi Code", "*.zcsf")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            code_editor.delete("1.0", tk.END)
            code_editor.insert("1.0", f.read())


# --- ARAYÜZ ---
root = tk.Tk()
root.title("Zimbappesi IDE 2.5 (.zcsf Support)")
root.geometry("800x750")
root.configure(bg="#1a1a1a")

# Menü Çubuğu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Aç (.zcsf)", command=open_file)
filemenu.add_command(label="Kaydet", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Çıkış", command=root.quit)
menubar.add_cascade(label="Dosya", menu=filemenu)
root.config(menu=menubar)

code_editor = scrolledtext.ScrolledText(root, height=20, font=("Consolas", 12), bg="#0c0c0c", fg="#ffffff",
                                        insertbackground="white")
code_editor.pack(fill=tk.BOTH, padx=20, pady=10)

run_btn = tk.Button(root, text="▶ EXECUTE SYSTEM",
                    command=lambda: execute_zimbappesi(code_editor.get("1.0", tk.END).strip(), console_display),
                    bg="#d32f2f", fg="white", font=("Courier", 12, "bold"), padx=50)
run_btn.pack(pady=5)

console_display = scrolledtext.ScrolledText(root, height=10, bg="#000000", fg="#00ff00", font=("Consolas", 11))
console_display.tag_config("error", foreground="#ff5252")
console_display.tag_config("system", foreground="#4fc3f7")
console_display.pack(fill=tk.BOTH, padx=20, pady=10)

root.mainloop()